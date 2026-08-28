---
title: "Geometric Product"
type: concept
tags: [pga, products, core]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Geometric Product

The fundamental product of [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) — "the most important part of PGA." Every other product (outer, regressive, inner) is defined in terms of it.

Its definition is two lines: distinct basis vectors anticommute, and basis vectors square to their magnitude squared, which in PGA means $e_1^2 = e_2^2 = 1$ and $e_0^2 = 0$ ([DegenerateMetric](DegenerateMetric.md)).

## Identities used throughout

- **Perpendicular objects:** their geometric product equals their outer product — so it is their [Meet](Meet.md). True for two perpendicular planes, three perpendicular planes, and a plane with a perpendicular line.
- **Incident objects:** the geometric product of an object with something lying *on* it equals their [InnerProduct](InnerProduct.md). If point $B$ lies on line $a$, then $aB = a \cdot B$, because the outer product term vanishes.
- **Vector $\times$ bivector:** $aB = a \cdot B + a \wedge B$ — the split used to derive both facts above.

## What it buys you

- Sandwiching reflects: $a\,u\,a$ — see [SandwichProduct](SandwichProduct.md)
- Products of even numbers of vectors are rotors — see [Rotor](Rotor.md)
- Rotors compose by plain multiplication, unlike rotation matrices plus vector addition

## Related

- [OuterProduct](OuterProduct.md), [RegressiveProduct](RegressiveProduct.md), [InnerProduct](InnerProduct.md)
