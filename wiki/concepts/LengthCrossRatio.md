---
title: "Length Cross Ratio"
type: concept
tags: [conformal-geometry, invariants]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Length Cross Ratio

The invariant that pins down a discrete conformal class. For two triangles $ijk, jil$ sharing edge $ij$:

$$
c_{ij} := \frac{\ell_{il}\,\ell_{jk}}{\ell_{ki}\,\ell_{lj}}.
$$

![Eq (5.3) as printed on page 22](../gold/crops/crane2020_EQ0032.jpg)

*Gold extraction: [crane2020_EQ0032](../gold/crane2020_EQ0032.md) — eq (5.3), ConformalGeometryOfSimplicialSurfaces.pdf p. 22.*

> **Theorem.** Two discrete metrics on the same triangulation are discretely conformally equivalent **iff** they induce the same length cross ratios.

## Why

*Forward*: substituting $\tilde\ell_{ij} = e^{(u_i+u_j)/2}\ell_{ij}$ into $\tilde c$, the exponential factors at $i, j, k, l$ appear once in the numerator and once in the denominator and cancel exactly.

*Backward*: by the single-triangle lemma of [DiscreteConformalEquivalence](DiscreteConformalEquivalence.md) each triangle already admits compatible scale factors; the condition that adjacent triangles agree on their shared edge works out, via the explicit formula for $e^{u_i}$, to equality of cross ratios.

## What it means

The cross ratios $c : E \to \mathbb{R}_{>0}$ effectively specify a point in the **Teichmüller space** of discrete metrics. For a surface immersed in $\mathbb{R}^n$ they are preserved by Möbius transformations of the vertices. But the space of maps inducing a conformally equivalent metric is much larger than the Möbius transformations — one characterization is that discrete conformal maps are the piecewise projective maps preserving triangle circumcircles.

The cross ratio also reappears in hyperbolic clothing: shear coordinates satisfy $\sigma_{ij} = \log c_{ij}$. See [IdealHyperbolicPolyhedron](IdealHyperbolicPolyhedron.md).

## Related

- [PtolemyFlip](PtolemyFlip.md), [DiscreteUniformization](DiscreteUniformization.md)
