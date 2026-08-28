---
title: "Characterizations of a Conformal Map"
type: concept
tags: [conformal-geometry, smooth-setting]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Characterizations of a Conformal Map

For a smooth, nondegenerate, orientation-preserving map $f$ from a disk-like surface $(M, g)$ to $\mathbb{C}$, all of the following say the same thing. **In the discrete setting they do not.** That gap is the entire subject of [DiscretizationRigidity](DiscretizationRigidity.md) and the reason discrete conformal geometry has several inequivalent theories.

1. **Angles** — at each $p \in M$ the angle between tangent vectors $X, Y$ equals the angle between $df_p(X)$ and $df_p(Y)$.
2. **Circles** — the image of a geodesic circle of radius $\varepsilon$ approaches a Euclidean circle as $\varepsilon \to 0$.
3. **Analytic** — the Cauchy–Riemann equation $df(JX) = i\,df(X)$, where $J$ is the linear complex structure ($J^2 = -\mathrm{id}$), a quarter-turn in each tangent space.
4. **Metric** — conformal equivalence of metrics, $\tilde g = e^{2u} g$ with $u : M \to \mathbb{R}$ the **log conformal factor**.
5. **Conjugate** — $f = a + bi$ with $a, b$ harmonic and $\nabla b = J \nabla a$.
6. **Dirichlet** — $f$ is a critical point of $E_D(f) = \int_M |df|^2\, dA$.
7. **Hodge** — $f$ preserves the Hodge star on 1-forms.

To someone versed in the smooth theory the list looks redundant. Crane's point is that "these minor shifts in perspective often lead to substantially different interpretations in the discrete setting" — each item is a distinct *starting point* for discretization, and they land in different places. Items 1, 3, 6 and 7 all collapse to rigidity; item 2 becomes [CirclePacking](CirclePacking.md) and [CirclePattern](CirclePattern.md); item 4 becomes [DiscreteConformalEquivalence](DiscreteConformalEquivalence.md), the one that works.

## Not to be confused with

[ConformalGeometricAlgebra](ConformalGeometricAlgebra.md) also concerns conformal transformations, but it is an algebraic framework for continuous space rather than a discretization of conformal structure. The source makes no connection between the two.

## Related

- [DiscreteDifferentialGeometry](DiscreteDifferentialGeometry.md) — the methodology this list exemplifies
