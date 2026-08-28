---
title: "Linear Space of Lines"
type: concept
tags: [pga, foundations, 2d]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Linear Space of Lines

The foundation of 2D [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md). Lines in the plane are written as linear equations and treated as vectors over the basis $e_1,\ e_2,\ e_0$:

- $e_1$ — the vertical line through the origin
- $e_2$ — the horizontal line through the origin
- $e_0$ — the [LineAtInfinity](LineAtInfinity.md)

So the horizontal line is $e_2 + e_0$, and a slanted line is $e_1 - e_2 + e_0$.

## Structure

- **Addition** of two lines gives a line through their intersection; the coefficients set how close the result sits to each input. Every line through that intersection is reachable.
- **Adding a multiple of $e_0$** shifts a line without rotating it.
- **Scaling** changes nothing about which line is represented — see [ScaleInvariance](ScaleInvariance.md).
- **Magnitude** is the usual Euclidean formula *with the $e_0$ component ignored*, which is exactly why $e_0^2 = 0$ ([DegenerateMetric](DegenerateMetric.md)).

## Inner product

Derived from the magnitude, so the $e_0$ component drops out of it too. Geometrically it behaves like the inner product of arrows: $a \cdot b = |a||b|\cos\theta$. Because $e_0$ never contributes, lines can be **shifted freely without changing the inner product**.

- perpendicular ⟺ $a \cdot b = 0$
- parallel ⟺ $|a \cdot b| = |a||b|$

## Two consequences worth remembering

1. $e_0$ is both perpendicular *and* parallel to every vector — it behaves like a zero vector under the inner product.
2. Parallelism does **not** require being a scalar multiple. $a$ and $\lambda e_0 + a$ are parallel: the $e_0$ term vanishes in the inner product, and $|\lambda e_0 + a| = |a|$. Geometrically these are two parallel shifted copies of the same line — so the algebraic and geometric notions of parallel agree.

## Related

- [LinearSpaceOfPlanes](LinearSpaceOfPlanes.md) — the 3D analogue, structurally identical
- [InnerProduct](InnerProduct.md) — extended beyond vectors
