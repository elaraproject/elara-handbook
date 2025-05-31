# Quantum field theory, Part 1

Up to this point, we have seen both Special Relativity and General Relativity, both of which are written in the language of tensors. But we have only seen relativity on big scales acting on macroscopic objects, not the small scales of quantum mechanics. So it natural to ask whether we can describe _quantum particles_ in a relativistic fashion.

The answer is yes, and in fact, the study of the intersection of relativity and quantum mechanics - called **relativistic quantum field theory** - is central to modern physics. It also has useful applications in giving a theoretical explanation of previously-unknown atomic transitions and performing incredibly-precise quantum calculations for atoms, particularly in extreme high-energy conditions. Some features of quantum mechanics we take for granted - like the photon as the quantum of light - are actually _only_ possible to fully explain using quantum field theory. So let's dive in!

## Introduction to quantum electrodynamics

Throughout our discussion of spontaneous and stimulated emission, we have discussed photons everywhere. But photons are not something that can be completely described using the Schrödinger equtaion. Photons must be described by **quantum electrodynamics**, the quantum theory of the electromagnetic field.

```{important}
We use Gaussian units instead of SI units for this section. Consult a conversions chart to convert Gaussian units to SI units.
```

Remember that light is classically-described as a wave, which obeys the solution to the Maxwell equations of electromagnetism in free space:

$$
\begin{align}
\dfrac{\partial^2 \mathbf{E}}{\partial t^2} - c^2 \nabla^2 \mathbf{E} = 0 \\
\dfrac{\partial^2 \mathbf{B}}{\partial t^2} - c^2 \nabla^2 \mathbf{B} = 0
\end{align}
$$

But in classical electrodynamics, we find that due to relativistic effects, the electric field and magnetic field can no longer be thought of as distinct entities. Rather, they must be considered together as part of an **electromagnetic field**. Instead of separate electric and magnetic fields, we define a common **electromagnetic 4-potential**, which is a more fundamental physical quantity from which the fields arise. The electromagnetic 4-potential is given by $A^\mu = (\varphi, A_x, A_y, A_z)$ where $\varphi$ is the electric scalar potential and $\mathbf{A} = (A_x, A_y, A_z)$ is the magnetic vector potential. The definitions of $\varphi$ and $\mathbf{A}$ are:

$$
\begin{align}
\mathbf{E} &= -\nabla \varphi - \dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t} \\
\mathbf{B} &= \nabla \times \mathbf{A}
\end{align}
$$

The electromagnetic 4-potential, being a _potential_, can be shifted by an arbitrary constant without changing the fields (and thus the physics). Indeed, they can even be shifted by the gradient of a function $f(\mathbf{r}, t)$ without changing the fields, with the transformations:

$$
\begin{align}
\varphi = \varphi - \dfrac{\partial f}{\partial t} \\
\mathbf{A} = \mathbf{A} + \nabla f
\end{align}
$$

This is known as **gauge freedom**, and therefore we must impose certain conditions to restrict the electromagnetic four-potential to a particular form, just as we define a reference position in classical mechanics to define the classical potential energy. Applying these chosen conditions (called "gauges") is called **gauge fixing**. There are two common gauges used: the Coulomb gauge, commonly used for non-relativistic quantum field theory, and the Lorenz (note: not "Lorentz") gauge, usually used for relativistic quantum field theory. As we work in the non-relativistic regime, we will choose the Coulomb gauge, which sets the condition $\nabla \cdot \mathbf{A} = 0$. Thus, the equations of motion become:

$$
\begin{align}
\dfrac{\partial^2 \varphi}{\partial t^2} - c^2 \nabla^2 \varphi = 0 \\
\dfrac{\partial^2 \mathbf{A}}{\partial t^2} - c^2 \nabla^2 \mathbf{A} = 0
\end{align}
$$

The general, normalized solutions to the system of PDEs in a region of volume $V$ is given by:

$$
\mathbf{A}(\mathbf{r}, t) = \dfrac{1}{V\sqrt2} \sum_{\mathbf{k}} \left[\mathbf{A}_\mathbf{k}(\mathbf{k}) e^{i \mathbf{k} \cdot \mathbf{r}} + \mathbf{A}_\mathbf{k}^*(\mathbf{k}) e^{-i\mathbf{k} \cdot \mathbf{r}}\right]
$$

