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

# Quantum mechanics


> "When you change the way you look at things, the things you look at change."
>
> **Max Plank**


Up to this point, we've explored physics that obeyed the principles of predictability and certainty. We took it for granted that particles moved on definite paths, that if we knew everything about the system we could predict everything about how it would evolve. All of those assumptions completely break down in quantum mechanics, when we take a look at the world near the scale of atoms. We'll explore this fascinating new world - and in time, hopefully realize that "the quantum world is not spooky or incomprehensible - it's just way different".


## Quantization and wavefunctions


When we speak of observable properties of a macroscopic object, such as its speed, momentum, and energy, we expect that these properties can take on _any_ value. For instance, we can have a speed of 5.34 m/s, or 100,000 m/s, or 0.0015 m/s. These are called **continuous** properties.


But in the quantum world, every property of a microscopic particle has to be made of indivisible unit values. One way to think about it is to imagine you have several basketballs - it would make sense to have 0 basketballs, or 50 basketballs, or 12 basketballs, but it wouldn't make sense to have $\pi$ basketballs or 1.513 basketballs. The indivisible unit, in our case, is one basketball, and in quantum mechanics we call the unit a **quantum** (plural _quanta_). For example, the quantum of charge is the elementary charge constant $e = 1.602 \times 10^{-19}$ Coulombs. This means that you can only have a charge of $2e$ or $5e$ or $17e$, never $1.352e$. The quantum of energy (for visible light) is approximately $2.605 \times 10^{-19}$ joules. We call properties that are composed of quanta **quantized**.


Energy is important, because it was Einstein who first discovered that the energy of light is quantized, and in particular that the quantum of light energy is given by:


$$
E_p = hf
$$


```{note}
$h$ is Plank's constant, approximately $6.626 \times 10^{−34}$, and $f$ is the frequency of the wave. $\hbar$ is equal to $\frac{h}{2\pi}$.
```


This means that if you measure the energy of any light, it must be $0E_p$ or $1E_p$ or $5E_p$ or $1000E_p$, not $1.5E_p$. Light can't just take any energy it wants; the energy must strictly be $N\cdot E_p$, where $N$ is the number of photons in the measured light.


Einstein recognized that the quantization of light isn't just a mathematical idea of integer multiples of a value, but that quanta of light are actually physical particles that we call **photons**. But isn't light a wave? Wasn't that what Maxwell's equations said? Physicists recognized that in fact, light was a particle _and_ a wave.


However, we hit one more roadblock. If light is a particle, why can't we just measure its observable properties (such as position) and know how it behaves? Through experimentation, scientists tried, and failed, to do exactly this. They concluded that quantum particles cannot be found exactly. We can only measure probabilities by using a **wavefunction** that describes the state of a quantum system. The wavefunction is oftentimes a complex function, and has no direct physical meaning (which makes sense; all physical quantities are real numbers, not complex numbers!) However, it turns out that if you integrate the square of the wavefunction, you find the **probability** of a particle being at a particular position at a particular time.


$$
P(x, t) = \int  |\Psi(x, t)^2 | dx
$$


Note that we can generalize this to multiple dimensions:


$$
P(x, t) = \int | \Psi(x, y, z, t)^2 | \, dx \, dy \, dz
$$


And integrating over all space gives a probability of 1, that is, 100% probability:


$$
\int \limits_{-\infty}^\infty | \Psi(x, y, z, t)^2 |~dx~dy~dz = 1
$$


```{note}
We typically use an uppercase $\Psi$ for time-dependent wavefunctions and a lowercase $\psi$ for time-independent wavefunctions.
```


## The Schrödinger equation


The key equation of quantum mechanics is the Schrödinger equation, which describes how the wavefunction evolves through space and time. It is given by:


$$
i \hbar \frac{\partial \Psi}{\partial t} = 
\left(-\frac{\hbar^2}{2m} \nabla^2 + V(x) \right)
\Psi
$$


Just as the geodesic equation was a generalization of Newton's laws to relativity, the Schrödinger equation was a generalization of Newton's laws to quantum mechanics. Solving this partial differential equation yields the wavefunction, which can then be used to find the probability of a particle being at a certain position.


While the Schrödinger equation is separable, the process of separation of variables is so tedious that the "method of inspired guessing" is often the faster method. Consider, for example, a constant potential $V(x) = 0$, and using the 1D Schrödinger equation. We can guess that the solution likely involves a complex exponential function, since wavefunctions are oftentimes complex. Let's try:


$$
\Psi(x, t) = e^{i(x - t)}
$$


We first take the derivatives of our guess solution for time and space:


$$
\frac{\partial \Psi}{\partial t} = -i e^{i(x - t)}
$$

