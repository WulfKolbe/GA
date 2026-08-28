---
report: 274
date: 2026-08-28
scope: build/make_tiddlers.py, GA.html
commit: f7bc37e
---

# 274 — site title

## What was wrong

The built wiki announced itself as:

```
$:/SiteTitle     PGA Wiki
$:/SiteSubtitle  Projective Geometric Algebra
```

Wrong on two counts. The wiki holds three bodies of work — projective geometric
algebra, discrete conformal geometry after Crane, and a mechanically imported
index into an edited QFT volume — so the title named one of three and the
subtitle repeated that same one. It had also stopped matching the artifact: the
file and the repository are both `GA`.

## The change

Two lines in `build/make_tiddlers.py`:

```
$:/SiteTitle     GA Wiki
$:/SiteSubtitle  geometric algebra, discrete conformal geometry, QFT methods
```

`GA` because that is what the file and repository are called; the subtitle now
carries the scope instead of naming one subject.

## Confirmation in the built artifact

Checked in the rebuilt `GA.html`, not inferred from the source change:

| check | result |
|---|---|
| `<title>` element | `GA Wiki — geometric algebra, discrete conformal geometry, QFT methods` |
| browser tab title (headless Chromium) | identical |
| sidebar `.tc-site-title` / `.tc-site-subtitle` | `GA Wiki` / `geometric algebra, discrete conformal geometry, QFT methods` |
| `grep -c 'PGA Wiki' GA.html` | **0** — no occurrence survives anywhere in the 4.4 MB file |
| page errors on load | none |

Build verification unchanged: 115 pages, 452/452 maths expressions compile,
0 broken links or images. `audit/verification.json` was regenerated in the same
commit so the published record stays in step.

## What this does not fix

- The directory is still `~/GA` locally and the repository still describes
  itself as "Geometric Algebra" in its GitHub description — the wiki is broader
  than that.
- Renaming the wiki does not change what is in it. The three bodies of work are
  adjacent in subject, not one theory; `wiki/overview.md` states that, and a
  reviewer should check the wiki does not imply otherwise elsewhere.
