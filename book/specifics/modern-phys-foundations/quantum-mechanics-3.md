# Quantum mechanics, Part 3

## Transition frequencies and spectrocopy

One of the first great successes of quantum theory was in its correct prediction of what light is emitted and absorbed by particular atoms (and molecules and crystals). The wavelengths a particular atom (or molecule or crystal) will absorb and emit are known as its **spectra** (the individual wavelengths are called _spectral lines_). The field devoted to the study of spectra is **spectroscopy**. Precise spectra are determined through experimental measurements with specialist instruments. However, high-accuracy calculation of spectra from quantum theory is also possible, although these need experimental verification to check that the spectra are indeed correct. In this and the following sections, we will be focused on the latter and we will discuss methods of calculating spectra for different material species (here, _species_ means the same thing as "types").

Calculating spectra from theory, also called _first-principles_ or _ab priori_ calculations, is a difficult task. Since calculating spectra _at minimum_ usually requires solving the Schrödinger equation, which has very few analytical solutions, approximation schemes, numerical methods, and a variety of techniques have grown around trying to solve the Schrödinger equation to find (among other things) the spectra of different material species.

One of the earliest successful theoretical calculations of spectra was that of atomic hydrogen. The **Rydberg formula**, which can derived from the solution to the Schrödinger equation for the hydrogen atom, predicts spectral lines at wavelengths $\lambda$ for which:

$$
\dfrac{1}{\lambda} = R_H\left(\dfrac{1}{{n_1}^2} - \dfrac{1}{{n_2}^2}\right)
$$

Where $n_1, n_2$ are positive integers, $n_1 < n_2$, and $R_H$ is the **Rydberg constant** for hydrogen, given by:

$$
R_H = \dfrac{m_p}{m_e + m_p} \dfrac{m_e e^4}{8 \varepsilon_0^2 h^3 c} \approx 1.097 \times 10^7 \text{ m}^{-1}
$$

Where $m_p$ is the proton mass, $m_e$ is the electron mass, $e$ is the elementary charge, $\varepsilon_0$ is the electric constant, $h$ is the reduced Planck constant, and $c$ is the speed of light. A very similar formula exists for the helium ion (_not_ helium atom). 

While the Rydberg formula does not predict _all_ the spectral lines of hydrogen and has been supplemented by more precise calculations, it represented a major step in our ability to predict atomic spectra. However, the Rydberg formula could only be found from theory thanks to the fact that an analytical solution could be found to the hydrogen atom.

Of course, the Rydberg formula, while a historical landmark in theoretical spectra analysis, is a specific result that makes rigorous predictions for the hydrogen atom (and a few other hydrogen-like atoms). One can attempt to apply the Rydberg formula to non-hydrogen atoms, but the predictions are inconsistent; while it works for some spectra lines of some atoms, it doesn't work for others.

The lack of a general formula to derive the spectra lines of arbitrary atoms, much less molecules or crystal solids, means that in general, spectral lines of non-hydrogenic atoms must be calculated on a case-by-case basis. However, we find from both approximate calculations and experimental data that we can categorize the wavelengths of transitions according to certain heuristic rules (_heuristic_ here means that the results are non-rigorous but are usually in the right direction). We summarize these rules using the table below:[^2][^4]

| Type of transition                                       | Associated wavelength of emitted light |
| -------------------------------------------------------- | -------------------------------------- |
| Electronic (electron transition between atomic orbitals) | Mostly UV or visible, up to infrared   |
| Vibrational (molecular-only)                             | Mid-Infrared                           |
| Rotational (molecular-only)                              | Far-Infrared or microwaves             |

There are also a few other "transitions" of note beyond the ones we have listed in the above table.  We say "transitions" because most of them are actually conventional types of transitions (such as electronic transitions), but between different energy levels that were not predicted by the Schrödinger model of simple atoms. These "new" energy levels are caused by spin-related and relativistic effects as well as interactions with electric and magnetic fields. Additionally, many (but not all) of these "transitions" result in the emission of microwave radiation (which is far weaker than the UV/visible/infrared light, making them far less detectable). We compile a table of these "transitions" in the following table[^3]:

