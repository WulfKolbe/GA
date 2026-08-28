---
title: "Projection"
type: concept
tags: [pga, operations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Projection

One formula, every pair of objects, every dimension:

$$
(B \cdot a)\,a
$$

$a$ and $B$ may be a line and a point, a plane and a line, a plane and a point — anything. **Which** projection you get depends only on which argument you feed where, and both directions come from the same expression.

## Why it works

$B \cdot a$ is perpendicular to $a$ ([InnerProduct](InnerProduct.md)), so:

- multiplying it by $a$ gives their [Meet](Meet.md) → **B projected onto a**
- multiplying it by $B$ — which lies entirely inside the inner product — gives their inner product → **a projected onto B**

The two readings look almost identical algebraically and are geometrically symmetric.

## Relation to the arrow formula

This is essentially the classical projection formula for arrows. The only difference is the missing inverse: the arrow version needs $a^{-1}$, but by [ScaleInvariance](ScaleInvariance.md) a scalar factor is irrelevant in PGA, so it is dropped.

## What it replaces

In 2D, two traditional formulas — projecting a line onto a point is easy; projecting a point onto a line is bad enough that the source could only find a *procedure* in the literature and had to derive the explicit formula, remarking "I can see now why people never use it."

In 3D there are **six** kinds of projection (line↔plane, point↔plane, point↔line). All six are this one formula.

## Related

- [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md), [Meet](Meet.md), [GeometricProduct](GeometricProduct.md)
