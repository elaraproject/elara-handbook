# Gravity and orbital mechanics

Given that we plan to construct complex space-based megastructures, we must of course design our system _for_ space, which comes with its unique challenges. Gravity is the primary force that determines the trajectories of objects in deep space, and so is something we have to give careful consideration to. Newtonian mechanics, luckily, gives a very good mathematical description of gravity that is sufficient for *preliminary* calculation purposes. The differential equation of motion for all solar orbits under Newtonian gravity is:

$$
\frac{d^2 \mathbf{r}}{dt^2} + \left(\frac{GM}{r^2} + \sum_i \frac{Gm_i}{|r_i -r|^2}\right)\hat r = 0
$$

Where $M$ is the mass of the Sun, and $m_1, m_2, \dots, m_i, r_1, r_2, \dots, r_i$ are the masses and positions of all the non-Earth gravitating bodies in the Solar system. The Sun and the 8 planets together account for 99.985% of the total mass of the Solar system, with the Sun itself being 99.85% of the total mass. Meanwhile, the differential equation of motion for a geosynchronous orbit around Earth, under Newtonian gravity, would be given by:

$$
\frac{d^2 \mathbf{r}}{dt^2} + \frac{GM_\mathrm{earth}}{r^2} \hat r_\mathrm{earth} + \frac{GM_\mathrm{sun}}{r_\mathrm{sun}{}^2} \hat r_\mathrm{sun} + \frac{GM_\mathrm{moon}}{r_\mathrm{moon}{}^2} \hat r_\mathrm{moon} =0
$$

Where $r$ is the distance from Earth to the orbiting satellite, $r_\mathrm{moon}$ is the distance from the satellite to the moon, $r_\mathrm{sun}$ is the distance from the satellite to the Sun, and each of the basis vectors represents the unit vector of the displacement vector pointing between the Earth and that particular celestial body (for instance, $\hat r_\mathrm{sun}$ is the displacement vector between the satellite and the Sun).

If use the approximation that Earth's gravity is dominant in this scenario, we may ignore the lunar and solar terms, and together with using the fact that orbits are planar, we have the system of equations:

$$
\begin{align}
\frac{d^2 x}{dt^2} + \frac{GM_\mathrm{earth}}{(x^2 + y^2)^{3/2}} &= 0 \\
\frac{d^2 y}{dt^2} + \frac{GM_\mathrm{earth}}{(x^2 + y^2)^{3/2}} &= 0 \\
\langle x_0, y_0 \rangle = r_0 \hat \theta, \langle v_{0x}, v_{0y} \rangle &= v_0 \hat \theta
\end{align}
$$

These aren't easy to solve but there _is_ an analytical solution if you convert to polar coordinates, do a substitution of variables, and then use some other math tricks. The solution is given by:

$$
r = \frac{L^2}{m^2} \frac{1}{GM(1 + e \cos \theta)}
$$

Where $h = L/m$, $L$ is the angular momentum, $m$ is the satellite's mass, and $M$ is the Earth's mass, and we can get typical Cartesian coordinates with the typical $x = r\cos \theta$ and $y = r \sin \theta$. $e$ is a parameter known as the _eccentricity_, given by:

$$
e = \sqrt{1 + \frac{2E L^2}{G^2 M^5}}
$$

Using $L = I \omega$, $I = mr^2$ for the satellite, the fact that that the tangential velocity obeys $v_\mathrm{tang.} = r\omega$, and the conservation of angular momentum, we find that:

$$
L = mr^2 \omega = mr v_\mathrm{tang.}
$$

In our case, $v_\mathrm{tang.} = v = \|\mathbf{v}\|$ where $\mathbf{v} = \langle v_x, v_y \rangle$ (this is because the tangent vector always points in the direction of motion and the direction of motion happens to be rotational). Conservation of angular momentum means we can equivalently write:

$$
L = mr_0v_0
$$

By a similar approach using the conservation of energy, we have:

$$
E = \frac{1}{2} mv_0 {}^2 - \frac{GMm}{r_0}
$$

Which means that the complete solution to the Newtonian differential equations for Earth orbits is given by:

$$
r(\theta) =\frac{r_0 {}^2 v_0 {}^2}{G {M}} \left(\sqrt{\frac{G^2 M^5 - r_{0}\ m^3\ v_{0}^2 \left(2 GM - r_{0}v_{0}^2 \right)}{G^2 M^5}}\ \cos{\left(\theta \right)} + 1 \right)^{-1}
$$

Hence the reason why real-world problems almost never appear in an introductory treatment of differential equations. Further, this is not something to be computed by hand - we highly recommend [sympad](https://github.com/tom-pytel/sympad), an awesome open-source computer algebra system interface, which speeds up calculations tremendously.

However, it should be noted that this is a _simplified_ gravitational model that works for limited purposes. First, it ignores the Moon completely, which is the biggest source of gravity other than the Sun and Earth. Second, it doesn't account for the fact that Earth's gravity is not technically uniform, with slight surface gravity variations and gravitational anomalies. Third, it does not incorporate any relativistic effects or the effects of radiation pressure or various other emissions from the spacecraft, which all have small - but tangible - effects on the spacecraft's orientation and trajectory through time, requiring orbital corrections. Finally, it does not take into account all the *other* gravitational influences caused by the uneven distribution of mass in the Solar System, and due to the fact that the $n$-body problem (that is, systems involving more than two gravitationally-interacting objects) is known to be chaotic, any orbit in the Solar System will decay over very long timespans. This is due to the tiny gravitational effects from other gravitational influences (e.g. comets, asteroids, dwarf planets) that we don't typically include in our calculations out of sheer complexity.

For this reason, while preliminary theoretical analysis is important, it is advisable to use professional orbital calculations software such as [NASA's Copernicus](https://www.nasa.gov/general/copernicus/) and standard gravitational models such as the [Earth Gravitational Models (EGM)](https://en.wikipedia.org/wiki/Earth_Gravitational_Model), which is part of the [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System) for the final high-precision research calculations.