Where $\mathbf{k}$ is the **wavevector**, which is directly related to the momentum of a wave as well as its wavelength by $|\mathbf{k}| = \dfrac{2\pi}{\lambda}$, and where $\mathbf{A}_\mathbf{k}(\mathbf{k})$ represents the polarization (directionality) and field strength of the wave, which are given respectively by the direction and the magnitude of $\mathbf{A}_\mathbf{k}(\mathbf{k})$. Here, $\mathbf{A}_\mathbf{k}^*$ represents the complex conjugate of $\mathbf{A}_\mathbf{k}(\mathbf{k})$. Those who are aware may recognize this as a Fourier expansion in terms of the normal modes; if that terminology is unfamiliar, don't worry about it. Importantly, the wavevector is related to the **angular frequency** by $\omega_\mathbf{k} = \mathbf{k} c$, which will be significant later.

```{note}
The series is significant, as pure plane waves in the form $e^{i\mathbf{k} \cdot \mathbf{r}}$, which are the simplest solutions to the PDEs, are mathematically consistent but physically impossible (they would need an infinite amount of energy to create). The sum over plane waves of different $\mathbf{k}$ and $\mathbf{A}_\mathbf{k}(\mathbf{k})$, however, produces a physical solution (as long as we just take the real part of the complex-valued waves).
```

### The classical field theory of electromagnetism

Now, we will use the tools of _classical field theory_ to be able to analyze the electromagnetic field, because classical quantities of fields translate into operators in quantum field theory. In classical field theory, we define a **Lagrangian** $\mathcal{L}(q, \dot q, \nabla q)$ based on the coordinate $q$ as well as its time and space derivatives (in more precise terms we should write $q^\mu$ to denote that this is a coordinate). In our case, $q = A^\mu$ is the electromagnetic four-potential. We may also define a **Hamiltonian** $\mathcal{H}(q, p)$ based on the coordinate $q$ as well as the _canonical momentum_ $p$ obtained from $p = \dfrac{\partial \mathcal{L}}{\partial \dot q}$ (this would also be more precisely be written as $p^\mu$). The Lagrangian of the electromagnetic field in free space is given by:

$$
\begin{align}
\mathcal{L} &= \dfrac{1}{8\pi} (\mathbf{E}^2 - \mathbf{B}^2) \\
&=\dfrac{1}{8\pi} \left(-\nabla \varphi - \dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t}\right)^2 - \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2 \\
\end{align}
$$

We can also write this in terms of the **canonical momentum**. First, let us derive it by findind the derivative of the Lagrangian with respect to $\dfrac{\partial \mathbf{A}}{\partial t}$. This comes out to:

$$
\begin{align}
\mathbf{p} &= \dfrac{\partial \mathcal{L}}{\partial \dot{\mathbf{A}}} \\
&= \dfrac{\partial \mathcal{L}}{\partial(\partial_t \mathbf{A})} \\
&= \dfrac{1}{4\pi c} \left(\nabla \varphi + \dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t}\right) \\
&= -\frac{1}{4\pi c}\mathbf{E}
\end{align}
$$

That is to say, we have found that the canonical momentum of the electromagnetic four-potential $\mathbf{p}$ is related to the electric field by $\mathbf{E} = -4\pi c\mathbf{p}$. This result allows us to write the Lagrangian in the simplified form:

$$
\begin{align}
\mathcal{L} &= \dfrac{1}{8\pi} (\mathbf{E}^2 - \mathbf{B}^2) \\
&= \dfrac{1}{8\pi}(-4\pi c\mathbf{p})^2 - \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2 \\
&= 2\pi c^2\mathbf{p}^2 - \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2
\end{align}
$$

It also means that we can rearrange to express $\dfrac{\partial \mathbf{A}}{\partial t}$ in terms of $\mathbf{p}$, something that will be very useful later:

$$
\begin{gather}
\mathbf{p} = \dfrac{1}{4\pi c} \left(\nabla \varphi + \dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t}\right) \\
4\pi c \mathbf{p} =\nabla \varphi + \dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t} \\
c(4\pi c \mathbf{p} - \nabla \varphi) = \dfrac{\partial \mathbf{A}}{\partial t}
\end{gather}
$$

We may use these results to find the Hamiltonian of the electromagnetic field:

$$
\begin{align}
\mathcal{H} &= \mathbf{p} \cdot \dot{\mathbf{q}} - \mathcal{L} \\
&= \mathbf{p} \cdot \dfrac{\partial \mathbf{A}}{\partial t} -2\pi c^2\mathbf{p}^2 + \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2 \\
&= \mathbf{p} \cdot c(4\pi c \mathbf{p} - \nabla \varphi) -2\pi c^2\mathbf{p}^2 + \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2 \\
&= 2\pi c^2 \mathbf{p}^2 - c\mathbf{p} \cdot \nabla \varphi + \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2
\end{align}
$$

