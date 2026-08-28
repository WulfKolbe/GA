---
title: "Sandwich Product (Reflection)"
type: concept
tags: [pga, transformations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Sandwich Product (Reflection)

$u\,a\,u$ reflects $a$ across $u$. This is the base case from which every [RigidTransformation](RigidTransformation.md) in [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) is built.

The treatment starts here rather than with a rotation formula because 2D PGA is *algebraically* three-dimensional, so the usual 2D rotation formula does not hold outside special subspaces. See [GradeGeometryCorrespondence](GradeGeometryCorrespondence.md).

## The derivation sketch

Decompose $u$ into components parallel and perpendicular to $a$:

- **Parallel part:** $u_\parallel$ and $a$ represent the same line, so their product is a scalar — $u_\parallel\,a\,u$ is a scalar multiple of $u$, hence the same line ([ScaleInvariance](ScaleInvariance.md)).
- **Perpendicular part:** perpendicular objects multiply to their [Meet](Meet.md), and the product of a line with a point on it is their [InnerProduct](InnerProduct.md) — giving the perpendicular line.

Both parts are multiplied by the same thing, so their relative magnitudes are preserved; the angle between the sum and $u_\parallel\,a\,u$ matches the angle between $u$ and $u_\parallel$. The result is a reflection.

## It works on every object

Reflecting a **point** across a line $a$: write the point as the geometric product of two perpendicular lines $u$, $v$; reflect each; the reflection is the meet of $a\,u\,a$ and $a\,v\,a$, which — still being perpendicular — is just their geometric product. A leftover factor of $a^2$ is scalar and gets dropped.

The resulting formula is **identical** to the one for reflecting lines. The sandwich product is grade-agnostic: one formula for every multivector, which is exactly what lets rigid transformations act uniformly on points, lines, and planes.

## Related

- [Rotor](Rotor.md), [Motor](Motor.md), [GeometricProduct](GeometricProduct.md)
