# Electrodynamics

> "We can scarcely avoid the inference that light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena."
> 
> **James Clerk Maxwell**

In the first chapter, we introduced the classical theory of electricity and magnetism. We discussed electric and magnetic fields, and we ended with a discussion on Maxwell's equations and electrodynamics. Now, we will take a closer look at electrodynamics - and gain critical insights into the nature of light and the electromagnetic field.

## Formulations of the Maxwell equations

We will start by reviewing the Maxwell's equations. Written in the language of vector calculus, they take the form of a system of four partial differential equations, which we show below:

$$
\begin{align}
\nabla \cdot \mathbf{E} &= \frac{1}{\epsilon_0} \rho \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \frac{1}{c^2} \frac{\partial \mathbf{E}}{\partial t}
\end{align}
$$

This form is excellent for conceptual understanding and for illustrating the relationships between the electric and magnetic fields. However, it is rather poorly-suited for actually finding _solutions_. First, there are _four_ PDEs to solve, and second, the last two PDEs are _coupled_, meaning that they cannot be solved independently of each other.

But we can simplify the Maxwell equations into a more tractable form. First, we can reduce the number of equations to solve, because, technically, the first two equations are just constraint equations. That is to say, these two equations don't need to be solved because they are *implicitly satisfied* for any solution of Maxwell equation #3 and Maxwell equation #4, a result first derived by J. A. Stratton in 1941. To show this, let's first take the divergence of the time derivative of $\mathbf{B}$. We get:

$$
\nabla \cdot \left(\frac{\partial \mathbf{B}}{\partial t}\right) = \nabla \cdot (-\nabla \times \mathbf{E}) = 0
$$

Where we substitute in the left-hand side of Maxwell equation #3 and use the [vector calculus identity](https://en.wikipedia.org/wiki/Vector_calculus_identities) that the divergence of the curl is always zero (the vector calculus identities Wikipedia page is a highly-useful resource when doing a lot of vector calculus). But remember, taking the divergence only affects the spatial components of fields (because $\nabla \cdot \mathbf{F} = \partial_x \mathbf{F}_x + \partial_y \mathbf{F}_y + \partial_z \mathbf{F}_z$, there is no time-dependent part in it) so we can swap the time derivative operator and the divergence operator:

$$
\nabla \cdot \left(\frac{\partial \mathbf{B}}{\partial t}\right) = \frac{\partial}{\partial t} (\nabla \cdot \mathbf{B})
$$

However, we already found that $\nabla \cdot (\partial_t \mathbf{B}) = 0$, so:

$$
\frac{\partial}{\partial t} (\nabla \cdot \mathbf{B}) = 0
$$

This means if the initial condition for the magnetic field obeys $\nabla \cdot \mathbf{B} = 0$, then $\nabla \cdot \mathbf{B} = 0$ holds for all times $t$, and therefore, Gauss's law for magnetism is **automatically satisfied** for any solution of just the last two of Maxwell's equations. 

Meanwhile, we can rearrange Maxwell equation #4 to have the time-derivative on the left via:

$$
\frac{\partial \mathbf{E}}{\partial t} = c^2 (\nabla \times \mathbf{B} - \mu_0 \mathbf{J})
$$

Which, knowing that $c^2 = \frac{1}{\mu_0 \varepsilon_0}$, we can simplify to:

$$
\frac{\partial \mathbf{E}}{\partial t} = \left(\frac{1}{\mu_0 \varepsilon_0} \nabla \times \mathbf{B} - \frac{1}{\varepsilon_0} \mathbf{J}\right)
$$

Taking the divergence of both sides, we get:

$$
\nabla \cdot \left(\frac{\partial \mathbf{E}}{\partial t}\right) = \nabla \cdot \left(\frac{1}{\mu_0 \varepsilon_0} \nabla \times \mathbf{B} - \frac{1}{\varepsilon_0} \mathbf{J}\right) = -\frac{1}{\varepsilon_0} \nabla \cdot \mathbf{J}
$$

Again, due to the fact that taking the divergence doesn't include taking any time derivatives, we can swap out the time derivative and divergence operators, that is:

$$
\nabla \cdot \left(\frac{\partial \mathbf{E}}{\partial t}\right) = \frac{\partial}{\partial t} (\nabla \cdot \mathbf{E})
$$

