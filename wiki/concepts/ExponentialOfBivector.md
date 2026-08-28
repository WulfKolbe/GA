---
title: "Exponential of a Bivector"
type: concept
tags: [pga, transformations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Exponential of a Bivector

Rotors are conventionally written as exponentials of bivectors. In 2D [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) bivectors are points, so this asks: *what is the exponential of a point?*

Note that here — unusually for PGA — the **magnitude of the argument matters**, so the vectors are taken to be unit vectors.

## Finite point → rotation about that point

Write the point as $uv$ with $u \perp v$ unit vectors. Then $(uv)^2 = -1$, so Euler's formula applies:

$$
\exp(\theta\,uv) = \cos\theta + \sin\theta\,uv
$$

Multiply the first term by $u^2 = 1$ and factor out $u$: the result is a product of two vectors, hence a [Rotor](Rotor.md). Since $u$ and $v$ have equal magnitude they add like vectors, so the second factor is $u$ rotated by $\theta$. Used in a [SandwichProduct](SandwichProduct.md), this rotates by **$2\theta$ about $uv$**.

> Exponentiating a point produces a rotation *around* that point — at an arbitrary angle, about an arbitrary point $P$.

## Point at infinity → translation

A [PointAtInfinity](PointAtInfinity.md) is the [Meet](Meet.md) of a vector with the [LineAtInfinity](LineAtInfinity.md); since $e_0$ is perpendicular to every vector, that meet is just the geometric product $u\,e_0$.

Now the argument contains $e_0$, so it squares to **zero**, not $-1$ ([DegenerateMetric](DegenerateMetric.md)) — Euler's formula no longer applies. Expand the Taylor series instead: every term past the first two carries a factor of $(u\,e_0\,x)^2$ and vanishes, leaving two terms. Multiply by $u^2 = 1$, factor out $u$, and again you have a product of two vectors — a rotor. Since adding $x\,e_0$ shifts a line by $x$, the sandwich product yields a **translation by 2x perpendicular to $u$**.

Same construction, same object type, different metric behaviour — rotations and translations really are the same thing here.

## In 3D

Identical, except the bivector is now a **line** rather than a point, and it plays the role of the **axis of rotation**.

## Related

- [Rotor](Rotor.md), [Motor](Motor.md), [RigidTransformation](RigidTransformation.md)
