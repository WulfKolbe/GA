---
title: "Linear Space of Planes"
type: concept
tags: [pga, foundations, 3d]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Linear Space of Planes

The foundation of 3D [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md), and "surprisingly similar" to the [LinearSpaceOfLines](LinearSpaceOfLines.md). Moving up a dimension is just adding one basis vector, turning the line equation into a plane equation.

Four basis vectors: three orthogonal planes through the origin, plus $e_0$, the **plane at infinity**.

- A linear combination of two planes is another plane through their line of intersection; coefficients say how close it sits to each input, and every such plane is reachable.
- Magnitude is again the usual formula with the $e_0$ component omitted — hence $e_0^2 = 0$ ([DegenerateMetric](DegenerateMetric.md)).

## Grades

| grade | components | represents |
|---|---|---|
| scalar | 1 | — |
| vector | 4 | plane |
| bivector | 6 | line |
| trivector | 4 | point |
| pseudoscalar | 1 | — |

Bivectors are 2D subspaces of planes — all planes through a common line — which are uniquely fixed by that line, so the bivector *is* the line. Trivectors are all planes through a common point, so the trivector *is* the point. See [GradeGeometryCorrespondence](GradeGeometryCorrespondence.md).

Numerically, points follow the same pattern as the 2D case, and lines turn out to use [PluckerCoordinates](PluckerCoordinates.md) — which you never have to learn, because PGA manipulates lines geometrically.

## Related

- [Meet](Meet.md), [Join](Join.md) — three kinds of each in 3D, one operation for all of them
