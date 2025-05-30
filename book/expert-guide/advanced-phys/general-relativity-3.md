# General Relativity, Part 3

After having explored geodesics, the metric tensor, and the curvature tensors, we are ready to tackle the formidable task of finally deriving Einstein's equations!


## Deriving the Einstein Field Equations


As with before, we can use the Euler-Lagrange equations and the principle of least action to obtain the Einstein Field Equations.


The action for General Relativity in empty spacetime can be generalized as:


$$
S =  \kappa \int R \sqrt{-g} ~d^4 x
$$


Here, $g = \det(g_{\mu \nu})$, $d^4x = dt\, dx\, \, dy\, dz$ and $\kappa$ is simply a proportionality constant. Note that while it describes a vacuum, that spacetime can still be curved. For example, you could say that the spacetime _outside_ of a black hole is a vacuum (because there is no matter), but the spacetime would still be curved (because the black hole warps its surrounding spacetime, even if we only include the spacetime around a black hole and not the black hole itself).


The action can be derived from one of two ways. It can be shown to be correct through dimensional analysis - the units on the left and right side of the equation match up. However, there is also a more intuitive way to illustrate this.


The action must be composed of scalar-valued functions (or scalars), as it is an integral over all spacetime, and multidimensional integrals can only take scalar-valued functions or scalars to integrate over (see for yourself that this must be true). But it must also include information about the curvature of spacetime and spacetime itself. As we know, all the information about the curvature of spacetime is captured in the Riemann tensor. But the Riemann tensor is not a scalar-valued function - it is instead a (rank-4) tensor-valued function. So we have to find a way to get a scalar from the Riemann tensor. We already know of a scalar that can be formed from the Riemann tensor - the Ricci scalar. We want to add an additional proportionality constant in front, which is also a scalar, because we'd expect to see constants in our final field equations as well. We can always set the constant $\kappa = 1$ if we find it's not necessary later. Since both the curvature of spacetime and the matter and energy present within spacetime should act on the metric, we add them together. Finally, since spacetime is often curved, we need a factor of $\sqrt{-g}$ to make sure the volume element $d^4 x$ is the same size no matter what coordinates or what spacetime we use. So from there, we obtain the action.


From our action, we know that the Lagrangian is:


$$
\mathscr{L} = \kappa R \sqrt{-g}
$$


We will use the Euler-Lagrange field equations, a slight variation of the original Euler-Lagrange equations we derived:


$$
\frac{\partial \mathscr{L}}{\partial \varphi} - \frac{\partial}{\partial x^\beta} \left( \frac{\partial \mathscr{L}}{\partial (\partial_\beta \varphi)}\right) = 0
$$


Here, $\varphi$ is the field, and in our case, the field is the metric tensor field $g_{\mu \nu} (x^\beta)$, thus $\varphi = g_{\mu \nu}$, so if we substitute, we have:


$$
\frac{\partial \mathscr{L}}{\partial g_{\mu \nu}} - \frac{\partial}{\partial x^\beta} \left( \frac{\partial \mathscr{L}}{\partial (\partial_\beta g_{\mu \nu})}\right) = 0
$$


Note that we use the curly L for the Lagrangian because it is not technically the Lagrangian per se, but the field equivalent of the Lagrangian, known as the **Lagrangian density**. But we'll just call it the Lagrangian here. The distinction between the Lagrangian density and the Lagrangian isn't important here; the practical difference here is that the Lagrangian uses the typical Euler-Lagrange equation, while the Lagrangian density uses the Euler-Lagrange _field_ equation.


We notice in the Euler-Lagrange field equations that the second term contains the partial derivative with respect to the derivatives of the metric. But note that in our Lagrangian, there are no terms that take the derivative of the metric as input. So the second term vanishes, and we are left with a comparatively easier equation:


$$
\frac{\partial \mathscr{L}}{\partial g_{\mu \nu}} = 0
$$


Before we take this derivative, let us first rewrite our Lagrangian as:


$$
\mathscr{L} = \kappa g^{\mu \nu} R_{\mu \nu} \sqrt{-g}
$$


