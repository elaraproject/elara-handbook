# Electricity and magnetism

> "Science is an ongoing process. It never ends. There is no single ultimate truth to be achieved...because this is so, the world is far more interesting."
> 
> **Carl Sagan**

Physics as we know today may have started with Newton, but it most certainly did not end with him. Newton's contemporaries (and sometimes rivals) continued to build on his work. In the following centuries, advancements in physics resulted in the successful theories explaining everything from sound, to mechanical vibrations, to heat flow, to even the tides. But among the most long-lasting - and most successful - achievements of classical physics is the classical theory of **electricity and magnetism**.

## Electrostatic force

The classical theory of electricity and magnetism concerns the behavior of **charged objects**. Objects are **charged** due to an imbalance in their number of protons and electrons. As protons are immobile, the *movement of electrons* causes changes in charge. Objects gaining electrons become negatively-charged, and objects losing electrons become positively charged. We measure charge using units of **coulombs** and typically use the symbol $q$ for charge. 

Like charges attract, and opposing charges repel, causing a force between any two charges placed together. The magnitude of this attraction (or repulsion) can be found from **Coulomb's force law**, expressed as follows:

$$
F_e = k\frac{q_1 q_2}{r^2}
$$

Here, $r$ is the separation between the charges, and $k$ is the Coulomb constant, equivalent to about $8.99 \times 10^9\ \mathrm{N \cdot m^2 / C^2}$. It is common to call $\vec F_e$ the _electrostatic force_ - here, we'll use the term _electric force_, which is more intuitive (though less accurate). _Electrostatic_ means that charges are moving so slowly that we may consider them essentially stationary (static). In many cases, we can _assume_ that this approximation holds true, even if charges are technically moving, as long as the charges are relatively slow-moving.

```{note}
It is common to write $k = \dfrac{1}{4\pi \varepsilon_0}$ in equations involving electrostatics, where $\varepsilon_0$ is the **electric constant**, but here we have chosen to just use $k$ for simplicity.
```

The **vector form** of Coulomb's force law is found by taking the scalar form and adding a unit vector $\hat r_{12}$ pointing between the two objects. This, however, is not as simple as it may seem, because a force must be the action of _one_ object on _another_ object. Thus the force of charge $q_1$ acting on $q_2$, which is a vector, is _not_ the same vector as the force of charge $q_2$ acting on $q_1$ (in fact they are opposite in direction, by Newton's third law). Therefore, we must define two different forces, $\vec F_{12}$ for the force _exerted by_ charge $q_1$ on charge $q_2$, and $\vec F_{21}$ for the force _exerted by_ charge $q_2$ on charge $q_1$. They are written as follows:

$$
\begin{align*}
\vec F_{12} = k\frac{q_1 q_2}{r^2} \hat r_{12} \\
\vec F_{21} = k\frac{q_1 q_2}{r^2} \hat r_{21} \\
\end{align*}
$$

Here, $\hat r_{12}$ is the unit vector pointing from $q_1$ to $q_2$, and similarly, $\hat r_{21}$ is the unit vector pointing from $q_2$ to $q_1$:

$$
\begin{align*}
\hat r_{12} = \dfrac{\vec r_2 - \vec r_1}{\|\vec r_2 - \vec r_1\|} \\
\hat r_{21} = \dfrac{\vec r_1 - \vec r_2}{\|\vec r_1 - \vec r_2\|}
\end{align*}
$$


A particularly nice quality about Coulomb's force law - and the whole of electricity and magnetism in general - is that electric forces (and as we'll see later on, magnetic forces) obey the **superposition principle**. This means that the combined electric (or magnetic) force is just a sum of the individual forces pointing between each of the charges. This also means that the differential equations in the theory of electricity and magnetism are **all linear differential equations**, and two solutions can be added together to find a new solution without any extra work. This will be a _very important_ and useful fact later on.

## Electric field

We recall that Coulomb's force law, like any force, is subject to Newton's second law, and thus results in a differential equation that can be solved to find the trajectories of each of the two charges. In the case of two charges $q_1, q_2$ interacting, the differential equations are:

$$
\begin{align*}
\dfrac{d^2 \vec r_2}{dt^2} = k\frac{q_1 q_2}{|\vec r_2 - \vec r_1|^2} \hat r_{12} \\
\dfrac{d^2 \vec r_1}{dt^2} = k\frac{q_1 q_2}{|\vec r_1 - \vec r_2|^2} \hat r_{21}
\end{align*}
$$

However, if there are more than two charges interacting, the forces between all the charges must be accounted for, meaning that the differential equations grow extremely long and become solvable only by computer. For this reason, while Coulomb's force law is sometimes useful, a **field formulation** is the far more preferred method of mathematically modelling the interactions of charges.

Recall that fields (in physics) denote quantities that are continuously spread out across all of space, such as the gravitational field and gravitational potential (potential field). The **electric field** is a vector field produced by a charge and extends throughout space. In the field formulation, instead of a charge directly exerting a force on other charges, it is the _electric field_ of the charge that exerts the force. Every other charge *also* produces an electric field that exerts a force on all the other charges except themselves. Each of these electric fields, that we've considered separate up to this point, are really just labels for parts of _one_ electric field that carries forces between _all_ charges. Every charge produces part of the electric field, and the electric field exerts a force on every charge, determining the trajectories of each charge. In words inspired by the physicist John Archibald Wheeler, we may surmize that: 

> _Charges make the electric field change, the electric field makes charges move._

While technically there is no distinction between the electric fields of different charges - they are all part of the same *singular electric field* - it is mathematically convenient to speak of electric fields specific to a single charged object. For instance the electric field *produced* by a single point charge $Q$ located at the origin is given by:

$$
\vec E(\vec r) = \frac{kQ}{r^2} \hat r
$$

This electric field exerts an electric force $\vec F_e$ on any other charge $q$, given by:

$$
\vec F_e = q \vec E
$$

```{note}
Be sure to remember that the $Q$ here is of the charge _creating_ the electric field, and $q$ is of the charge that _feels_ the force from the electric field.
```

Since the electric field is a vector field - more precisely, a force field - we can visualize it with vector plots. Using the example of our point charge, the electric field vectors extend outwards if the point charge is positive, and inwards if the point charge is negative:

![](https://cdn.kastatic.org/ka-perseus-images/6db3d4851432e3cded684cd6748f779fea347f52.svg)

When the electric field is created by _two_ charges of opposite sign, we call it a dipole. There exist electric fields produced by more than two charges, right up to arrangements of uncountably many charges. In any case with more than one charge, we must superimpose (sum) the individual electric fields from each charge, resulting in an electric field formed by a _superposition_ of charges:

$$
\vec E(\vec r) = \sum_i \frac{kQ_i}{|\vec r- \vec r_i|^2} \hat r_i
$$

Here, $\vec r_i$ is the position of a charge $Q_i$ in the collection of charges, and $\hat r_i$ is the unit vector pointing from $\vec r_i$ to $\vec r$ (this direction can be somewhat confusing: draw these vectors out on paper to see why it's the case).

```{note}
Unless otherwise specified, we always use $\vec r = \langle x, y, z\rangle$ as the **position vector** pointing from the origin to point $(x, y, z)$ in space.
```

This formula may be slightly clearer if we rewrite it explicitly in terms of coordinate (rather than vector) form:

$$
\vec E(x, y, z) = \sum_i \frac{kQ_i}{[(x - x_i)^2 + (y-y_i)^2 + (z-z_i)]^2} \hat r_i
$$

If we want to continue this process by considering a collection of ever-smaller charges, we can find the electric field of a _continuous distribution_ of charges by integration. To do so, we shrink the charges $Q_i$ to infinitesimal charges $dq$, then integrate along every point $\vec r' = (x', y', z')$ within the charge-containing region. The charge distribution can be assumed to be continuous as the charges shrink to very very small, so we may define a charge density function $\rho(\vec r')$, where $dq' = \rho(\vec r')\, dV'$ is the infinitesimal amount of charge contained in a tiny region of space $dV'$ within the charge-containing region. The electric field produced by the entire distribution of charges is then given by:

$$
\begin{align*}
\vec E(\vec r) &= \int \dfrac{k\, dq'}{|\vec r - \vec r'|^2} \hat r' \\
&= \int \dfrac{k\, dq'}{|\vec r - \vec r'|^2} \dfrac{\vec r - \vec r'}{|\vec r - \vec r'|} \\
&= k\int \dfrac{\vec r - \vec r'}{|\vec r - \vec r'|^3} \rho(\vec r')\, dV'
\end{align*}
$$

Where $\hat r' = \dfrac{\vec r - \vec r'}{|\vec r - \vec r'|}$ is the unit vector pointing from a point $\vec r' = (x', y', z')$ within the charge-containing region to point $\vec r = (x, y, z)$. All the primes in the integral (e.g. $\vec r', \hat r', dV'$) indicate points _within_ the charge-containing region, as we integrate over every point within that region, whereas all the unprimed coordinates (e.g. $\vec r$) indicate a point in space (which can be outside the charge-containing region). This is **the integral form of Coulomb's law** for the electric field, and does give the right expression for the electric field, at least when the electrostatic approximation holds. It is (understandably) rather tedious to solve and often can only be solved by computer.

Note that the integral form of Coulomb's law has three specific cases depending on whether the charge density is a _linear_ charge density $\lambda(\vec r')$, _surface_ charge density $\sigma(\vec r')$, or _volume_ charge density $\rho(\vec r')$.

For linear charge distributions, we have $dq' = \lambda(\vec r') dr'$ where $dr'$ is the line element of the linear charge distribution to integrate over (e.g. charged rod, loop of wire, etc.) This means the integral becomes a line integral betweem the endpoints of the linear charge distribution (e.g. between ends of wire, 360 degrees around a circular loop, along the path of a charge helix, etc.):

$$
\vec E(\vec r) = \int \limits_\mathrm{line} k\dfrac{\lambda(\vec r') dr'}{|\vec r - \vec r'|^3} (\vec r - \vec r')
$$

For surface charge distributions (e.g. plane of charge, disk of charge, etc.) we have $dq' = \sigma(\vec r') dA' = \sigma dx' dy'$ where $dA'$ is the surface element of the surface charge distribution to integrate over. Therefore, Coulomb's law becomes a surface integral over every patch of charge $dq'$ across every patch of surface $dA'$:

$$
\vec E(\vec r) = \iint \limits_\mathrm{surface} k\dfrac{\sigma(\vec r') dA'}{|\vec r - \vec r'|^3} (\vec r - \vec r') = \iint \limits_\mathrm{surface} k\dfrac{\sigma(\vec r') dx'dy'}{|\vec r - \vec r'|^3} (\vec r - \vec r')
$$

For volume charge distributions (e.g. solid sphere of charge, shell of charge, block of charge), we have $dq' = \rho dV' = \rho(\vec r') dx' dy' dz'$ where $dV'$ is the volume element of the volume charge distribution to integrate over. Therefore, Coulomb's law becomes volume integral over every infinitesimal volume $dV'$ containing charge $dq'$:

$$
\vec E(\vec r) = k\iiint \limits_\mathrm{volume} \dfrac{\rho(\vec r') dV'}{|\vec r - \vec r'|^3} (\vec r - \vec r') = k\iiint \limits_\mathrm{volume} \dfrac{\rho(\vec r')\, dx'dy'dz'}{|\vec r - \vec r'|^3} (\vec r - \vec r')
$$

```{note}
It is important to remember that in all cases of applying Coulomb's law, the integrals are _always_ done **with respect to the primed coordinates**. That is, we integrate over $x', y', z'$, _not_ $x, y, z$. Each point $(x', y', z')$ represents a point _within the charge distribution_, and we integrate over the contribution to the electric field from all the points within the charge distribution to be able to find the total electric field.
```

It is common to say that applying Coulomb's law is finding the electric field by _brute-force_, understandably, given its tediousness. But there is a more _elegant_ way of computing the electric field. Suppose we analyze an bounded region of space around an electric field. For instance, this could be the spherical region around a point charge, as shown in the figure below:

![Spherical region around point charge](https://study.com/cimages/multimages/16/point_charge_example255946289342482603.png)

We could model this spherical region as a sphere (unsurprisingly). Then the region would be defined by a sphere of radius $r$, which contains a total volume of:

$$
V = \dfrac{4}{3} \pi r^3
$$

Which is just the volume of a sphere. Now, we can describe the _bounds_ of this region as the edge of the sphere. The edge of the sphere is simply its surface, and the formula of the surface area of the sphere is given by:

$$
A = 4\pi r^2
$$

If we divide the surface of the sphere into tiny "patches" of surface, each of size $dA$, then we can _integrate_ the electric field over the entire surface of the sphere to get the total electric field "passing" the boundary of the sphere. We call this the **electric flux**, symbol $\Phi_E$, and we can write it as an integral (the circle means "closed boundary", i.e. no holes in the boundary), like this:

$$
\Phi_E=\oint \limits_\text{surface} \mathbf{E} \cdot d\mathbf{A}
$$

We can illustrate the flux across the spherical boundary (the technical term is _Gaussian surface_) of our spherical region as follows:


![A spherical bounding surface](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6aVmAotCl6bOvJFZuqZRfEU2zzMGVNkQ-Sg&s)


```{note}
The reason this is a dot product rather than normal multiplication is that the amount of electric field "passing" the boundary of our spherical region also depends the angle between the electric field and the surface. In this case, the electric field vectors are perfectly perpendicular to the surface, so it reduces to a normal dot product, but this is not _always_ the case.
```

Through a mathematical law called **Gauss's law**, the total amount of flux is equal to the total charge density *within* the region, multiplied by a constant:

$$
\oint \mathbf{E} \cdot d\mathbf{A} = 4\pi k Q_\mathrm{total}
$$

This leads to a crucial result: the electric field passing through the _bounds_ of our spherical region is *determined* by the total amount of charge *within* the spherical region's volume. Thus, if we know the total charge within the spherical region, then we can figure out the electric field within it! In addition, Gauss's law also can be converted (through some vector calculus identities) into a partial differential equation. We call it the _differential form_ of Gauss's law, and it takes the following form:

$$
\nabla \cdot \mathbf{E} = 4\pi k \rho
$$

While not as easy to work with, solutions to the differential form of Gauss's law are perfectly equivalent to the integral version, and also give you the electric field.

## Electrical potential energy and electric potential

The **electrical potential energy** is the energy stored in a collection of charges, and we denote it by $U_E$. For two charges $q_1, q_2$, the electric potential energy stored within the system of charges is given by:

$$
U_E = \frac{kq_1 q_2}{r}
$$

The electric potential energy arises as a consequence of the electric force. When the electric force is attractive, charges are bound together, and it _takes energy_ to "knock" a charge out of position. An example of this is within an atom, where the positively-charged protons and the negatively-charge electrons are held together by an attractive force, preventing them from flying away from each other. In such cases, the electric potential energy of the system is **negative**, meaning that the system is stable (physics-wise) and an amount of energy *equal* in magnitude to the electric potential energy must be _put in_ to break apart the system. The converse is true if the electric force is repulsive. In this case, _no energy is required_ to "knock" the like charges out of position; in fact, it would _take_ energy to keep the like charges in place. So the electric potential energy of the system is **positive**, meaning that energy must be _released_ - typically by converting the potential energy of the system to some other form of energy - to keep the system together.

But just as we found that electric fields are mathematically more useful than simply analyzing electric forces, there exists a more useful and elegant way to formulate electric potential energy. Instead of considering the electric potential energy of a collection of charges, we examine just a _single charge_ $Q$, and ask what the electric potential energy _would theoretically be_ if we chose to place another charge $q$ at some position $\vec r$ to form a two-charge system. We may then write the electric potential energy as $U_E = q V$, where $V(r)$ is the **electric potential**:

$$
V(r) = \dfrac{kQ}{r}
$$

The electric potential describes what the electric potential energy _would be_ if we place an arbitrary number of charges at any location in space. Unlike the electric potential energy, it is a function of position, which means that it is not a number; it is a **field**. More specifically, it is a scalar field that is closely related to the electric field. But first, it may be helpful to have a more intuitive picture.

The electric potential can be thought of like electrical pressure of a sort. Just as normal water pressure causes fluid motion of water molecules that are within the water, voltage causes the motion of the charges placed in an electric field. One may say that the electric potential "pushes" (positive) charges from regions of *higher energy to lower energy* - outwards if the electric potential is positive, and inwards if the electric potential is negative (the opposite is true for negative charges). The strength of this "push" depends on the difference in electric potential between two points; if two points have nearly the *same* electric potential, the "push" is very weak, but if two points have a *great difference* in electric potential, the "push" can be very strong. But a distribution of charges creates an electric field! Thus the electric potential's variation in space is also the _source_ of the electric field, which we may write mathematically as:

$$
E = -\nabla V
$$

Voltage, also called **potential difference**, is when you evaluate the _difference_ in potential between two points, $V(b) - V(a)$, just as we alluded to earlier. These two points could be one point on a wire in the air and the other point on the ground. Another two points could be a charge in empty space and a point infinitely far away. The first point pair is most useful for calculations that require accuracy, while the second is most useful for calculations where we can approximately assume that the potential would become weaker and weaker at longer distances from a charge.

With all that being said, how do we actually go about _calculating_ the electric potential? There exist two primary ways of computing the electric potential. The first, the sum/integral method, is very similar to that of the electric field. In the discrete case (i.e. individual charges at different locations) it reads:

$$
V(r) = \sum_i\dfrac{kQ_i}{|\vec r - \vec r_i|}
$$

While in the continuous case, it reads:

$$
V(r) = k\int \dfrac{\rho\, dV}{|\vec r - \vec r'|} 
$$

Again, $\vec r - \vec r_i$ represents the vector pointing from the location $\vec r_i$ of a given charge to $\vec r$, and $\vec r - \vec r'$ represents the vector pointing from a given point $\vec r'$ in the charge distribution to (the position vector) $\vec r$.

The second method of computing the electric potential, however, is the _far_ more elegant way of computing the electric potential, and it is **Poisson's equation**. It reads:

$$
\nabla^2 V = -4\pi k\rho
$$

Poisson's equation is a partial differential equation (PDE) that can be solved for the electric potential using any number of techniques for solving differential equations. Once solved, the electric field is easily found through $\vec E = -\nabla V$, and from there, the equations of motion (differential equations describing the trajectories) of any charge in the electric field can be found.

## The magnetic field

Up to this point, we have considered _electrostatics_, where charges are slow-moving or don't move at all. But what happens if charges _do_ move? We observe that a strange _new_ force shows up, one that is distinct yet strangely similar to the electric force. We call this force the **magnetic force**.

A magnetic force arises whenever there is a **current**. A current is a _flow_ of charge; more precisely, we define it as:

$$
I = \dfrac{dQ}{dt}
$$

Where $I$ is the current, and $Q$ is the amount of charge passing through a given cross-section of wire at a given time $t$. Just as we defined $\rho$ as the charge density, we may also define a **current density**, denoted $\vec J$, where $\vec J$ is given by:

$$
\vec J = \dfrac{\partial I}{\partial A} \hat I
$$

Here, $A$ is the cross-sectional area through which the current flows, and $\hat I$ is the direction of the motion of positive charges. Why a current density would ever prove useful will be revealed in a few sections.

The crucial other component that makes magnetic forces possible is the **magnetic field**. The magnetic field is like the electric field in some ways; it is a vector field, it acts on charged objects, and it spans across all space. But it is also different; it is **velocity-dependent** and vanishes as charges slow to a stop. In addition, there are _no magnetic charges_ - in fact, magnetic charges, also called _monopoles_, are forbidden. The closest physically-possible analogue to a "magnetic charge" is a magnetic _dipole_, consisting of two opposite charges.

We write the magnetic field as $\vec B$, and the magnetic field strength is given in units of **Tesla**, shorthand $\text{T}$. The magnetic force can then be written in one of two ways:

$$
\vec F_B = q \vec v \times \vec B = \int I d\ell \times \vec B
$$

These two forms describe the magnetic force generated by 1) a moving point charge $q$ and 2) a current-carrying segment of wire of current $I$. Note that both expressions use a **cross product**: this is because the magnetic force is always _perpendicular_ to the direction of the moving charges.

```{note}
What about the magnetic fields and forces generated by permanent magnets like bar magnets or fridge magnets? The answer is that while they can be macroscopically-modelled with classical theory, the full explanation for why they remain magnetized even without moving charges requires special relativity and quantum mechanics.
```

How do we _compute_ the magnetic field though? As with before, there are several different options. But first, let's cover an option that you perhaps would _think_ could work, but doesn't actually work. Perhaps you would think that since there is a Gauss's law for the _electric field_, there would also be one for the _magnetic field_. Indeed, there is actually one, but it is rather disappointing:

$$
\begin{align*}
\begin{cases}
\displaystyle \oint \mathbf{B} \cdot d\mathbf{A} = 0,& \text{(integral form)} \\
\nabla \cdot \mathbf{B} = 0,& \text{(differential form)} \\
\end{cases}
\end{align*}
$$

Which leaves much to be desired. The formal reason for _why_ Gauss's law for magnetic fields is this way, however, is important _conceptually_. Remember how we said that there are **no magnetic charges**. But the right-hand side of Gauss's law for electic fields is the total charge enclosed within a region of space. Since a magnetic charge is _not defined_, the right-hand side of Gauss's law for magnetic fields has to be zero - after all, there are no charges! 

In addition, the differential version also tells us that magnetic fields always come in _loops_ - the vectors follow looping field lines that ultimately trace back to the point they started from - which means that the magnetic field has _no net divergence_.

So instead of Gauss's law for magnetism, we instead use an analogue of Coulomb's law for the electric field. This is the **Biot-Savart law**. In the discrete case, for charges located at distinct points in space, it takes the form:

$$
\mathbf{B}(r) = \dfrac{\mu_0}{4\pi}\sum_i  Q_i \dfrac{\vec v_i \times \vec r_i}{|r - r_i|^2}
$$

In the continuous case, where we consider many, many moving charges that form a continuous current, Biot-Savart's law becomes an integral:

$$
\begin{align*}
\vec B(\vec r) &= \dfrac{\mu_0}{4\pi}\int \dfrac{I\, \vec {d\ell} \times \hat r'}{|\vec r - \vec r'|^2} \\
&= \dfrac{\mu_0}{4\pi} \int \dfrac{I\, \vec {d\ell}}{|\vec r - \vec r'|^2} \dfrac{\vec r - \vec r'}{|\vec r - \vec r'|} \\
&= \dfrac{\mu_0}{4\pi}\int \dfrac{I \vec {d\ell} \times (\vec r - \vec r')}{|\vec r - \vec r'|^3}
\end{align*}
$$

Where $\vec{d\ell}$ is a current-carrying path segment (such as a segment of wire), $\vec r'$ is a point along the current-carrying path, $\vec r$ is the position vector, and $\mu_0$ is the magnetic constant. This integral's particular form means that Biot-Savart's law is a (vector) **line integral** over the current-carrying path (which is usually, though not always, a wire), as we integrate over every portion of that path.

As with Coulomb's law for the electric field, Biot-Savart's law is very tedious to work with and can often be only solved by computer. In addition, just like Coulomb's law for the electric field only works when the electrostatic approximation can be made, Biot-Savart's law only works when the **magnetostatic approximation** can be made, meaning that charges move at near-constant velocities and currents change very slowly, if at all. 

```{note}
The magnetostatic and electrostatic assumptions mean that the electric fields (in the former) and magnetic fields (in the latter) **do not change** - we say they are _static_. Thus, as long as the assumptions hold, neither field has a dependence on time.
```

The second method that can be used is very similar to Poisson's equation for electric fields. If we define a **magnetic potential** $\mathbf{A}$ such that $\mathbf{B} = \nabla \times \mathbf{A}$, the magnetic potential can be solved for by Poisson's equation for the magnetic field, which reads:

$$
\nabla^2 \mathbf{A} = -\mu_0 \mathbf{J}
$$

In Cartesian coordinates, this expands to:

$$
\dfrac{\partial^2 \mathbf{A}}{\partial x^2} + \dfrac{\partial^2 \mathbf{A}}{\partial y^2} + \dfrac{\partial^2 \mathbf{A}}{\partial z^2} = -\mu_0\,\mathbf{J}
$$

This method is used more often in advanced physics such as relativity and quantum mechanics, but it generally follows the same approach as using Poisson's equation for the electric field - solve the (partial) differential equation using any number of methods (and computer if need be), then find the magnetic field by taking its curl, that is, $\mathbf{B} = \nabla \times \mathbf{A}$. Although elegant, Poisson's equation for the magnetic field only works in cases when the magnetostatic approximation holds. In many cases, we _cannot_ make this assumption.

The third method for computing the magnetic field, however, works universally even when currents are not constant and charges are changing velocity. It is what we will cover next - **Maxwell's equations**.

## Electrodynamics and Maxwell's equations

It is a well-known fact that light in all its forms (radio, gamma, x-ray, microwave, visible, UV, and more) is an electromagnetic phenomenon, so to be able to describe it, we need to use 

Up to this point, we have discussed electostatics and magnetostatics, but we will now cover **electrodynamics** - the more general study of electricity and magnetism in cases where electric and magnetic fields change through time. The laws of electrodynamics are given by the system of partial differential equations known as **Maxwell's equations**. These equations govern the evolution of the electric and magnetic fields, and they read:

$$
\begin{align}
\nabla \cdot \mathbf{E} &= 4\pi k \rho \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \frac{1}{c^2} \frac{\partial \mathbf{E}}{\partial t}
\end{align}
$$

These equations are also often appear in integral form, in which they are given as:

$$
\begin{aligned}
\oint \limits_\mathrm{surface} \mathbf{E} \cdot d\mathbf{A} &= 4\pi k Q_\mathrm{total}\\
\oint \limits_\mathrm{surface} \mathbf{B} \cdot d\mathbf{A} &= 0 \\
\oint \limits_\mathrm{loop} \mathbf{E} \cdot \vec{d\ell} &= -\frac{\partial}{\partial t} \int_\mathrm{surface} \mathbf{B} \cdot d\mathbf{A} \\
\oint \limits_\mathrm{loop} \mathbf{B} \cdot \vec{d\ell} &= \mu_0 I + \frac{1}{c^2} \frac{\partial}{\partial t} \int_\mathrm{surface} \mathbf{E} \cdot d\mathbf{A}
\end{aligned}
$$

The Maxwell equations show a surprising fact: oscillating electric fields can actually _induce_ magnetic fields, and oscillating magnetic fields can actually _induce_ electric fields. So rather than two separate phenomena, electricity and magnetism are actually interrelated phenomena, caused by the interplay of electric and magnetic fields. Thus, we often group electricity and magnetism together as **electromagnetism**, and speak of an _electromagnetic field_ as the combination of the electric and magnetic components of the field.

The equation that govern the motion of charged objects in an electromagnetic field is the **Lorentz force law**, which reads:

$$
m \dfrac{d^2 \mathbf{r}}{dt^2} = \mathbf{F}_{EM} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
$$

Solving the Maxwell equations is a topic so extensive that it is its own field. We'll sketch out one of the most common methods; however, to avoid making this chapter overwhelmingly long, we will have to skip a lot of the details.

The general process of this method is to first set boundary conditions such that the first two equations (Gauss's laws for the electric and magnetic fields) hold true. Then, we are left with the two remaining equations:

$$
\begin{align*}
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \frac{1}{c^2} \frac{\partial \mathbf{E}}{\partial t}
\end{align*}
$$

The top equation is called **Faraday's law**, and the bottom equation is called the **Maxwell-Ampère law**. Now, it turns out that by reworking the electric and magnetic potentials, we can substitute them in to find an _electromagnetic_ potential, assuming that:

$$
\begin{align*}
\mathbf {E} &=-\mathbf {\nabla } V -{\frac {\partial \mathbf {A} }{\partial t}} \\
\mathbf{B} &= \nabla \times \mathbf{A}
\end{align*}
$$

Then, if we impose something called the _Lorenz gauge condition_ (it's something we will cover more in the Expert's Guide), we can substitute the potentials into Maxwell's equations to get:

$$
\begin{align*}
\nabla^2 \mathbf{A} -\dfrac{1}{c^2} \dfrac{\partial^2 V}{\partial t^2} = -\mu_0 \mathbf{J} \\
\nabla^2 V -\dfrac{1}{c^2} \dfrac{\partial^2 V}{\partial t^2} = -4\pi k\rho
\end{align*}
$$

These equations are much easier (though by no means _easy_) to solve and are often used in advanced electromagnetic theory to solve for complicated field configurations. However, we won't go that far, at least for now. Rather, we'll explore _one_ simplified case of Maxwell's equations, and its profound consequences on the physical nature of light.

```{note}
For more detailed information about Maxwell's equations, we recommend reading [A student's guide to Maxwell's equations](https://www.danfleisch.com/maxwell/), which is slower-paced compared to the guide here in the Elara Handbook.
```

## Electromagnetic waves

When only simulating electromagnetic waves radiating within space, and not the source currents or charges, Maxwell's equations can be simplified by setting $\rho = \mathbf{J} = 0$, resulting in two wave equations:

$$
\begin{aligned}
\frac{\partial^2 \mathbf{E}}{\partial t^2} &= c^2 \nabla^2 \mathbf{E} \\
\frac{\partial^2 \mathbf{B}}{\partial t^2} &= c^2 \nabla^2 \mathbf{B}
\end{aligned}
$$

Where $c^2 = \frac{1}{\mu_0 \varepsilon_0}$ and $c$ is the speed of light. These are called the _electromagnetic wave equations_ because their solutions are very similar to classical wave solutions to the generalized wave equation, such as solutions describing sound waves or the waves formed by a vibrating string. But these waves are special - their speed of propagation is the speed of light. That is to say, the electromagnetic wave equations **describe light**, and their solutions describe all forms of light, from visible light in all its colors to X-rays to gamma rays to the microwaves and radio waves that carry global communications and internet.

If we take a close look at the electromagnetic wave equations, electromagnetic waves are just a special case of electric and magnetic fields, with the special property that they oscillate throughout space without needing any wires or currents. This is also what makes them ideal for wireless applications, such as WiFi, communications, or in our case, wireless power transfer. They are generated when there are **both** time-varying electric and magnetic fields.

But what physical configurations can _generate_ electromagnetic waves? Recall from Maxwell equation #3 (Faraday's law) that a changing magnetic field $\mathbf{B}(t, \mathbf{x})$ causes (induces) an electric field $\mathbf{E}_\mathrm{ind}(t, \mathbf{x})$. The induced electric field $\mathbf{E}_\mathrm{ind}(t, \mathbf{x})$ can then induce a changing magnetic field $\mathbf{B}_\mathrm{ind}(t, \mathbf{x})$ by Maxwell equation #4 (Ampère-Maxwell law). However, for this to be true, the original magnetic field must satisfy the condition $\displaystyle \frac{\partial^2 \mathbf{B}}{\partial t^2} \neq 0$. This means it must not be a constant or linear function, because otherwise, the induced electric field from the original magnetic field would produce a constant (or zero) electric field by Maxwell equation #4. In mathematical terms, wave solutions require a current (density) that satisfies $\displaystyle \frac{\partial^2 \mathbf{J}}{\partial t^2} \neq 0$. That is to say, the current (density) must also be twice-differentiable in time and not constant or linear, so it cannot be a steady current. And so we have found our answer: in the case where currents are _non-constant_, which means they are _changing_ with time, electromagnetic waves are produced.

The classical method of generating electromagnetic waves is to use some type of oscillating current, especially one that follows a sine or cosine curve (AC currents) - this is the basic operating principle of the **antenna**. Another method is to pass current through some form of spinning loop within a magnetic field (such as that generated by a magnet); the changing angle of the loop leads to induced electric fields that produce a changing current, generating (albeit weak) electromagnetic waves (typically radio waves, which can be amplified). A third, and the most common, method is to accelerate charges along a path; this principle is used in magnetrons for microwave ovens, where fast-moving (and accelerating) electrons move through a magnet field, producing (unsurprisingly) microwaves.

But what about the Sun, you may ask, or a light bulb, or a general hot object like a fire or plasma? In these cases, the mechanisms that produce light are _quantum_ in nature. We will discuss how that occurs in the next chapter, "The Specifics".