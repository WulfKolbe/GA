---
title: "Rotor"
type: concept
tags: [pga, transformations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Rotor

The product of an even number of vectors, e.g. $R = uv$. Applied by the [SandwichProduct](SandwichProduct.md):

$$
R\,X\,R^\dagger
$$

where $\dagger$ is the reverse — reversing the order of vectors in a product.

## Two reflections make a rotation

Reflecting across two lines is a rotation about their intersection point by **twice** the angle between them — as usual in geometric algebra. And if the two lines are **parallel**, they meet at a [PointAtInfinity](PointAtInfinity.md), and the "rotation" turns out to be a **translation** by twice the distance between them.

## Terminology

Strictly, a rotor requires normalized vectors. Because [ScaleInvariance](ScaleInvariance.md) makes normalization mostly unnecessary in PGA, the source is deliberately lax about this. Some authors reserve "rotor" for genuine rotations and use [Motor](Motor.md) for the general case.

## Composition

Rotors compose by plain multiplication: $R = R_1R_2R_3$ applies as a single rotor. This is the concrete advantage over rotation matrices / complex numbers / quaternions **plus** separate vector addition for translation, where composing the two kinds of operation is awkward.

## Related

- [ExponentialOfBivector](ExponentialOfBivector.md) — the exponential form
- [RigidTransformation](RigidTransformation.md)
