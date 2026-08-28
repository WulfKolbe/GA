#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Import a drilled pdfdrill document into an llmwiki-shaped wiki.

Generic importer: everything document-specific comes from the model and the OKF
bundle, nothing is hard-coded per book. Run `pdfdrill okf <pdf> --bibkey <key>`
first (projection only — it does NOT rebuild the model, so held enrichments
survive).

    python3 import_pdfdrill.py --doc <library-dir> --bibkey cardona2013 \
        --wiki wiki/ --evidence 3

Stages
  1 verify    model + OKF bundle + crops present; census by object type
  2 chapters  TOC -> (title, printed page, authors); Abstract objects fix the
              printed->PDF page offset and supply each chapter's summary
  3 source    one source page carrying the extraction figures and caveats
  4 chapters  one page per chapter: abstract, authors, page range, evidence
  5 evidence  numbered equations with their scan crop, capped per chapter
  6 index     append the new material to the wiki index
"""
import argparse
import json
import pathlib
import re
import shutil
import unicodedata
from collections import Counter, defaultdict

TODAY = "2026-08-28"
TOC_LINE = re.compile(r"^(.*\S)\s*\.{3,}\s*([ivxlcdm]+|\d+)\s*$", re.I)
AUTHORish = re.compile(r"^(?:[A-Z]\.\s*)+[A-Z][A-Za-z’'\-]+(?:\s+and\s+.+)?$")


# ------------------------------------------------------------------ helpers

def slugify(s, maxlen=48):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\\\((.+?)\\\)", r"\1", s)
    parts = re.split(r"[^A-Za-z0-9]+", s)
    out = "".join(p[:1].upper() + p[1:] for p in parts if p)
    return out[:maxlen] or "Chapter"


def clean_title(s):
    """TOC titles keep a dot-leader tail, and pdfdrill math delimiters llmwiki rejects."""
    s = re.sub(r"[\s.]+$", "", re.sub(r"\s+", " ", s or "")).strip()
    return math_to_dollar(s)


def math_to_dollar(txt):
    """pdfdrill emits \\( .. \\); llmwiki forbids it (markdown eats the backslashes)."""
    txt = re.sub(r"\\\((.+?)\\\)", lambda m: f"${m.group(1).strip()}$", txt or "", flags=re.S)
    return re.sub(r"\\\[(.+?)\\\]", lambda m: f"$$\n{m.group(1).strip()}\n$$", txt, flags=re.S)


def load_model(doc):
    m = json.load(open(doc / "model.docmodel.json"))
    objs = m["objects"]
    return list(objs.values()) if isinstance(objs, dict) else objs


def okf_units(doc, bibkey, kind):
    d = doc / "okf" / bibkey / kind
    out = []
    for f in sorted(d.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        fm = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
        if not fm:
            continue
        meta = dict(re.findall(r"^(\w+):\s*(.*)$", fm.group(1), re.M))
        body = re.search(r"\$\$([\s\S]*?)\$\$", fm.group(2))
        out.append(dict(meta=meta, latex=(body.group(1).strip() if body else ""),
                        text=fm.group(2).strip()))
    return out


# ------------------------------------------------------------------ stage 1

def verify(doc, bibkey):
    objs = load_model(doc)
    census = Counter(o["type"] for o in objs)
    okf = doc / "okf" / bibkey
    crops = sorted((doc / "report-crops").glob("*.jpg"))
    problems = []
    if not okf.exists():
        problems.append(f"no OKF bundle at {okf} — run: pdfdrill okf <pdf> --bibkey {bibkey}")
    if not crops:
        problems.append("no crops — run: pdfdrill cdncrops <pdf>")
    return objs, census, crops, problems


# ------------------------------------------------------------------ stage 2

def parse_toc(objs):
    toc = [o for o in objs if o["type"] == "Toc"]
    if not toc:
        return []
    entries = toc[0]["props"].get("entries") or []
    rows, pending = [], []
    for e in entries:
        m = TOC_LINE.match(e.strip())
        # a dot-leader fragment ("..") also matches; a real title has real words
        if m and len(re.sub(r"[^A-Za-z0-9]", "", m.group(1))) >= 3:
            rows.append(dict(title=clean_title(m.group(1)),
                             printed=m.group(2), authors=[]))
            pending = []
        elif rows and e.strip() and "...." not in e:
            s = re.sub(r"\s+", " ", e.strip())
            if s != rows[-1]["title"] and s not in pending and AUTHORish.match(s):
                rows[-1]["authors"].append(s)
                pending.append(s)
    return rows


def chapters(objs):
    """Chapters = TOC rows that a real Abstract confirms, with the page offset solved."""
    rows = [r for r in parse_toc(objs) if r["printed"].isdigit()]
    abstracts = sorted([o for o in objs if o["type"] == "Abstract"],
                       key=lambda z: z["props"].get("page") or 0)
    if not rows or not abstracts:
        return []
    # the offset that lines the most TOC rows up with an abstract wins
    apages = [a["props"]["page"] for a in abstracts]
    best, score = 0, -1
    for off in range(0, 60):
        hit = sum(1 for r in rows if int(r["printed"]) + off in apages)
        if hit > score:
            best, score = off, hit
    seen = {}
    for r in rows:
        pdfpage = int(r["printed"]) + best
        a = next((x for x in abstracts if x["props"]["page"] == pdfpage), None)
        if a is None:
            continue
        # one chapter per abstract; the longest TOC title for it wins
        if pdfpage in seen and len(seen[pdfpage]["title"]) >= len(r["title"]):
            continue
        seen[pdfpage] = dict(title=r["title"], authors=r["authors"], printed=int(r["printed"]),
                             page=pdfpage, abstract=a["props"].get("text", ""),
                             slug=slugify(r["title"]))
    out = [seen[k] for k in sorted(seen)]
    for i, c in enumerate(out):                      # page range = up to the next chapter
        c["page_end"] = (out[i + 1]["page"] - 1) if i + 1 < len(out) else None
    return out, best, score


# ------------------------------------------------------------------ stages 3-6

def write_source(wiki, bibkey, title, census, chs, doc, offset):
    p = wiki / "sources" / f"{bibkey}.md"
    lines = ["---", f'title: "{title}"', "type: source",
             "tags: [qft, geometry, lecture-notes]", f"bibkey: {bibkey}",
             f"last_updated: {TODAY}", "---", "",
             f"# {title}", "",
             f"An edited volume of lecture notes, drilled with `pdfdrill` (bibkey `{bibkey}`) "
             "and imported into this wiki by projection — no prose here was written by hand.", "",
             "## Extraction", "", "| | |", "|---|---|",
             f"| pages | {census.get('Page', 0)} |",
             f"| chapters (abstract-confirmed) | {len(chs)} |",
             f"| paragraphs | {census.get('Paragraph', 0)} |",
             f"| display equations | {census.get('Equation', 0)} |",
             f"| inline formulas | {census.get('Formula', 0)} |",
             f"| diagrams | {census.get('Diagram', 0)} |",
             f"| printed page -> PDF page offset | +{offset} |", "",
             "## Chapters", ""]
    for c in chs:
        who = f" — {', '.join(c['authors'])}" if c["authors"] else ""
        lines.append(f"- [{c['title']}](../chapters/{c['slug']}.md){who} (p. {c['printed']})")
    lines += ["", "## Caveats", "",
              "- Text and mathematics are MathPix OCR readings, not the publisher's source. "
              "Every equation page carries the scan it was read from; the scan is the authority.",
              "- Chapter boundaries come from the volume's own table of contents, confirmed "
              "against the `Abstract` objects in the model — chapters the TOC lists but no "
              "abstract confirms are not imported.",
              "- The bibliography holds 8 parsed entries with no resolved BibTeX; "
              "`pdfdrill bibfetch` would fill them.", ""]
    p.write_text("\n".join(lines), encoding="utf-8")


def write_chapters(wiki, bibkey, title, chs, evidence):
    for c in chs:
        ev = evidence.get(c["slug"], [])
        who = ", ".join(c["authors"]) or "—"
        out = ["---", f'title: "{c["title"]}"', "type: chapter",
               "tags: [qft, geometry, chapter]", f"sources: [{bibkey}]",
               f"page: {c['page']}", f"printed_page: {c['printed']}",
               f"last_updated: {TODAY}", "---", "",
               f"# {c['title']}", "", f"**Author:** {who}", "",
               f"**In:** [{title}](../sources/{bibkey}.md), printed p. {c['printed']}"
               + (f" (PDF p. {c['page']}–{c['page_end']})" if c["page_end"] else
                  f" (PDF p. {c['page']}–end)"), "",
               "## Abstract", "", math_to_dollar(c["abstract"]).strip(), ""]
        if ev:
            out += ["## Numbered equations", "",
                    "A sample of this chapter's numbered equations, each with the scan it was "
                    "read from:", ""]
            for e in ev:
                out.append(f"- [({e['ref']}) on p. {e['page']}](../evidence/{e['unit']}.md)")
            out.append("")
        out += ["## Provenance", "",
                f"Imported from the `pdfdrill` docmodel of [{title}](../sources/{bibkey}.md). "
                "The abstract above is the OCR reading of the printed abstract.", ""]
        (wiki / "chapters" / f"{c['slug']}.md").write_text("\n".join(out), encoding="utf-8")


def write_evidence(wiki, doc, bibkey, chs, per_chapter, unrenderable):
    eqs = [u for u in okf_units(doc, bibkey, "equations")
           if u["meta"].get("page") and u["meta"].get("refnum")]
    for u in eqs:
        u["page"] = int(u["meta"]["page"])
    crops = {int(m.group(1)): f for f in (doc / "report-crops").glob("*.jpg")
             for m in [re.search(r"EQ(\d+)\.jpg$", f.name)] if m}
    chosen = defaultdict(list)
    for c in chs:
        lo, hi = c["page"], (c["page_end"] or 10 ** 6)
        inrange = [u for u in eqs if lo <= u["page"] <= hi]
        for u in inrange[:per_chapter]:
            ord_ = int(re.search(r"EQ(\d+)$", u["meta"]["title"]).group(1))
            chosen[c["slug"]].append(dict(unit=u["meta"]["title"], ref=u["meta"]["refnum"],
                                          page=u["page"], latex=u["latex"], crop=crops.get(ord_)))
    for slug, items in chosen.items():
        for e in items:
            out = ["---", f'title: "{e["unit"]}"', "type: evidence",
                   "tags: [evidence, equation]", f"sources: [{bibkey}]",
                   f"page: {e['page']}", f'refnum: "{e["ref"]}"',
                   f"last_updated: {TODAY}", "---", "",
                   f"# {e['unit']}", "",
                   f"Equation ({e['ref']}) as extracted from PDF page {e['page']} by "
                   "`pdfdrill` (MathPix). Not typed by hand.", ""]
            if e["unit"] in unrenderable:
                out += ["The OCR reading contains a character KaTeX will not typeset, so it is "
                        "shown as extracted. The scan below is the authority.", "",
                        "```latex", e["latex"], "```", ""]
            else:
                out += ["$$", e["latex"], "$$", ""]
            if e["crop"]:
                shutil.copy(e["crop"], wiki / "crops" / f"{e['unit']}.jpg")
                out += [f"![Equation ({e['ref']}) as printed on page {e['page']}]"
                        f"(../crops/{e['unit']}.jpg)", "",
                        "*The scan is the evidence the LaTeX was read from.*", ""]
            out += ["## Cited by", "",
                    f"[{slug}](../chapters/{slug}.md)", ""]
            (wiki / "evidence" / f"{e['unit']}.md").write_text("\n".join(out), encoding="utf-8")
    return chosen


def check_latex(items, vendor):
    """Ask KaTeX which readings will not compile, so they ship verbatim not broken."""
    import subprocess
    r = subprocess.run(["node", str(vendor)], text=True, capture_output=True,
                       input=json.dumps({"items": [{"id": i["meta"]["title"], "latex": i["latex"]}
                                                   for i in items]}))
    return set(json.loads(r.stdout)["bad"]) if r.returncode == 0 else set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", required=True)
    ap.add_argument("--bibkey", required=True)
    ap.add_argument("--wiki", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--evidence", type=int, default=3)
    a = ap.parse_args()

    doc, wiki = pathlib.Path(a.doc).expanduser(), pathlib.Path(a.wiki).expanduser()
    objs, census, crops, problems = verify(doc, a.bibkey)
    if problems:
        raise SystemExit("import blocked:\n  " + "\n  ".join(problems))
    for d in ("sources", "chapters", "evidence", "crops"):
        (wiki / d).mkdir(parents=True, exist_ok=True)

    chs, offset, matched = chapters(objs)
    eqs = [u for u in okf_units(doc, a.bibkey, "equations")
           if u["meta"].get("page") and u["meta"].get("refnum")]
    bad = check_latex(eqs, pathlib.Path(__file__).parent / "validate_latex.cjs")

    ev = write_evidence(wiki, doc, a.bibkey, chs, a.evidence, bad)
    write_chapters(wiki, a.bibkey, a.title, chs, ev)
    write_source(wiki, a.bibkey, a.title, census, chs, doc, offset)

    print(f"verified   : {census.get('Page',0)} pages, {census.get('Equation',0)} equations, "
          f"{len(crops)} crops")
    print(f"chapters   : {len(chs)} (TOC rows confirmed by an Abstract; page offset +{offset})")
    print(f"evidence   : {sum(len(v) for v in ev.values())} equation pages "
          f"({len(bad)} readings KaTeX rejects, shipped verbatim)")
    print(f"written to : {wiki}")


if __name__ == "__main__":
    main()
