---
title: "Meet"
type: concept
tags: [pga, operations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Meet

The intersection of two geometric objects — "where two lines meet." In [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) the meet **is the [OuterProduct](OuterProduct.md)**, in every case and every dimension.

## 2D

$a \wedge b$ of two lines is the point they cross. Special cases fall out for free:

- **Line $\wedge$ line at infinity** = the [PointAtInfinity](PointAtInfinity.md) in the direction of the line. An arbitrary line $ax + by + c$ runs in direction $(b,\,-a)$, and the computation returns exactly that point at infinity.
- **Two parallel lines.** Write the second as $a + \lambda e_0$. The $a \wedge a$ term vanishes, leaving $a \wedge e_0$ — the point at infinity in the line's direction. Geometrically right: parallel lines converge on the horizon.
- **Perpendicular lines:** their meet equals their plain [GeometricProduct](GeometricProduct.md).

## 3D

Vector algebra needs three *different* formulas here — plane∩plane (a line), plane∩line (a point), three planes (a point). PGA uses the outer product for all three.

## Related

- [Join](Join.md) — the dual operation
- [PointAtInfinity](PointAtInfinity.md), [LineAtInfinity](LineAtInfinity.md)
