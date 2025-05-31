# General Relativity, Part 1


**General relativity** is a theory of how gravity works. In General Relativity, gravity is not a force, but rather an effect caused by curved spacetime. This conclusion is based on two fundamental principles:

- The **Equivalence Principle**, which says that gravity is indistinguishable from the effect of an accelerating reference frame
- The **Principle of Covariance**, which says that all laws of physics should be in the same form in all reference frames

The culminating breakthrough of General Relativity is summarized succinctly by the Einstein Field Equations:


$$
G_{\alpha \beta} = \frac{8\pi G}{c^4} T_{\alpha \beta}
$$


However, to truly understand what the equation means, we need to go slowly and build our understanding of relativity first. And it often helps to start with the physical intuition underlying relativity - the **equivalence principle**.


## The Equivalence Principle


Consider an observer inside a closed room. This room is accelerating upwards at a constant rate of $9.81\mathrm{\ m/s^2}$. The observer holds a 1-kilogram ball. What would happen if the observer would drop a ball?


Well, we know that the room is under constant upwards acceleration, so when the observer releases the ball, the floor of the room will travel upwards towards it at $9.81\mathrm{\ m/s^2}$. However, to the observer, who is moving upwards *along with* the floor, it would look like everything is stationary, and the *ball* is the object that is falling down.


If we use Newton's second law of motion, we find that the force experienced by the ball would be given by:


$$
\vec F_b = m \vec a
$$


Thus, the force would be:


$$
\vec F_b = -9.81 N
$$


Now, consider another observer, inside another closed room. This room is placed on the surface of the Earth. The observer inside this second room drops another 1-kilogram ball. What would happen next?


Well, the ball will experience the force of Earth's gravity, causing it to fall downwards as well. If we use Newton's law of universal gravitation, we find that the force experienced by the ball would be given by:


$$
\vec F_b = -G\frac{M_1 M_2}{r^2}
$$


We can rearrange this equation to the form:


$$
\vec F_b = \left(\frac{-GM_\oplus}{(r_\oplus)^2}\right) M_2
$$


Using our closest measurements of the mass of the Earth and its radius, we arrive at the result:


$$
\vec F_b = -9.81 N
$$


Notice that this is the **same result** as our closed room moving upwards through space at $9.81\mathrm{\ m/s^2}$. The effect of gravity and of an accelerated reference frame is the same. But this is just a coincidence, right? Or is it...?


Imagine you were in either the closed room in space or the closed room on Earth, but you weren't told which one. Is there any way you could tell which room it was? No, it would be impossible to perform an experiment to tell the closed room in space from the closed room on Earth.


So, gravity is **indistinguishable** from accelerated reference frames. This is the **equivalence principle**.


## Reviewing the spacetime metric


To understand General Relativity, we must first be familiar with the idea of **events**.


An event is _anything that happens_. This could be, “a spaceship flew through my window”. Yes, that is an event.


We can describe the event by finding the position and time it occured, *relative* to a chosen reference frame:

- E.g. “a spaceship flew through my window at 5 meters left and 6 meters in front of my head, at 2 meters above sea level, at 2:30 pm, on January 15th, 2021”
- We have a x-coordinate (5 meters left of my head), a y-coordinate (6 meters in front of my head), a z-coordinate (2 meters above sea level), and a time coordinate (2:30 pm 1/15/21)

To describe the distance between two events, we use a spacetime metric. This could be the Euclidean metric $\delta_{\alpha \beta}$, the Minkowski metric $\eta_{\alpha \beta}$, or the general metric $g_{\alpha \beta}$. As we've seen before, the Minkowski metric in particular is given by $\eta_{\alpha \beta}$, where $\alpha$ and $\beta$ represent the $(\alpha, \beta)$-th entry of the matrix:


$$
\eta_{\alpha\beta} = \begin{pmatrix}-1 & 0 & 0 &0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{pmatrix} = \begin{pmatrix}\eta_{{00}}& \eta_{{01}}& \eta_{{02}}& \eta_{{03}}\\\eta_{{10}}& \eta_{{11}}& \eta_{{12}}& \eta_{{13}}\\\eta_{{20}}& \eta_{{21}}& \eta_{{22}}& \eta_{{23}}\\\eta_{{30}}& \eta_{{31}}& \eta_{{32}}& \eta_{{33}}\\\end{pmatrix}
$$


