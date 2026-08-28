---
title: "Steiner's Problem"
type: concept
tags: [hyperbolic-geometry, combinatorics, history]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Steiner's Problem

Posed by Jakob Steiner in the 19th century:

> Given a convex polyhedron, when can you find a combinatorially equivalent convex polyhedron inscribed in the sphere (or another quadratic surface)?

Equivalently: which combinatorial tessellations of the 2-sphere can be realized as convex polyhedra with all vertices on the sphere? Crane notes this is very much in the spirit of [DiscreteDifferentialGeometry](DiscreteDifferentialGeometry.md) — a finite analogue of the sphere that exactly preserves a key property of its smooth counterpart, namely convexity.

## Not all of them

The octahedron sits on the sphere. The **stellated** octahedron — each face split into three — cannot be made convex with vertices on the sphere, no matter where they are placed (Rivin). Only certain "nice" combinatorial tessellations of the topological sphere can be read as geometric spheres.

Restated: every planar Delaunay triangulation is the stereographic image of a sphere-inscribed convex polyhedron, so Steiner's question asks **which combinatorial triangulations can be realized as planar Delaunay triangulations**. See [IntrinsicDelaunayTriangulation](IntrinsicDelaunayTriangulation.md).

## The resolution, 150 years later

The general solution came from reframing it hyperbolically (Rivin), via the bridge in [IdealHyperbolicPolyhedron](IdealHyperbolicPolyhedron.md): interpret each Euclidean triangle as an ideal triangle in the Klein model, and building a convex sphere-inscribed Euclidean polyhedron with given combinatorics becomes finding a convex *ideal hyperbolic* polyhedron with the same combinatorics.

## The chain of equivalences

Circle patterns with prescribed intersection angles
$\;\Leftrightarrow\;$ convex ideal hyperbolic polyhedra with prescribed dihedral angles
$\;\Leftrightarrow\;$ convex Euclidean polyhedra inscribed in the sphere
$\;\Leftrightarrow\;$ planar Delaunay triangulations.

In the Poincaré half-space model of $H^3$, two Euclidean circles meeting at angle $\Phi_{ij}$ are two copies of $H^2$ meeting at that dihedral angle — which is what makes the first link work. See [CirclePattern](CirclePattern.md).

## Related

- [ConvexVariationalPrinciple](ConvexVariationalPrinciple.md)