Up to this point, we have been very sloppy with our language: what we have been calling the Lagrangian is actually called the **Lagrangian density**, and what we have been calling the Hamiltonian is actually called the **Hamiltonian density**. We may find the Lagrangian and the Hamiltonian by integrating the Lagrangian and Hamiltonian densities over space (here $d^3 x = dx\, dy\, dz$):

$$
\begin{align}
L &= \int \mathcal{L}\, d^3x \\
&= \int d^3 x \left[2\pi c^2\mathbf{p}^2 - \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2\right] \\
H &= \int \mathcal{H} \, d^3x \\
&= \int d^3 x \left[2\pi c^2 \mathbf{p}^2 - c\mathbf{p} \cdot \nabla \varphi + \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2\right]
\end{align}
$$

But notice something peculiar. If we explicitly evaluate the middle term, using the results we have derived previously, we get:

$$
\begin{align}
c\mathbf{p} \cdot \nabla \varphi &= c\left(-\frac{1}{4\pi c}\mathbf{E}\right) \cdot \nabla \varphi \\
&= \underbrace{-\dfrac{1}{4\pi} (\nabla \cdot \mathbf{E}) \varphi}_{\mathbf{F} \cdot (\nabla \phi) = (\mathbf{F} \cdot \nabla) \phi} \\
&= 0
\end{align}
$$

Which comes from the vector calculus identity $\mathbf{F} \cdot (\nabla \phi) = (\mathbf{F} \cdot \nabla) \phi$ and the fact that $\nabla \cdot \mathbf{E} = 0$ in free space. Thus the middle term in our expression for the Hamiltonian drops out, leaving us with just:

$$
H = \int d^3 x \left[2\pi c^2 \mathbf{p}^2 + \dfrac{1}{8\pi} (\nabla \times \mathbf{A})^2\right]
$$

```{note}
Further, the Coulomb gauge enforces the requirement that $\varphi = 0$ in our given conditions, so we could have done all of this without needing to do the math.
```

This, together with the general solution we found for $\mathbf{A}(\mathbf{r}, t)$, lays the classical foundation for quantizing the electromagnetic field.

### Quantization of the electromagnetic field

Before we proceed onto the process of treating the electromagnetic field in a fully quantum way, let us take some time to review the **quantum harmonic oscillator**. The quantum harmonic oscillator has a Hamiltonian $\hat H$ given by:

$$
\hat H = \dfrac{\hat p^2}{2m} + \dfrac{1}{2} m\omega^2 \hat q^2
$$

Where $\hat q$ is the coordinate used, which, in non-QFT, is equal to the position operator $\hat x$. One may write the Hamiltonian in a more useful form by defining the operators $\hat a$ and $\hat a^\dagger$, as follows:

$$
\begin{align}
\hat a  &= \sqrt{\dfrac{m\omega}{2\hbar}} \hat q + i \dfrac{1}{\sqrt{2m\omega \hbar}} \hat p \\
\hat a^\dagger  &= \sqrt{\dfrac{m\omega}{2\hbar}} \hat q - i \dfrac{1}{\sqrt{2m\omega \hbar}} \hat p \\
\end{align}
$$

Which allows the Hamiltonian to be written as:

$$
\hat H = \hbar \omega\left(\hat a \hat a^\dagger - \dfrac{1}{2}\right)
$$

We may now take these results for the non-QFT quantum harmonic oscillator and generalize it to the quantized electromagnetic field. To do so, we promote the _classical quantities_ to their quantum operator analogues: we replace the generalized coordinate $\hat q$ with our field expression $\hat q \to \mathbf{A}_\mathbf{k}$, and we replace the momentum operator $\hat p$ with the canonical momentum we just derived earlier, and substitute them into the $\hat a$ and $\hat a^\dagger$ operators. For the momentum, we know that $\mathbf{p} = -\dfrac{1}{4\pi c} \mathbf{E}$; using the relationship $\mathbf{E} = -\nabla \varphi - \dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t}$, which just becomes $\mathbf{E} = -\dfrac{1}{c} \dfrac{\partial \mathbf{A}}{\partial t}$ in our case, yields:

$$
\begin{align}
\mathbf{p} &= -\dfrac{1}{4\pi c} \mathbf{E} \\
&= \dfrac{1}{4\pi c^2} \dfrac{\partial \mathbf{A}}{\partial t} \\
&=\dfrac{-i}{8\pi c^2 \sqrt{V}}\omega_\mathbf{k} \sum_{\mathbf{k}} \left[\mathbf{A}_\mathbf{k}(\mathbf{k}) e^{i \mathbf{k} \cdot \mathbf{r}} + \mathbf{A}_\mathbf{k}^*(\mathbf{k}) e^{-i\mathbf{k} \cdot \mathbf{r}}\right] \\
&= \dfrac{1}{2\sqrt{V}} \sum_{\mathbf{k}} \left[\mathbf{p}_\mathbf{k} e^{i \mathbf{k} \cdot \mathbf{r}} + \mathbf{p}_\mathbf{k}^* e^{-i\mathbf{k} \cdot \mathbf{r}}\right] \\
&\qquad \Rightarrow \mathbf{p}_\mathbf{k} = \dfrac{-i\omega_\mathbf{k}}{4\pi c^2} \mathbf{A}_\mathbf{k}
\end{align}
$$

From here, we may define the operators $\hat Q$ and $\hat P$, by:

$$
\begin{align}
\hat Q &= \sqrt{\dfrac{m\omega_\mathbf{k}}{\hbar}} \hat q \\
&= \sqrt{\dfrac{m\omega_\mathbf{k}}{\hbar}} \mathbf{A}_\mathbf{k} \\
\hat P &= \dfrac{1}{\sqrt{m\hbar \omega}_\mathbf{k}} \hat p \\
&= \dfrac{1}{\sqrt{m\hbar \omega}_\mathbf{k}} \left(\dfrac{-i\omega_\mathbf{k}}{4\pi c^2} \mathbf{A}_\mathbf{k}\right) \\
&= \dfrac{-i}{4\pi c^2} \dfrac{1}{\sqrt{m\hbar \omega}_\mathbf{k}}  \mathbf{A}_\mathbf{k}
\end{align}
$$

For which we then have:

$$
\begin{align}
\hat a &= \dfrac{1}{\sqrt{2}}(\hat Q + i \hat P) \\
&= \sqrt{\dfrac{m\omega_\mathbf{k}}{2\hbar}} \mathbf{A}_\mathbf{k}
+ \dfrac{1}{4\pi c^2} \dfrac{1}{\sqrt{2m\hbar \omega}_\mathbf{k}}  \mathbf{A}_\mathbf{k} \\
\hat a^\dagger &= \dfrac{1}{\sqrt{2}}(\hat Q - i\hat P) \\
&= \sqrt{\dfrac{m\omega_\mathbf{k}}{2\hbar}} \mathbf{A}_\mathbf{k}
- \dfrac{1}{4\pi c^2} \dfrac{1}{\sqrt{2m\hbar \omega}_\mathbf{k}}  \mathbf{A}_\mathbf{k}
\end{align}
$$

The Hamiltonian becomes the Hamiltonian density, and so it must be integrated over all of space:

$$
\hat H = \int d^3 x \, \left[\hbar \omega_\mathbf{k}\left(\hat a \hat a^\dagger - \dfrac{1}{2}\right)\right]
$$

It is common to denote the states of the quantum electromagnetic field with $|n\rangle$, where $|0\rangle$ is the ground state, $|1\rangle$ is the first excited state, $|2\rangle$ is the second excited state, and so on. The creation and annihilation operators have the properties that:

$$
\begin{align}
\hat a |n\rangle = c_n |n-1\rangle \\
\hat a^\dagger |n\rangle = c_n^* |n+1\rangle \\
\end{align}
$$

That is to say, applying the creation operator $\hat a^\dagger$ raises the electromagnetic field from state $|n\rangle$ to a higher-energy state $|n + 1\rangle$, while applying the annihilation operator $\hat a$ lowers the electromagnetic field from state $|n\rangle$ to a lower-energy state $|n - 1\rangle$, with $c_n, c_n^*$ being normalization constants given by:

$$
\begin{align}
c_n &= \sqrt{n} \\
c_n^* &= \sqrt{n + 1}
\end{align}
$$

This process continues until we reach the ground state, where $n = 0$, and thus applying the annihilation operator on the ground state yields $\hat a | 0 \rangle = (\sqrt{0}) | 0 \rangle = 0$.

### Calculating the ground-state energy of the electromagnetic field