So substituting that in, we have:

$$
\frac{\partial}{\partial t} (\nabla \cdot \mathbf{E}) = -\frac{1}{\varepsilon_0} \nabla \cdot \mathbf{J}
$$

But due to charge conservation, the current density $\mathbf{J}$ and charge density $\rho$ are related by the partial differential equation:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0
$$

This is the **continuity equation** for charge conservation and it means that charge can never be created or destroyed, just moved around. If we rearrange it, we get:

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t}
$$

If we substitute this into $\partial_t (\nabla \cdot \mathbf{E}) = -1/\varepsilon_0 \nabla \cdot \mathbf{J}$  which we derived two steps before, we get:

$$
\frac{\partial}{\partial t} (\nabla \cdot \mathbf{E}) = -\frac{1}{\varepsilon_0} \nabla \cdot \mathbf{J} = \frac{1}{\varepsilon_0} \frac{\partial \rho}{\partial t}
$$

So that we have the relation:

$$
\frac{\partial}{\partial t} (\nabla \cdot \mathbf{E}) =  \frac{1}{\varepsilon_0} \frac{\partial \rho}{\partial t}
$$

Rearranging the terms and doing some straightforward rewriting, we get:

$$
\frac{\partial}{\partial t} (\nabla \cdot \mathbf{E}) - \frac{1}{\varepsilon_0} \frac{\partial \rho}{\partial t} = 0 \Rightarrow \frac{\partial}{\partial t} \left(\nabla \cdot \mathbf{E} - \frac{\rho}{\varepsilon_0}\right) = 0
$$

But we know that $\nabla \cdot \mathbf{E} - \rho / \varepsilon_0$ is just a different way of writing Maxwell equation #1, which is Gauss's law for electricity! So if the initial condition for the electric field obeys $\nabla \cdot \mathbf{E} - \rho / \varepsilon_0 = 0$, then $\nabla \cdot \mathbf{E} - \rho / \varepsilon_0 = 0$ holds for all times $t$, and therefore, Gauss's law for electricity, just like Gauss's law for magnetism that we looked at earlier, is also **automatically satisfied** for any solution of just the last two of Maxwell's equations. To our relief, this means that so long as we check our initial conditions to ensure that the divergence of both the electric and magnetic fields is zero, Maxwell's equations reduce to just two coupled PDEs!

$$
\begin{align}
\frac{\partial \mathbf{E}}{\partial t} &= c^2 (\nabla \times \mathbf{B} - \mu_0 \mathbf{J}) \\
\frac{\partial \mathbf{B}}{\partial t} &= -\nabla \times \mathbf{E}
\end{align}
$$

In free space, that is, when we're not considering any current sources, we can set $\mathbf{J} = \rho = 0$, meaning that $\nabla \cdot \mathbf{E} = 0$ as well as $\nabla \cdot \mathbf{B} = 0$. Maxwell's equations then become:

$$
\begin{align}
\frac{\partial \mathbf{E}}{\partial t} &= c^2 \nabla \times \mathbf{B} \\
\frac{\partial \mathbf{B}}{\partial t} &= -\nabla \times \mathbf{E}
\end{align}
$$

If we take the curl of both sides of each, we find that:

$$
\begin{align}
\nabla \times \left(\frac{\partial \mathbf{E}}{\partial t}\right) &= \nabla  \times c^2 \nabla \times \mathbf{B} \\
\nabla \times \left(\frac{\partial \mathbf{B}}{\partial t}\right) &= -\nabla \times \mathbf{E}
\end{align}
$$

