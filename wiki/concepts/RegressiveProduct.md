---
title: "Regressive Product"
type: concept
tags: [pga, products]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Regressive Product

The regressive product of two objects is their **common subspace** — the dual counterpart to the [OuterProduct](OuterProduct.md). In [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) it is the [Join](Join.md).

## 2D

The only interesting 2D case is point ∨ point. Remember that a point *is* the set of all lines through it. A line lies in both subspaces exactly when it passes through both points — and there is only one such line. So the regressive product of two points is the line joining them.

Compare the traditional route: point-slope form, then algebra to reach general form. In PGA you never touch components.

## 3D

- point ∨ point = the line through them
- line ∨ point = the plane through both (the unique plane common to both subspaces)
- point ∨ point ∨ point = the plane through all three — derivable by joining the first two into a line, then joining that line with the third point

One operation, three traditional formulas replaced.

## Related

- [Join](Join.md), [Meet](Meet.md), [LinearSpaceOfPlanes](LinearSpaceOfPlanes.md)
