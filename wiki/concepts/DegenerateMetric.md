---
title: "Degenerate Metric"
type: concept
tags: [pga, foundations, algebra]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Degenerate Metric ($e_0^2 = 0$)

The single algebraic quirk that separates [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) from ordinary geometric algebra.

In geometric algebra a vector squares to its magnitude squared. In PGA the magnitude formula deliberately **ignores the $e_0$ component**, so:

$$
e_1^2 = e_2^2 = 1 \qquad e_0^2 = 0
$$

$e_0$ is the [LineAtInfinity](LineAtInfinity.md) (2D) or the plane at infinity (3D). Its null square is what makes the metric *degenerate*, and it is doing real work everywhere:

- The inner product with $e_0$ is always zero, so $e_0$ is simultaneously parallel and perpendicular to every vector.
- Adding multiples of $e_0$ shifts objects without changing magnitude or inner products — the mechanism behind translation.
- In [ExponentialOfBivector](ExponentialOfBivector.md), an argument containing $e_0$ squares to **zero** rather than $-1$, so Euler's formula is replaced by a two-term Taylor series — and the rotation becomes a translation.

Together with anticommutation of distinct basis vectors, this is the *entire* definition of the geometric product in PGA: "everything we will do in this video can be derived from what is on the screen right here."

## Related

- [GeometricProduct](GeometricProduct.md), [PointAtInfinity](PointAtInfinity.md), [ScaleInvariance](ScaleInvariance.md)