```{admonition} A note about really confusing metric notation
In General Relativity, it is customary to count time as the 0th dimension rather than the 4th dimension. This is why $\alpha$ and $\beta$ range from 0 to 3 instead of 1 to 4 (as you ordinarily might expect).
```


```{admonition} A note about signatures
The Minkowski metric is similar to the Euclidean metric $\delta_{\alpha \beta}$ with one major difference: $\eta_{00} = -1 \neq \delta_{00}$ (see second appendix for why). So, the metric tensor has a _signature_ - that of $(- + + +)$ along its diagonals. Note that sometimes, physicists will confusingly use a metric signature of $(+---)$, which returns the same distance in spacetime. These two metric signatures are _functionally equivalent_ because the metric tensor is symmetric; the only difference is your personal preference. I will stick with $(- + + +)$ for consistency here.
```


Recall that the line element can be written in terms of the product of two infinitesimal displacement vectors multiplied by the metric:


$$
ds^2 = \begin{bmatrix}cdt & dx & dy & dz\end{bmatrix} \begin{bmatrix}cdt \\ dx \\ dy \\ dz\end{bmatrix} \begin{pmatrix}-1 & 0 & 0 &0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{pmatrix}
$$


We can denote one of these infinitesimal displacement vectors $dx^\alpha$ and the other $dx^\beta$, so we have:


$$
ds^2 = \eta_{\alpha \beta} dx^\alpha dx^\beta
$$


Additionally, since the components of metric tensors can vary as spacetime is curved and distances change, we shouldn't expect that the metric of spacetime will always be $\eta_{\alpha \beta}$; in fact, that would only be true for flat (uncurved) spacetime. So, we replace $\eta_{\alpha \beta}$ with the more general form of the metric tensor $g_{\alpha \beta}$, which applies to all spacetime metrics. We finally arrive at the general metric tensor:


$$
ds^2 = g_{\alpha \beta} dx^\alpha dx^\beta
$$


This is the most common form of the spacetime metric you will see, and it is the form we will use going forward.


### Spacelike, Timelike, and Lightlike Intervals


When finding the spacetime interval between two events, we can describe the interval using one of three terms:

* If the spacetime interval is **positive**, it is spacelike: the two events are separated by space
* If the spacetime interval is **negative**, it is timelike: the two events are separated by time
* If the spacetime interval is **zero**, it is lightlike: a beam of light could travel directly from one event to the other


## The Einstein Summation Convention


Previously, we have already been introduced to index notation - for example, we saw that position could be represented by $x^\mu = x, y, z$, and that an equation such as $v^\mu = \frac{dx^\mu}{dt}$ is actually a system of three equations, one each for $x$, $y$, and $z$. W've also seen that we can generally let the letters we use for tensor indices to be whatever we want, and the equations will still be consistent. For example, $g_{\alpha \beta} = g_{ij} = g_{\alpha \gamma} = g_{\mu \gamma}$. There is a difference between these two forms of indices, however.


The first type, where we have a single index, is called a **free index**. Free indices result in a different equation for each coodinate - for instance, given $F^\mu = ma^\mu$, then we have the system of equations:


$$
\begin{cases}
F^x = ma^x \\
F^y = ma^y \\
F^z = ma^z
\end{cases}
$$


The second type, where we have an index that repeats once as a lower index and once as an upper index in a term, is used to stand for summation. For example, recall the multivariable chain rule:


$$
\frac{\partial f}{\partial t} = \frac{\partial f}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial f}{\partial y} \frac{\partial y}{\partial t} + \frac{\partial f}{\partial z} \frac{\partial z}{\partial t}
$$


We can rewrite this with summation:


$$
\frac{\partial f}{\partial t} = \sum_{i = 1}^3 \frac{\partial f}{\partial x_i} \frac{\partial x_i}{\partial t}
$$