| Type of transition                                                            | Occurs due to                                                                                      |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Electronic, between "new" energy levels caused by relativistic/spin effects   | [Fine-structure splitting](https://en.wikipedia.org/wiki/Fine_structure)                           |
| Electronic, in presence of a magnetic field                                   | [Zeeman effect](https://en.wikipedia.org/wiki/Zeeman_effect)                                       |
| Electronic, in presence of an electric field                                  | [Stark effect](https://en.wikipedia.org/wiki/Stark_effect)                                         |
| Spin-flip transition, caused by nuclear spin                                  | [Hyperfine splitting](https://en.wikipedia.org/wiki/Hyperfine_structure)                           |
| Electronic, between "new" energy levels caused by quantum vacuum fluctuations | [Lamb shift](https://en.wikipedia.org/wiki/Lamb_shift) (both predicted by quantum electrodynamics) |

```{note}
The majority of these results can be found by solving the relativistic **Dirac equation**, which is more accurate than the Schrödinger equation, with a perturbed potential known as the [Uehling potential](https://en.wikipedia.org/wiki/Uehling_potential) that captures the contribution of quantum electrodynamics. They can also be found through advanced density-functional theory techniques.
```

#### Vibrational spectra

We have already seen that certain transitions can be approximately modelled by known quantum systems. For instance, vibrational transitions in a diatomic molecule (which roughly come from the chemical bond joining the two atoms in the molecule) can be modelled by the quantum harmonic oscillator, which has a constant spectral line given by:

$$
\dfrac{1}{\lambda} = \dfrac{1}{2\pi c} \sqrt{\dfrac{k}{\mu}}
$$

Where $k$ is the force constant of the molecular bond (determined experimentally) and $\mu$ is the reduced mass of the molecule, given by:

$$
\mu = \dfrac{m_1 m_2}{m_1 + m_2}
$$

However, the quantum harmonic oscillator is only a very _idealized_ model. Its results are far from general enough or accurate enough to describe the spectral lines of most material species. To be able to compute more accurate results, we need to use more powerful techniques, which we will introduce in time.

#### Rotational spectra

We will now investigate _rotational_ transitions in molecules - these are the dominant microwave-producing transitions. For a diatomic molecule composed of two atoms of masses $m_1, m_2$, with bond length $d$, the rotational Hamiltonian is given by the **rigid rotor**:

$$
\hat H_\text{rot.} = \dfrac{\hat L^2}{2I}, \quad I = \mu d^2
$$

Where $\mu = \dfrac{m_1 m_2}{m_1 + m_2}$ is the _reduced mass_ of the molecule, and $I$ is its *moment of inertia*. The solution yields eigenstates in terms of the spherical harmonics $Y_{j, m}$ and energy eigenvalues:

$$
E_j = \dfrac{j(j+1)\hbar^2}{2I} = Cj(j + 1), \quad C = \dfrac{\hbar^2}{2I}
$$

For reasons we will cover later, rotational transitions must be between energy eigenstates of $\Delta j = \pm 1$, that is, _only_ between two adjacent energy levels. To find the transition wavelengths, we must calculate the energy difference $\Delta E$ between $E_{j + 1}$ and $E_j$ energy levels:

$$
\begin{gather}
E_j = Cj(j+1) \\
E_{j + 1} = C(j + 1)(j + 2) \\
\Delta E = E_{j + 1} - E_j = 2C(j + 1) \\
\end{gather}
$$

Thus, for a rotational transition between energy levels $j' \to j$, where $j' = j + 1$, we have:

$$
\begin{align}
\Delta E = &\dfrac{hc}{\lambda} = 2Cj' \\
\dfrac{1}{\lambda} &= \dfrac{2C}{hc} j' \\
&= \dfrac{\hbar^2}{2I}\dfrac{2}{hc} j' \\
&= \dfrac{h^2}{4\pi^2 hIc} j' \\
&= \dfrac{h}{4\pi^2 Ic} j', \quad j' = 1, 2, 3, \dots
\end{align}
$$

Where, remember, $j'$ is the total angular momentum quantum number of the _upper_ energy level, and $j$ is that of the _lower_ energy level. In the literature, the expression for the reciprocal of the wavelength is more commonly expressed in terms of a molecular constant $B$, defined as:

$$
\dfrac{1}{\lambda} = 2Bj', \quad B = \dfrac{h}{8\pi^2 cI}
$$

Thus our expression gives the _absorption_ spectral lines for molecules _excited to_ the $j'$-th state, and the _emission_ spectral lines for molecules _decaying from_ the $j'$-th state. Meanwhile, the relative population of the lower level relative to the ground state (**need to check on whether I'm understanding this right**) is given by:

$$
\dfrac{N_l}{N_0} = (2J_l + 1) \exp \left(-\dfrac{hcBJ_l (J_l + 1)}{k_B T }\right) = (2J_l + 1) \exp \left(-\dfrac{h^2J_l (J_l + 1)}{8\pi^2 Ik_B T }\right)
$$

### The general problem and selection rules

In the most general case, the energy levels of a system are given by taking the inner product of the system Hamiltonian acting on the system's wavefunction, with the conjugate of the wavefunction:

$$
E_{n, \ell, m} = \int_\Omega \psi_{n, \ell, m}^*(\vec x) \hat H \psi_{n, \ell, m}(\vec x) \, dV
$$

However, due to _selection rules_, we find that such integrals often evaluate to zero, meaning that the transition is impossible (?)

### Selection rules

But before we go in-depth into using DFT to be able to compute spectra

https://adpcollege.ac.in/online/attendence/classnotes/files/1587884742.pdf

### Theoretical and numerical computation of spectra

It's important to note that simply calculating the energy levels _isn't_ what gives the spectral lines. This is because spectra are the result of _transitions_ between different energy levels, not the energy levels themselves, so we need to find the _differences_ between energy levels; those differences are what are actually proportional to the wavelength.

Also go through the Hartree-Fock method and its generalization to the Dirac equation (Dirac-Hartree-Fock)

Relativistic + QED DFT: https://arxiv.org/abs/2102.10465

[^1]: https://en.wikipedia.org/wiki/Microwave_cavity
[^2]: http://chemistry.ncssm.edu/labs/DiatomicMoleculeMath.pdf
[^3]: https://en.wikipedia.org/wiki/Degenerate_energy_levels#Removing_degeneracy
[^4]: https://www.damtp.cam.ac.uk/user/tong/aqm/justsix.pdf
[^5]: https://advancedlaserinstitute.com/wp-content/uploads/2016/03/Laser-Physics-1.pdf