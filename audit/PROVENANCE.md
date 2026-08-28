# Provenance — how each page kind was produced

An auditor's first question should be "who wrote this sentence". Per directory:

| directory | pages | written by | from |
|---|---|---|---|
| `wiki/concepts/` | 42 | **me, synthesising** | a video transcript (PGA) and Keenan Crane's survey |
| `wiki/entities/` | 3 | **me, synthesising** | the same survey |
| `wiki/gold/` | 24 | machine | `pdfdrill` + MathPix, verbatim, with the scan |
| `wiki/chapters/` | 11 | machine | the volume's own abstracts and table of contents |
| `wiki/evidence/` | 29 | machine | numbered equations + their scans |
| `wiki/sources/` | 3 | me | extraction figures and caveats |
| `wiki/overview.md`, `index.md` | 2 | me | — |

**The 45 synthesised pages are where an error would hide.** The 64 machine pages
can be wrong (OCR misreads) but not *invented*, and each carries its scan.

## The chain, per source

**PGA (`concepts/`, the geometric-algebra half).** A cleaned transcript of a
video introduction. No PDF, no OCR. I wrote the pages from the transcript and
typeset all mathematics by hand; nothing machine-extracted backs them. This is
the least externally checkable material in the wiki.

**Crane, *Conformal Geometry of Simplicial Surfaces* (`concepts/`, `gold/`).**
Originally ingested from a shallow text-layer extraction whose maths was badly
damaged (`(cid:96)` for ℓ, `&gt;` inside formulas — 81 of 764 expressions did
not compile). I hand-typeset every formula from the surrounding prose rather
than copying it. A proper MathPix model was built afterwards and **every formula
was compared against it**; all matched but one, now corrected. The `gold/` pages
are that comparison, kept.

**Cardona (ed.), *Geometric, Algebraic and Topological Methods for QFT*
(`chapters/`, `evidence/`).** Imported mechanically; I did not read the volume.
Chapter pages carry the printed abstract, author and page range. A chapter the
table of contents lists but no `Abstract` object confirms is **not** imported —
Marcolli's chapter is absent for that reason, and `sources/cardona2013.md` says
so.

## Conventions that carry meaning

- A formula shown with a scan beneath it: the scan is the authority, the LaTeX is
  a reading of it.
- A formula in a fenced ```latex block instead of rendered: the extraction
  contains a character KaTeX refuses (Cyrillic Л; a stray Unicode glyph). Shown
  verbatim rather than as a broken render.
- `lang:` / `lang_source:` in frontmatter: the body is a translation and the
  original is available.