Note that we have an index $i$ that appears in the lower index and one that appears in the upper index, so by the Einstein summation convention, we can get rid of the summation sign:


$$
\frac{\partial f}{\partial t} = \frac{\partial f}{\partial x_i} \frac{\partial x_i}{\partial t}
$$


And because the index is used for summation, it makes no difference if we change $i$ to $j$ or $k$ or $u$, the equation will mean the same thing:


$$
\frac{\partial f}{\partial t} = \frac{\partial f}{\partial x_j} \frac{\partial x_j}{\partial t}
$$


This works the same way if are working with tensors. Consider the following tensor equation:


$$
K_{i} = a_{ij} b^{j} 
$$


Notice that $j$ appears once as a top index, and once as a bottom index. Thus, $j$ must be a summation index - in GR we call these **dummy indices**. In contrast, $i$ and $k$ don't appear twice on the top and bottom, so are free indices, representing a system of equations. Therefore, if we were to expand the dummy summation index, where $j$ goes from 1 - 3, we'll get:


$$
K_i = a_{i1} b^1 + a_{i2} b^2 + a_{i3} b^3
$$


And we let $x = 1, y = 2, z = 3$, then:


$$
K_i = a_{ix} b^x + a_{iy} b^y + a_{iz} b^z
$$


In comparison, remember that $i$ is a free index that expands into a system of equations. So, using $i = (x, y, z)$, we have:


$$
\begin{cases}
K_x = a_{xx} b^x + a_{xy} b^y + a_{xz} b^z \\
K_y = a_{yx} b^x + a_{yy} b^y + a_{yz} b^z \\
K_z = a_{zx} b^x + a_{zy} b^y + a_{zz} b^z
\end{cases}
$$


In general, dummy indices can be changed at will, but free indices cannot. This is because changing a dummy index is just changing the index you use for the summation, which is totally arbitrary, but changing a free index would change the system of equations into a completely different system of equations.


The use of the Einstein summation convention allows the equations of General Relativity to be written very compactly. For instance, take the definition of the Ricci tensor, given by:


$$
R_{ij} = \frac{\partial \Gamma^k_{ij}}{\partial x^k} - \frac{\partial \Gamma^k_{ik}}{\partial x^j} + \Gamma^k_{ij} \Gamma^m_{km} - \Gamma^k_{im} \Gamma^m_{jk}
$$


Observe that only $i$ and $j$ are free indices - the other two indices $m$ and $k$ appear both on upper and on lower indices, making them summation indices. If we were to fully write out just the summation of the Ricci tensor, where $m$ and $k$ both sum from 0 to 3, and we assume $0 = t$, $1 = x$, $2 = y$, $3 = z$, we'd get:


$$
\begin{align}
R_{ij} &= \frac{\partial \Gamma^t_{ij}}{\partial x^t} - \frac{\partial \Gamma^t_{it}}{\partial x^j} + \Gamma^t_{ij} \Gamma^t_{tt} - \Gamma^t_{it} \Gamma^t_{jt} + \frac{\partial \Gamma^x_{ij}}{\partial x^x} - \frac{\partial \Gamma^x_{ix}}{\partial x^j} + \Gamma^x_{ij} \Gamma^t_{xt} - \Gamma^x_{it} \Gamma^t_{jx} \\
&\qquad+ \frac{\partial \Gamma^y_{ij}}{\partial x^y} - \frac{\partial \Gamma^y_{iy}}{\partial x^j} + \Gamma^y_{ij} \Gamma^t_{yt} - \Gamma^y_{it} \Gamma^t_{jy} + \frac{\partial \Gamma^z_{ij}}{\partial x^z} - \frac{\partial \Gamma^z_{iz}}{\partial x^j} + \Gamma^z_{ij} \Gamma^t_{zt} - \Gamma^z_{it} \Gamma^t_{jz} \\
&\qquad+ \frac{\partial \Gamma^t_{ij}}{\partial x^t} - \frac{\partial \Gamma^t_{it}}{\partial x^j} + \Gamma^t_{ij} \Gamma^x_{tx} - \Gamma^t_{ix} \Gamma^x_{jt} + \frac{\partial \Gamma^x_{ij}}{\partial x^x} - \frac{\partial \Gamma^x_{ix}}{\partial x^j} + \Gamma^x_{ij} \Gamma^x_{xx} - \Gamma^x_{ix} \Gamma^x_{jx} \\
&\qquad+ \frac{\partial \Gamma^y_{ij}}{\partial x^y} - \frac{\partial \Gamma^y_{iy}}{\partial x^j} + \Gamma^y_{ij} \Gamma^x_{yx} - \Gamma^y_{ix} \Gamma^x_{jy} + \frac{\partial \Gamma^z_{ij}}{\partial x^z} - \frac{\partial \Gamma^z_{iz}}{\partial x^j} + \Gamma^z_{ij} \Gamma^x_{zx} - \Gamma^z_{ix} \Gamma^x_{jz} \\
&\qquad+ \frac{\partial \Gamma^t_{ij}}{\partial x^t} - \frac{\partial \Gamma^t_{it}}{\partial x^j} + \Gamma^t_{ij} \Gamma^y_{ty} - \Gamma^t_{iy} \Gamma^y_{jt} + \frac{\partial \Gamma^x_{ij}}{\partial x^x} - \frac{\partial \Gamma^x_{ix}}{\partial x^j} + \Gamma^x_{ij} \Gamma^y_{xy} - \Gamma^x_{iy} \Gamma^y_{jx} \\
&\qquad+ \frac{\partial \Gamma^y_{ij}}{\partial x^y} - \frac{\partial \Gamma^y_{iy}}{\partial x^j} + \Gamma^y_{ij} \Gamma^y_{yy} - \Gamma^y_{iy} \Gamma^y_{jy} + \frac{\partial \Gamma^z_{ij}}{\partial x^z} - \frac{\partial \Gamma^z_{iz}}{\partial x^j} + \Gamma^z_{ij} \Gamma^y_{zy} - \Gamma^z_{iy} \Gamma^y_{jz} \\
&\qquad+ \frac{\partial \Gamma^t_{ij}}{\partial x^t} - \frac{\partial \Gamma^t_{it}}{\partial x^j} + \Gamma^t_{ij} \Gamma^z_{tz} - \Gamma^t_{iz} \Gamma^z_{jt} + \frac{\partial \Gamma^x_{ij}}{\partial x^x} - \frac{\partial \Gamma^x_{ix}}{\partial x^j} + \Gamma^x_{ij} \Gamma^z_{xz} - \Gamma^x_{iz} \Gamma^z_{jx} \\
&\qquad+ \frac{\partial \Gamma^y_{ij}}{\partial x^y} - \frac{\partial \Gamma^y_{iy}}{\partial x^j} + \Gamma^y_{ij} \Gamma^z_{yz} - \Gamma^y_{iz} \Gamma^z_{jy} + \frac{\partial \Gamma^z_{ij}}{\partial x^z} - \frac{\partial \Gamma^z_{iz}}{\partial x^j} + \Gamma^z_{ij} \Gamma^z_{zz} - \Gamma^z_{iz} \Gamma^z_{jz}
\end{align}
$$


And remember, this is just expanding the summations! This isn't even writing out the system of equations for each free index! You can go and see the full Einstein field equations with each system of equations written out at <https://github.com/bnschussler/Fully-Expanded-Einstein-Field-Equations>, and it is 22 pages long!


Finally, in General Relativity, partial derivatives are often written in a compact way:


$$
\frac{\partial}{\partial x^\mu} \Rightarrow \partial_\mu 
$$


And if we have a partial derivative, it is considered a lower index in a tensor:


$$
{T^\mu}_\nu = \partial_\nu A^\mu
$$


## The Geodesic Equation


We know from Newton's first law of motion that an object in motion stays in motion at constant speed - that is, it undergoes no acceleration. In other terms:


$$
\frac{d^2x^\alpha}{d\tau^2} = 0
$$


Where:


$$
x^\alpha = x^1, x^2, x^3 ... \: x^n = x, y, z \: ... \: n
$$


