---
title: "Intrinsic Delaunay Triangulation"
type: concept
tags: [discrete-differential-geometry, combinatorics]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Intrinsic Delaunay Triangulation

The canonical triangulation that lets discrete conformal equivalence range over *different* combinatorics.

In the plane, Delaunay is usually stated as the empty-circumcircle condition. The equivalent **angle sum** form is what generalizes: for triangles $ijk, jil$ sharing edge $ij$,

$$
\theta_k^{ij} + \theta_l^{ji} \le \pi.
$$

![Eq (5.4) as printed on page 24](../gold/crops/crane2020_EQ0035.jpg)

*Gold extraction: [crane2020_EQ0035](../gold/crane2020_EQ0035.md) — eq (5.4), ConformalGeometryOfSimplicialSurfaces.pdf p. 24.*

This needs only interior angles, which a [DiscreteMetric](DiscreteMetric.md) already determines — so it applies to any triangulated surface, with no embedding required. A discrete surface satisfying it at every edge is **intrinsic Delaunay**.

## Existence, uniqueness, computation

- Every polyhedral [ConeMetric](ConeMetric.md) admits one: there is always a triangulation of the cone points whose geodesic arcs satisfy the condition — arcs that need not follow the extrinsic edges.
- It is **unique** as long as no two adjacent triangles are cocircular. Cocircular pairs satisfy the condition with equality either way, since opposite angles of a cyclic quadrilateral sum to $\pi$.
- **Algorithm:** flip non-Delaunay edges in any order until all satisfy the condition. This terminates in finitely many flips.

A subtlety: the resulting triangulation is generally **not simplicial** — two edges of one triangle may be identified — which is why $\Delta$-complexes are the right setting.

## Why it is the right canonical choice

Different triangulations of the same Euclidean polyhedron induce *different* hyperbolic metrics. The Delaunay triangulation is special because Euclidean and hyperbolic ([PtolemyFlip](PtolemyFlip.md)) flips coincide exactly when the triangulation fails to be unique, i.e. on cocircular pairs. That coincidence is what makes the two formulations of [DiscreteUniformization](DiscreteUniformization.md) equivalent.

## Related

- [DiscreteConformalEquivalence](DiscreteConformalEquivalence.md), [SteinersProblem](SteinersProblem.md)
