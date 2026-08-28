---
title: "Motor"
type: concept
tags: [pga, transformations, terminology]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Motor

Some PGA practitioners use **motor** rather than [Rotor](Rotor.md) for the general even-grade transformation object, to emphasize that it represents **translations as well as rotations** — reserving "rotor" for motors that are genuine rotations.

The source notes the convention but does not adopt it, calling everything a rotor.

The substantive point behind the naming is the one that matters: rotation and translation are the same kind of object in [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md), differing only in whether the centre of rotation is finite or a [PointAtInfinity](PointAtInfinity.md) — so they compose by multiplication like anything else.

## Related

- [RigidTransformation](RigidTransformation.md), [ExponentialOfBivector](ExponentialOfBivector.md)