Now, we can finally take the derivative with respect to the metric:


$$
\frac{\partial \mathscr{L}}{\partial g_{\mu \nu}} = \kappa \frac{\partial}{\partial g_{\mu \nu}} \left(g^{\mu \nu} R_{\mu \nu} \sqrt{-g}\right) = 0
$$


We immediately run into a hurdle! The Lagrangian has three multiplied functions, the inverse metric, the Ricci tensor, and the square root of the determinant of the metric. How do we differentiate a triple product? We can use the triple product rule:


$$
(f \cdot g \cdot h)' = f'gh + fg'h + fgh'
$$


Another problem! How do we differentiate the inverse metric with respect to the metric? The answer comes from a matrix calculus identity, which, translated to tensor notation, is this:


$$
\frac{\partial g^{\mu \nu}}{\partial g_{\mu \nu}} = -g^{\mu \nu} g^{\mu \nu}
$$


Final problem! How do we differentiate the determinant of the metric with respect to the metric? This answer also comes from a matrix calculus identity, which is this:


$$
\frac{\partial \det(g_{\mu \nu})}{\partial g_{\mu \nu}} = \frac{\partial g}{\partial g_{\mu \nu}} = g g^{\mu \nu}
$$


With all this in mind, we can finally compute the derivatives. The first term of the derivative is just the derivative of the inverse metric, multiplied by the other two terms in the triple product. The derivative of the Ricci tensor with respect to the metric is zero (it doesn't depend on the metric), so the second term of the derivative of the triple product is zero. In the third term, we need to use the chain rule to differentiate the square root. The final result is this:


$$
-\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} - \kappa \frac{1}{2\sqrt{-g}}g g^{\mu \nu} g^{\mu \nu} R_{\mu \nu} = 0
$$


We can clean this up a bit. First, we can multiply both sides by $-1$, to get:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} + \kappa \frac{1}{2\sqrt{-g}}g g^{\mu \nu} g^{\mu \nu} R_{\mu \nu} = 0
$$


Then, we can multiply both sides of the equation by $\frac{1}{\sqrt{-g}}$, which results in:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} - \kappa \frac{1}{2} g^{\mu \nu} g^{\mu \nu} R_{\mu \nu} = 0 
$$


We remember that $R = g^{\mu \nu} R_{\mu \nu}$, so we can substitute it in:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} - \kappa \frac{1}{2} g^{\mu \nu} R = 0
$$


We want to get rid of the double $g^{\mu \nu}$ terms, so we can multiply both sides of the equation by $g_{\mu \nu} g_{\mu \nu}$, to get:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} g_{\mu \nu} g_{\mu \nu} - \kappa \frac{1}{2} g^{\mu \nu} g_{\mu \nu} g_{\mu \nu} R = 0
$$


The inverse metric contracts with the metric:


$$
g^{\mu \nu} g^{\mu \nu} g_{\mu \nu} g_{\mu \nu} = g^{\mu \nu} g_{\mu \nu} = \delta_\mu^\mu = \sum_{i = 0}^3 1 = 4
$$


So this entire expression becomes:


$$
\kappa 4R_{\mu \nu} - \kappa 2 R g_{\mu \nu} = 0
$$


But we can divide by 4 right after as the right-hand side is zero, to yield:


$$
\kappa R_{\mu \nu} - \kappa \frac{1}{2} R g_{\mu \nu} = 0
$$


We can factor out the constant:


$$
\kappa \left(R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu}\right) = 0
$$


The term inside the parentheses is called the **Einstein tensor** and describes the curvature and characteristics of spacetime:


$$
G_{\mu \nu} = R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu}
$$


In vacuum, the equation we just derived is the Einstein Field Equation:


$$
G_{\mu \nu} = 0
$$


Now, there is matter and energy within space, then we use a modified action, where $\mathcal{M}$ is the contribution to the action of the gravitating matter and energy:


$$
S = \int (\kappa R -\mathcal{M} )\sqrt{-g}~d^4x
$$


So the Lagrangian is:


$$
\mathscr{L} =  (\kappa R -\mathcal{M} )\sqrt{-g}
$$


Using the Euler-Lagrange field equations, this becomes:


$$
-\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} \sqrt{-g} - \kappa \frac{1}{2\sqrt{-g}}g g^{\mu \nu} g^{\mu \nu} R_{\mu \nu} - \frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} \sqrt{-g} + \frac{1}{2 \sqrt{-g}} gg^{\mu \nu} \mathcal{M} = 0
$$


First, we multiply by $-1$:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu} \sqrt{-g} + \kappa \frac{1}{2\sqrt{-g}}g g^{\mu \nu} g^{\mu \nu} R_{\mu \nu} + \frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} \sqrt{-g} - \frac{1}{2 \sqrt{-g}} gg^{\mu \nu} \mathcal{M} = 0
$$


Then we multiply by $\frac{1}{\sqrt{-g}}$:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu}  - \kappa \frac{1}{2} g^{\mu \nu} g^{\mu \nu} R_{\mu \nu} + \frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} \sqrt{-g} + \frac{1}{2} g^{\mu \nu} \mathcal{M} = 0
$$


We use the definition $R = g^{\mu \nu} R_{\mu \nu}$:


$$
\kappa R_{\mu \nu} g^{\mu \nu} g^{\mu \nu}  - \kappa \frac{1}{2} g^{\mu \nu} R + \frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} \sqrt{-g} + \frac{1}{2} g^{\mu \nu} \mathcal{M} = 0
$$


And by contraction with $g_{\mu \nu} g_{\mu \nu}$ we have:


$$
\kappa R_{\mu \nu}   - \kappa \frac{1}{2} g_{\mu \nu} R + \frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} g_{\mu \nu} g_{\mu \nu} \sqrt{-g} + \frac{1}{2} g_{\mu \nu} \mathcal{M} = 0
$$


We can move the second and third terms, which depend on $\mathcal{M}$ to the right of the equation:


$$
\kappa R_{\mu \nu}   - \kappa \frac{1}{2} g_{\mu \nu} R = -\frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} g_{\mu \nu} g_{\mu \nu} \sqrt{-g} - \frac{1}{2} g_{\mu \nu} \mathcal{M}
$$


And factor the left-hand side of the equation:


$$
\kappa \left(R_{\mu \nu} - \frac{1}{2} g_{\mu \nu} R\right) = -\frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} g_{\mu \nu} g_{\mu \nu} \sqrt{-g} - \frac{1}{2} g_{\mu \nu} \mathcal{M}
$$


We recognize our familiar friend, the Einstein tensor, on the left. If we define a tensor $T_{\mu \nu}$ to equal the right-hand side:


$$
T_{\mu \nu} = -\frac{\partial \mathcal{M}}{\partial g_{\mu \nu}} g_{\mu \nu} g_{\mu \nu} \sqrt{-g} - \frac{1}{2} g_{\mu \nu} \mathcal{M}
$$


Then we have the complete field equations:


$$
G_{\mu \nu} = \frac{1}{\kappa} T_{\mu \nu}
$$


The tensor $T_{\mu \nu}$ on the right is called the **stress-energy tensor**. There is no one "general formula" for the stress-energy tensor; we can define different expressions for the stress-energy tensor depending on what matter, energy, momentum, and stresses are present within the region of spacetime being analyzed, with the only real rule being that the resulting expression follow tensor algebra conventions (e.g. same number of free indices on both sides of the equation). One of the simplest expressions for a stress-energy tensor is:


$$
T_{\mu \nu} = \rho U_\mu U_\nu
$$


Here, $U_\mu$ and $U_\nu$ are four-velocities, as shown before in special relativity, and $\rho$ is the density of the gravitating matter-energy.


But back to the equation:


$$
G_{\mu \nu} = \frac{1}{\kappa} T_{\mu \nu}
$$


What is the constant $\kappa$? We will need to use the Newtonian limit of relativity to answer that question. When gravity is weak, and objects are moving much slower than the speed of light, we expect that we can recover Poisson's equation from the field equation. We will cover that in the following derivation.


