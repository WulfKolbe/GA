---
title: "Overview"
type: synthesis
tags: [pga, geometric-algebra, discrete-differential-geometry, conformal-geometry]
sources: [pga-swift-introduction-transcript, conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Overview

This wiki holds three bodies of work, from three sources. They share a subject — geometry, and specifically what is preserved by which maps — but they are **not** two views of one theory, and nothing here claims otherwise.

1. **[Projective geometric algebra](#projective-geometric-algebra)** — one algebra in which meet, join, projection and rigid motion are each a single operation, in any dimension. From [the PGA transcript](sources/pga-swift-introduction-transcript.md).
2. **[Discrete conformal geometry](#discrete-conformal-geometry)** — how the smooth notion of an angle-preserving map should be defined on a triangulated surface. From [Keenan Crane's survey](sources/conformal-geometry-of-simplicial-surfaces.md).
3. **[Geometric, algebraic and topological methods for QFT](#geometric-algebraic-and-topological-methods-for-qft)** — eleven lecture courses from a summer school. From [the Cardona volume](sources/cardona2013.md).

---

## Projective Geometric Algebra

### The central idea

Ordinary vector algebra treats points, lines, and planes as different kinds of thing, so each pairing needs its own formula. In three dimensions that means 3 meet formulas, 3 join formulas, and 6 projection formulas, plus two unrelated mechanisms for rotation and translation.

[ProjectiveGeometricAlgebra](concepts/ProjectiveGeometricAlgebra.md) removes the distinctions. Build the algebra on the [LinearSpaceOfLines](concepts/LinearSpaceOfLines.md) (2D) or the [LinearSpaceOfPlanes](concepts/LinearSpaceOfPlanes.md) (3D) — so vectors *are* lines or planes — and geometric objects of every kind become multivectors of different grades in one algebra ([GradeGeometryCorrespondence](concepts/GradeGeometryCorrespondence.md)). Then:

| operation | in PGA |
|---|---|
| [Meet](concepts/Meet.md) (intersection) | [OuterProduct](concepts/OuterProduct.md) |
| [Join](concepts/Join.md) | [RegressiveProduct](concepts/RegressiveProduct.md) |
| [Projection](concepts/Projection.md) | $(B \cdot a)\,a$, via the [InnerProduct](concepts/InnerProduct.md) |
| [RigidTransformation](concepts/RigidTransformation.md) | [SandwichProduct](concepts/SandwichProduct.md) $R\,X\,R^\dagger$ |

Four operations, no case analysis, and — the strongest claim in the source — **unchanged in any number of dimensions** ([DimensionIndependence](concepts/DimensionIndependence.md)).

### What makes it work

Two structural facts do most of the load-bearing:

- **[DegenerateMetric](concepts/DegenerateMetric.md)** — $e_0^2 = 0$, because the magnitude formula ignores the $e_0$ component. This makes $e_0$ the [LineAtInfinity](concepts/LineAtInfinity.md), lets translation be expressed as shifting, and turns the exponential's Euler expansion into a two-term Taylor series ([ExponentialOfBivector](concepts/ExponentialOfBivector.md)).
- **[ScaleInvariance](concepts/ScaleInvariance.md)** — nonzero scaling never changes the object represented, so stray factors are dropped freely and normalization is usually skipped.

Together they yield the unification the source keeps returning to: a [PointAtInfinity](concepts/PointAtInfinity.md) is a legitimate object, a rotation about one is a translation, and so rotation and translation are the same kind of thing — a [Rotor](concepts/Rotor.md) (or [Motor](concepts/Motor.md)) — composed by plain multiplication.

### Where it goes

[ApplicationsOfPGA](concepts/ApplicationsOfPGA.md) covers computer graphics (where [PluckerCoordinates](concepts/PluckerCoordinates.md), homogeneous coordinates, and dual quaternions turn out to be PGA in disguise), animation, and rigid body dynamics in n dimensions. [ConformalGeometricAlgebra](concepts/ConformalGeometricAlgebra.md) is the named next step, adding circles and spheres.

### Gaps

The PGA source deliberately skips: elliptic and hyperbolic PGA, points/lines/planes at infinity in 3D, the projective-geometry and rigid-transformation routes to PGA, and the mechanics of Plücker coordinates.

---

## Discrete Conformal Geometry

### The central idea

Smoothly, "conformal" has at least seven equivalent definitions — angles, circles, Cauchy–Riemann, metric scaling, conjugate harmonics, Dirichlet energy, Hodge duality ([ConformalMapCharacterizations](concepts/ConformalMapCharacterizations.md)). **Discretize them and they stop agreeing.** Each becomes a different theory, so the choice of starting point is the whole design decision ([DiscreteDifferentialGeometry](concepts/DiscreteDifferentialGeometry.md)).

Most obvious starting points fail the same way. Preserving interior angles forces a similarity per triangle, and shared edges then force one global scale factor — so the map is an isometry up to a constant. The discretized Cauchy–Riemann equation, Dirichlet energy and Hodge star all collapse to *exactly* that same rigidity ([DiscretizationRigidity](concepts/DiscretizationRigidity.md)). Where the smooth theory has a whole function $u$ of freedom, these have one number.

### What works

Put the scale factor at the **vertices**:

$$
\tilde\ell_{ij} = e^{(u_i + u_j)/2}\,\ell_{ij}
$$

![Eq (5.1) as printed on page 21](gold/crops/crane2020_EQ0028.jpg)

*Gold extraction: [crane2020_EQ0028](gold/crane2020_EQ0028.md) — eq (5.1), ConformalGeometryOfSimplicialSurfaces.pdf p. 21.*

Per-edge factors are too flexible, per-face too rigid, per-vertex just right ([DiscreteConformalEquivalence](concepts/DiscreteConformalEquivalence.md)). The resulting classes are characterized exactly by the [LengthCrossRatio](concepts/LengthCrossRatio.md), and extending them across different triangulations — via the [IntrinsicDelaunayTriangulation](concepts/IntrinsicDelaunayTriangulation.md) and [PtolemyFlip](concepts/PtolemyFlip.md)s — yields a complete **[DiscreteUniformization](concepts/DiscreteUniformization.md)** theorem whose existence condition is *only* discrete Gauss–Bonnet.

The near-miss is worth knowing: [CirclePacking](concepts/CirclePacking.md) sees only combinatorics and so is too flexible, while [CirclePattern](concepts/CirclePattern.md)s have the right structure but an existence condition that depends on the domain, not just the target curvature.

### Why hyperbolic geometry appears

Every Euclidean triangulation becomes an [IdealHyperbolicPolyhedron](concepts/IdealHyperbolicPolyhedron.md) by reading each triangle's circumcircle as a Klein-model copy of $H^2$. Under that translation, shear coordinates encode the conformal class and Penner coordinates pick the metric within it — so **isometry classes of ideal hyperbolic polyhedra are conformal equivalence classes of discrete metrics**. It also connects to [SteinersProblem](concepts/SteinersProblem.md) and, through the [LobachevskyFunction](concepts/LobachevskyFunction.md), to the convex energies that make all of this computable ([ConvexVariationalPrinciple](concepts/ConvexVariationalPrinciple.md), [DiscreteRicciFlow](concepts/DiscreteRicciFlow.md)).

### Gaps

Crane's survey leaves open: domains with boundary, monodromy around noncontractible cycles, extrinsic conformal maps, and much of the convergence theory under mesh refinement. Quadrilateral nets are excluded by choice.

The extraction of this source also has known math defects — 81 of 764 expressions do not compile. Formulas here were re-typeset by hand; see the source page.

---

## Geometric, Algebraic and Topological Methods for QFT

Unlike the two sections above, **this material was not written for the wiki** — it was
imported mechanically from a drilled PDF. Each of the eleven chapter pages carries the
volume's own abstract, its author and page range from the printed table of contents, and
links to a sample of its numbered equations with the scan each was read from. Nothing has
been synthesised, and no concept pages have been written: this is a navigable index into a
378-page volume, not a reading of it.

The [source page](sources/cardona2013.md) records what the extraction contains and what it
does not. One caution carried there: a chapter the table of contents lists but no `Abstract`
object confirms is **not** imported — Marcolli's *Noncommutative Geometry Models for
Particle Physics* is in the book but absent here for that reason.

## What this wiki does *not* claim

[ConformalGeometricAlgebra](concepts/ConformalGeometricAlgebra.md) (from the PGA source) and discrete conformal geometry (from Crane) both concern angle-preserving maps. They are **different frameworks**, not two halves of one story: CGA represents conformal transformations of continuous space with rotors; Crane discretizes conformal structure on triangulations. Crane's paper never mentions geometric algebra. The adjacency is topical only.
