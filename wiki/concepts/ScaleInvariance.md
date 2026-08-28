---
title: "Scale Invariance"
type: concept
tags: [pga, foundations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Scale Invariance

**Scaling a PGA multivector by any nonzero value does not change the geometric object it represents.** The line $e_2 + e_0$ and the line $2e_2 + 2e_0$ are the same line; the bivector for a point can be rescaled at will.

This holds for *all* PGA objects, at every grade, and the source flags it early as something to keep in mind throughout.

## Why it matters in practice

- **Normalizing is optional.** A bivector's point coordinates are recovered by dividing by its $e_{12}$ component — which is just normalization — but you rarely need to.
- **Stray scalar factors can be dropped.** Reflecting a point produces a factor of $a^2$; it is simply discarded.
- **The projection formula loses its inverse.** The arrow formula $(B \cdot a)\,a^{-1}$ becomes $(B \cdot a)\,a$ in PGA, since the inverse only contributes a scalar. See [Projection](Projection.md).
- **"Rotor" is used loosely.** The standard definition requires normalized vectors; PGA usually does not bother. See [Rotor](Rotor.md).

## Related

- [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md), [DegenerateMetric](DegenerateMetric.md)
