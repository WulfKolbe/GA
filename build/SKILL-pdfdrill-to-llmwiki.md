---
name: pdfdrill-to-llmwiki
description: |
  Import a drilled pdfdrill document into an llmwiki-shaped wiki. Use when a PDF
  has been drilled (model + crops exist) and its content should become wiki
  pages with citations back to the extraction. Produces source, chapter and
  evidence pages that carry the scan each formula was read from.
allowed-tools: [Read, Bash, Write, Edit]
---

# pdfdrill → llmwiki

pdfdrill turns a PDF into a docmodel. llmwiki wants Markdown pages with
frontmatter, standard links and footnote citations. This is the seam between
them.

**Do not hand-write pages from a drilled document.** Project them. The model
already knows the chapters, the equations, the page numbers and where every
crop came from; retyping any of it introduces errors the wiki cannot detect.

---

## 0. Preconditions

```bash
pdfdrill preflight --ack DRILL-xxxxxxxx     # once per session; token = SKILL's last line
pdfdrill status <pdf>                       # what is already known
pdfdrill steps okf <pdf>                    # what a projection would still need
```

`steps` is the gate. If it says *"prerequisites satisfied … runs directly"*, the
document is ready and the import costs nothing. If it names `mathpix` or
`model`, decide deliberately — those are paid and/or destructive (see rule 2).

---

## 1. Give the document a clean bibkey — at projection time

The bibkey becomes the prefix of every unit id. A library folder is often named
after the original file:

```
Geometric, Algebraic and Topological Methods for Quantum Field Theory (Alexander Cardona (ed.) etc.) (Z-Library)
```

Spaces, commas and parentheses in an identifier that ends up in filenames,
tiddler titles and links. Fix it with the projection flag, **not** by rebuilding:

```bash
pdfdrill okf <pdf> --bibkey cardona2013     # 3s, no model rebuild
```

> **Rule 1 — never rebuild a model to rename it.** `pdfdrill model --bibkey`
> re-derives the model and silently drops held enrichments (measured: a rebuild
> destroyed 105 translated units). `okf`/`tiddlers` take `--bibkey` directly.

> **Rule 2 — crops keep the bibkey they were fetched under.** `cdncrops` names
> files from the bibkey at fetch time, so re-projecting under a new key
> desynchronises unit ids from crop filenames. The `EQ####` ordinal is stable —
> map on that, or re-run `cdncrops`.

---

## 2. Find the structure — never invent it

Three model objects carry the document's own structure. Use them, in this order:

| object | gives | reliability |
|---|---|---|
| `Toc` | chapter titles, authors, **printed** page numbers | high, but dot-leader noise |
| `Abstract` | where each chapter actually starts in the PDF | high — one per chapter |
| `Section` | headings | **noisy** — many empty, many mid-chapter |

The printed page in the TOC is not the PDF page. Solve the offset instead of
assuming it: try each offset and keep the one that lines up the most TOC rows
with an `Abstract` page. On the Cardona volume this found **+11** and confirmed
11 chapters.

> **Rule 3 — a chapter is a TOC row an Abstract confirms.** Rows nothing
> confirms are not chapters. This correctly excluded Marcolli's chapter, which
> the TOC lists but which has no `Abstract` object — and the source page says so
> rather than leaving a silent gap.

> **Rule 4 — TOC titles carry dot-leader tails.** `"Spectral Geometry .."` and
> `"Index Theory for Non-compact \(G\)-manifolds .."`. Strip trailing `[\s.]+`,
> and require ≥3 alphanumerics or a bare `".."` will parse as a chapter — it
> did, producing 22 chapters from 11 abstracts and silently overwriting pages
> through slug collisions.

---

## 3. Convert to llmwiki's dialect

Two conversions are mandatory, both from llmwiki's own guide
(`mcp/tools/guide.py`):

- **Math**: pdfdrill emits `\( … \)`; llmwiki forbids it (line 138 — "markdown
  eats the backslashes and the formula renders as plain text"). Convert to
  `$ … $` and `$$ … $$`. Titles too.
- **Links**: standard markdown links to wiki paths (line 157). **Not**
  `[[WikiLinks]]` — llmwiki's `react-markdown` has no wikilink plugin and
  renders them as literal text. If a TiddlyWiki build is also wanted, convert
  markdown links → wikilinks *in the builder*, so one source serves both.

---

## 4. Write three page kinds

- **Source page** — extraction census (pages, paragraphs, equations, formulas,
  diagrams), the page offset, the chapter list, and the caveats. This is where
  the reader learns what the wiki does *not* contain.
- **Chapter page** — the volume's own abstract, author and page range from the
  TOC, plus links to evidence. No synthesis.
- **Evidence page** — one numbered equation: the LaTeX, and **the crop it was
  read from**, with a "cited by" backlink.

> **Rule 5 — every extracted formula ships with its scan.** OCR is a reading,
> not a fact. The crop is what makes a claim checkable, and it is the only thing
> that makes a wrong reading visible.

Bound the evidence. 1012 equations is not 1012 pages: select numbered equations
(`refnum` present), capped per chapter.

---

## 5. Validate before publishing — gates, not glances

```bash
node build/check_math.cjs wiki/**/*.md      # exits non-zero if any $…$ fails KaTeX
```

1. **Every expression compiles.** Compile at build time with the *same* KaTeX
   the renderer uses. A reading that will not compile ships verbatim in a code
   block with the scan as authority — never as red error text.
2. **Every link and image resolves.** Walk the markdown, resolve each relative
   target against the page set, and fail on the first miss.
3. **Both renderers.** Server-side render proves structure; a headless browser
   proves it actually paints. They disagree: TiddlyWiki server-side rendering
   hid a markdown-it crash that blanked the page in Chromium.

> **Rule 6 — a line starting with `!` is a TiddlyWiki heading.** `![alt](src)`
> on its own line becomes `<h1>[alt](src)</h1>`. Emit `<$image>` instead.

> **Rule 7 — mathematics does not fit in an attribute.** Real formulas contain
> `<`, `>` and `&` (the alignment character inside `aligned`), and `&` cannot be
> escaped without breaking the environment. TiddlyWiki does not decode entities
> in attributes either. Put each formula in its own tiddler and transclude:
> `<$latex text={{math/0042}} displayMode="true"/>` — pdfdrill's own EQBLOCK
> pattern.

---

## Reference implementation

`import_pdfdrill.py` in this directory implements stages 1–5 generically:

```bash
pdfdrill okf "<pdf>" --bibkey cardona2013
python3 build/import_pdfdrill.py \
    --doc "<library-dir>" --bibkey cardona2013 \
    --wiki ~/PGA/wiki --title "…" --evidence 3
```

Measured on the Cardona volume: 378 pages, 1012 equations and 1012 crops
verified; 11 chapters confirmed at offset +11; 29 evidence pages, of which 1
reading KaTeX rejects and which therefore ships verbatim.

## What this does not do

It builds a **navigable index into** a document, not a reading of it. Concept
pages — the synthesis that makes a wiki worth reading — still require someone to
read the material. Say so on the source page rather than letting an imported
skeleton look like coverage.