Using the double-curl vector calculus identity $\nabla \times (\nabla \times \mathbf{A}) = \nabla (\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}$, and swapping the time derivative and curl operators (remember that like the divergence, the curl is spatial-only, doesn't have any effect on time), we have:

$$
\begin{align}
\frac{\partial}{\partial t}(\nabla \times \mathbf{E}) &= -c^2 \nabla^2 \mathbf{B} \\
\frac{\partial}{\partial t}(\nabla \times \mathbf{B}) &= \nabla^2 \mathbf{E}
\end{align}
$$

But we know what $\nabla \times \mathbf{E}$ and $\nabla \times \mathbf{B}$ are from Maxwell equations #3 and #4, and we can substitute those in:

$$
\begin{align}
\frac{\partial}{\partial t}(\nabla \times \mathbf{E}) &= \frac{\partial}{\partial t} \left(-\frac{\partial \mathbf{B}}{\partial t}\right) =-\frac{\partial^2 \mathbf{B}}{\partial t^2} \\
\frac{\partial}{\partial t}(\nabla \times \mathbf{B}) &= \frac{\partial}{\partial t} \left(\frac{1}{c^2}\frac{\partial \mathbf{E}}{\partial t}\right) = \frac{1}{c^2}\frac{\partial^2 \mathbf{E}}{\partial t^2}
\end{align}
$$

Equating these expressions with the expressions we got by applying the double-curl identity, we get the wave equations that we analyzed earlier:

$$
\begin{align}
\frac{\partial^2 \mathbf{E}}{\partial t^2} &= c^2 \nabla^2 \mathbf{E} \\
\frac{\partial^2 \mathbf{B}}{\partial t^2} &= c^2 \nabla^2 \mathbf{B}  \\
\end{align}
$$

So we can summarize the results as follows:

| Configuration                                  | System of equations                                                                                                                                                                  | Interpretation             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| Free space (no current/charge sources)         | $\displaystyle \frac{\partial^2 \mathbf{E}}{\partial t^2} = c^2 \nabla^2 \mathbf{E}, \quad \frac{\partial^2 \mathbf{B}}{\partial t^2} = c^2 \nabla^2 \mathbf{B}$                     | EM waves                   |
| General case (can have current/charge sources) | $\displaystyle \frac{\partial \mathbf{E}}{\partial t} = c^2 (\nabla \times \mathbf{B} - \mu_0 \mathbf{J}), \quad \frac{\partial \mathbf{B}}{\partial t} = -\nabla \times \mathbf{E}$ | Any EM field configuration |

But again, the PDEs themselves are not enough. For a complete boundary-value problem, we also need the boundary conditions, and those come from the physics we want to model. We will now look at different boundary-value problems in which we can solve the Maxwell equations analytically.

## Solutions to the electromagnetic wave equation

The solutions to the first case - the Maxwell equations in free space - are of particular interest, as their solutions describe _electromagnetic waves_. The first, and simplest, solution that we will examine is that of the plane wave, given by:

$$
\mathbf{E}(t, x, y, z) = \mathbf{E}_0 \cos(k_x x + k_y y + k_z z - k c t + \phi)
$$

Which is sometimes written in more compact notation as:

$$
\mathbf{E}(t, \mathbf{r}) = \mathbf{E}_0  \cos k(\hat{\mathbf{n}} \cdot \mathbf{r} - ct + \phi)
$$

Or written in equivalent complex exponential form (recall: $e^{i\phi} = \cos \phi + i \sin \phi$), omitting the phase shift for now since we can always include it back in later:

$$
\mathbf{E}(t, \mathbf{r}) = \mathbf{E}_0 e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

The magnitude (electric field strength) is then given by:

$$
E(t, \mathbf{r}) = \|\mathbf{E}\| = E_0 e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

Where $\hat{\mathbf{n}}$ is the normal vector that points in the direction of propagation of the wave. Of course, complex-valued waves are just for mathematical convenience; to get any physically meaningful results, we only consider the real part of the complex exponential, and ignore the imaginary part.

Recall that the output of the function is the _magnitude_ of the wave, and in electrodynamics it is associated with the magnitude of the electromagnetic field at that point. In 1 dimension, this is the familiar sinusoidal wave; in 2 dimensions, this becomes a sinusoidally-rippling surface, see https://www.math3d.org/JdgRCZD3l. In 3 dimensions, it is a bit more difficult to visualize, but here is a volume (density) plot to serve as a visual:

```{figure} img/3d_plane_wave_volume.png
:alt: A 3D density plot of a plane wave. The plot indicates the electric field's magnitude oscillates sinusoidally.
:width: 300px
:align: center

The magnitude of the electric field for a plane wave, which oscillates sinusoidally along the direction of propagation.
```

The intensity still varies sinusoidally, but the wavefronts are planar, as is expected. Note that plane waves are a mathematical idealization; true waves are only approximately planar and would spread out over long enough distances.

We now want to find the associated $\mathbf{B}$ field from the electric field. To do so recall the third of Maxwell's equations:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

Taking the curl of $\mathbf{E}$ is highly nontrivial; however, luckily, we have a very nice identity that $\nabla \times \mathbf{A} = \hat{\mathbf{A}} \times \nabla A$ where $A = \|\mathbf{A}\|$, the proof is in the appendix and is very involved and was partially the result of countless hours on board an airplane spent doing math because I am a weird person. Be aware that $\hat{\mathbf{E}} \neq \hat{\mathbf{n}}$, the unit vector of the electric field is **not** the same thing as the normal vector in the argument of the complex exponential! The electric field has $\hat{\mathbf{E}} = \mathbf{E}/E = \mathbf{E}_0 / E_0$ , remember the unit vector doesn't care about magnitude, only direction, so these two are equivalent. The $\hat{\mathbf{n}}$ in the argument of the complex exponential is the direction of _propagation_ of the wave, but $\hat{\mathbf{E}}$ is the unit vector, i.e. the direction that the _electric field is align_. These are not the same thing because electromagnetic fields are **transverse**; the electric field oscillates up and down, but the wave moves forward. 

With that distinction out of the way, we can resume the calculations. The magnitude of $\mathbf{E}$ is:

$$
E = \|\mathbf{E}\| = E_0 e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

The gradient, $\nabla E$, becomes:

$$
\nabla E = ik\hat{\mathbf{n}}E_0e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

Which can be found by simply taking the gradient component-by-component, and then rearranging them into a vector. Applying the previously-mentioned identity $\nabla \times \mathbf{A} = \hat{\mathbf{A}} \times \nabla A$ results in:

$$
\begin{align}
\nabla \times \mathbf{E} &= \frac{\mathbf{E}_0}{E_0} \times ik\hat{\mathbf{n}}E_0e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)} \\
&= \mathbf{E}_0 \times ik \hat{\mathbf{n}} E_0e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)} \\
&= -ik\hat{\mathbf{n}} \times E_0e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)} \\
&= -ik \hat{\mathbf{n}} \times \mathbf{E}
\end{align}
$$

