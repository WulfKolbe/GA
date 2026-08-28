---
title: "Inner Product"
type: concept
tags: [pga, products]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Inner Product

For vectors, the inner product in the [LinearSpaceOfLines](LinearSpaceOfLines.md) is the familiar one with the $e_0$ component omitted. The interesting cases are **mixed grades** — and they are what makes the single [Projection](Projection.md) formula possible.

## The general rule

> The inner product of two objects is the object **perpendicular to the higher-dimensional object, passing through the lower-dimensional one.**

Mechanically: project the lower-grade element onto the higher-grade one, then contract.

## Cases

**2D — point $\cdot$ line** → the line perpendicular to the given line passing through the point. (Projecting a line onto a point's subspace and contracting removes every line with a component along the original.)

**3D:**

| operands | result |
|---|---|
| plane $\cdot$ line | the plane $\perp$ to the input plane through the line |
| plane $\cdot$ point | the line $\perp$ to the plane through the point |
| line $\cdot$ point | the plane $\perp$ to the line through the point |

## Two useful identities

- **Incidence:** if an object lies *on* another, their [GeometricProduct](GeometricProduct.md) equals their inner product (the outer product term vanishes). Holds in 2D and in all three 3D cases.
- **bivector $\cdot$ bivector** in 2D reduces to $-a_3 b_3$ — normalized, that is a constant, so it carries no geometric information and the source drops it.

## Related

- [Projection](Projection.md) — built entirely out of these cases
