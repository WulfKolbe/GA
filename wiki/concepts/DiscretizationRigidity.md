---
title: "Rigidity of Naive Discretizations"
type: concept
tags: [discrete-differential-geometry, conformal-geometry]
sources: [conformal-geometry-of-simplicial-surfaces]
last_updated: 2026-08-27
---

# Rigidity of Naive Discretizations

The negative result that organizes Part I of Crane's survey: **four independent-looking discretizations all collapse to the same, far too rigid, answer.**

The benchmark is the smooth setting, where a conformal equivalence class is parameterized by a *function* — the log conformal factor $u : M \to \mathbb{R}$. Each failed discretization gives a class parameterized by a single *constant*.

## 1. Interior angle preservation

Preserving all interior angles $\theta_i^{jk}$ means each triangle undergoes a similarity: $\tilde\ell_{ab} = \lambda_{ijk}\,\ell_{ab}$ for $ab \in ijk$. But each interior edge is shared by two triangles, so adjacent scale factors must agree — and globally every $\lambda$ is the same. **Any angle-preserving piecewise linear map is an isometry up to one constant $c$.**

One can still minimize $E_{\mathrm{ang}}(\tilde\theta) := \sum_{ijk \in F} (\tilde\theta_i^{jk} - \theta_i^{jk})^2$ subject to positivity and the discrete integrability conditions (Euclidean triangle sums, vertex angle sums of $2\pi$, and a closure condition on edge lengths around each vertex from the law of sines). That minimizer is typically *unique* — still rigid, though empirically it approximates the map of least area distortion.

## 2. Cauchy–Riemann

The only affine maps satisfying $df(JX) = i\,df(X)$ on a single triangle are Euclidean motions and uniform scaling; agreement across shared edges again forces identical scaling everywhere. The least-squares residual $E_C(f) = \int_M |{*}df - i\,df|^2 dA$ gives a standard Galerkin finite element method whose constrained discrete energy has a unique minimizer — so it depends unstably on superficial features such as the tessellation.

## 3. Dirichlet energy

$\hat E_D(f) := \sum_{ij \in E} w_{ij}\,|f_j - f_i|^2$ with [CotangentWeights](CotangentWeights.md). Since $E_C(f) = E_D(f) - A(f)$ and the area term is constant for a fixed target, minimizing discrete Dirichlet minus signed area turns out to be **identical** to the discretized Cauchy–Riemann energy — same rigidity.

## 4. Hodge duality

Naively promising: preserving edge weights $w_{ij}$ imposes only $|E| \approx 3|V|$ conditions, versus $3|F| \approx 6|V|$ for interior angles. But:

> **Theorem.** The primal-dual length ratios $w_{ij} = \tfrac{1}{2}(\cot\alpha_{ij} + \cot\beta_{ij})$ uniquely determine the discrete metric $\ell : E \to \mathbb{R}_{>0}$, up to global scaling.

Exactly the same rigidity again.

## The one exception in Part I

**Conjugate harmonic functions** (§3.5) do give the right flexibility. Given a discrete harmonic $a$, define its conjugate $b$ as the minimizer of the discrete conformal energy with $a$ fixed — the solution of $Lb = 0$ with Neumann data $h_i = \tfrac{1}{2}(a_{i+1} - a_{i-1})$ along the boundary. One then gets a whole family of maps parameterized by $a$, matching the smooth situation where holomorphic maps are parameterized by boundary data. But it is a finite element notion: it holds only under refinement, does not preserve Möbius covariance on a fixed triangulation, and gives no notion of conformal *equivalence* — the composition of two piecewise linear harmonic functions is not harmonic.

## Related

- [ConformalMapCharacterizations](ConformalMapCharacterizations.md) — the smooth statements being discretized
- [DiscreteConformalEquivalence](DiscreteConformalEquivalence.md) — the escape from rigidity
