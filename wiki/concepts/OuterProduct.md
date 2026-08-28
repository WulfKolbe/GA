---
title: "Outer Product"
type: concept
tags: [pga, products]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Outer Product

In geometric algebra the outer product of two vectors represents their **span**. In [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) that span has a startlingly simple geometric reading: it is the **intersection** of the objects — the [Meet](Meet.md).

## Why span = intersection here

In the [LinearSpaceOfLines](LinearSpaceOfLines.md), every linear combination of two lines passes through their intersection point, and every line through that point is reachable. So the span of two line-vectors is *the set of all lines through one point* — a set uniquely determined by that point. Rather than carry the whole set around, identify the bivector **with the point**.

## The verification

Expanding $a \wedge b$ for arbitrary lines $a$, $b$: terms of the form $v \wedge v$ vanish, swaps cost a minus sign, outer products of distinct basis vectors are their geometric products, and the basis bivectors factor out. Divide through by the $e_{12}$ coefficient — legal by [ScaleInvariance](ScaleInvariance.md) — and the remaining coefficients are *exactly* the coordinates you get by solving the two line equations simultaneously.

The outer product and the intersection were defined completely independently. They are the same thing.

## In 3D

Same operation, all three cases: plane $\wedge$ plane = their line, plane $\wedge$ plane $\wedge$ plane = their point, plane $\wedge$ line = their point (write the line as the outer product of two planes and it reduces to the three-plane case).

## Related

- [Meet](Meet.md), [GeometricProduct](GeometricProduct.md), [GradeGeometryCorrespondence](GradeGeometryCorrespondence.md)
