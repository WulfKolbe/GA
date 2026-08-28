#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Bilingual OKF emitter — reference implementation of the format proposed to pdfdrill.

The docmodel already holds both languages after `pdfdrill translate`:
    props['text']         -> the translation (working language)
    props['text_source']  -> the original
`pdfdrill okf` emits only one of them, and no marker that a translation exists.
This projects both, so a wiki can cite a claim *and* show the original it was
read from.

Usage:  python3 okf_bilingual.py <bibkey> [<bibkey> ...] [--out DIR]
"""
import json
import pathlib
import sys

LIB = pathlib.Path.home() / "pdfdrill-library"
PROSE = {"Paragraph", "Section", "Abstract", "ListItem", "Footnote", "Caption", "Title"}
PLURAL = {"Paragraph": "paragraphs", "Section": "sections", "Abstract": "abstracts",
          "ListItem": "lists", "Footnote": "footnotes", "Caption": "captions", "Title": "titles"}


def load_model(bibkey):
    m = json.load(open(LIB / bibkey / "model.docmodel.json"))
    objs = m["objects"]
    return list(objs.values()) if isinstance(objs, dict) else objs


def lang_of(bibkey):
    """translated_lang lives only in the tiddler bundle, not the model."""
    try:
        t = json.load(open(LIB / bibkey / f"{bibkey}.tiddlers.json"))
        langs = {x.get("translated_lang") for x in t if x.get("translated_lang")}
        return (langs.pop() if len(langs) == 1 else "und")
    except Exception:
        return "und"


def esc(s):
    return str(s).replace("\n", " ").strip()


def emit(bibkey, out_root):
    objs = load_model(bibkey)
    target = lang_of(bibkey)
    units = [o for o in objs if o["type"] in PROSE and (o.get("props") or {}).get("text")]
    bilingual = [o for o in units if (o["props"].get("text_source") or "").strip()
                 and o["props"]["text_source"] != o["props"]["text"]]

    root = out_root / bibkey
    written = 0
    for o in units:
        p = o["props"]
        title = p.get("tiddler_title") or f"{bibkey}_{o['type'][:4].upper()}_{o['id'][-8:]}"
        folder = root / PLURAL.get(o["type"], o["type"].lower() + "s")
        folder.mkdir(parents=True, exist_ok=True)
        src = (p.get("text_source") or "").strip()
        has_src = bool(src) and src != p["text"]
        fm = [
            "---",
            f"type: {o['type']}",
            f"title: {title}",
            f'description: "{esc(p["text"])[:160]}"',
            f"resource: pdfdrill:{bibkey}/{title}",
            f"tags: [{PLURAL.get(o['type'], o['type'].lower())}, {bibkey}"
            + (", translated]" if has_src else "]"),
            f"lang: {target if has_src else 'de'}",
        ]
        if has_src:
            fm += ["lang_source: de", "translated_by: deepl"]
        if p.get("page"):
            fm.append(f"page: {p['page']}")
        fm.append("---")

        body = [p["text"].strip(), ""]
        if has_src:
            body += ['<!--okf:source lang="de"-->', src, "<!--/okf:source-->", ""]
        (folder / f"{title}.md").write_text("\n".join(fm) + "\n\n" + "\n".join(body), encoding="utf-8")
        written += 1

    (root / "index.md").write_text(
        f"---\ntype: Index\ntitle: {bibkey}\nlang: {target}\nlang_source: de\n---\n\n"
        f"# {bibkey}\n\n{written} prose units, {len(bilingual)} carrying both languages "
        f"({target} body, German original in an `okf:source` block).\n",
        encoding="utf-8")
    return written, len(bilingual), target


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    out = pathlib.Path.home() / "pdfdrill-library" / "okf-bilingual"
    if "--out" in sys.argv:
        out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1])
    for bibkey in args:
        n, b, lang = emit(bibkey, out)
        print(f"{bibkey:12} {n:5} units, {b:5} bilingual ({lang} + de) -> {out/bibkey}")


if __name__ == "__main__":
    main()
