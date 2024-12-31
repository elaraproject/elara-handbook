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

# Multivariable calculus


> "Give me a lever long enough and a fulcrum on which to place it, and I shall move the world."
>
> **Archimedes**


Within the first hundred years of the invention of calculus, Newton and Leibnitz had already pushed single-variable calculus to its limit. A new generation of mathematicians had cropped up, ones who yearned to push the envelope of calculus, extending it to multivariable functions. Multivariable calculus allowed for physics, then in its infancy, to finally flourish, bringing with it our modern understanding of the world. And so it is invaluable that we explore this critical tool in the physicist's toolbox, and follow in the footsteps of Lagrange and Euler; seeing further, "standing on the shoulders of giants".


## Prerequisites for multivariable calculus


### Parametric Equations


Parametric equations are equations where $x$ and $y$ are functions of a _parameter_ $t$. For instance, the following is a parametric equation:


$$
\begin{cases}
x = \sin t \\
y = \cos t
\end{cases}
$$


Note that $x^2 + y^2 = \sin^2 (t) + \cos^2 (t) = 1$, so this is the parametric equation of the unit circle, as we will confirm below:

```{code-cell} ipython3
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting.plot import *
sp.init_printing()
```

```{code-cell} ipython3
def plot_p2d_example():
    t = sp.Symbol("t")
    plt = plot_parametric(sp.sin(t), sp.cos(t), show=False, aspect_ratio=(1.0, 1.0))
    plt.show()
```

```{code-cell} ipython3
plot_p2d_example()
```

The same concept can be generalized with a 3D parametric equation:

```{code-cell} ipython3
def plot_p3d_example():
    t = sp.Symbol("t")
    plt = plot3d_parametric_line(sp.sin(t), sp.cos(t), t, show=False)
    plt.show()
```

```{code-cell} ipython3
plot_p3d_example()
```

### Monovariable calculus


The derivative of a monovariable function is defined as:


$$
\frac{dy}{dx} = \lim_{x \to h} \frac{f(x + h) - f(x)}{h}
$$


The indefinite integral of a function is the inverse operation of the derivative:


$$
\int \frac{dy}{dx} dx = f(x)
$$


And is defined by:


$$
\int f(x) dx = \lim_{\Delta x_a \rightarrow 0} \sum_{a = 1}^n f(x_a) \Delta x_a
$$


Definite integrals are the (signed) area under the curve of a function, and can be evaluated by the fundamental theorem of calculus:


$$
\frac{dF}{dx} = f(x) \Rightarrow \int_a^b f(x)dx = F(b) - F(a)
$$


## Partial Derivatives


If you were travelling along a mountain, you would notice something interesting. Let's assume you take two journeys across the mountain, measuring the height of the mountain as you go. If you walk strictly from east to west of the mountain, you find that the rate of change of the height is given by a specific function $a(x)$. If you then change directions and walk strictly from north to south of the mountain, then you find that the rate of change of the height is given by a _different_ specific function $b(y)$. Clearly these two rates of change are different.


```{image} ../images/raster/partial-derivatives.png
:alt: Partial derivatives diagram
:width: 500px
:align: center
```


If we call the height of the mountain a function $h(x, y)$, we would call the rate of change of the height in strictly the east-west direction (along $x$) is the **partial derivative** of the height $h$ with respect to $x$, which we notate with:


$$
a(x, y) = \frac{\partial h(x, y)}{\partial x}
$$


And the rate of change of the height in strictly the north-south direction (along $y$) is the **partial derivative** of the height $h$ with respect to $y$, which we notate with:


$$
b(x, y) = \frac{\partial h(x, y)}{\partial y}
$$


Essentially, partial derivatives take the derivative of a multivariable function with respect to one variable and leave all other variables constant. For example, take $f(x, y) = 2x^2 y$:


$$
\frac{\partial (2x^2 y)}{\partial x} = y \cdot \frac{d (2x^2)}{dx} = y \cdot 4x = 4xy
$$


Here, we treat $y$ as a constant, allowing us to factor it out of the equation as a constant, and then we can just take the ordinary derivative of $2x^2$. Similarly:


$$
\frac{\partial (2x^2 y)}{\partial y} = 2x^2 \cdot \frac{d(1y)}{dy} = 2x^2 \cdot 1 = 2x^2
$$


