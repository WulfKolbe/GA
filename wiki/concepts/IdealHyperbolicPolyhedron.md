---
title: "Ideal Hyperbolic Polyhedron"
type: concept
tags: [hyperbolic-geometry, conformal-geometry]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Ideal Hyperbolic Polyhedron

The hyperbolic reformulation that "helps to simplify and unify the story."

## Why hyperbolic

Ideal hyperbolic polyhedra are easier to construct than Euclidean ones because they are more rigid. Convex hyperbolic polyhedra are essentially determined by their dihedral angles, whereas Euclidean ones are not. And although Alexandrov's theorem says a convex Euclidean polyhedron is determined by its metric, actually building the embedding is hard — while an ideal convex hyperbolic polyhedron with prescribed metric is the minimizer of a convex energy.

## Models

$H^2$ is the complete simply-connected surface of constant curvature $K = -1$; it cannot be isometrically embedded in $\mathbb{R}^3$, so one uses models.

- **Poincaré disk** — conformal: faithful angles, geodesics as circular arcs orthogonal to $\partial D^2$.
- **Klein disk** — faithful straight-line geodesics, distorted angles.
- **Hyperboloid** — one sheet of $x^2 + y^2 - t^2 = -1$, geodesics as intersections with planes through the origin. Homogeneous projection $(x, y, t) \mapsto (x/t, y/t)$ gives the Klein model; shifting a unit along $t$ first gives Poincaré.

An **ideal triangle** is bounded by three pairs of limiting parallels; all its angles are zero, all its edges infinite, and **all ideal triangles are congruent**.

## The construction

Take a Euclidean triangle, view its circumcircle as a copy of $H^2$ in the Klein model, and its three straight edges become geodesics — the triangle becomes an ideal hyperbolic triangle. Gluing these along shared edges turns any Euclidean triangulation into an ideal hyperbolic polyhedron: constant curvature away from cusps at the vertices.

## Where the geometry hides

Since all ideal triangles are congruent, the content is not in the triangles but in **how they are glued** — one may slide one ideal triangle along a shared edge by a hyperbolic isometry fixing that edge.

- **Shear coordinates** (Penner): $\sigma_{ij} \in \mathbb{R}$ per edge, the distance between the altitudes of the two triangles with base $ij$.
- **Penner coordinates**: decorate each vertex with a horocycle; $\lambda_{ij}$ is the signed distance between the horocycles at $i$ and $j$ — positive if disjoint, negative if intersecting. A single one carries no information (the horocycles are arbitrary), but they determine the shears:

$$
2\sigma_{ij} = \lambda_{jk} - \lambda_{ik} + \lambda_{il} - \lambda_{jl}.
$$

![Eq (6.1) as printed on page 30](../gold/crops/crane2020_EQ0039.jpg)

*Gold extraction: [crane2020_EQ0039](../gold/crane2020_EQ0039.md) — eq (6.1), ConformalGeometryOfSimplicialSurfaces.pdf p. 30.*

## The bridge

The resemblance between that relation and the [LengthCrossRatio](LengthCrossRatio.md) is not superficial. For a polyhedron built from a Euclidean one,

$$
\sigma_{ij} = \log c_{ij},
$$

![P. 31 as printed on page 31](../gold/crops/crane2020_EQ0040.jpg)

*Gold extraction: [crane2020_EQ0040](../gold/crane2020_EQ0040.md) — p. 31, ConformalGeometryOfSimplicialSurfaces.pdf p. 31.*

independent of any choice of horocycles — so it is natural to choose horocycles with $\lambda_{ij} = 2\log \ell_{ij}$, making Penner coordinates the logarithmic edge lengths. Then:

- **shear coordinates encode the conformal equivalence class**,
- **Penner coordinates pick the particular metric within it**.

Both are hyperbolic distances, hence preserved by hyperbolic isometries — so **isometry classes of ideal hyperbolic polyhedra correspond to conformal equivalence classes of discrete metrics** (Bobenko–Pinkall–Springborn).

## Related

- [PtolemyFlip](PtolemyFlip.md), [DiscreteUniformization](DiscreteUniformization.md), [LobachevskyFunction](LobachevskyFunction.md)