When we say "ground-state energy", we should be careful about our use of words: there is no _singular_ ground-state energy for a quantum field, as it constantly fluctuates in energy due to the Heisenberg uncertainty principle $\Delta E \Delta t \geq \dfrac{\hbar}{2}$. Thus the ground-state energy we speak of is in fact the _average_ ground-state and would be given by the _expectation value_ of the Hamiltonian:

$$
\begin{align}
\langle E_0\rangle &= \langle 0 |\hat H |0\rangle \\
&= \big \langle 0 \big| \int d^3 x \, \left[\hbar \omega_\mathbf{k}\left(\hat a \hat a^\dagger - \dfrac{1}{2}\right)\right] \big|0\big\rangle \\
&= \big \langle 0 \big| \left( \int d^3 x \left( \hbar \omega_\mathbf{k} \hat a \hat a^\dagger\right)  - \dfrac{1}{2} \int d^3 x\, \hbar \omega_\mathbf{k}\right)\big|0\rangle
\end{align}
$$

Remember that the annihilation operator annihilates the ground state, so the first term in the integral is zero. We are simply left with:

$$
\langle E_0 \rangle = \big \langle 0 \big| \left( - \dfrac{1}{2} \int d^3 x\, \hbar \omega_\mathbf{k}\right)\big|0\rangle
$$

But wait! This integral looks divergent! Indeed it is, since every point in space has a nonzero energy $\dfrac{1}{2} \hbar \omega_\mathbf{k}$, and therefore if we integrate this over _all space_, the integral becomes infinite and unphysical. Thus, we usually just ignore this integral by redefining the energy of a state as the energy _above the ground state_. By this redefinition, the ground state would then be at $E_0 = 0$, and the successive excited states would have non-infinite energies $E_n > 0$.

However, if we _wanted_, we could restrict our integral over a particular region, such as a cubical box of side length $L$. Then, assuming that the electromagnetic field is restricted to one wavelength within the box, the integral could be evaluated, and we get a reasonable value for the energy:

$$
\begin{align}
\langle E_0 \rangle &= \big \langle 0 \big| \left( - \dfrac{1}{2} \int d^3 x\, \hbar \omega_\mathbf{k}\right)\big|0\rangle \\
&= \big \langle 0 \big| \left( - \dfrac{1}{2} \int_0^L \int_0^L \int_0^L dx\, dy\, dz\, \hbar \omega_\mathbf{k}\right)\big|0\rangle \\
&= -\langle 0 |\dfrac{L^3 \hbar \omega_\mathbf{k}}{2} |0 \rangle \\
&= -\dfrac{L^3 \hbar \omega_\mathbf{k}}{2} \langle 0 | 0 \rangle  \\
&= -\dfrac{L^3 \hbar \omega_\mathbf{k}}{2}
\end{align}
$$

This is exactly what happens in the **Casimir effect**, an effect that arises due to the nonzero ground-state energy of the quantum electrodynamical vacuum, which leads to a force between two metal plates brought close together. Within finite distances and volumes, it is indeed possible to calculate the ground-state energy, and this is essential to many quantum effects.

### Gauge coupling

Unlike the quantum electrodynamical field $\hat A_\mu$, which reduces to the _classical_ electromagnetic 4-potential (field) $A_\mu$ in the classical limit, the quantum electron field $\psi$ has no classical field it reduces to. In the classical picture, $A_\mu$ satisfies a wave equation, and therefore describes (among other things) electromagnetic waves; light is an electromagnetic wave and can be described by $A_\mu$. But in the classical picture, there is no analog for $\psi$; an electron is just a particle, it isn't a field. In fact, _only_ massless particles with integer spin are associated with _classical fields_ (the only two particles that satisfy this requirement are the photon and graviton, but the latter has yet to be experimentally confirmed and remains purely theoretical for now).

### QED correction to the Coulomb potential

Uehling potential

### Multi-state systems with the quantized electromagnetic field

Derive the Einstein A and B coefficients for spontaneous and stimulated emission.


### The nonrelativistic and classical limit



### Other corrections

See https://books.google.com/books?id=nxz2CAAAQBAJ&lpg=PA103&pg=PA99#v=onepage&q&f=false
This guide is based on:
- https://www.phys.ksu.edu/personal/wysin/notes/quantumEM.pdf
- https://www.damtp.cam.ac.uk/user/tong/qft/six.pdf
- https://www.damtp.cam.ac.uk/user/tong/aqm/aqmeight.pdf