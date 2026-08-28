---
title: "Conformal Geometry of Simplicial Surfaces"
type: source
tags: [discrete-differential-geometry, conformal-geometry, uniformization, survey]
date: 2026-08-27
source_file: raw/ConformalGeometryOfSimplicialSurfaces.md
---

## Summary

Keenan Crane's survey (Proceedings of Symposia in Applied Mathematics) of how conformal geometry is discretized for triangulated surfaces. The organizing observation is that the many *equivalent* characterizations of a smooth conformal map become *inequivalent* once discretized, and each one yields a different discrete theory. Crane grades them: most naive starting points are **too rigid**, circle-based theories are nearly right, and conformal equivalence of discrete metrics is the one that works — it now carries a complete discrete uniformization theorem mirroring the classical one for Riemann surfaces.

## Key Claims

- The smooth definition admits at least seven equivalent phrasings — angles, circles, Cauchy–Riemann, metric scaling, conjugate harmonics, Dirichlet energy, Hodge duality — and discretizing each gives a *different* theory. See [ConformalMapCharacterizations](../concepts/ConformalMapCharacterizations.md), [DiscreteDifferentialGeometry](../concepts/DiscreteDifferentialGeometry.md).
- **Preserving interior angles is far too rigid**: it forces a similarity per triangle, and shared edges force one global scale factor — so the whole map is an isometry up to one constant. The discretized Cauchy–Riemann equation, Dirichlet energy, and Hodge star all collapse to exactly the same rigidity. See [DiscretizationRigidity](../concepts/DiscretizationRigidity.md).
- A discrete surface's intrinsic geometry is a [DiscreteMetric](../concepts/DiscreteMetric.md) — positive edge lengths satisfying the triangle inequality — which induces a [ConeMetric](../concepts/ConeMetric.md) with cone angles $\Omega_i = 2\pi - \Theta_i$ playing the role of Gaussian curvature.
- **Circle packings are too flexible** (they see only combinatorics), while **circle patterns** with prescribed intersection angles are "just right" but come with no guaranteed existence — Thurston's condition can fail. See [CirclePacking](../concepts/CirclePacking.md), [CirclePattern](../concepts/CirclePattern.md).
- The definition that works: two discrete metrics are conformally equivalent when $\tilde\ell_{ij} = e^{(u_i+u_j)/2}\,\ell_{ij}$ for vertex scale factors $u$. See [DiscreteConformalEquivalence](../concepts/DiscreteConformalEquivalence.md).
- That equivalence class is exactly characterized by the [LengthCrossRatio](../concepts/LengthCrossRatio.md) — same cross ratios iff conformally equivalent.
- Extending it across *different* triangulations requires the [IntrinsicDelaunayTriangulation](../concepts/IntrinsicDelaunayTriangulation.md) and [PtolemyFlip](../concepts/PtolemyFlip.md)s, which yields a complete **discrete uniformization theorem** in the spherical, Euclidean, and hyperbolic cases. See [DiscreteUniformization](../concepts/DiscreteUniformization.md).
- Isometry classes of ideal hyperbolic polyhedra correspond to conformal equivalence classes of discrete metrics — the hyperbolic view that unifies the story. See [IdealHyperbolicPolyhedron](../concepts/IdealHyperbolicPolyhedron.md).
- The governing energies are **convex**, so existence and uniqueness are clean and standard convex optimization applies. See [ConvexVariationalPrinciple](../concepts/ConvexVariationalPrinciple.md), [LobachevskyFunction](../concepts/LobachevskyFunction.md).
- Flows: Chow–Luo's combinatorial Ricci flow and Luo's combinatorial Yamabe flow drive a metric toward constant curvature. See [DiscreteRicciFlow](../concepts/DiscreteRicciFlow.md).
- Exact structure preservation is not automatically better than fast inexact numerics — the two are complementary, not ranked.

## Key Quotes

> "What information about a surface is encoded by angles, but not lengths?" — the opening framing of conformal geometry

> "In the discrete setting, however, the idea of literally preserving angles leads to an interpretation of conformal geometry that is far too rigid."

> "The most important features of geometry are not inherently smooth nor discrete, but ... can be faithfully described in either language." — the central thesis of discrete differential geometry

> "This definition again gives the impression of merely aping the smooth relationship — yet in this case the resulting theory is neither too rigid nor too flexible."

