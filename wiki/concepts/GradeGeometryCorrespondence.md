---
title: "Grade–Geometry Correspondence"
type: concept
tags: [pga, foundations]
sources: [pga-swift-introduction-transcript]
last_updated: 2026-08-27
---

# Grade–Geometry Correspondence

Which grade of multivector represents which geometric object — the dictionary that makes [ProjectiveGeometricAlgebra](ProjectiveGeometricAlgebra.md) readable.

| | 2D PGA | 3D PGA | n-D PGA |
|---|---|---|---|
| vector | line | plane | $(n-1)$-dimensional hyperplane |
| bivector | **point** | line | ... |
| trivector | pseudoscalar | **point** | ... |
| pseudovector | — | — | **point** |

## The argument, once

A bivector is the span of two vectors, i.e. all lines through their intersection (2D) or all planes through their line of intersection (3D). That set is *uniquely determined* by the single object all its members share. Thinking about the infinite set is hard; thinking about the one point or line is easy — so **identify the bivector with that object**. The same argument, one grade up, makes trivectors points in 3D.

The source keeps visualizations tractable by drawing only three orthogonal planes through a point, or two orthogonal planes through a line, rather than the whole pencil.

## The dimensional offset

2D PGA has three basis vectors ($e_1,\ e_2,\ e_0$), so it is *algebraically* a three-dimensional geometric algebra even though the geometry is planar. Much of 3D GA's behaviour shows up in the 2D setting — including the fact that the standard 2D rotation formula does **not** generally hold, which is why the treatment starts from reflections instead. See [SandwichProduct](SandwichProduct.md).

## Related

- [LinearSpaceOfLines](LinearSpaceOfLines.md), [LinearSpaceOfPlanes](LinearSpaceOfPlanes.md), [DimensionIndependence](DimensionIndependence.md)
