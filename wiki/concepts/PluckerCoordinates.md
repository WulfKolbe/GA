---
title: "Plücker Coordinates"
type: concept
tags: [pga, 3d, representation]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Plücker Coordinates

One of the best known ways to represent a line in three dimensions with vector algebra: a **pair of vectors**. Alongside planes (a vector plus a scalar) and points (a single vector), they complete the traditional 3D toolkit — the one that then needs twelve separate formulas for meets, joins, and projections.

The notable fact for [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md): 3D PGA's **bivectors turn out to be Plücker coordinates**, arrived at without ever being designed for. But you do not need to learn how they work — the source admits to having forgotten — because PGA manipulates lines geometrically. If you ever do need the explicit line, find two points on it with PGA operations and derive the equation from those.

This is one instance of a broader pattern: techniques that look ad hoc in traditional treatments — Plücker coordinates, homogeneous coordinates, dual quaternions — **arise naturally** in PGA.

## Related

- [LinearSpaceOfPlanes](LinearSpaceOfPlanes.md), [GradeGeometryCorrespondence](GradeGeometryCorrespondence.md), [ApplicationsOfPGA](ApplicationsOfPGA.md)