Where we used the property of cross products that $\mathbf{A} \times \mathbf{B} = -\mathbf{B} \times \mathbf{A}$, and the fact that the cross product is linear so we can simply pull out the constant factors.

Solving for Maxwell #3 and plugging in the previously-obtained expression, we have:

$$
\nabla \times \mathbf{E} = -ik \hat{\mathbf{n}} \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

Which we simply integrate with respect to time to obtain the magnetic field:

$$
\begin{align}
\mathbf{B} &= -\int -ik \hat{\mathbf{n}} \times \mathbf{E}~dt \\
&= ik \int \hat{\mathbf{n}} \times\mathbf{E}_0 e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)} \\
&= \frac{ik}{ikc} \hat{\mathbf{n}} \times\mathbf{E}_0 e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)} \\
&= \frac{1}{c} \hat{\mathbf{n}} \times \mathbf{E}
\end{align}
$$

Or written explicitly, the magnetic field is given by:

$$
\mathbf{B} = \mathbf{B}_0 e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)} = \hat{\mathbf{n}}\times\frac{\mathbf{E}_0}{c} e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

The fact that:

$$
\mathbf{B} = \frac{1}{c} \hat{\mathbf{n}} \times \mathbf{E}
$$

means that the magnetic fields and electric fields are perpendicular to each other. Here's a visual to make things more clear:

```{figure} ./img/plane-waves.svg
:alt: A diagram of electric and magnetic fields, shown perpendicular to each other
:align: center
:width: 200px

Electric and magnetic fields of a plane wave. Notice how the wavefronts are flat, and $\mathbf{E}$ and $\mathbf{B}$ are perpendicular to each other.
```

We should mention that this diagram is not entirely physically accurate; in reality, the electric and magnetic fields span every point in space, so imagine every point filled with electric and magnetic vectors. In addition, the plane waves span the entire domain too, here only slices (isosurfaces is the technical term) are shown. Also, plane waves can propagate in any direction, not just forwards along the $x$ axis, this is a simplified example. However, it is a diagram that is a good approximation for the physical reality.

Electromagnetic waves, like all waves, deliver power and energy from one location to another. Electromagnetic power is given by the Poynting vector:

$$
\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B}
$$

