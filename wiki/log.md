# Wiki Log

## [2026-08-27] ingest | A Swift Introduction to Projective Geometric Algebra (transcript)

Source staged at `raw/pga-swift-introduction-transcript.md` (from `~/Downloads/cleaned_transcript.md`).

Created:
- `wiki/sources/pga-swift-introduction-transcript.md`
- `wiki/overview.md`, `wiki/index.md`
- 24 concept pages under `wiki/concepts/`

Contradictions: none — first source in this wiki.

## [2026-08-27] ingest | Conformal Geometry of Simplicial Surfaces

Source staged at `raw/ConformalGeometryOfSimplicialSurfaces.md` (Keenan Crane, Proc. Symp. Appl. Math.).

Created:
- `wiki/sources/conformal-geometry-of-simplicial-surfaces.md`
- 18 concept pages under `wiki/concepts/`
- 3 entity pages under `wiki/entities/` (first entities in this wiki)

Updated: `wiki/index.md`, `wiki/overview.md`.

Contradictions: none. Scope note recorded on the source page — this wiki previously covered
projective geometric algebra only; conformal geometric algebra and discrete conformal geometry
are topically adjacent but unrelated frameworks, and Crane's paper never mentions geometric algebra.

Source quality: the PDF extraction has 81/764 math expressions (10.6%) that do not compile
(`(cid:NN)` glyph artifacts, HTML entities inside math, raw Unicode). All formulas on the wiki
pages were re-typeset by hand; run `node build/check_math.cjs raw/*.md` to re-measure.

## [2026-08-27] cite-into | ground the Crane pages in the gold extraction

Converted every `[[wikilink]]` in the wiki to a standard markdown link (368 links). llmwiki's
renderer has no wikilink plugin, so `[[Rotor]]` was displaying as literal text; its guide
(`mcp/tools/guide.py:157`) specifies standard markdown links between wiki pages. The
TiddlyWiki build converts them back to wikilinks, so both renderers work from one source.

Added 24 gold-unit pages under `wiki/gold/` with their MathPix scan crops
(`wiki/gold/crops/`, 232 KB), and inserted 25 citation blocks beneath the cited display
formulas across 14 pages. Each block shows the original scan and links to the unit.

Two gold units (EQ0042, EQ0043) carry the Cyrillic Л for the Lobachevsky function, which
KaTeX rejects; those pages show the extraction verbatim in a code block and note that the
wiki writes \Lambda instead.
