---
title: "Circle Packing"
type: concept
tags: [conformal-geometry, circles]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Circle Packing

A collection of closed circular disks meeting only at points of tangency. Its **nerve** is the graph $G = (V, E)$ with one vertex per disk and an edge exactly where two disks are tangent.

This is the discretization of the "circles" characterization in [ConformalMapCharacterizations](ConformalMapCharacterizations.md): a linear map preserves angles iff it is a rotation composed with a dilation, hence also preserves circles.

## The theorems

> **Circle Packing Theorem.** Every planar graph can be realized as a circle packing in the plane.

> **Koebe.** A connected maximal planar graph has a unique circle packing, up to Möbius transformations and reflections.

A finite maximal planar graph is a triangulated sphere via stereographic projection — so any triangulated sphere is a family of packings parameterized by Möbius transformations, exactly as smooth conformal maps of the sphere have Möbius symmetry.

> **Rodin–Sullivan** (conjectured by Thurston). Hexagonally pack a simply connected region $\Omega$ with disks of radius $\varepsilon$, then repack with the same incidence relations so boundary disks are tangent to the unit disk $D^2$. Mapping each point to the corresponding circle's center converges to a conformal homeomorphism as $\varepsilon \to 0$ — a discrete Riemann mapping theorem.

## Why it is *too flexible*

A circle packing depends **purely on the combinatorics** of the edge graph. Two simplicial disks with identical combinatorics but completely different discrete metrics are realized by identical families of packings — which would make *all* discrete metrics on a given disk conformally equivalent. It also cannot account for curvature of the domain, and finite hexagonal packings of two regions generally do not share combinatorics.

The fix is to enrich the data: see [CirclePattern](CirclePattern.md).

## Related

- [DiscretizationRigidity](DiscretizationRigidity.md) — the opposite failure mode
