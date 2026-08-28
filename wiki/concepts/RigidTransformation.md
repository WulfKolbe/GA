---
title: "Rigid Transformation"
type: concept
tags: [pga, transformations, applications]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Rigid Transformation

Rotations, translations, reflections, and their compositions. In [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) **every** one of them, acting on **every** kind of object, is the [SandwichProduct](SandwichProduct.md) $R\,X\,R^\dagger$.

Built up from the bottom: reflection is $u\,a\,u$; two reflections give a rotation (intersecting mirrors) or a translation (parallel mirrors); enough reflections give any rigid transformation. See [Rotor](Rotor.md).

## The two problems this solves

**1. Composition.** Traditionally rotations use rotation matrices, complex numbers, or quaternions, while translations use vector addition — two different mechanisms that are annoying to compose. In PGA both are rotors, so composing them is multiplication: $R = R_1R_2R_3$.

**2. Centre of rotation.** Traditional orthogonal transformations can only rotate **about the origin**. Rotating about some other point $p$ requires the subtract–rotate–add dance. In PGA "rotations don't care about what point they're rotating around" — every rotation, about any point or any axis, is the same formula.

## Uniformity across objects

Because reflection has the same form for points as for lines, and everything is built from reflections, one formula transforms points, lines, and planes alike — in any dimension ([DimensionIndependence](DimensionIndependence.md)).

## Related

- [ExponentialOfBivector](ExponentialOfBivector.md), [Motor](Motor.md), [PointAtInfinity](PointAtInfinity.md)