This is why, for instance, a ball rolling along an infinitely long hallway will keep going in a path in the same direction - its velocity vector, and thus its directions, stays constant. In nice Euclidean space, we call this path a "straight line" - the effect of going ahead in the same direction forever.

As we know, in Euclidean space, a straight line is the shortest path between two points, which we call a _geodesic_. We might be tempted to phrase Newton's first law to say that "a particle in motion will travel along a straight line". However, in non-Euclidean geometries, a geodesic is not necessarily a straight line. So, we must generalize Newton's first law with modifications: **a particle in motion will move along a geodesic**.

To formulate this law mathematically, we can say that the action along the path $x^k(\lambda)$ between 2 points $A = x^k(0)$ and $B = x^k(1)$ must be minimized. We include the units of $mc$ to get the units for action right, so the full action along the path $x^k (\lambda)$ is:


$$
S = -mc \int \sqrt{-ds^2}
$$


```{admonition} About the line element
Here, the line element is negative to get rid of the annoying $-c^2 dt^2$ element which would yield an imaginary number if square rooted. Because the distance along the path is the same whether you travel in the forwards direction ($\sqrt{ds^2}$) or in the backwards direction ($\sqrt{-ds^2}$), the result is equivalent.
```


We can expand this out by writing $ds^2 = g_{ij} dx^i dx^j$, so:


$$
S = -mc \int \sqrt{-g_{ij} dx^i dx^j}
$$


Now, to actually be able to solve, we need to write the integrand in terms of our path parameter $\lambda$. To do this, we can divide $dx^i$ and $dx^j$ both by $d\lambda$, then, to keep the integrand the same, multiply by $d\lambda \cdot d\lambda = d\lambda^2$:


$$
S = -mc \int \sqrt{-g_{ij} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} d\lambda^2}
$$


We can then take out the $d\lambda$ from the square root to have:


$$
S = -mc \int \sqrt{-g_{ij} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}} d\lambda
$$


Knowing that the integrand of the action is the Lagrangian, we can write:


$$
\mathcal{L} = \sqrt{-g_{ij} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}}
$$


We can more specifically write it out that that metric $g_{ij}$ is a function of $x^k$, so:


$$
\mathcal{L} = \sqrt{-g_{ij}(x^k) \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}}
$$


We can apply the familiar Euler-Lagrange equations to our Lagrangian, as we've done before, to find the equations of motion for the particle traveling along the path:


$$
\frac{d}{d\lambda} \frac{\partial \mathcal{L}}{\partial \dot x^k}
= \frac{\partial \mathcal{L}}{\partial x^k}
$$


Let's first take the derivative with respect to $x^k$. We use the chain rule and the fact that $\frac{\partial}{\partial x} \sqrt{u} = \frac{1}{2} u^{-\frac{1}{2}} \frac{\partial u}{\partial x}$. In our Lagrangian, the only part that actually depends on $x^k$ is $g_{ij}$, so the rest of the Lagrangian can be thought of as a constant. So we have:


$$
\frac{\partial \mathcal{L}}{\partial x^k} = -\frac{1}{2} 
\left(g_{ij}(x^k) \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}\right)^{-1/2}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}
$$


We can simplify this by noticing that the Lagrangian itself appears in its derivative, so we can write:


$$
\frac{\partial \mathcal{L}}{\partial x^k} = -\frac{1}{2} 
\mathcal{L}^{-1}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}
$$


Which simplifies to:


$$
\frac{\partial \mathcal{L}}{\partial x^k} = -\frac{1}{2 \mathcal{L}}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}
$$


Now, let's take the derivative with respect to $\dot x^k$. Here, using the same Lagrangian substitution technique and square root derivative, we find that:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
-\frac{1}{2\mathcal{L}}
\left(-\frac{\partial}{\partial \dot x^k} g_{ij} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}\right)
$$


Remember that $g_{ij}$ isn't dependent on $\dot x^k$, so we can simplify factor it out for now:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{2\mathcal{L}} g_{ij}
\left(\frac{\partial}{\partial \dot x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda}\right)
$$