$$
\frac{\partial^2 \Psi}{\partial x^2} = i^2 e^{i(x - t)} = -e^{i(x - t)}
$$


Plugging these into the equation gives:


$$
i \hbar (-i e^{i(x - t)}) = -\frac{\hbar^2}{2m} (-e^{i(x - t)})
$$


$$
\hbar e^{i(x - t)} = -\frac{\hbar^2}{2m} e^{i(x - t)}
$$


$$
\hbar = -\frac{\hbar}{2m}
$$


Hmmm...maybe that guess wasn't quite right, but we can now refine our solution for it to satisfy Schrödinger's equation. Perhaps a better guess would be:


$$
\Psi(x, t) = e^{i(x - t)/\hbar}
$$


Upon simplification, this leads to:


$$
1 = \frac{1}{2m}
$$


Not quite right either, but we're getting there. Let's try one more guess:


$$
\Psi(x, t) = e^{i\left(x - \frac{t}{2m}\right)/\hbar}
$$


This does actually work! And as the Schrödinger equation is linear, we can append two scaling factors $k$ and $\omega$ to make for a general solution:


$$
\Psi(x, t) = e^{i\left(kx - \frac{\omega t}{2m}\right)/\hbar}
$$


So using the method of inspired guessing, we have officially solved the 1D Schrödinger equation!


However, clearly, this method is not foolproof, and getting to a correct solution is not easy. Thus, Schrödinger's equation is usually solved numerically, using either the finite volume method or finite element method, discussed in the differential equations chapter.


## Observables


Just like how we explored the quantization of energy for photons, other measurable quantities, such as momentum, charge, and angular momentum of quantum particles, are also quantized. We call these measurable quantities **observables**. Observables have defined real values, but those values are discrete values, not continuous functions. Therefore, since observables are discrete numbers, then momentum, charge, energy, and angular momentum cannot be represented by functions, as functions have continuous outputs.

But we know of one different mathematical representation that can work to give discrete numbers - _eigenfunctions and eigenvalues_. Indeed, in quantum mechanics, an observable $a$ is an eigenvalue of an eigenfunction $\psi$:


$$
\hat A \psi = a \psi
$$


Here, $\hat A$ is a linear operator acting on $\psi$. The most common type of linear operator for eigenfunctions are derivative operators. For instance, the momentum operator is given by:


$$
\hat p = -i\hbar \frac{\partial}{\partial x}
$$


So if we wanted to find the measured value of the momentum $p$, we would need to solve the equation:


$$
\hat p \psi = p \psi
$$


Or, plugging in the value of the momentum operator:


$$
-i\hbar \frac{\partial \psi}{\partial x} = p \psi
$$


This ensures that the observable - in this case, the measured value of momentum - has to be a discrete number, rather than a continuous function. In a similar way, the kinetic energy and total energy operators are (given in order):


$$
\hat K = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2}
$$

$$
\hat E = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x)
$$


So, the eigenfunction-eigenvalue equations for kinetic energy and total energy are given by:


$$
\hat K \psi = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} = K \psi
$$

$$
\hat E \psi = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} + V(x) \psi = E \psi
$$


Notice the energy operator is identical to the Hamiltonian $\hat H$, as it is the sum of the kinetic energy operator and the potential energy. Therefore, we often rewrite the eigenfunction-eigenvalue equation for energy as:


$$
\hat H \psi = E \psi
$$


This is the **time-independent Schrödinger equation**.


## The uncertainty principle


Knowing more about a particular observable in general means that we know less about another observable. This is the **uncertainy principle** - when we express the certainty of an observable in terms of its standard deviation $\sigma$, then:


$$
\sigma_x \sigma_p \geq \frac{\hbar}{2}
$$


To derive this, let's consider the position and momentum operators. They are given respectively by:


$$
\hat x = x
$$

$$
\hat p = -i\hbar \frac{\partial}{\partial x}
$$


Now, it is important to recognize that these two operators do not commute - if we switch the order we apply these operations, we get different results. That is:


$$
\hat x \hat p \psi \neq \hat p \hat x \psi
$$


We call the difference between applying these two operators in either order the **commutator**, denoted by square brackets:


$$
[\hat x, \hat p] = \hat x \hat p - \hat p \hat x
$$


If we compute this commutator by substituting the operators in, we get:


$$
[\hat x, \hat p] = i \hbar
$$


We can now make use of a statistical theorem:


$$
\sigma_a \sigma_b \geq \frac{1}{2i} [\hat a, \hat b]
$$


Plugging in our result, we get the uncertainty principle:


$$
\sigma_x \sigma_p \geq \frac{\hbar}{2}
$$