Here, we treat $x$ as a constant, allowing us to factor everything in terms of $x$ (that being $2x^2$) out of the equation as a constant, and then we can just take the ordinary derivative of $1y$.


Formally, the partial derivative of a multivariable function $f(x_1, x_2, x_3, \dots, x_i, \dots, x_n)$ is defined by:


$$
\frac{\partial f}{\partial x^i} = \lim_{a \rightarrow 0} \frac{f(x_1, \dots, (x_i + a), \dots, x_n) + f(x_1, \dots, (x_i), \dots, x_n)}{a}
$$


For a two-variable function, such as $f(x, y)$, the partial derivative with respect to $x$ is given by:


$$
\frac{\partial f}{\partial x} = \lim_{a \rightarrow 0} \frac{f(x + a, y) - f(x, y)}{a}
$$


And the partial derivative with respect to $y$ is given by:


$$
\frac{\partial f}{\partial y} = \lim_{a \rightarrow 0} \frac{f(x, y + a) - f(x, y)}{a}
$$


The **multivariable chain rule** for derivatives of a composite function is based on the single-variable version. For a function $f(x, y) = (x(t), y(t))$, the derivative with respect to $t$ is given by:


$$
\frac{df}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}
$$


For instance, we could calculate the partial derivative of $f(x, y) = 2x^2 y$ with respect to $x$. Let's say that $x(t) = 3t^5 + 5$ and $y(t) = 7 \sqrt{t}$. We can then calculate our derivative with respect to $t$ like so:

$$
\frac{df}{dt} =
\frac{\partial (2x^2 y)}{\partial x} \frac{d (3t^5 + 5)}{dt} +
\frac{\partial (2x^2 y)}{\partial y} \frac{d (7 \sqrt{t})}{dt}
$$

$$
\frac{df}{dt} = 4xy \cdot 15t^4 + \frac{2x^2}{2 \sqrt{t}}
$$

$$
\frac{df}{dt} = \frac{x \left(60 t^{\frac{9}{2}} y + x\right)}{\sqrt{t}}
$$


The more general form of the chain rule with a multivariable function $f(q_1, q_2, q_3, \dots, q_n) = (q_1(t), q_2(t), q_3(t), \dots, q_n(t))$ is given by:


$$
\frac{df}{dt} = \sum_i^n \frac{\partial f}{\partial q^i} \frac{d q^i}{dt}
$$


And if both the outer and inner functions are multivariable:


$$
\frac{\partial f}{\partial t} = \sum_i^n \frac{\partial f}{\partial q^i} \frac{\partial q^i}{\partial t}
$$


## Mixed partial derivatives


Second partial derivatives are denoted by $\frac{\partial^2 f}{\partial x^2}$ or $f_{xx}$. When using the "del" notation (with the $\partial$ symbol) you take derivatives from right to left order.

Second partial derivatives **commute**, which means the order you take them doesn't matter. Thus $\frac{\partial f}{\partial x \partial y} = \frac{\partial f}{\partial y \partial x}$.


## Scalar-valued functions


A scalar-valued function is a function that always outputs a number for each input, not a vector, such as $f(x, y) = 2x + 3y^2$.


### Scalar field


A scalar field is when a scalar-valued function gives the value of every point in space. An example of a scalar field could be a temperature field; then the temperature at each point $(x, y, z)$ in space is a number given by the function $T(x, y, z)$.


## Vector-valued functions


Vector-valued functions produce a vector for each input, for instance:


$$
\vec f(t) = 
\begin{bmatrix}
t^2 + 2t \\
\sin(2t) + t
\end{bmatrix}
$$


Note that vector-valued functions can have components that are functions of $x, y, z$, or functions of $t$, in which case its components are **parametric functions**.


The derivative of a vector-valued function is another vector in all cases. For example, velocity is often given by a vector-valued function where:


$$
\vec v(t) = \begin{bmatrix}
v_x(t) \\
v_y(t) \\
v_z(t)
\end{bmatrix} = \begin{bmatrix}
x'(t) \\
y'(t) \\
z'(t)
\end{bmatrix}
$$


Speed is given by the norm of the velocity function:


$$
v = \sqrt{v_x^2 + v_y^2 + v_z^2}
$$


If the vector-valued function is of one variable, e.g. $\vec v(t)$, then its derivative is a regular derivative $\frac{d \vec v}{dt}$ that is a vector. If the vector-valued function is of several variables, e.g. $\vec v(s, t)$, then it has one partial derivative for each variable, e.g. $\frac{\partial \vec v}{\partial s}$ and $\frac{\partial \vec v}{\partial t}$, and each of those partial derivatives is also a vector.


### Vector field


A vector field is when a vector-valued function gives the value of every point in space. An example of a vector field could be a wind velocity field; then the wind velocity vector at each point $(x, y, z)$ in space is a number given by the function $\vec W_v(x, y, z)$.


## Div, Grad, Curl


The **gradient** of a multivariable function takes scalar-valued function (or more generally scalar field) and produces a vector field. The vector produced follows 2 attributes:

- Its direction is in the direction of greatest increase
- Its magnitude is proportional to the steepness (rate of increase)


In Cartesian coordinates, the gradient of a function $f(x, y)$ is defined using the nabla ($\nabla$) symbol as follows:


$$
\nabla f =
\begin{bmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y}
\end{bmatrix}
$$


For example, let's take the gradient of $f(x, y) = x^2 - y^2$. The gradient at each point $(x, y, z)$ would be then given by:


$$
\nabla f =
\begin{bmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y}
\end{bmatrix} =
\begin{bmatrix}
2x \\
-2y
\end{bmatrix}
$$


Or more generally, of a function $f(q_1, q_2, q_3, \dots, q_n)$:


$$
\nabla f =
\begin{bmatrix}
\frac{\partial f}{\partial q_1} \\
\frac{\partial f}{\partial q_2} \\
\frac{\partial f}{\partial q_3} \\
\vdots \\
\frac{\partial f}{\partial q_n}
\end{bmatrix}
$$


To intuitively understand the gradient, take a look at the graph of $f(x, y)$:

```{code-cell} ipython3
def plot_fxy():
    x, y = sp.symbols("x y")
    f = x ** 2 - y ** 2
    plot3d(f)
```

```{code-cell} ipython3
plot_fxy()
```

Let's now take a look at its gradient:

```{code-cell} ipython3
def gradient(f):
    x, y = sp.symbols("x y")
    return (f.diff(x), f.diff(y))

def plot_vecfield(g, description):
    x, y = sp.symbols("x y")
    xrange = np.linspace(-3,3,15)
    yrange = np.linspace(-3,3,15)
    X,Y = np.meshgrid(xrange, yrange)

    U=X
    V=Y

    for i in range(len(xrange)):
        for j in range(len(yrange)):
            x1 = X[i,j]
            y1 = Y[i,j]
            U[i,j] = g[0].subs({x:x1, y:y1})
            V[i,j] = g[1].subs({x:x1, y:y1})

    plt.quiver(X,Y,U,V, linewidth=1)
    plt.title(description)
    plt.show()

def fxy_plt_vecfield():
    x, y = sp.symbols("x y")
    f = x ** 2 - y ** 2
    g = gradient(f)
    plot_vecfield(g, "Gradient of $f(x, y) = x^2 - y^2$")
```

```{code-cell} ipython3
fxy_plt_vecfield()
```

Note how the vectors all point outwards from the center towards the "hills" of the function, the direction of greatest increase.


The **directional derivative** is built on the gradient and gives the rate of change of a function with respect to any direction $\vec v$, rather than just the $x, y, z$ directions. It is defined as follows:


$$
\nabla_{\vec v} f(x, y) = \frac{\partial f}{\partial \vec v} = \nabla f \cdot \vec v
$$


```{note}
Remember that this is a **dot product**, not just multiplication! The output of the directional derivative has always to be a scalar function!
```


This means that given a vector $\langle a, b \rangle$, then the directional derivative at a point $(x, y)$ is given by:


$$
\nabla_{\vec v} f(x, y) = a \frac{\partial f}{\partial x} + b \frac{\partial f}{\partial y} 
$$


We cannot take the gradient of a vector field. However, there are two other operations we can do on a vector field - they are the **curl** and **divergence**, notated as follows:


