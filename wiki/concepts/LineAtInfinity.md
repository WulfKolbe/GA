---
title: "Line at Infinity"
type: concept
tags: [pga, foundations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Line at Infinity

The basis vector $e_0$ in 2D [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md). Its 3D counterpart is the plane at infinity.

Its defining property is $e_0^2 = 0$ — see [DegenerateMetric](DegenerateMetric.md) — which follows from the magnitude formula ignoring the $e_0$ component.

## Behaviour

- Adding a scalar multiple of $e_0$ to a line **shifts** it, leaving direction and magnitude untouched.
- Its inner product with anything is zero, making it both parallel and perpendicular to every vector — much like a zero vector.
- Its [Meet](Meet.md) with any line is the [PointAtInfinity](PointAtInfinity.md) in that line's direction.
- Unlike points at infinity there is only **one** line at infinity.

## Related

- [PointAtInfinity](PointAtInfinity.md), [LinearSpaceOfLines](LinearSpaceOfLines.md)
