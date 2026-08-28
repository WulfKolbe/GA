---
title: "Discrete Differential Geometry"
type: concept
tags: [discrete-differential-geometry, methodology]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Discrete Differential Geometry

The discipline of building discrete theories that *exactly* preserve structure from smooth differential geometry, rather than merely approximating it in the limit of refinement.

## "The Game"

Crane describes discretization of conformal maps as an excellent example of "The Game" played in discrete differential geometry: take a smooth notion with many equivalent characterizations ([ConformalMapCharacterizations](ConformalMapCharacterizations.md)), discretize each one, and see which discrete theory you land in. Since the equivalences do not survive discretization, the choice of starting point *is* the design decision.

## The central thesis

> The most important features of geometry are not inherently smooth nor discrete, but can be faithfully described in either language.

## The honest tradeoff

Crane is explicit that structure preservation is **not** a value judgement on utility:

- Exact structure-preserving schemes typically cost more computation.
- Inexact numerical schemes are often perfectly adequate, especially on fine tessellations.
- The mature reading is that they are **complementary**: fast numerics initialize or approximate intermediate steps for exact schemes, which in turn supply the guarantees.

The field also bridges areas that otherwise stay apart — geometry, analysis, combinatorics, and Euclidean vs. hyperbolic geometry ([IdealHyperbolicPolyhedron](IdealHyperbolicPolyhedron.md), [SteinersProblem](SteinersProblem.md)).

## Related

- [DiscretizationRigidity](DiscretizationRigidity.md), [DiscreteUniformization](DiscreteUniformization.md)