$$
\mathrm{grad}\: (f) = \nabla f
$$

$$
\mathrm{div}\: (f) = \nabla \cdot f
$$

$$
\mathrm{curl}\: (f) = \nabla \times f
$$


The divergence is defined as follows:


$$
\nabla \cdot F = \left\langle \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z}\right\rangle \cdot \langle \vec F_x, \vec F_y, F_z \rangle = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
$$


The divergence can be thought of as describing fluid flow - if the divergence is positive, fluid is flowing outwards, whereas if the divergence is negative, fluid is flowing inwards.


Meanwhile, the curl, a measure of fluid rotation, is defined much like the typical cross product:


$$
\nabla \times F =
\begin{vmatrix}
\hat i & \hat j & \hat k \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix}
$$


Which, when expanded out, results in:


$$
\nabla \times F = 
\left\langle
\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z},
\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x},
\frac{\partial F_{y}}{\partial x}- \frac {\partial F_x}{\partial y}
\right\rangle
$$


```{note}
Note that the center term of the curl using the normal cross product formula is actually $-\left(\frac{\partial F_z}{\partial x} - \frac{\partial F_x}{\partial z}\right)$, which we just distributed the negative sign to get $\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}$
```


The Laplacian operator is the gradient of the divergence of a scalar field, given as follows:


$$
\mathrm{lapl}\: (f) = \nabla \cdot \nabla f = \nabla^2 f =
\frac{\partial^2 F_x}{\partial x^2} + \frac{\partial^2 F_y}{\partial y^2} + \frac{\partial^2 F_z}{\partial z^2}
$$


## Multiple integrals


We are already familiar with the idea of an integral along a single-variable function $f(x)$:


$$
\int_a^b f(x) dx = \lim_{\Delta \to 0} \sum f(x_i) \Delta x
$$


Here, we are adding thin slices of width $dx$ and height $f(x_i)$ to find the area under the curve of $f(x)$. We can generalize this to two-variable functions $f(x, y)$:


$$
\iint\limits_{R}{{f\left( {x,y} \right)\,dA}} = \lim_{\Delta \to 0} \sum f(x_i, y_i) \Delta A
$$


This is called a **double integral**, and it finds the volume under the _surface_ $f(x, y)$ by adding thin _cubes_ of area $dA$ and height $f(x_i, y_i)$ within the bounds $R$.


To evaluate double integrals, we use a similar process as partial derivatives: we integrate first with respect to $y$, then with respect to $x$:


$$
\iint \limits_{R} f(x, y) dA = \int_{x_0}^{x_1} \int_{y_0}^{y_1} f(x, y) \, dy \, dx
$$


For example, let's evaluate:


$$
\iint \limits_R 6xy^2 dA, x \in [2, 4], y\in [1, 3]
$$


This becomes:


$$
\int_2^4 \int_1^2 6xy^2 \, dy \, dx
$$


Let's first evaluate the inner integral. Treating everything that doesn't contain $y$ as constant, we have:


$$
\int_1^2 6xy^2 dy = (2xy^3) \Big|_1^2 = 2x(2^3) - 2x(1^3) = 16x - 2x = 14x
$$


Here we integrated $6xy^2$ with respect to $y$, then substituted the resulting $y$'s in the answer for the bounds of integration. Now, let's plug this into our second integral:


$$
\int_2^4 14x dx = (7x^2) \Big|_2^4 = 84
$$


The same procedure is true for **triple integrals** over a region $f(x, y, z)$, where we find the volume under a 4-dimensional surface by adding thin 4D regions of volume $dV$ and height $f(x_i, y_i, z_i)$:


$$
\iiint_E f(x, y, z) dV = \int_{x_0}^{x_1} \int_{y_0}^{y_1} \int_{z_0}^{z_1} f(x, y, z) \, dz \, dy \, dx
$$


## Line integrals


Similar to integrals over a 1D line, 2D area, or 3D volume, we can take integrals over a curve - these are called **line integrals**. There are two types of line integrals - ones over scalar fields, and ones over vector fields. Line integrals over **scalar fields** take the form:


$$
\int_C f(r) \, ds
$$


They can be evaluated with:


$$
\int_C f(x, y) \, ds = \int_a^b f(x(t), y(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt} \right)^2} dt
$$