Given that four-velocity is defined as $U_\mu = (\gamma c, \gamma v)$, and we defined objects to be moving much slower than the speed of light, the 0th component of four-velocity, so slow that their speeds are effectively zero compared to the speed of light, we can effectively say that $\gamma \approx 1$ and $U_\mu \approx (c, 0, 0, 0)$. Therefore, the component $T_{00}$ of the stress-energy tensor is just $\rho c^2$, and all other components of the stress-energy tensor are zero.


Given a static metric, that is, one that doesn't change much in time, we can also say that $\partial_0 g_{\mu \nu} = 0$. And because we expect spacetime to be very close to Minkowski spacetime, we will set:


$$
g_{\mu \nu} = \eta_{\mu \nu} + h_{\mu \nu}
$$


Where $h_{\mu \nu}$ is a tiny bit of metric that accounts for Newtonian gravity. Also, given our low velocity assumtions, we already mentioned that:


$$
U^{\mu} = \left(\frac{dt}{d\tau}, \frac{dx}{d\tau}, \frac{dy}{d\tau}, \frac{dz}{d\tau}\right) \approx (c, 0, 0, 0)
$$


We consider the geodesic equations:


$$
\frac{d^2 x^\mu}{d\tau^2}  + \Gamma^\mu_{\gamma \sigma} \frac{dx^\gamma}{d\tau} \frac{dx^\sigma}{d\tau} = 0
$$


We can simplify given that given that only the $\frac{dt}{d\tau}$ component matters, because all the other velocities are zero:


$$
\frac{d^2 x^\mu}{d\tau^2}  + \Gamma^\mu_{00} \frac{dt}{d\tau} \frac{dt}{d\tau} = 0
$$


We can rewrite this as:


$$
\frac{d^2 x^\mu}{d\tau^2}  = -\Gamma^\mu_{00} \frac{dt}{d\tau} \frac{dt}{d\tau}
$$


And recalling $\frac{dt}{d\tau} \approx c$, we have:


$$
\frac{d^2 x^\mu}{d\tau^2}  = -\Gamma^\mu_{00} c^2
$$


Now, we can compare this to Newton's equation for gravity:


$$
\frac{d^2 r}{dt^2} = -\nabla  \phi
$$


Therefore:


$$
\Gamma^\mu_{00} c^2 = \nabla \phi
$$

$$
\Gamma^\mu_{00} = \frac{1}{c^2} \nabla \phi
$$


Now, given that:


$$
\Gamma^i_{k l} = \frac{1}{2} g^{im} (\partial_l g_{mk} + \partial_k g_{ml} - \partial_m g_{kl})
$$


If we substitute $i \to \mu, k \to t, l \to t$, we have:


$$
\Gamma^\mu_{00} = \frac{1}{2} g^{\mu m} (\partial_t g_{mt} + \partial_t g_{mt} - \partial_m g_{00})
$$


But recall that $\partial_t g_{\mu \nu} = 0$ given our static metric assumption, so:


$$
\Gamma^\mu_{00} = -\frac{1}{2} g^{\mu m} \partial_m g_{00}
$$


Since $g^{\mu \nu} = \eta^{\mu \nu} - h^{\mu \nu}$, we have:


$$
\Gamma^\mu_{00} = -\frac{1}{2} (\eta^{\mu m} - h^{\mu m} )(\partial_m \eta_{00} - \partial_m h_{00})
$$


We can simplify this by noting that because $\eta_{00} = -1$, its derivative is zero, so:


$$
\Gamma^\mu_{00} = -\frac{1}{2} (\eta^{\mu m} - h^{\mu m} ) \partial_m h_{00}
$$


If we expand this out, we would get:


$$
\Gamma^\mu_{00} = -\frac{1}{2} \eta^{\mu m} \partial_m h_{00} + h^{\mu m} \partial_m h_{00}
$$


But the second term is very tiny, so we can effectively say it is zero, and given $\eta^{\mu m} = -1$, we get:


$$
\Gamma^\mu_{00} = \frac{1}{2} \partial_m h_{00}
$$


```{note}
How did we know that $\eta_{\mu m} = -1$? This is because $\eta_{\mu m}$ is the first column of the Minkowski metric (as $m$ is a dummy index, so you can think of it as $\eta_{0 m} \dots \eta_{3 m}$), and the only non-zero term in its first column is $\eta_{00}$.
```


The partial derivative with respect to an arbitrary coordinate is just the gradient:


$$
\Gamma^\mu_{00} = \frac{1}{2} \nabla h_{00}
$$


We already know what $\Gamma^\mu_{00}$ is though, so:


$$
\frac{1}{c^2} \nabla \phi = \frac{1}{2} \nabla h_{00}
$$


So we find that $h_{00} = \frac{2\phi}{c^2}$, and therefore $g_{00} = - 1 - \frac{2\phi}{c^2}$.


Now, we have everything we need to compute the Einstein tensor. Using the definition of the Ricci tensor, we have:


$$
R_{ij} = \partial_k \Gamma^k_{ij} - \partial_j \Gamma^k_{ik} + \Gamma^k_{ij} \Gamma^m_{km} - \Gamma^k_{im} \Gamma^m_{jk}
$$


Given our knowledge of $\Gamma^\mu_{00}$, and with substitutions $k \to \mu, i \to t, j \to t$, we have:


$$
R_{00} = \partial_\mu \Gamma^\mu_{00} - \partial_t \Gamma^\mu_{t\mu} + \Gamma^\mu_{00} \Gamma^m_{\mu m} - \Gamma^\mu_{tm} \Gamma^m_{t\mu}
$$


But recall that the time derivative of the metric must be zero, so the second term cancels out. And recall that all the Christoffel symbols that are not $\Gamma^\mu_{00}$ are zero. If we expand out the dummy summation indices, we find that they all go to zero. Therefore, we just have:


$$
R_{00} = \partial_\mu \Gamma^\mu_{00}
$$


Which becomes:


$$
R_{00} = \frac{1}{c^2} \nabla^2 \phi
$$


Recall the definition of the Einstein tensor:


$$
G_{\mu \nu} = R_{\mu \nu} - \frac{1}{2} g_{\mu \nu} g^{\mu \nu} R_{\mu \nu}
$$


If we substitute, we have:


$$
G_{00} = R_{00} - \left[\left(- 1 - \frac{2\phi}{c^2}\right) R_{00}\right] = \frac{1}{c^2} \nabla^2 \phi + \frac{1}{c^2} \nabla^2 \phi + \frac{2\phi}{c^4} \nabla^2 \phi
$$


Now, since $c^4$ is a massive number, $\frac{2\phi}{c^4} \approx 0$, so:


$$
G_{00} = \frac{2}{c^2} \nabla^2 \phi
$$


Using the Einstein field equations:


$$
G_{\mu \nu} = \frac{1}{\kappa} T_{\mu \nu}
$$


We can substitute in our values for the Einstein and stress-energy tensors:


$$
\frac{2}{c^2} \nabla^2 \phi = \frac{1}{\kappa} \rho c^2
$$
$$
\nabla^2 \phi = \frac{1}{2\kappa} \rho c^4
$$


Compare this with Poisson's equation:


$$
\nabla^2 \phi = 4\pi G\rho
$$


This means that:


$$
\frac{1}{2\kappa} \rho c^4 = 4\pi G\rho
$$

$$
\kappa = \frac{c^4}{8\pi G}
$$


Remember the field equations:


$$
G_{\mu \nu} = \frac{1}{\kappa} T_{\mu \nu}
$$


Now knowing the value of $\kappa$, we need only substitute to get:


$$
G_{\mu \nu} = \frac{8\pi G}{c^4} T_{\mu \nu}
$$


This elegant equation is the apotheosis of general relativity, and it rightfully deserves its place as one of the most famous equations in all of physics.


Note that sometimes, there is an alternate form of the Einstein Field Equations that is easier to solve. To do this, we expand out the full equations:


$$
R_{\mu \nu} - \frac{1}{2} Rg_{\mu \nu} = \frac{8\pi G}{c^4} T_{\mu \nu}
$$


We now multiply both sides by $g^{\mu \nu}$:


$$
g^{\mu \nu} R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu} g^{\mu \nu} = \frac{8\pi G}{c^4} T_{\mu \nu} g^{\mu \nu}
$$


Using the fact that $g_{\mu \nu} = g^{\mu \nu} = 4$ and $T_{\mu \nu} g^{\mu \nu} = T$, this becomes:


$$
R - \frac{1}{2} (4R) = \frac{8\pi G}{c^4} T \Rightarrow -R = \frac{8\pi G}{c^4} T
$$


So, substituting back into the original EFEs:


$$
R_{\mu \nu} +\frac{1}{2} \frac{8\pi G}{c^4} T g_{\mu \nu} = \frac{8\pi G}{c^4} T_{\mu \nu}
$$

$$
R_{\mu \nu} = \frac{8\pi G}{c^4} \left(T_{\mu \nu} - \frac{1}{2} g_{\mu \nu} T \right)
$$


This makes the field equations simpler for vacuum solutions, where $T_{\mu \nu} = T = 0$. Thus, the equations just become:


$$
R_{\mu \nu} = 0
$$


which is still incredibly hard to solve, but more manageable than the typical case.


Finally, there is one more important fact about the field equations: taking the covariant derivatives of both sides is equal to zero. This means that:


$$
\nabla_\mu T_{\mu \nu} = 0
$$


This expression may look familiar if we recall that the covariant derivative with a repeated index is just the divergence of a field. What this is saying is that the total change in matter-energy flux in all of spacetime is zero - essentially, the conservation of energy.


## A recap with intuition


After doing so much math, it is helpful to reconnect with what the math is actually _saying_. That is, we want to regain our physical intuition for what the math describes.


Gravity is a fictitious force, caused by the curvature of spacetime. When spacetime isn't curved, particles undergo no acceleration, and thus feel no gravitational force. But when spacetime is curved, which happens whenever masses are present in spacetime, particles undergo a definite acceleration. Due to the equivalence principle, the effect of gravity is indistinguishable from the effect of an acceleration, so therefore particles that are being accelerated feel like a force is acting on them.


The gravitational field is an object that extends through all space that gives each point a vector proportional to the gravitational force. Masses create and vary the gravitational field, and in turn the field exerts a force on masses within the field.


The gravitational potential is a function whose slope is equal to the gravitational field. It can be thought of as a landscape that masses are placed in. Where that landscape is very steep, the gravitational force is very strong; where that landscape is very flat, the gravitational force is very weak.


The metric tensor is a mathematical description of a spacetime. The classical analogue of it is the gravitational potential. Just as the gravitational potential influences the force of gravity, the metric tensor influences the curvature of spacetime, which particles experience as gravity.


We can measure distances in typical Euclidean space using a fixed grid, where the increments between the grid line are measured by constant basis vectors. In curved spacetime, basis vectors are no longer constant. The Christoffel symbols are a precise measure of how basis vectors changes in spacetime, or essentially, how the Euclidean constant grid gets distorted in spacetime. It is roughly analogous to the gravitational field. Just as a gravitational field disappears in empty space far away from any masses, the Christoffel symbols vanish too.


The Riemann tensor describes how the curvature of spacetime changes a vector as you move it in different directions in spacetime. The Ricci tensor describes how a volume in spacetime located at a given point in spacetime becomes contracted due to the curvature of spacetime. The Einstein tensor is the _average_ value of this contraction of volume across all of the region of spacetime being studied.


The stress-energy tensor describes the matter-energy fluxes within a region of spacetime. The classical analogue would be matter density. Finally, just as matter is the source for gravity in Newtonian mechanics, matter is the source of spacetime curvature in General Relativity, and spacetime curvature is what we feel as gravity. John Archibald Wheeler famously summarized all of these ideas with the succint observation:

> "Spacetime tells matter how to move; matter tells spacetime how to curve"
