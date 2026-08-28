# Wiki Index

## Overview
- [Overview](overview.md) — living synthesis: what PGA is and why the four operations collapse into one framework

## Sources
- [A Swift Introduction to Projective Geometric Algebra (transcript)](sources/pga-swift-introduction-transcript.md) — video transcript introducing Euclidean PGA via the linear space of lines and planes
- [Conformal Geometry of Simplicial Surfaces](sources/conformal-geometry-of-simplicial-surfaces.md) — Keenan Crane's survey of how conformal geometry is discretized for triangulated surfaces
- [Geometric, Algebraic and Topological Methods for Quantum Field Theory](sources/cardona2013.md) — edited volume of lecture notes (Villa de Leyva school), imported by projection

## Entities
- [Keenan Crane](entities/KeenanCrane.md) — author of the discrete conformal geometry survey; CMU
- [Boris Springborn](entities/BorisSpringborn.md) — explicit energy for conformal equivalence; spherical uniformization
- [Feng Luo](entities/FengLuo.md) — combinatorial Yamabe flow; Euclidean uniformization

## Concepts

### Foundations
- [Projective Geometric Algebra](concepts/ProjectiveGeometricAlgebra.md) — the algebra built on lines/planes; the hub page
- [Linear Space of Lines](concepts/LinearSpaceOfLines.md) — 2D foundation: lines as vectors over $e_1,\ e_2,\ e_0$
- [Linear Space of Planes](concepts/LinearSpaceOfPlanes.md) — 3D foundation: planes as vectors, one basis vector up
- [Degenerate Metric](concepts/DegenerateMetric.md) — the single algebraic quirk that defines PGA
- [Scale Invariance](concepts/ScaleInvariance.md) — nonzero scaling never changes the object represented
- [Grade–Geometry Correspondence](concepts/GradeGeometryCorrespondence.md) — which grade is a point, a line, a plane
- [Line at Infinity](concepts/LineAtInfinity.md) — $e_0$, and what its null square buys
- [Point at Infinity](concepts/PointAtInfinity.md) — bivectors with no $e_{12}$ component; where translation comes from

### Products
- [Geometric Product](concepts/GeometricProduct.md) — the fundamental product; everything else is defined from it
- [Outer Product](concepts/OuterProduct.md) — span, which in PGA *is* intersection
- [Regressive Product](concepts/RegressiveProduct.md) — common subspace, which in PGA *is* the join
- [Inner Product](concepts/InnerProduct.md) — perpendicular-through-the-other-object, across mixed grades

### Operations
- [Meet](concepts/Meet.md) — intersection, in every case, as the outer product
- [Join](concepts/Join.md) — the dual operation, as the regressive product
- [Projection](concepts/Projection.md) — all six 3D kinds from the single formula $(B \cdot a)\,a$
- [Rigid Transformation](concepts/RigidTransformation.md) — every transformation of every object as $R\,X\,R^\dagger$

### Transformations
- [Sandwich Product (Reflection)](concepts/SandwichProduct.md) — $u\,a\,u$, the base case everything is built from
- [Rotor](concepts/Rotor.md) — even products of vectors; two reflections make a rotation or a translation
- [Motor](concepts/Motor.md) — the alternative term emphasizing translations
- [Exponential of a Bivector](concepts/ExponentialOfBivector.md) — finite point → rotation; point at infinity → translation

### Beyond and around
- [Dimension Independence](concepts/DimensionIndependence.md) — the same four operations in any dimension; the n-D cube demo
- [Plücker Coordinates](concepts/PluckerCoordinates.md) — what 3D PGA bivectors turn out to be, and why you can ignore them
- [Applications of PGA](concepts/ApplicationsOfPGA.md) — graphics, animation, n-dimensional rigid body dynamics
- [Conformal Geometric Algebra](concepts/ConformalGeometricAlgebra.md) — the extension adding circles and spheres

## Concepts — Discrete Conformal Geometry

### Framing
- [Discrete Differential Geometry](concepts/DiscreteDifferentialGeometry.md) — "The Game", and the smooth/discrete thesis
- [Characterizations of a Conformal Map](concepts/ConformalMapCharacterizations.md) — the seven smooth statements that stop agreeing once discretized
- [Rigidity of Naive Discretizations](concepts/DiscretizationRigidity.md) — why angles, Cauchy–Riemann, Dirichlet and Hodge all collapse

### Discrete surfaces
- [Discrete Metric](concepts/DiscreteMetric.md) — edge lengths satisfying the triangle inequality; why edges carry no meaning
- [Cone Metric and Cone Angle](concepts/ConeMetric.md) — curvature as angle defect; discrete Gauss–Bonnet
- [Cotangent Weights and the Discrete Hodge Star](concepts/CotangentWeights.md) — the one weight behind the Laplacian, Hodge star and Dirichlet energy
- [Intrinsic Delaunay Triangulation](concepts/IntrinsicDelaunayTriangulation.md) — the canonical triangulation, and edge flips
- [Ptolemy Flip](concepts/PtolemyFlip.md) — the flip that preserves hyperbolic but not Euclidean conformal structure

### Circles
- [Circle Packing](concepts/CirclePacking.md) — Koebe, Rodin–Sullivan, and why packings are too flexible
- [Circle Pattern](concepts/CirclePattern.md) — intersection angles as conformal structure; Thurston's existence condition

