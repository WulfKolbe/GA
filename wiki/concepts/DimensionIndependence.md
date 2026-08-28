---
title: "Dimension Independence"
type: concept
tags: [pga, applications]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Dimension Independence

The headline payoff of [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md): the four operations are **identical in every dimension**.

- [Meet](Meet.md) = [OuterProduct](OuterProduct.md)
- [Join](Join.md) = [RegressiveProduct](RegressiveProduct.md)
- [Projection](Projection.md) = $(B \cdot a)\,a$
- [RigidTransformation](RigidTransformation.md) = [SandwichProduct](SandwichProduct.md)

The source makes the point by copy-pasting its 2D summary verbatim as the 3D summary. In n dimensions, vectors are $(n-1)$-dimensional hyperplanes, pseudovectors are points, intermediate grades are everything in between — and the four operations are unchanged. See [GradeGeometryCorrespondence](GradeGeometryCorrespondence.md).

## The demo

A spinning-cube animation, with the screen projection done by hand rather than by the renderer. Rotation takes **one line**; projection takes **one line**. The dimension appears in exactly **one place** in the source — so changing a single character turns the 3D cube into a rotating 4D cube, or 5D, or any dimension at all.

## Contrast

Ordinary 3D vector algebra needs a representation per object type — a vector+scalar pair for planes, [PluckerCoordinates](PluckerCoordinates.md) for lines, a vector for points — and then 3 meet formulas, 3 join formulas, and 6 projection formulas. None of them generalize by changing a number.

## Related

- [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md)
