---
title: "Applications of PGA"
type: concept
tags: [pga, applications]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Applications of PGA

Three application areas named by the source, plus the general case.

## Computer graphics

PGA's first main application. Rigid transformations are central to graphics, and PGA represents them efficiently ([RigidTransformation](RigidTransformation.md)). Techniques already in use that look mathematically strange — **homogeneous coordinates**, **dual quaternions** — arise naturally in PGA rather than as tricks. See [PluckerCoordinates](PluckerCoordinates.md).

## Making math videos

The source uses geometric algebra, and PGA in particular, throughout their own animation work. It simplifies animation code and has solved hard problems outright — notably **drawing many transparent intersecting objects**, a well-known problem whose solution used PGA extensively.

## Rigid body dynamics

Conventionally, linear and rotational motion must be handled separately — force and torque as distinct quantities. PGA represents translations and rotations **at the same time**, so the two can be combined into one, simplifying the equations. And because PGA is dimension-independent ([DimensionIndependence](DimensionIndependence.md)), it gives a straightforward route to **n-dimensional rigid body dynamics**.

## In general

Useful in "pretty much any situation where you're doing computational geometry."

## Related

- [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md), [ConformalGeometricAlgebra](ConformalGeometricAlgebra.md)