To differentiate the part inside brackets of the previous expression, we use the product rule, namely $\frac{\partial}{\partial x} fg = \frac{\partial}{\partial x}f \cdot g + \frac{\partial}{\partial x} g \cdot f$, to get:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
-\frac{1}{2\mathcal{L}} g_{ij}
\left(\frac{\partial \dot x^i}{\partial \dot x^k} \frac{dx^j}{d\lambda} + \frac{\partial \dot x^j}{\partial \dot x^k} \frac{dx^i}{d\lambda}\right)
$$


Now, we will use the Kronecker delta-partial derivative rule:


$$
\frac{\partial \dot x^i}{\partial \dot x^k} = {\delta^i}_k
$$


This simplifies the expression to:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{2\mathcal{L}} g_{ij}
\left({\delta^i}_k \frac{dx^j}{d\lambda} + {\delta^j}_k \frac{dx^i}{d\lambda}\right)
$$


Finally, we distribute the expression with the metric $g_{ij}$:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{2\mathcal{L}}
\left(g_{ij} {\delta^i}_k \frac{dx^j}{d\lambda} + g_{ij} {\delta^j}_k \frac{dx^i}{d\lambda}\right)
$$


Remembering that the Kronecker delta can be used to relabel indices:


$$
g_{\alpha \beta} {\delta^\alpha}_\mu = g_{\beta \mu}
$$


We rewrite the expression as:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{2\mathcal{L}}
\left(g_{jk} \frac{dx^j}{d\lambda} + g_{ik} \frac{dx^i}{d\lambda}\right)
$$


Finally, let's remember the Einstein summation convention, which tell us that dummy indices can be changed to whatever indices we want, because they are just summation indices. Here, since $i$ and $j$ appear both as lower indices and as upper indices, they are dummy indices. That means:


$$
g_{jk} \frac{dx^j}{d\lambda} = g_{ik} \frac{dx^i}{d\lambda}
$$


So to simplify the expression, we can replace all the $j$'s with $i$'s (as we can do with dummy indices), to obtain:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{2\mathcal{L}}
\left(g_{ik} \frac{dx^i}{d\lambda} + g_{ik} \frac{dx^i}{d\lambda}\right)
$$


Which simplifies to:


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{2\mathcal{L}}
\left(2 g_{ik} \frac{dx^i}{d\lambda}\right)
$$


$$
\frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{\mathcal{L}}
g_{ik} \frac{dx^i}{d\lambda}
$$


Now we simply need to differentiate our previous result with respect to $\lambda$:


$$
\frac{d}{d\lambda} \frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{d}{d\lambda} \left(\frac{1}{\mathcal{L}}
g_{ik} \frac{dx^i}{d\lambda}\right) = 
\frac{1}{\mathcal{L}} \frac{d}{d\lambda} \left(
g_{ik} \frac{dx^i}{d\lambda}\right)
$$


Here, we use the product rule again with the terms in the brackets, which give us:


$$
\frac{d}{d\lambda} \frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{\mathcal{L}} \left(
\frac{\partial g_{ik}}{\partial \lambda} \frac{dx^i}{d\lambda} + \frac{d^2 x^i}{d\lambda^2} g_{ik}
\right)
$$


Now, we know that technically $g_{ij} = g_{ij} (x^k (\lambda))$, so we can use the chain rule to write:


$$
\frac{\partial g_{ik}}{\partial \lambda} = \frac{\partial g_{ik}}{\partial x^a}
\frac{d x^a}{d \lambda}
$$


Here, $a$ can be any index that isn't already one of the free indices (the free indices are $i$ and $k$ here). We'll choose $a$, but really it can be anything.


So we have:


$$
\frac{d}{d\lambda} \frac{\partial \mathcal{L}}{\partial \dot x^k} =
\frac{1}{\mathcal{L}} \left(
\frac{\partial g_{ik}}{\partial x^a}
\frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda} + \frac{d^2 x^i}{d\lambda^2} g_{ik}
\right)
$$


Equating the two sides of the Euler-Lagrange equation, we have:


