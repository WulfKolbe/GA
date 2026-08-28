---
title: "Projective Geometric Algebra"
type: concept
tags: [pga, geometric-algebra, core]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Projective Geometric Algebra

PGA is the geometric algebra built on the [LinearSpaceOfLines](LinearSpaceOfLines.md) (2D) or the [LinearSpaceOfPlanes](LinearSpaceOfPlanes.md) (3D) — not on the usual space of arrows. Its vectors *are* lines or planes; points appear as higher-grade elements.

## Why the name is misleading

It was originally described as geometric algebra plus projective geometry. Other developments skip projective geometry entirely: one builds it from rigid transformations, another — the route taken by the source — does geometric algebra directly on the linear space of lines or planes. So PGA can be presented with **no projective geometry at all**.

PGA is also not restricted to Euclidean geometry; elliptic and hyperbolic PGA exist. Only Euclidean PGA is covered here.

## The entire foundation

Two rules generate everything:

1. Distinct basis vectors anticommute (as in any geometric algebra).
2. $e_1^2 = e_2^2 = 1$, but $e_0^2 = 0$ — see [DegenerateMetric](DegenerateMetric.md).

Every other product — outer, regressive, inner — is defined in terms of the [GeometricProduct](GeometricProduct.md).

## Grades and what they represent

| | 2D PGA (3-dim algebra) | 3D PGA (4-dim algebra) |
|---|---|---|
| vector | line | plane |
| bivector | **point** | line |
| trivector | pseudoscalar | **point** |

Note the dimensional offset: 2D PGA is *algebraically* three-dimensional, so it inherits the behaviour of 3D geometric algebra even though the geometry is planar. See [GradeGeometryCorrespondence](GradeGeometryCorrespondence.md).

## The four operations

- [Meet](Meet.md) (intersection) = [OuterProduct](OuterProduct.md)
- [Join](Join.md) = [RegressiveProduct](RegressiveProduct.md)
- [Projection](Projection.md) = $(B \cdot a)\,a$, via the [InnerProduct](InnerProduct.md)
- [RigidTransformation](RigidTransformation.md) = [SandwichProduct](SandwichProduct.md) $R\,X\,R^\dagger$

Each is a *single* operation covering every combination of object types — replacing 3 meet formulas, 3 join formulas, and 6 projection formulas in ordinary vector algebra. They are identical in 2D, 3D, and n dimensions ([DimensionIndependence](DimensionIndependence.md)).

## Related

- [ScaleInvariance](ScaleInvariance.md) — nonzero scaling never changes the object represented
- [Rotor](Rotor.md), [Motor](Motor.md) — rotations and translations as one composable object
- [ConformalGeometricAlgebra](ConformalGeometricAlgebra.md) — the extension that adds circles and spheres