The magnitude of the Poynting vector is the **power flux density**: the power passing through each unit area in space. In our case, since $\mathbf{B} = \frac{1}{c} \hat{\mathbf{n}} \times \mathbf{E}$, if we take $E$ to be the magnitude of the electric field, then $S = \frac{1}{\mu_0 c} E^2$ (why? because the electric and magnetic fields are mutually orthogonal and orthogonal to the normal vector so the cross product is one). To get the actual power, we have to integrate over all considered surface areas:

$$
P = \iint \mathbf{S} \cdot d\mathbf{A} = \frac{1}{\mu_0 c} \iint E^2~dA
$$

In the case that the surface areas are uniform, we have:

$$
P = E_0^2 A e^{2ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

Taking only the real part and using the trigonometric identity $\cos^2 \theta = \frac{1}{2}(1 + \cos 2\theta)$, we have:

$$
P = E_0^2 A \cos^2 k (\hat{\mathbf{n}} \cdot \mathbf{r} - ct)
$$

As a side note, if considering surfaces of constant area, then the intensity would correspondingly be:

$$
I = \frac{P}{A} = E_0^2 \cos^2 k (\hat{\mathbf{n}} \cdot \mathbf{r} - ct)
$$

### Further wave solutions

Plane waves are not physically possible to realize. They are only a good approximation for electromagnetic waves that have dispersed far enough that they _appear_ to be parallel over small enough cross-sections, and thus the electric and magnetic fields are well-approximated with flat, perfectly constant wavefronts. For example, sunlight can be modeled using plane waves, because the waves of light have spread out sufficiently far by the time they reach earth and because we view a tiny cross-section of those waves (they are a solar system radius spread out!) that they look like plane waves. However, real waves falloff by the inverse of distance, where $r = \|\mathbf{r}\|$:

$$
\mathbf{E}(t, \mathbf{r}) = \frac{E_0}{r} e^{ik(\hat{\mathbf{n}} \cdot \mathbf{r} - ct)}
$$

This ensures that assuming surfaces of uniform area, the measured power through each area is given by:

$$
P = \frac{E_0^2 A}{r^2} \cos^2 k (\hat{\mathbf{n}} \cdot \mathbf{r} - ct)
$$

Which is an inverse-square law, required to guarantee energy conservation. Spherical waves are often _also_ called plane waves, due to the fact that other than their spherical propagation, they are essentially *the same* as plane waves. This is because they are monochromatic (have a fixed wavelength, and thus fixed wavenumber) and their wavefronts are flat and uniform. 

But we will now examine a solution that is neither monochromatic nor has flat wavefronts. To start, recall that the linearly of the electromagnetic wave equation means that _any superposition_ of plane waves will _also_ be a solution. This means that we can sum any number of plane waves together to form a new wave. In the limit of infinitely-many plane waves added together, we obtain an integral:

$$
\mathbf{E}(\mathbf{r}, t) = \int_{-\infty}^\infty \dfrac{dk}{2\pi} A(k) e^{ik(\hat{\mathbf{n}}\cdot \mathbf{r} - c t)}
$$

where $A(k)$ is the _amplitude_ of each component plane wave, and dividing by $2\pi$ is just a way of normalizing the plane wave (and we technically don't need it). But this is just in the 1-dimensional case, when we consider only one component of the wavevector. For the full 3-dimensional case, the integral becomes:

$$
\mathbf{E}(\mathbf{r}, t) = \iiint_{-\infty}^\infty \dfrac{d^3k}{(2\pi)^3} A(k) e^{ik(\hat{\mathbf{n}}\cdot \mathbf{r} - c t)}
$$

The integral over an infinite number of waves of differing wavelengths means that the resulting wave can take very different shapes as compared to the component plane waves. In addition, by integrating over individual plane waves, destructive and constructive interference effects (that is, where waves added together amplify each other in some regions and cancel out in others) means that the wave no longer needs infinite energy to be created and obeys energy conservation.

## The Helmholtz equation

Up to this point, we have worked with solutions to the electromagnetic wave equation that were variations of plane waves. But for analyzing more complicated problems in electromagnetics, we need to look beyond plane waves.

For this, we need to directly work with the electromagnetic wave equation:

$$
\dfrac{\partial^2 \mathbf{E}}{\partial t^2} = c^2 \nabla^2 \mathbf{E}
$$

To solve it, we assume that the electric field $\mathbf{E}(\mathbf{r}, t)$ can be written as a product of two functions. We will call the first function $\mathbf{E}_s(\mathbf{r})$, where $s$ denotes "spatial" (for reasons that will become apparent later), and the second function $\mathcal{E}(t)$. Then we have:

$$
\mathbf{E}(\mathbf{r}, t) = \mathbf{E}_s(\mathbf{r}) \mathcal{E}(t)
$$

We may now find the Laplacian and second time derivative of the electric field explicitly:

$$
\begin{align}
\nabla^2 \mathbf{E} = \nabla^2(\mathbf{E}_s(\mathbf{r}) \mathcal{E}(t)) = \mathcal{E}\nabla^2 \mathbf{E}_s \\
\dfrac{\partial^2 \mathbf{E}}{\partial t^2} = \dfrac{\partial^2}{\partial t^2}(\mathbf{E}_s(\mathbf{r}) \mathcal{E}(t)) = \mathbf{E}_s\dfrac{\partial^2 \mathcal{E}}{\partial t^2}
\end{align}
$$

```{note}
The reason why these derivatives turned out to have such simple forms, despite the fact that we normally need to use the verbose product rule when differentiating products of functions, is because $\mathbf{E}_s(\mathbf{r})$ is dependent only on space and $\mathcal{E}(t)$ is dependent only on time. Since the Laplacian is _also_ dependent only on space and the 2nd time (partial) derivative is _also_ dependent only on time, the components independent of space (for the first) and independent of time (for the second) can be treated as constants on differentiation, leading to these simple expressions.
```

By substituting the computed Laplacian and second time derivative into the electromagnetic wave equation, we have:

$$
\mathbf{E}_s\dfrac{\partial^2 \mathcal{E}}{\partial t^2} = c^2 \mathcal{E}\nabla^2 \mathbf{E}_s
$$

If we then divide both sides by $\mathbf{E}_s(\mathbf{r}) \mathcal{E}(t)$ (which is algebraically sound), we have:

$$
\begin{gather}
\dfrac{1}{\mathbf{E}_s(\mathbf{r}) \mathcal{E}(t)} \mathbf{E}_s\dfrac{\partial^2 \mathcal{E}}{\partial t^2} = \dfrac{1}{\mathbf{E}_s(\mathbf{r}) \mathcal{E}(t)}c^2 \mathcal{E}\nabla^2 \mathbf{E}_s \\
\dfrac{1}{\mathcal{E}(t)} \dfrac{\partial^2 \mathcal{E}}{\partial t^2} = \dfrac{1}{\mathbf{E}_s(\mathbf{r})}c^2 \nabla^2 \mathbf{E}_s
\end{gather}
$$

It is also common (as a matter of convention) to divide both sides by $c^2$, such that we have:

$$
\dfrac{1}{c^2\mathcal{E}(t)} \dfrac{\partial^2 \mathcal{E}}{\partial t^2} = \dfrac{1}{\mathbf{E}_s(\mathbf{r})} \nabla^2 \mathbf{E}_s
$$

Since each side is now composed of functions and derivatives of only _one_ variable ($t$ and $\mathbf{r}$ respectively), we say we have _separated_ the variables. And because we have two combinations of derivatives with respect to different variables, they must be equal to a constant (or some multiple or square or cube of a constant). As a matter of fact, we can choose *any* constant formed by any operation on another constant, it just matters that it preserves the fact that it is _constant_. We will call this constant $-k^2$ (this is, in fact, the square of the *wavenumber*, the scalar magnitude of the wavevector, which can be shown via dimensional analysis):

$$
\dfrac{1}{c^2\mathcal{E}(t)} \dfrac{\partial^2 \mathcal{E}}{\partial t^2} = \dfrac{1}{\mathbf{E}_s(\mathbf{r})} \nabla^2 \mathbf{E}_s = -k^2
$$

By just looking at the second equation, we have:

$$
\dfrac{1}{\mathbf{E}_s(\mathbf{r})} \nabla^2 \mathbf{E}_s = -k^2
$$

Which we can rearrange as:

$$
\nabla^2 \mathbf{E}_s + k^2 \mathbf{E}_s = 0
$$

This is the **Helmholtz equation**, the time-independent form of the electromagnetic wave equation. The subscripts can often be dropped to write it in the more simple form $(\nabla^2 + k^2) \mathbf{E} =0$. By separating the time and space components, we can much more readily solve complicated boundary-value problems and only need to solve for spatial boundary conditions  

### Gaussian beams

A Gaussian beam is a particular solution to the Helmholtz equation, given by:

$$
{\mathbf {E} (r,z)}=E_{0}\,{\hat {\mathbf {x} }}\,{\frac {w_{0}}{w(z)}}\exp \left({\frac {-r^{2}}{w(z)^{2}}}\right)\exp \left(\!-i\left(kz+k{\frac {r^{2}}{2R(z)}}-\psi (z)\right)\!\right)
$$

Where $r$ is the radial coordinate along the cross-section of the beam, $z$ is the coordinate along the axis of propagation, $w_0$ is the beam diameter at $z=0$, $k$ is the magnitude of the wavevector, and $w(z)$, $R(z)$ and $\psi(z)$ are functions we will elaborate on shortly. The Gaussian beam models highly-focused and highly-directional electromagnetic waves, such as laser beams or the waves produced by an idealized parabolic antenna - understandably, it is highly-relevant to antenna and laser physics as well as optics.

One of the most important characteristics of a Gaussian beam is its **beam diameter**. The function $w(z)$ describes how the beam loses focus and spreads out with distance. $w(z)$ gives the general beam diameter for any given value of $z$, given by:

$$
w(z) = w_0 \sqrt{1 + \left(\frac{z}{z_R}\right)^2}, \quad z_R = \frac{\pi {w_0}^2 n}{\lambda} = \frac{1}{2} k {w_0}^2
$$

Where $n$ is the refractive index of the medium, and $n \geq 1$, with $n = 1$ in vacuum. The function $\psi(z)$ is called the **Gouy phase**, and is given by:

$$
\psi(z) = \operatorname{arctan} \left(\frac{z}{z_R}\right)
$$

Meanwhile, the function $R(z)$ is the **radius of curvature** of the beam, which describes the curvature of the wavefront, and is given by:

$$
R(z) = z \left[1 + \left(\dfrac{z_R}{z}\right)^2\right]
$$

The magnitude of the Poynting vector (power flux density) of the Gaussian beam is:

$$
S = \frac{{E_0}^2}{2\eta}\left({\frac {w_{0}}{w(z)}}\right)^{2}\exp \left({\frac {-2r^{2}}{w(z)^{2}}}\right)
$$

Where $\eta$ is the impedance (a form of electric resistance), and can be approximated via $\eta = 377 \Omega$ which is the impedance of free space. That is to say, the power falls off with an exponential decay, but the decay is also proportional to the electric field strength and inversely proportional to $w(z)$. Allowing $w(z)$ to increase slowly and using a powerful electric field would be able to minimize the decay.

## Conservation laws

In physics, every theory has its conservation laws, and electrodynamics is no different. There are two important conservation laws within electrodynamics. The first is the **global conservation of charge**:

$$
\dfrac{d}{dt} Q_\mathrm{total} =\dfrac{d}{dt} \iiint \rho \,dV = 0
$$

The conservation of charge requires that the total charge across all of space stay constant. Charges can change between different regions of space, but the _total amount of charge_ across all space is conserved. Thus, we call it the _global_ conservation of charge.

The second is the **continuity equation**:

$$
\dfrac{\partial \rho}{\partial t} = -\nabla \cdot \mathbf{J}
$$

The continuity equation imposes the additional constraint that any change in the charge density $\rho$ must be coupled with a change in the current density $\mathbf{J}$. In physical terms, it means that the charge within a region can _only_ decrease by charges moving in (or out) of the region. 

Let's examine what this means. The global conservation of charge would allow charges to vanish from one local region and appear in another region (so long as the total charge does not change). But the continuity equation would say that this is _impossible_. The amount of charge within a region can **only** change by charges *entering or leaving the region*. Furthermore, any amount of charge *entering* a region must mean that the same amount of charge *left* another region. Thus the net charge of the two regions does _not_ change, and the total amount of charge across all space does not change either.

To the best of our knowledge, charge conservation is universal. Requiring that the continuity equation be satisfied is a fundamental requirement to ensuring that solutions to Maxwell's equations are physically possible.