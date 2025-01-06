---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Tensor Calculus

As we move into more advanced physics, vector calculus quickly becomes insufficient, and vector notation becomes incredibly inelegant and hard to work with. We need a new type of mathematical object to describe vector-like quantities in these theories - **tensors**. Fluid mechanics, advanced electrodynamics, and many numerical methods for partial differential equations *all* use tensors. General relativity is famously written in the language of differential geometry, known for its difficulty, and uses tensors near-exclusively. This is hopefully a gentler guide to tensors, one that preserves the essense of their mathematical beauty without baffling the mind.

```{code-cell} ipython3
import sympy as sp
from sympy.plotting.plot import *
import matplotlib.pyplot as plt
import numpy as np
sp.init_printing()
```

## Invariants


The whole idea behind tensors is that we want to create mathematical objects that are the same in every coordinate system - we call that **invariant**. Why is this? The reason is because in the universe, objects _are_ invariant. Intuitively, if you ask a friend to push you, whether you measure the force of your friend's push in cylindrical or spherical or cartesian coordinates, you're going to feel the same force. If you have, say, a magnetic force, that force is going to still exist and be the same physical quantity whichever coordinate system we use. The same goes for any other physical quantity, such as momentum, velocity, energy, etc. It makes sense that just using a different coordinate system to measure, say, a racecar, wouldn't cause that racecar to be 20% faster or 15% slower - instead, the speed of the racecar would be the same. Mathematical objects that have the same _physical_ quantity between differing coordinate systems are called **tensors**. Some tensors are scalars such as temperature; others are vectors such as position; still others are matrices; the commonality is that they correspond to one measurable physical object.


However, because we use coordinate systems to measure physical quantities, the _components_ of a physical quantity may be dependent on the coordinate system we use, even though the physical quantity remains the same. For example, consider a vector $\vec a$. This vector would have the following components in Cartesian coordinates:


$$
\begin{bmatrix}
1 \\
\sqrt{3}
\end{bmatrix}
$$


And the following components in polar coordinates:


$$
\begin{bmatrix}
2 \\
\frac{\pi}{3}
\end{bmatrix}
$$


These represent the exact same vector, but the _components_ are different. This is the motivation to find common transformation laws that help transform the the components of the same physical quantity - the same tensor -  between differing coordinate systems. Thus, we can express the same physical object, say force, in one coordinate system or another, but the laws of physics that describe that physical object would be the **same** in any coordinate system.


## Tensors and tensor notation


A 3D vector in Cartesian coordinates can be written in terms of the basis vectors $(e_x, e_y, e_z)$:


$$
\vec V = a_x e_x + a_y e_y + a_z e_z
$$


Thus, we can write the sum more compactly as follows:


$$
\vec V_i = \sum_{i = 0}^3 a_i e_i
$$


In Einstein summation notation, the summation is implied, so we can more simply write our vector as:


$$
\vec V_i = a_i e_i
$$


When writing vectors as tensors, it's customary to put the indices on top (as superscripts) instead of on the bottom (subscripts). Note that these are **not** raising to a power. So we now have:


$$
\vec V \Rightarrow V^i
$$


Given two vectors $\vec A$ and $\vec J$, we can now write the inner product more succintly as:


$$
\vec A \cdot \vec J = A^i J^i
$$


And we can define other vector field operations, such as the gradient, using the same notation:


$$
\nabla f = \frac{\partial f}{\partial x^i}
$$


```{note}
Remember that when writing tensors, the letters we use for the summed-over index are arbritary. We use $i$ because that's how we write summation most often, but we could use any letter we want. Later one, we'll use greek letters when denoting tensors in spacetime, but that's just a convention, not an absolute rule.
```


Contravariant tensors, usually just called vectors, are most generally written with Einstein summation convention. We denote their components with $V_i$ and their basis with $e_i$, so:


$$
\vec V = V^i e_i
$$


Covariant tensors, usually just called covectors, are also written using the convention. They are marked by a tilde over the letter, and are denoted (in terms of their basis $e^i$) as:


$$
\tilde V = V_i e^i
$$


Covectors in the 2D and 3D case can be thought of as row vectors that are multiplied by column vectors to give the dot product:


$$
\begin{bmatrix}
a & b & c
\end{bmatrix}
\cdot 
\begin{bmatrix}
d \\
e \\
f
\end{bmatrix}
$$


```{admonition} Note on generalization
In the more general $N$ dimensional case, covectors are what you multiply by a vector to obtain a scalar using the dot product. They don't have to be row vectors.
```


Tensors that are not scalars, covectors, or vectors are formed by multiplying one or more vectors with covectors using the rules of the tensor product (which we'll see next) and tensor algebra.


### Rules of Tensor Algebra


Scalar multiplication rule:


$$
T_{\alpha \beta} = k X_{\alpha \beta}
$$


Addition/subtraction rule:


$$
T^\alpha_{\: \: \beta} = A^\alpha_{\: \: \beta} \pm B^\alpha_{\: \: \beta}
$$


Multiplication rule (which raises the rank of a tensor) - also called **tensor product**:


$$
T^{\alpha \beta} = A^\alpha B^\beta
$$


$$
T^{\alpha \beta \gamma}_{\: \lambda} = (A^\alpha B^\beta) \: C^\gamma_{\: \lambda}
$$


Contraction rule (which lowers the rank of a tensor) by multiplying with another tensor with an identical index in the opposite position:


$$
T_{\lambda} = A^\alpha_{\: \lambda} B_\alpha
$$


$$
T_{\lambda} = A_{\alpha \lambda} B^\alpha
$$


The other tensor to be multiplied by is often going to be the _metric tensor_ - more on that later.


The contraction rule also applies when a tensor has identical upper and lower indices:


$$
T^\gamma = T^{\alpha \gamma}_{\: \: \: \alpha}
$$


Tensors can also obey several crucial symmetries. A symmetric tensor is one in the form:


$$
T_{\alpha \beta} = T_{\beta \alpha}
$$


Whereas an antisymmetric tensor is in the form:


$$
T_{\alpha \beta} = - T_{\beta \alpha}
$$


The double contraction of a symmetric tensor $S^{\alpha \beta}$ and antisymmetric tensor $A_{\alpha \beta}$ is zero:


$$
A_{\alpha \beta} S^{\alpha \beta} = 0
$$


Basis vectors and basis covectors obey the relation:


$$
e^i e_j = \delta^i{}_j
$$


Where ${\delta^i}_j$ (called the Kronecker delta) is defined as:


$$
{\delta_i}_j = 
\begin{cases}
1 \text{ if } i = j \\
0 \text{ if } i \neq j
\end{cases}
$$


For example, the 3D version of the Kronecker delta is given by:


$$
\delta_{ij} = 
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$


You might recognize this as the **identity matrix**, and the special property of the identity matrix is that it returns the original vector when multiplied by any vector.


If we take two basis vectors in Cartesian space and take their dot product, the result is Kronecker delta:


$$
e_i \cdot e_j = \delta_{ij}
$$


The Kronecker delta is the Cartesian form of the more general **metric tensor**, which is when we take the dot product of two non-Cartesian basis vectors:


$$
e_\mu \cdot e_\nu = g_{\mu \nu}
$$


Given a covector $\tilde A$ and a vector $\vec B$, we find that we end up with a scalar using tensor notation :


$$
\tilde A \vec B = A_i B^j e^i e_j = A_i B^j \delta^i{}_j = S
$$


Let's examine this equation in detail to familiarize ourselves with tensor algebra. First, we wrote out our vector and covector in terms of their components and basis:


$$
\tilde A \Rightarrow A_i e^i
$$

$$
\vec B \Rightarrow B^j e_j
$$


We then used the Kronecker delta to rewrite the dot product of the basis vectors as the Kronecker delta:


$$
e^i e_j = \delta^i{}_j
$$


Now, we used the Kronecker delta to relabel the indices of the components of our vector and covector:


$$
A_i B^j {\delta^i}_j = {A^i}_i {B^j}_j
$$


Finally, we used tensor contraction due to the same index on the upper and lower indices to contract the components to scalars:


$$
{A^i}_i {B^j}_j = AB \Rightarrow S
$$


We can also write the cross product using tensors. To do this, we introduce the **Levi-Civita symbol**:


$$
\epsilon_{ijk} = 
\begin{cases}
1 \text{ if cyclic permutation} \\
-1 \text{ if anticyclic permutation} \\
0 \text{ if indices repeat}
\end{cases}
$$


A cyclic permutation is if the indices go in order from left to right, such as 123, 231, or 312. An anticyclic permutation is if the indices go in order from right to left, such as 321, 213, or 132. Indices repeat in any case like 122 or 233:


```{image} ../images/special/levi-civita.png
:alt: Levi-civita symbol explained
:width: 100px
:align: center
```


With this defined, we can express the cross product as:


$$
\vec A \times \vec B = \epsilon_{ijk} A^j B^k
$$


Or if we insist on producing a vector rather than a covector, though the result is identical:


$$
\vec A \times \vec B = {\epsilon^i}_{jk} A^j B^k
$$


## Coordinate transformations


To understand tensor transformations, let's consider the case of transforming a vector $\vec V$ between $(x, y)$ and $(r, \theta)$ coordinates.

The crux of the problem is that we have two definitions of $\vec V$:


$$
\vec V = v^x e_x + v^y e_y
$$

$$
\vec V = v^r e_r + v^\theta e_\theta
$$


What we need is a reliable way to express $e_x$ in terms of $r$, and $e_y$ in terms of $\theta$.


At first glance, there is not much we can do. However, we know that the components of a vector are **linearly independent** - that is, do not affect each other. This means we can say that:


$$
v^x e_x = v^r e_r
$$

$$
v^y e_y = v^\theta e_\theta
$$


Let's focus on the first equation first. We can replace $v^x$ with just a function $x$, as $v^x$ is really just a displacement in the $x$ direction. We can similarly replace $v^r$ with a function $r$, as $v^r$ is just a displacement in the $r$ direction:


$$
x e_x = r e_r
$$


Given that this first equation holds true, then the same should be true in terms of the differentials of the components:


$$
dx e_x = dr e_r
$$


Now, if we divide by $dx$ on both sides of the equation, we have:


$$
e_x = \frac{dr}{dx} e_r
$$


Using the same process for the second equation, we get a similar result for $e_y$:


$$
e_y = \frac{d\theta}{dy} e_\theta
$$


Now, plugging in this to our original expression for our vector:


$$
\vec V = v^x e_x + v^y e_y
$$


We have:


$$
\vec V = v^x \frac{dr}{dx} e_r + v^y \frac{d\theta}{dy} e_\theta
$$


But we also know that:


$$
\vec V = v^r e_r + v^\theta e_\theta
$$


Equating this equation and the previous, we have:


$$
v^r e_r + v^\theta e_\theta = v^x \frac{dr}{dx} e_r + v^y \frac{d\theta}{dy} e_\theta
$$


Using index notation, we can write this (with $i' = r, \theta$ and $i = x, y$):


$$
v^{i'} e_{i'} = v^i \frac{dx^{i'}}{dx^i} e_{i'}
$$


```{note}
Remember the summation is implied, which is how we were able to shrink the two terms on the left hand side and the right hand side to just one term on either side.
```


We notice that the $e_{i'}$ term appears on both sides of the equation, so we can cancel them out to have:


$$
v^{i'} = v^i \frac{dx^{i'}}{dx^i}
$$


Finally, note that technically, $x^{i'}$ is a multivariable function, so:


$$
v^{i'} = v^i \frac{\partial x^{i'}}{\partial x^i}
$$


We have derived the vector transformation law. A similar derivation, just with oppositely-placed indices, is true for covectors.


## Tensor transformation law


What's most interesting about tensors is how they are defined, because they are defined in terms of _how they transform_. For instance, let's go through the formal definitions of contravariant and covariant tensors. They are defined like so:


Vectors (contravariant tensors) transform by the following transformation law from coordinate system $x^i$ to $x^{i'}$:


$$
V^{i'} = \frac{\partial x^{i'}}{\partial x^i} V^i
$$


While this definition is already workable, mathematicians more abstractly define contravariant tensors in a slightly different fashion: as the tangent vector to a parametrized curve in spacetime. The parameter used is most commonly $\tau$, the proper time. So:


$$
V^i = \frac{dx^i}{d\tau} =
\left(\frac{dx^0}{d\tau} + \frac{dx^1}{d\tau} + \frac{dx^2}{d\tau} + \frac{dx^3}{d\tau}\right)
$$


```{note}
**Remember:** We are using the convention $(x^0, x^1, x^2, x^3) = (t, x, y, z)$
```


Covectors (covariant tensors) transform instead by the following transformation law:


$$
V_{i'} = \frac{\partial x^i}{\partial x^{i'}} V_i
$$


Again, we can also define covariant tensors with an alternate method. Consider a function $f(x^i)$, where again $x^i = (x^0, x^1, x^2, x^3) = (t, x, y, z)$. Its gradient would be given by:


$$
V_i = \frac{\partial f}{\partial x^i}
= \left(\frac{\partial f}{\partial x^0}, 
\frac{\partial f}{\partial x^1}, 
\frac{\partial f}{\partial x^2}, 
\frac{\partial f}{\partial x^3}\right)
$$


The components of the gradient, given by $\frac{\partial f}{\partial x^i}$, are the components of a covariant tensor.


So now, having seen how covariant tensors and contravariant tensors transform, we can more generally describe what a tensor is:


```{admonition} Definition of a tensor
A mathematical object represented by a collection of components that transform according to certain transformation laws.
```


The **type** $(m, n)$ of a tensor is given by how many upper indices ($m$) it has, and how many lower indices ($n$) it has. The total number of upper and lower indices is its **rank**.


Now, let's look through several typical tensors:


First, we have scalars, which are $(0, 0)$ or rank-0 tensors.


$$
S
$$


Then, we have vectors and covectors, both rank-1, which are respectively $(1, 0)$ and $(0, 1)$ tensors. We usually write vectors like this:


$$
V^i =
\begin{bmatrix}
a \\
b \\
c \\
d
\end{bmatrix}
$$


And we usually write covectors like this:


$$
V_i =
\begin{bmatrix}
a & b & c & d
\end{bmatrix}
$$


Multiplying a vector and a covector is taking their **tensor product**, which gives a rank-2 tensor, also called a matrix:


$$
V^\alpha V_\beta = {T^\alpha}_\beta
$$


$$
{T^\alpha}_\beta =
\begin{pmatrix}
T_{00} & T_{01} & T_{02} & T_{03} \\
T_{10} & T_{11} & T_{12} & T_{13} \\
T_{20} & T_{21} & T_{22} & T_{23} \\
T_{30} & T_{31} & T_{32} & T_{33} \\
\end{pmatrix}
$$


The tensor product is the primary way we construct new tensors in tensor calculus (which we'll use in differential geometry). Any two tensors can be multiplied through the tensor product, so we can use the tensor product to construct any tensor. Most importantly, because the tensor transformation rule is preserved every time we take the tensor product, we can now use it to define _any_ tensor. This is the most general **definition of a tensor**:


$$
\large T^{\mu_1' \mu_2' \dots \mu_m'}_{\: \: \nu_1' \nu_2' \dots \nu_n'}
\small =
\frac{\partial x^{\mu_1'}}{\partial x^{\mu_1}} \frac{\partial x^{\mu_2'}}{\partial x^{\mu_2}}
\dots
\frac{\partial x^{\mu_m'}}{\partial x^{\mu_m'}}
\frac{\partial x^{\nu_1}}{\partial x^{\nu_1'}} \frac{\partial x^{\nu_2}}{\partial x^{\nu_2'}}
\dots
\frac{\partial x^{\nu_n}}{\partial x^{\nu_n'}}
\large T^{\mu_1 \mu_2 \dots \mu_m}_{\: \: \nu_1 \nu_2 \dots \nu_n}
$$


This horribly long and scary-looking equation is what gives tensors their reputation for frying minds, but, reassuringly, you almost never need to use this definition in practice. However, the definition is really just a formalized version of a simple idea: a tensor is a combination of vector and covector transformations that preserve the tensor transformation law. We therefore arrive at the common but unhelpful observation that:

> "A tensor is anything that transforms like a tensor."


### Practical application: Newton's laws in Tensor Calculus


To rewrite Newton's laws of motion in tensor calculus is not difficult. For example, we can take $\vec F = m \vec a$ and rewrite with tensors as:


$$
F^i = m a^i
$$


We can rewrite $a^i$ as:


$$
a^i = \frac{d^2 x^i}{dt^2}
$$


Allowing us to write Newton's second law as:


$$
F^i = m \frac{d^2 x^i}{dt^2}
$$


In practice, however, this is only true in Cartesian coordinates. To generalize to any set of curvilinear coordinates, the actual correct formula is:


$$
F^i = m \left(\frac{d^2 x^i}{dt^2} + \Gamma^i_{\mu \nu} \frac{dx^\mu}{dt} \frac{dx^\nu}{dt} \right)
$$


Where $\Gamma^i_{\mu \nu}$ is a quantity that depends on the metric $g_{\mu \nu}$ of the space (more about this next chapter).


Our new form of Newton's (2nd) law is now valid in all coordinate systems. Obviously, though, no one writes Newton's laws in this way; this is just a demonstration. Instead, let's look at a more practical example.


### Practical application 2: Maxwell's equations in tensor calculus


When using tensor calculus to express Maxwell's equations, the advantages of tensors becomes much more clear. But first, let's take a look at Maxwell's typical laws (these are expressed in SI units):


$$
\nabla \cdot \vec E = \frac{\rho}{\epsilon_0}
$$

$$
\nabla \times \vec E = -\frac{\partial \vec B}{\partial t}
$$

$$
\nabla \times \vec B = 0
$$

$$
\nabla \times \vec B = \mu_0 \vec J + \mu_0 \epsilon_0 \frac{\partial \vec E}{\partial t}
$$


We can define a quantity $\vec A$ called the vector potential, where:


$$
\vec B = \nabla \times \vec A
$$


And a quantity called $\phi$ called the scalar potential, where:


$$
\vec E = - \nabla \phi - \frac{\partial \vec A}{\partial t}
$$


This allows us to simplify Maxwell's 4 equations to just 2:


$$
A^\mu = \left(\frac{1}{c} \phi, \vec A\right)
$$

$$
J^\mu = (c\rho, \vec J)
$$


We can then define an electromagnetic tensor $F_{ij}$ like this:


$$
F_{ij} = \frac{\partial A_j}{\partial x^i} - \frac{\partial A_i}{\partial x^j}
$$


Now, using the electromagnetic field tensor, we can rewrite Maxwell's equation using just 2 tensor equations, which, like any tensor equation, is coordinate-independent:


$$
\partial_{m} F_{i k}+\partial_{k} F_{m i}+\partial_{i} F_{k m}=0
$$

$$
\partial_{i} F^{i k}=\mu_{0} J^k
$$


[Derivation source](https://profoundphysics.com/are-maxwell-equations-relativistic/)


## Differential geometry in GR


Studying differential geometry as it applies to General Relativity starts with the basic Pythagorean theorem. The distance between any 2 points in a 2D space can be found with the theorem:


```{image} https://homework.study.com/cimages/multimages/16/drawing242540949694109156314.jpg
:alt: Differentials illustrated
:width: 300px
:align: center
```


Thus, we can say that:


$$
ds^2 = dx^2 + dy^2
$$


We call this the **line element** of the space, which tells us how distances between two points are measured.


The line element of 3D space is very similar to the 2D case - just add an additional coordinate:


$$
ds^2 = dx^2 + dy^2 + dz^2
$$


However, in 4D spacetime, things are a bit different. In flat spacetime, also called Minkowski spacetime, the line element is given by:


$$
ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2
$$


This is equal to the inner product of the infinitesimal displacement vectors of Euclidean space multiplied by a matrix:


$$
ds^2 =
\begin{bmatrix}
cdt & dx & dy & dz
\end{bmatrix}
\begin{bmatrix}
cdt \\ dx \\ dy \\ dz
\end{bmatrix}
\begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$


This matrix is called the **metric tensor** - we've seen this before, it generalizes the dot product to spaces where the basis vectors aren't constant. Why the need for a metric tensor? Imagine we had two vectors, $x^\mu$ and $x^\nu$. Their product would be given by:


$$
x^\mu \cdot x^\nu = x^\mu e_\mu x^\nu e_\nu = g_{\mu \nu} x^\mu x^\nu
$$


This is why we need a metric tensor. Note that, as we saw before, the metric tensor is a rank-2 tensor, as it is the tensor product of two rank-1 vectors (which are contravariant tensors).


Also note that we often use the metric tensor for raising or lowering indices via tensor contraction. Thus:


$$
T_\beta = g_{\alpha \beta} T^\alpha
$$

$$
T^\beta = g^{\alpha \beta} T_\alpha
$$


And if we multiply the metric tensor by its inverse, we get the identity matrix, equal to the Kronecker delta, which yields a scalar:


$$
g^{\alpha \beta} g_{\beta \mu} = \delta^\alpha_{\: \mu}
$$


Finally, we can convert line elements between different coordinate systems. A more tensor-based system for doing so will be given the next chapter, but as just an example, let's attempt to convert the 3D line element to spherical coordinates.


In spherical coordinates, $(r, \theta, \phi)$, we recall that spherical coordinates are defined in terms of cartesian coordinates as follows:


$$
x = r \sin \theta \cos \phi \\
y = r \sin \theta \sin \phi \\
z = r \cos \theta
$$


Thus, after evaluating the differentials using the total differential rule, we find that:


$$
dx
= \frac{\partial x}{\partial r} dr + \frac{\partial x}{\partial \theta} d\theta + \frac{\partial x}{\partial \phi} d \phi \\
= \sin \theta \cos \phi dr + r \cos \theta \cos \phi d\theta - r \sin \phi \sin \theta d\phi
$$


$$
dy = \frac{\partial y}{\partial r} dr + \frac{\partial y}{\partial \theta} d\theta + \frac{\partial y}{\partial \phi} d \phi \\
= \sin \phi \sin \theta dr + r \sin \theta \cos \theta d\theta + r \sin \theta \cos \phi d\phi
$$


$$
dz = \frac{\partial z}{\partial r} dr + \frac{\partial z}{\partial \theta} d\theta \\
= \cos \theta dr - r \sin \theta d \theta
$$


After an ungodly long process of adding in our evaluated values for the squares of the three differentials $dx$, $dy$, and $dz$, we finally get the line element in spherical coordinates:


$$
dl^2 = dr^2 + r^2 d \theta^2 + r^2 \sin^2 \theta d \phi^2
$$


Therefore, our metric tensor becomes:


$$
g_{\alpha \beta} =
\begin{pmatrix}
1 & 0 & 0 \\
0 & r^2 & 0 \\
0 & 0 & r^2 \sin^2(\theta) \\
\end{pmatrix}
$$


Which still satisfies:


$$
dl^2 =
\begin{bmatrix}
dr & d\theta & d\phi
\end{bmatrix}
\begin{bmatrix}
dr \\ d\theta \\ d\phi
\end{bmatrix}
\begin{pmatrix}
1 & 0 & 0 \\
0 & r^2 & 0 \\
0 & 0 & r^2 \sin^2(\theta) \\
\end{pmatrix}
$$


After doing all of these calculations with tensors, why do we need to use them at all? It's because **tensor equations take the same form in any coordinate system**. This important fact will be crucial in working on a theory of general relativity.