> "Even for a completely flat domain, a Euclidean edge flip will (in general) change the discrete conformal structure — even though it does not change the Euclidean geometry."

## Crane's Summary Table

| Approach | Data | Outcome | Why |
|---|---|---|---|
| Angles (§3.1) | interior angles $\theta_i^{jk}$ | too rigid | similarity per triangle forces one global scale factor |
| Dirichlet (§3.3) | vertex coordinates $f_i$ | too rigid | same collapse as Angles |
| Hodge (§3.4) | length ratios $w_{ij}$ | too rigid | uniquely determines the discrete metric |
| Conjugate (§3.5) | vertex coordinates $f_i$ | just right | only under refinement; no finite notion of equivalence |
| Circles — packings (§4) | graph $G = (V, E)$ | too flexible | only combinatorics; cannot distinguish metrics |
| Circles — patterns (§4) | intersection angles | just right | existence not guaranteed for all triangulations |
| Metric (§5) | edge lengths $\ell_{ij}$ | just right | **existence is guaranteed** |

## Connections

- [KeenanCrane](../entities/KeenanCrane.md) — the author
- [BorisSpringborn](../entities/BorisSpringborn.md), [FengLuo](../entities/FengLuo.md) — the two names most load-bearing for uniformization
- [DiscreteConformalEquivalence](../concepts/DiscreteConformalEquivalence.md) → [DiscreteUniformization](../concepts/DiscreteUniformization.md) — the spine of the paper
- [ConformalGeometricAlgebra](../concepts/ConformalGeometricAlgebra.md) — the *only* pre-existing page in this wiki that touches conformal geometry, and the relationship needs care; see Contradictions

## Contradictions

- **None with existing wiki content**, but a scope boundary worth stating explicitly. This wiki previously covered [ProjectiveGeometricAlgebra](../concepts/ProjectiveGeometricAlgebra.md) only. [ConformalGeometricAlgebra](../concepts/ConformalGeometricAlgebra.md) and this paper both concern angle-preserving maps, but they are unrelated frameworks: CGA is an *algebra* in which conformal transformations of continuous space are represented by rotors, whereas Crane studies how to *discretize* conformal structure on triangulated surfaces. **Crane's paper never mentions geometric algebra.** Any link between them is a topical adjacency, not a claim made by either source.
- Internal tension the paper names itself: exact structure preservation often costs more computation than inexact numerical schemes, and the paper explicitly refuses to treat that as a ranking.

## Verification Against the Gold Extraction

The Markdown originally ingested was a shallow text-layer extraction. A proper `pdfdrill` model has since been
built from the same PDF (`~/pdfdrill-library/ConformalGeometryOfSimplicialSurfaces/`, bibkey `crane2020`):
**49 equations with MathPix LaTeX + real page crops, 316 formulas, 51 references, 216 citations.**

Every formula on these wiki pages was compared against that gold LaTeX. All matched except one, now corrected:
the normalized Ricci flow is $\frac{d}{dt}g = (\bar K - K)g$, not $(K - \bar K)g$ — the bar was lost in the
text extraction and the sign was inferred wrongly. See [DiscreteRicciFlow](../concepts/DiscreteRicciFlow.md).

One deliberate deviation remains: equation (6.3) is printed as $\varphi(\alpha, x)$ in the paper; the wiki
writes the second argument as $\lambda$, consistent with the derivative $\partial\varphi/\partial\lambda_{ij}$
stated two lines later.

Citation data: `pdfdrill bibfetch` (Perplexity SONAR) has enriched 10 of the 51 references with full BibTeX
including DOIs and MR numbers. The remaining 41 are printed-text only.

## Source Quality Caveat

The Markdown in `raw/ConformalGeometryOfSimplicialSurfaces.md` is a PDF extraction with **81 of 764 math expressions (10.6%) that do not compile** — `(cid:96)` for $\ell$, `(cid:88)` for $\sum$, `(cid:81)` for $\prod$, HTML entities such as `&gt;` inside math, and raw Unicode where LaTeX commands belong. Every formula quoted on this page and in the concept pages was **re-typeset by hand** from the surrounding prose, not copied. Figures are referenced by number in the source but the images themselves are absent. Section cross-references in the extraction read "Setion" and often run into the following number.
