---
title: "Point at Infinity"
type: concept
tags: [pga, foundations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Point at Infinity

A 2D PGA bivector with **no $e_{12}$ component**. Since a bivector's point is recovered by dividing by its $e_{12}$ coefficient, such a bivector cannot be normalized — and as that coefficient tends to zero, the point it represents shoots off to infinity.

Unlike the single [LineAtInfinity](LineAtInfinity.md), there are **many** points at infinity: one for every direction.

## Where they come from

- [Meet](Meet.md) of a line with the line at infinity → the point at infinity in the line's direction $(b,\,-a)$.
- Meet of two **parallel** lines → the same thing. Writing the second line as $a + \lambda e_0$, the $a \wedge a$ term vanishes and only $a \wedge e_0$ survives. Parallel lines converge on the horizon.

## Why they matter

They are the mechanism that unifies rotation and translation. A rotation about a point at infinity **is a translation** — the further the centre of rotation, the more a rotation resembles a translation, and infinitely far away it becomes one exactly. See [Rotor](Rotor.md), [Motor](Motor.md), [ExponentialOfBivector](ExponentialOfBivector.md).

## Related

- [DegenerateMetric](DegenerateMetric.md), [RigidTransformation](RigidTransformation.md)
