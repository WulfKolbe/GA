# GA — a geometry wiki, built from drilled sources

A single-file wiki (`GA.html`, 4.3 MB) that opens offline in any browser, built
from the Markdown under `wiki/`. The Markdown is the source of truth and also
renders in [llmwiki](https://github.com/lucasastorian/llmwiki); the HTML is a
build artifact.

Three bodies of work, from three sources:

- **Projective geometric algebra** — meet, join, projection and rigid motion as
  one operation each, in any dimension.
- **Discrete conformal geometry** — how "angle-preserving" should be defined on a
  triangulated surface, after Keenan Crane's survey.
- **Geometric, algebraic and topological methods for QFT** — an index into an
  edited volume of lecture notes, imported mechanically.

They are adjacent in subject, not one theory. `wiki/overview.md` says so
explicitly, and states what the wiki does not claim.

## Layout

| path | |
|---|---|
| `GA.html` | the built wiki — open it directly |
| `wiki/` | source Markdown, the thing to edit |
| `wiki/gold/`, `wiki/evidence/` | machine extractions, each with the scan it was read from |
| `build/` | the build; KaTeX vendored, runs offline |
| `audit/` | review channel — start at `audit/README.md` |

## Build

```bash
./build/build.sh          # wiki/ -> GA.html
python3 build/verify.py   # regenerate audit/verification.json
```

## Provenance

Sources were extracted with [`pdfdrill`](https://pdfdrill.info); mathematics was
typeset by hand and then checked against the machine extraction. Every extracted
formula is published with its scan, because OCR is a reading and not a fact.
`audit/PROVENANCE.md` records which pages are synthesis and which are machine
output — they are not the same kind of claim.

The verbatim source extractions are **not** published: they are third-party
copyrighted works. Equation scans are published as excerpts, since they are what
make a formula checkable.

## Licence

Three distinguishable things live here, and only one of them is mine to license.

| what | licence |
|---|---|
| `build/` — the build scripts | **MIT** © 2026 Wulf Kolbe — see `build/LICENSE`; every file carries an SPDX tag |
| `build/vendor/katex/` | MIT © Khan Academy — its own `LICENSE`, unmodified |
| `wiki/`, `GA.html` — the content | **no licence granted** |

The content quotes and reproduces excerpts of third-party publications (an AMS
chapter, a Springer volume, a video transcript). No licence choice of mine can
relicense those, so none is asserted over the wiki.

There is deliberately **no repository-root `LICENSE`**: one would make GitHub
report the whole repository as MIT, which would be wrong about the content —
the part a reader is most likely to reuse.

The repository previously carried MIT © 2022 Sanjib Kumar Sen from an unrelated
project; that was removed with the project it covered.