$$
-\frac{1}{2 \mathcal{L}}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 
\frac{1}{\mathcal{L}} \left(
\frac{\partial g_{ik}}{\partial x^a}
\frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda} + \frac{d^2 x^i}{d\lambda^2} g_{ik}
\right)
$$


We can move the left-hand side to the right to get:


$$
\frac{1}{\mathcal{L}} \left(
\frac{\partial g_{ik}}{\partial x^a}
\frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda} + \frac{d^2 x^i}{d\lambda^2} g_{ik}
\right) -\frac{1}{2 \mathcal{L}}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


And we can factor out the common factor of the Lagrangian and get rid of it by dividing it from both sides of the equation (remember zero divided by anything is still zero):


$$
\left(
\frac{\partial g_{ik}}{\partial x^a}
\frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda} + \frac{d^2 x^i}{d\lambda^2} g_{ik}
\right) -\frac{1}{2}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


As well as rearranging the terms to put the second derivative in front:


$$
\left(
\frac{d^2 x^i}{d\lambda^2} g_{ik} + \frac{\partial g_{ik}}{\partial x^a} \frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda}
\right) -\frac{1}{2}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


Now, we can remove the brackets:


$$
\frac{d^2 x^i}{d\lambda^2} g_{ik} + \frac{\partial g_{ik}}{\partial x^a} \frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda}
 -\frac{1}{2}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


Notice that this equation has **three** dummy indices - $i$ (which appears both in $d^2 x^i$ as upper index and $g_{ik}$ as lower index), $a$ (which appears both in the lower part of a partial derivative and upper part of another derivative $dx^a$), and $j$ (which appears as a lower index in $g_{ij}$ and an upper index in $dx^j$). Remember this! It'll be very important later! 


Let's take a close look at the middle term:


$$
\frac{\partial g_{ik}}{\partial x^a} \frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda}
$$


It can be seen that it can be alternatively written as:


$$
\frac{1}{2} \left(\frac{\partial g_{ik}}{\partial x^a} + \frac{\partial g_{ik}}{\partial x^a} \right)
\frac{d x^a}{d \lambda} \frac{dx^i}{d\lambda}
$$


Let's distribute this:


$$
\frac{1}{2} \frac{\partial g_{ik}}{\partial x^a} \frac{dx^a}{d \lambda} \frac{dx^i}{d\lambda} + \frac{1}{2} \frac{\partial g_{ik}}{\partial x^a} \frac{dx^a}{d \lambda} \frac{dx^i}{d\lambda}
$$


Note here that again, $a$ and $i$ are dummy indices - $a$ appears on the lower partial derivative and upper partial derivative terms, and $i$ appears in the lower $g_{ik}$ and upper $dx^i$ term. So let's do two index substitutions which will make the equation so much easier to solve. First, note that the equation we extracted this expression from had three dummy indices - let's reduce it to just two by swapping $a$ with $j$:


$$
\frac{1}{2} \frac{\partial g_{ik}}{\partial x^j} \frac{dx^j}{d \lambda} \frac{dx^i}{d\lambda} + \frac{1}{2} \frac{\partial g_{ik}}{\partial x^j} \frac{dx^j}{d \lambda} \frac{dx^i}{d\lambda}
$$


Second, in a somewhat bizarre move, we will do a twin substitution $i \rightarrow j$ and $j \rightarrow i$ in the second term, while leaving the first term alone:


$$
\frac{1}{2} \frac{\partial g_{ik}}{\partial x^j} \frac{dx^j}{d \lambda} \frac{dx^i}{d\lambda} + \frac{1}{2} \frac{\partial g_{jk}}{\partial x^i} \frac{dx^i}{d \lambda} \frac{dx^j}{d\lambda}
$$


Third, we will switch the order of the ordinary derivative terms in both terms, which we can do, as they are commutative products:


$$
\frac{1}{2} \frac{\partial g_{ik}}{\partial x^j} \frac{dx^i}{d\lambda} \frac{dx^j}{d \lambda} + \frac{1}{2} \frac{\partial g_{jk}}{\partial x^i} \frac{dx^i}{d \lambda} \frac{dx^j}{d\lambda} 
$$