### The theory that works
- [Discrete Conformal Equivalence](concepts/DiscreteConformalEquivalence.md) — scale factors at vertices; locally flexible, globally rigid
- [Length Cross Ratio](concepts/LengthCrossRatio.md) — the invariant that characterizes a conformal class
- [Discrete Uniformization](concepts/DiscreteUniformization.md) — existence guaranteed by Gauss–Bonnet alone
- [Discrete Ricci and Yamabe Flow](concepts/DiscreteRicciFlow.md) — how one computes it

### The hyperbolic picture
- [Ideal Hyperbolic Polyhedron](concepts/IdealHyperbolicPolyhedron.md) — shear and Penner coordinates; the unifying correspondence
- [Lobachevsky Function](concepts/LobachevskyFunction.md) — ideal tetrahedron volume, Schläfli, and the convex potential
- [Convex Variational Principles](concepts/ConvexVariationalPrinciple.md) — the energies, and the history that ran backwards
- [Steiner's Problem](concepts/SteinersProblem.md) — which tessellations are inscribable, and the chain of equivalences

## Chapters — Geometric, Algebraic and Topological Methods for QFT

Eleven lecture courses, each page built from the volume's own abstract and table of
contents. Imported mechanically from the `pdfdrill` docmodel; see the
[source page](sources/cardona2013.md) for the extraction figures.

- [Spectral Geometry](chapters/SpectralGeometry.md) — B. Iochum (p. 3)
- [Index Theory for Non-compact $G$-manifolds](chapters/IndexTheoryForNonCompactGManifolds.md) — M. Braverman and L. Cano (p. 60)
- [Generalized Euler Characteristics, Graph Hypersurfaces, and Feynman Periods](chapters/GeneralizedEulerCharacteristicsGraphHypersurface.md) — P. Aluffi (p. 95)
- [Gravitation Theory and Chern-Simons Forms](chapters/GravitationTheoryAndChernSimonsForms.md) — J. Zanelli (p. 137)
- [Noncommutative Spacetimes and Quantum Physics](chapters/NoncommutativeSpacetimesAndQuantumPhysics.md) — A.P. Balachandran (p. 224)
- [Integrability and the AdS/CFT Correspondence](chapters/IntegrabilityAndTheAdSCFTCorrespondence.md) — M. Staudacher (p. 255)
- [Compactifications of String Theory and Generalized Geometry](chapters/CompactificationsOfStringTheoryAndGeneralizedGeo.md) — — (p. 278)
- [Groupoids and Poisson Sigma Models with Boundary](chapters/GroupoidsAndPoissonSigmaModelsWithBoundary.md) — A. Cattaneo and I. Contreras (p. 315)
- [A Survey on Orbifold String Topology](chapters/ASurveyOnOrbifoldStringTopology.md) — A. Angel (p. 331)
- [Grothendieck Ring Class of Banana and Flower Graphs](chapters/GrothendieckRingClassOfBananaAndFlowerGraphs.md) — — (p. 346)
- [On the Geometry Underlying a Real Lie Algebra Representation](chapters/OnTheGeometryUnderlyingARealLieAlgebraRepresenta.md) — — (p. 357)

## Gold Extraction Units

Machine-extracted evidence from the source PDF (`pdfdrill model` / MathPix), one page per
display equation, each carrying the original scan. The concept pages cite into these — they
are provenance, not prose, and were not written by hand.

- [crane2020_EQ0001](gold/crane2020_EQ0001.md) — display eq, p. 5
- [crane2020_EQ0002](gold/crane2020_EQ0002.md) — display eq, p. 5
- [crane2020_EQ0003](gold/crane2020_EQ0003.md) — eq (2.1), p. 5
- [crane2020_EQ0017](gold/crane2020_EQ0017.md) — eq (3.5), p. 13
- [crane2020_EQ0019](gold/crane2020_EQ0019.md) — eq (3.7), p. 14
- [crane2020_EQ0022](gold/crane2020_EQ0022.md) — eq (4.1), p. 18
- [crane2020_EQ0023](gold/crane2020_EQ0023.md) — display eq, p. 18
- [crane2020_EQ0027](gold/crane2020_EQ0027.md) — display eq, p. 20
- [crane2020_EQ0028](gold/crane2020_EQ0028.md) — eq (5.1), p. 21
- [crane2020_EQ0031](gold/crane2020_EQ0031.md) — eq (5.2), p. 22
- [crane2020_EQ0032](gold/crane2020_EQ0032.md) — eq (5.3), p. 22
- [crane2020_EQ0035](gold/crane2020_EQ0035.md) — eq (5.4), p. 24
- [crane2020_EQ0036](gold/crane2020_EQ0036.md) — display eq, p. 26
- [crane2020_EQ0037](gold/crane2020_EQ0037.md) — display eq, p. 26
- [crane2020_EQ0038](gold/crane2020_EQ0038.md) — eq (5.5), p. 27
- [crane2020_EQ0039](gold/crane2020_EQ0039.md) — eq (6.1), p. 30
- [crane2020_EQ0040](gold/crane2020_EQ0040.md) — display eq, p. 31
- [crane2020_EQ0042](gold/crane2020_EQ0042.md) — display eq, p. 32
- [crane2020_EQ0043](gold/crane2020_EQ0043.md) — display eq, p. 33
- [crane2020_EQ0044](gold/crane2020_EQ0044.md) — eq (6.2), p. 33
- [crane2020_EQ0045](gold/crane2020_EQ0045.md) — eq (6.3), p. 34
- [crane2020_EQ0047](gold/crane2020_EQ0047.md) — display eq, p. 34
- [crane2020_EQ0048](gold/crane2020_EQ0048.md) — eq (6.4), p. 36
- [crane2020_EQ0049](gold/crane2020_EQ0049.md) — display eq, p. 37

## Syntheses
_(none yet)_
