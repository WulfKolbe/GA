# Open questions and known defects

Self-reported. An auditor should treat this as the list I already know about, and
look for what is *not* here.

## 1. One mathematical error was found and fixed — by machine, not by me

I wrote the normalised Ricci flow as `d/dt g = (K - K̄)g`. The source has
`(K̄ - K)g`. The bar had been destroyed in the text extraction (`g = (K -K)g`)
and I inferred the sign wrongly. Caught only when a gold MathPix model was built
and every formula compared against it.

Fixed in `wiki/concepts/DiscreteRicciFlow.md`. **The relevant question for an
auditor is not this error but its class**: what else did I infer from a damaged
extraction and get away with? The `gold/` pages cover 24 formulas; the PGA half
of the wiki has no gold layer at all.

## 2. The PGA material has no machine-checkable backing

`concepts/` for projective geometric algebra derives from a video transcript.
There is no PDF, no OCR, no scan. Every formula there is mine, typeset from
prose. It compiles, which says nothing about whether it is right.

## 3. A deliberate deviation from the source

Crane's equation (6.3) is printed as `φ(α, x)`. The wiki writes `φ(α, λ)`,
consistent with the derivative `∂φ/∂λ_ij` stated two lines later. I judged `x` to
be a typo in the source. Recorded in `wiki/sources/conformal-geometry-of-simplicial-surfaces.md`.
If that judgement is wrong, the wiki misquotes the paper.

## 4. Two equations shipped unrendered

`gold/crane2020_EQ0042` and `EQ0043` contain the Cyrillic **Л** (Lobachevsky
function), which KaTeX refuses. They are shown verbatim with the scan. The wiki
writes `\Lambda` in prose. Reasonable, but it is a substitution.

## 5. Imported chapters were not read

`chapters/` is an index into a 378-page volume, produced from its abstracts and
table of contents. Nothing there is a reading. If any chapter page implies
comprehension, that is a defect — flag it.

## 6. Coverage claims

`overview.md` states what is missing. Check it is honest: the Cardona volume
contributes 11 chapter pages and 29 equations out of 1012; the Crane survey has
24 gold units out of 49 display equations.

## 7. Unverified by anyone

- Whether my summaries of Crane's argument are *faithful* — structural checks
  cannot test this.
- Whether the `→` cross-reference resolution in the concept pages links to the
  term the author meant.
- Whether the German→English translations used elsewhere in this project (not in
  this repo) preserve technical meaning.

## Questions I would like answered

1. In `concepts/`, is any claim stated more strongly than the source supports?
2. Does any page read as though I had read a source I only indexed?
3. Is the light/dark distinction between "the source says" and "I conclude"
   maintained, or do they blur?