Plugging our modified but technically identical version of the middle term back into the equation, we have:


$$
\frac{d^2 x^i}{d\lambda^2} g_{ik} + \frac{1}{2} \frac{\partial g_{ik}}{\partial x^j} \frac{dx^i}{d\lambda} \frac{dx^j}{d \lambda} + \frac{1}{2} \frac{\partial g_{jk}}{\partial x^i} \frac{dx^i}{d \lambda} \frac{dx^j}{d\lambda} 
 -\frac{1}{2}
\frac{\partial g_{ij}}{\partial x^k} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


We now have common factors, which we can combine to form:


$$
\frac{d^2 x^i}{d\lambda^2} g_{ik} + \frac{1}{2} \left(
\frac{\partial g_{ik}}{\partial x^j} + \frac{\partial g_{kj}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^k}\right) \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


Now we want to get rid of the $g_{ik}$ term. To do this, we will multiply both sides of the equation with the inverse metric $g^{\mu k}$. This gives:


$$
g^{\mu k} \frac{d^2 x^i}{d\lambda^2} g_{ik} + \frac{1}{2} g^{\mu k} \left(
\frac{\partial g_{ik}}{\partial x^j} + \frac{\partial g_{kj}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^k}\right) \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


Let's focus on the first term:


$$
g^{\mu k} \frac{d^2 x^i}{d\lambda^2} g_{ik}
$$


We'll make the tensor contractions easier to see by moving the terms around:


$$
g^{\mu k} g_{ik} \frac{d^2 x^i}{d\lambda^2} 
$$


Recall that $g^{\mu k} g_{ik} = {\delta^\mu}_i$ by the rules of tensor contraction, so we have:


$$
{\delta^\mu}_i \frac{d^2 x^i}{d\lambda^2}
$$


Now, the upper index on the derivative $x^i$ and the lower index $i$ of the Kronecker delta cancel to relabel $i$ to $\mu$, as we saw before in tensor calculus:


$$
{\delta^\mu}_i \frac{d^2 x^i}{d\lambda^2} = \frac{d^2 x^\mu}{d\lambda^2}
$$


So our full equation is:


$$
\frac{d^2 x^\mu}{d\lambda^2} + 
\frac{1}{2} g^{\mu k} \left(
\frac{\partial g_{ik}}{\partial x^j} + 
\frac{\partial g_{kj}}{\partial x^i} - 
\frac{\partial g_{ij}}{\partial x^k}\right) 
\frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


We can further simplify this equation by extracting out the partial derivatives terms in the middle as the **Christoffel symbols**:


$$
\Gamma^\mu_{ij} = \frac{1}{2} g^{\mu k} \left(
\frac{\partial g_{ik}}{\partial x^j} + \frac{\partial g_{kj}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^k}\right)
$$


Where (this is clearer if we expand out the partial derivatives term by term, but it can be seen by just glancing at the equation too) the free indices are $\mu$, $j$, and $i$ (which is why they appear on the Christoffel symbol itself), while the dummy index $k$ is used for summation (which is why it's only present in the partial derivatives).


So we finally arrive at the **geodesic equation**:


$$
\frac{d^2 x^\mu}{d\lambda^2} + 
\Gamma^\mu_{ij} \frac{dx^i}{d\lambda} \frac{dx^j}{d\lambda} = 0
$$


Note that for particles with mass, the paramter $\lambda$ is interpreted to be the proper time $\tau$, but really $\lambda$ can be any invariant parameter along a particle's trajectory. If we set $\lambda = \tau$, then the equations become:


$$
\frac{d^2 x^\mu}{d\tau^2} + 
\Gamma^\mu_{ij} \frac{dx^i}{d\tau} \frac{dx^j}{d\tau} = 0
$$


Any path that obeys the geodesic equation in spacetime is a geodesic. Since spacetime can be curved, these geodesics are not straight lines. The curvature of spacetime - what we experience as gravity - causes distances to change. This causes the metric to change, which in turn affects the paths of particles.