Or in the 3D scalar field case:


$$
\int_C f(x, y, z) \, ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} dt
$$


For example, we can evaluate the line integral, with a curve $C$ with endpoints $(1, 2)$, and $(4, 7)$ ([source](https://www.whitman.edu/mathematics/calculus_online/section16.02.html)):


$$
\int_C ye^x ds
$$


To do this, we must parameterize $C$ with two parametric equations:


$$
x(t) = 1 + 3t
$$

$$
y(t) = 2 + 5t
$$


This means that at $t = 0$, $C = (1, 2)$, and at $t = 1$, $C = (4, 7)$. We now take their derivatives:


$$
\frac{dx}{dt} = 3
$$

$$
\frac{dy}{dt} = 5
$$


We now subsitute into the equation for scalar 2D line integrals:


$$
\int_C ye^x ds = \int_0^1 (2 + 5t) e^(1 + 3t) \sqrt{3^2 + 5^2} dt = \frac{16}{9}\sqrt{34}e^4-{1\over9}\sqrt{34}\,e
$$


The main application for scalar line integrals is to calculate the mass, moment of inertia, and center of mass of a wire. However, vector line integrals are far more common, and in many cases, far more useful.


Line integrals over **vector fields** take a different form. They look like this:


$$
\int_C \vec F \cdot d\vec r
$$


And are evaluated with:


$$
\int_C \vec F \cdot d\vec r = \int_a^b \vec F(\vec r(t)) \cdot \vec r'(t) dt
$$


Note that the dot is not multiplication, but a **dot product**. In evaluating a line integral over a vector field, both $\vec F$ and $\vec r(t)$ _must_ be known to solve.


The main application of vector line integrals is in various physical laws - for example, the **work** done by a vector field $\vec F$ (such as a gravitational or magnetic field) on a particle that travels along the curve $C$ through that field is given by a vector line integral:


$$
W = \int_C F \cdot d\vec r
$$


Meanwhile, the integral forms of two of **Maxwell's equations** all use vector line integrals. For example, Ampère's law states that the line integral of a magnetic field $\vec B$ is proportional to the enclosed current:


$$
\oint_C \vec B \cdot d\vec r = \mu_0 I
$$


Note that here, we use a special symbol to denote that the curve $C$ enclosing the magnetic field is _closed_. Additionally, the more generalized version of Ampère's law is slightly more complex:


$$
\oint_C \vec B \cdot d \vec r = \mu_0 \left(I + \epsilon_0 \frac{\partial \Phi_E}{\partial t}\right)
$$


Additionally, Faraday's law states that the line integral of an electric field $\vec E$ is proportional to the rate of change of the magnetic flux:


$$
\oint_C \vec E \cdot d \vec r = - \frac{\partial \Phi_B}{\partial t}
$$


## Surface integrals


Surface integrals generalize the idea of a line integral to surfaces. They can be defined over scalar fields or vector fields. I will add more to this section later. For now though, just note that they look very similar to double integrals, just the integration is of an infinitesimal portion of surface $dS$:


$$
\iint \limits_\Sigma f(x, y) dS
$$


The most important application of surface integrals is in the integral form of **Maxwell's equations** - the first two equations extensively utilize surface integrals. Gauss's law states that the surface integral of the electric field over a closed surface (often, a sphere) is proportional to the enclosed charge:


$$
\Phi_E = \iint \limits_{\Sigma_{\text{closed}}} \vec E \cdot d\vec S = \frac{Q}{\epsilon_0}
$$


And Gauss's law for magnetism states that the surface integral of the magnetic field over a closed surface is zero:


$$
\iint \limits_{\Sigma_{\text{closed}}} \vec B \cdot d\vec S = 0
$$


## Vector calculus theorems


There are several important vector calculus theorems. First, the divergence theorem, which relates surface and triple integrals:


$$
\iiint \limits_\Omega (\nabla \cdot \vec F) \, dV = \iint \limits_\Sigma \vec F \cdot d\vec S
$$


Then, Stokes' theorem, which relates surface integrals around a region and line integrals enclosing that region:


$$
\iint \limits_\Sigma (\nabla \times \vec F) \, dS = \oint_C \vec F \cdot d \vec r
$$
