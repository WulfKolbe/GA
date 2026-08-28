---
title: "A Swift Introduction to Projective Geometric Algebra (transcript)"
type: source
tags: [geometric-algebra, pga, video-transcript, computational-geometry]
date: 2026-08-27
source_file: raw/pga-swift-introduction-transcript.md
---

## Summary

A cleaned transcript of a video introduction to **projective geometric algebra (PGA)**, built without any projective geometry: the presenter does geometric algebra directly on the linear space of lines (2D) or planes (3D). The through-line is that four traditionally unrelated families of formulas — meet, join, projection, and rigid transformation — collapse into four single operations that work on every kind of object in any number of dimensions. It covers 2D PGA in full, then shows 3D PGA reproduces it verbatim, and closes with applications in computer graphics, animation, and rigid body dynamics.

## Key Claims

- PGA is the geometric algebra built on the linear space of lines (2D) or planes (3D); vectors *are* lines/planes, not arrows. See [LinearSpaceOfLines](../concepts/LinearSpaceOfLines.md), [LinearSpaceOfPlanes](../concepts/LinearSpaceOfPlanes.md).
- The whole algebra follows from two rules: distinct basis vectors anticommute, and $e_1^2 = e_2^2 = 1$ while $e_0^2 = 0$. See [GeometricProduct](../concepts/GeometricProduct.md), [DegenerateMetric](../concepts/DegenerateMetric.md).
- Scaling a multivector by any nonzero scalar does not change the geometric object it represents. See [ScaleInvariance](../concepts/ScaleInvariance.md).
- The **meet** (intersection) is the outer product — for every combination of objects. See [Meet](../concepts/Meet.md), [OuterProduct](../concepts/OuterProduct.md).
- The **join** is the regressive product — for every combination of objects. See [Join](../concepts/Join.md), [RegressiveProduct](../concepts/RegressiveProduct.md).
- **Projection**, in all six 3D cases, is the single formula $(B \cdot a)\,a$. See [Projection](../concepts/Projection.md), [InnerProduct](../concepts/InnerProduct.md).
- **Every rigid transformation** — of any object — is the sandwich product $R\,X\,R^\dagger$. See [SandwichProduct](../concepts/SandwichProduct.md), [RigidTransformation](../concepts/RigidTransformation.md).
- Translation is rotation about a [PointAtInfinity](../concepts/PointAtInfinity.md); rotors and translators are the same kind of thing, composed by multiplication. See [Rotor](../concepts/Rotor.md), [Motor](../concepts/Motor.md).
- Exponentiating a bivector gives a rotor: a finite point → rotation about it; a point at infinity → translation. See [ExponentialOfBivector](../concepts/ExponentialOfBivector.md).
- 3D PGA represents lines with [PluckerCoordinates](../concepts/PluckerCoordinates.md), but you never need to know how they work.
- The framework is dimension-independent: the demo turns a spinning 3D cube into a 4D or 5D one by changing one character. See [DimensionIndependence](../concepts/DimensionIndependence.md).
- [ConformalGeometricAlgebra](../concepts/ConformalGeometricAlgebra.md) extends PGA with circles and spheres; historically CGA came first and PGA was seen as a subset of it.

## Key Quotes

> "PGA is the geometric algebra built from the linear space of lines." — the one-sentence definition of 2D PGA

> "Everything we will do in this video can be derived from what is on the screen right here." — after stating anticommutation and $e_0^2 = 0$

> "The outer product of two vectors is simply their intersection." — the geometric reading of the outer product

> "A rotation around a point at infinity is simply a translation." — why PGA unifies rotation and translation

> "I literally just copied and pasted this part of the video from the two-dimensional part." — on the 3D summary being identical to the 2D one

> "We could do a rotating five-dimensional cube as well ... just by changing this single character in the source code!"

## Scope and Caveats Stated by the Source

- Despite the name, **no projective geometry is used**; PGA is developed directly on the linear space of lines/planes. Two other routes exist (via projective geometry, and via rigid transformations) and are not taken.
- Only **Euclidean** PGA is covered. Elliptic and hyperbolic PGA exist and are out of scope.
- Points, lines, and planes at infinity in 3D are mentioned but not developed.
- The inner product of two bivectors in 2D reduces to $-a_3 b_3$ and is dismissed as uninteresting.
- The presenter uses "rotor" loosely, skipping the usual normalization requirement, because [ScaleInvariance](../concepts/ScaleInvariance.md) makes normalization mostly unnecessary.

## Connections

- [ProjectiveGeometricAlgebra](../concepts/ProjectiveGeometricAlgebra.md) — the subject; every other page hangs off it
- [Meet](../concepts/Meet.md), [Join](../concepts/Join.md), [Projection](../concepts/Projection.md), [RigidTransformation](../concepts/RigidTransformation.md) — the four operations the source is organized around
- [DimensionIndependence](../concepts/DimensionIndependence.md) — the payoff claim demonstrated by the cube demo
- [ConformalGeometricAlgebra](../concepts/ConformalGeometricAlgebra.md) — the named generalization beyond PGA

## Contradictions

- None with existing wiki content — this is the first source in this wiki.
- Internal tension worth noting: the source calls the subject "projective geometric algebra" while explicitly not doing projective geometry, and flags this itself.
