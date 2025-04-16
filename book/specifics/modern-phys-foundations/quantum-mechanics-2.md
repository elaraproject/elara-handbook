# Quantum mechanics, Part 2

Building on what we've learned in the first part of quantum mechanics, we can now explore more complex concepts in quantum theory. In this second part, we will cover the

## Introduction to matrix mechanics

In studying complex multi-state quantum systems, numerical methods are often the only way to solve a variety of problems, as solving the Schrödinger equation by hand becomes impossible. One important feature of these numerical methods is utilizing the [Heisenberg picture](https://en.wikipedia.org/wiki/Heisenberg_picture) of quantum mechanics, also known as **matrix mechanics**.

In matrix mechanics, we describe the system not through its total wavefunction, but by its **operators**. The quantum state $|\Psi\rangle$ stays constant; the **operators** (energy, momentum, etc.) are what evolve through time. In particular, the operators can be expressed in specific _bases_ (bases are plural of "basis"). For discrete operators, as we have seen for the spin matrices, we can choose a discrete basis. In our case, the $\hat S_z$ operator can be expressed using the basis of the two spin states, as given by:

$$
\chi_{z^{+}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad
\chi_{z^{-}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

Meanwhile, for continuous (differential) operators, we can choose a functional basis. For instance, we can use the Legendre, Laguerre, and Hermite polynomials, all of which form a complete basis set, to find the **matrix representation** of the operator. Within this section, we will give a brief introduction on determining the matrix representation of various operators, based on the book _Basic Theory of Lasers and Masers_ by Jacques Vanier.

### The Hamiltonian in general bases

In the time-independent regime, the state of a quantum system is represented by its state-vector $|\Psi\rangle$, which can be expanded into a set of eigenstates $|\psi_n\rangle$ by $|\Psi\rangle = \displaystyle \sum_n |\psi_n\rangle$. Each eignestate satisfies eigenvalue equation $\hat H |\psi_n \rangle = E_n |\psi_n\rangle$, where $\hat H$ is the Hamiltonian and $E_n$ is the energy eigenvalue of a particular eigenstate. We may extract the energy eigenvalues $E_n$ as follows. First, we multiply both sides by a bra $\langle\psi_m|$:

$$
\langle \psi_m | \hat H |\psi_n\rangle = \langle \psi_m | E_n |\psi_n\rangle
$$

Now, the eigenstates $|\psi_n\rangle$ can theoretically be expressed in _any_ basis, but we typically choose to use a **complete orthonormal basis**. Such bases include Fourier series as well as the Legendre, Laguerre, and Hermite polynomials. The specific basis doesn't matter; it simply matters that a complete and orthonormal basis satisfies $\langle  \psi_m | \psi_n \rangle = \delta_{mn}$. Therefore, we have $\langle \psi_m | E_n | \psi_n \rangle = E_n \langle \psi_m |\psi_n\rangle$ (since $E_n$ is a constant and can be factored out of the expression). Given that we have an orthonormal basis, $E_n \langle \psi_m |\psi_n\rangle$ is only nonzero when $m = n$, in which case we have $E_n \langle \psi_n |\psi_n \rangle = E_n$, and thus:

$$
\begin{align*}
\langle \psi_m | \hat H |\psi_n\rangle &= \langle \psi_m | E_n |\psi_n\rangle \\
&= E_n \langle \psi_m | \psi_n \rangle  \\
&= E_n\, \delta_{mn}  \\
\langle \psi_m | \hat H |\psi_n\rangle &= E_n \delta_{mn} \quad (\text{zero if } m \neq n) \\
\langle \psi_n | \hat H |\psi_n\rangle &= E_n  \\
\end{align*}
$$

Thus, to find $E_n$, we "only" need to calculate $\langle \psi_n | \hat H |\psi_n\rangle$, which can also be written in terms of the Schrödinger formalism as:

$$
E_n = \int_{-\infty}^\infty \psi_n^*(x) \hat H \psi_n(x) \, dx
$$

But returning to the matrix representation - we may write the set of eigenvalues $E_n$ with the following matrix equation:

$$
\begin{pmatrix}
\langle \psi_1 | \hat H | \psi_1 \rangle & 0 & 0 & \dots & 0 \\
0 & \langle \psi_2 | \hat H | \psi_2 \rangle & 0 & \dots & 0 \\
0 & 0 & \langle \psi_3 | \hat H | \psi_3 \rangle & \dots & 0 \\
0  & 0 & 0 & \ddots & \vdots \\
0 & 0 & 0 & \dots & \langle \psi_n | \hat H | \psi_n \rangle
\end{pmatrix} =
\begin{pmatrix}
E_1 & 0 & 0 & \dots & 0 \\
0 & E_2 & 0 & \dots & 0 \\
0 & 0 & E_3 & \dots & 0 \\
0  & 0 & 0 & \ddots & \vdots \\
0 & 0 & 0 & \dots & E_n
\end{pmatrix}
$$

This is a diagonal matrix - so one might wonder, why bother writing this when each side can just be written as a vector multiplied by an identity matrix? The reason is that if we *don't* know the eigenstates, we can always choose to expand our quantum state $|\Psi\rangle$ in some other complete and orthonormal basis instead, which we will refer to as $|\phi_n\rangle$ (since we can always choose any basis to write out our state-vector). As both bases are complete and orthogonal, we can then express a state in our new basis $|\phi_n\rangle$ in terms of our eigenstate basis $|\psi_n\rangle$ as a linear sum:

$$
\begin{align*}
|\phi_n\rangle &= \sum_k a_{nk} |\psi_k \rangle \\
&= a_{n1} |\psi_1\rangle + a_{n2} |\psi_2 \rangle + a_{n3}|\psi_3\rangle + \dots + a_{nk} |\psi_k\rangle
\end{align*}
$$

Where all the $a_{nk}$'s are constant coefficients. We can write this in matrix form as:

$$
\underbrace{\begin{pmatrix}
|\phi_1\rangle \\ |\phi_2\rangle \\ |\phi_3\rangle \\ \vdots \\ |\phi_n\rangle
\end{pmatrix}}_\text{new basis} =
\underbrace{\begin{pmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1k} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2k} \\
a_{31} & a_{32} & a_{33} & \dots & a_{3k} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nk}
\end{pmatrix}}_{\text{matrix } A_{nk}}\,
\underbrace{\begin{pmatrix}
|\psi_1\rangle \\ |\psi_2\rangle \\ |\psi_3\rangle \\ \vdots \\ |\psi_k \rangle
\end{pmatrix}}_\text{old basis}
$$

We can extract out the components of $A_{nk}$ using another orthogonality argument. If we take the components of our new basis $|\phi_n\rangle$, then multiply by a bra $\langle \psi_j|$, then we have:

$$
\begin{align*}
|\phi_n\rangle &= \sum_k A_{nk} |\psi_k \rangle \\
|\phi_n\rangle \langle \psi_j | &= \langle \psi_j| \sum_k A_{nk} |\psi_k \rangle \\
&=  \sum_k A_{nk} \langle \psi_j| \psi_k\rangle \\
&= A_{nk} \delta_{jk}
\end{align*}
$$

Where $\langle \psi_j |\psi_k\rangle = \delta_{jk}$ since our bases are othogonal. The only case were $\langle \psi_j | \phi_n \rangle = A_{nk} \delta_{jk}$ does _not_ vanish is when $j = k$ and therefore we have:

$$
|\phi_n\rangle \langle \psi_k | = A_{nk} \delta_{kk} = A_{nk}
$$

Thus we have $A_{nk} = |\phi_n\rangle \langle \psi_k|$. We may also derive an expression for the _inverse_, i.e. $A^{-1}$. Recall that the inverse of $A$ must satisfy $A A^{-1} = I$ where $I$ is the identity matrix. We recall that the identity matrix is given by $I = \displaystyle \sum_n |\phi_n \rangle \langle \phi_n |$. Then, we have:

$$
\begin{align*}
A A^{-1} &= I \\
|\phi_n\rangle \langle \psi_k| A^{-1} &= \sum_i |\phi_i \rangle \langle \phi_i | \\
\end{align*}
$$

Now, if we take the inner product of both  sides with the ket $|\psi_k\rangle$, then:

$$
\begin{align*}
|\psi_k\rangle \bigg( |\phi_n\rangle \langle \psi_k| \bigg) A^{-1} &= |\psi_k\rangle \sum_i |\phi_i \rangle \langle \phi_i | \\
\bigg( |\phi_n\rangle \langle \psi_k| \bigg)|\psi_k\rangle  A^{-1} &= \left(\sum_i |\phi_i \rangle \langle \phi_i |\right)|\psi_k\rangle \\
|\phi_n\rangle \langle \psi_k|\psi_k\rangle  A^{-1} &= \sum_i |\phi_i \rangle \langle \phi_i |\psi_k\rangle \\
|\phi_n\rangle \cancel{\langle \psi_k|\psi_k\rangle}  A^{-1} &= \sum_i |\phi_i \rangle \langle \phi_i |\psi_k\rangle \\
|\phi_n\rangle A^{-1} &= \sum_i |\phi_i \rangle \langle \phi_i |\psi_k\rangle \\
\end{align*}
$$

Where we were able to swap the order of the inner product since the inner product is commutative, and we were able to pull the $|\psi_k\rangle$ into the sum since the sum does not sum over the index $k$ (so $|\psi_k\rangle$ can essentially be treated as a constant in the sum).  Now if we take the inner product with the bra $\langle \phi_n|$ we have:

$$
\begin{align*}
\langle \phi_n|\phi_n\rangle A^{-1} &= \langle \phi_n|\sum_i |\phi_i \rangle \langle \phi_i |\psi_k\rangle \\
\cancel{\langle \phi_n|\phi_n\rangle} A^{-1} &= |\psi_k\rangle\underbrace{\langle \phi_n|\sum_i |\phi_i \rangle}_{= \delta_{n i}} \langle \phi_i | \\
A^{-1} &= |\psi_k\rangle\delta_{ni}\langle \phi_i\rangle \\
A^{-1} &= |\psi_k\rangle \langle \phi_n|
\end{align*}
$$

Where again, since $|\psi_k\rangle$ is not summed over, we were able to pull it out of the sum, and we used orthogonality to collapse the sum into a single term.

Having computed $A$ and $A^{-1}$, we will now show that our transformation of basis actually leads to a very nice expression for the matrix representation of the Hamiltonian. The Hamiltonian in our new basis, which we write as $\hat{\mathscr{H}}$, is given by $\hat{\mathscr{H}} = A \hat H A^{-1}$ (this is a standard result of linear algebra). If we then substitute our expressions for $A$ and $A^{-1}$, we have: 

$$
\begin{align*}
\hat{\mathscr{H}} &= A \hat H A^{-1} \\
&= |\phi_n\rangle \langle \psi_k | \hat H |\psi_k\rangle \langle \phi_n| \\
|\phi_n \rangle \hat{\mathscr{H}} &= |\phi_n \rangle\bigg(|\phi_n\rangle \langle \psi_k| \hat H |\psi_k\rangle \langle \phi_n |\bigg) \\
&= \bigg(|\phi_n\rangle \langle \psi_k| \hat H |\psi_k\rangle \langle \phi_n |\bigg) |\phi_n \rangle \\
&= |\phi_n\rangle \langle \psi_k| \hat H |\psi_k\rangle \cancel{\langle \phi_n |\phi_n\rangle} \\
\langle \phi_n |\phi_n \rangle \hat{\mathscr{H}} &= \langle \phi_n |\phi_n\rangle \langle \psi_k| \hat H |\psi_k\rangle \\
\cancel{\langle \phi_n |\phi_n \rangle} \hat{\mathscr{H}} &= \cancel{\langle \phi_n |\phi_n\rangle} \langle \psi_k| \hat H |\psi_k\rangle \\
\hat{\mathscr{H}} &= \langle \psi_k| \hat H |\psi_k\rangle \\ &= E_k
\end{align*}
$$

> Here, $E_k$ should technically be written $E_k \cdot I$, i.e. $E_k$ is a matrix with the energy eigenvalues along its diagonal and zero everywhere else.

Where the last step comes from $\langle \psi_n | \hat H |\psi_n\rangle = E_n$ (the index does not matter at this point because we use only one index in the expression). Thus we find that:

$$
\hat{\mathscr{H}} = A \hat H A^{-1} = E_n
$$

Let us demonstrate the same with, in the functional picture. Consider a system described by wavefunction $\psi(\mathbf{r})$. By the postulates of quantum mechanics, the wavefunction may be expanded in any complete and orthonormal set of functions $\phi_n(\mathbf{r})$, such that:

$$
\psi(\mathbf{r}) = \sum_{n = 1}^\infty c_n \phi_n(\mathbf{r}) = c_1 \phi_1 + c_2 \phi_2 + c_3 \phi_3 + \dots + c_n \phi_n
$$

Where we assume all $\phi_n$ are normalized. From here, we may prepare a matrix $A_{mn}$ with elements given by:

$$
A_{mn} = \int_{-\infty}^\infty \phi_
m^* \hat H \phi_n dV
$$

Now, $A_{mn}$ is not necessarily a diagonal matrix, so it does not necessarily give the energy eigenvalues. However, if we diagonalize it, we are left with the matrix $E_{mn}$, which _is_ diagonal (that is, for all $m \neq n$, $E_{mn} = 0$, and whose diagonals $E_{nn} = E_n$ are equal to the energy eigenvalues.

The matrix operator approach therefore condenses the difficult problem of solving the Schrödinger equation into a more straightforward problem of finding the correct matrix $A$ that diagonalizes the Hamiltonian in a particular basis; from there, we can simply read off the energy eigenvalues from the diagonal.

### Example: quantum harmonic oscillator

We will use the matrix representation approach to solve for the quantum harmonic oscillator, which will act as a toy model. We want to obtain a matrix representation for the Hamiltonian of the quantum harmonic oscillator and find the energy eigenvalues.

The well-known Hamiltonian for the quantum harmonic oscillator is given by:

$$
\hat H = \dfrac{\hat p^2}{2m} + \dfrac{1}{2} m \omega^2 \hat x^2
$$

We will now need to pick a basis to be able to obtain its matrix representation. In theory, when we don't know the precise eigenstates of the matrix, any set of basis functions would do (as long as they are complete and orthogonal) - but luckily for us, we already know the eigenstates of the Hamiltonian. So for demonstrative purposes, it is easiest to choose the basis of the eigenstates of the Hamiltonian, which we can write as $|\psi_1\rangle, |\psi_2\rangle, |\psi_3\rangle, \dots, |\psi_n\rangle$. Then, we have $E_n = \langle \psi_n | \hat H |\psi_n\rangle$. But recall that in the example of the quantum harmonic oscillator, $\hat H |\psi_n\rangle = \hbar \omega \left(n + \dfrac{1}{2}\right) |\psi_n\rangle$. Thus, $\langle \psi_n | \hat H | \psi_n\rangle$ is given by:

$$
\begin{align*}
\langle \psi_n |\hat H | \psi_n\rangle &= \langle \psi_n|\hbar \omega \left(n + \dfrac{1}{2}\right) |\psi_n\rangle \\
&= \hbar \omega \left(n + \dfrac{1}{2}\right) \langle \psi_n|\psi_n\rangle \\
&= \hbar \omega \left(n + \dfrac{1}{2}\right) \delta_{nn}
\end{align*}
$$

Thus our resulting energy matrix becomes[^3]:

$$
\langle \psi_n|\hat{H}|\psi_n\rangle = \hbar \omega\begin{pmatrix}
\frac{1}{2} & 0 & 0 & \dots & 0 \\
0 & \frac{3}{2} & 0 & \dots & 0 \\
0 & 0 & \frac{5}{2} & \dots & 0 \\
0 & 0 & 0 & \ddots & \vdots \\
0 & 0 & 0 & \dots & (n + \frac{1}{2}) \\
\end{pmatrix}
$$

And thus our energy eigenvalues can be found (as expected) by just reading off the diagonals the diagonals, from which we can surmise that:

$$
E_n = \left(n + \dfrac{1}{2}\right)\hbar \omega
$$

Let us now show that even though this matrix representation method for the quantum harmonic oscillator is a "toy model", it can still predict real-world results. The transition energy $\Delta E$ from our result is the difference between energy levels $n_1, n_2$, and thus:

$$
\begin{align*}
\Delta E &= \left(n_2 + \dfrac{1}{2}\right)\hbar \omega - \left(n_1 + \dfrac{1}{2}\right)\hbar \omega \\
&= (n_2 - n_1) \hbar \omega
\end{align*}
$$

From which we may derive the spectral lines for various different transitions, given that $\Delta E = hc/\lambda$, with:

$$
\dfrac{1}{\lambda} = \dfrac{\omega}{2\pi c}(n_2 - n_1) \quad \Rightarrow \quad \lambda = \dfrac{2\pi c}{(n_2 - n_1)\omega}
$$

The angular frequency of the vibrations, $\omega$, can be found through $\omega = \sqrt{k/\mu}$ where $\mu$ is the reduced mass of the molecule and $k$ is its force constant. Let us compute the vibrational transitions of carbon dioxide, which, although not strictly speaking a _diatomic_ molecule, can be somewhat treated as such. The reduced mass of the triatomic carbon dioxide molecule is given by[^5]:

$$
\mu = \dfrac{2m_\ce{C} m_\ce{O} + m_\ce{O}^2}{2 m_\ce{C} + m_\ce{O}} \approx \pu{2.567E-27 kg}
$$

Where $m_\ce{C}$ is the mass of the carbon atom and similarly $m_\ce{O}$ is the mass of the oxygen atom. The force constant of $\ce{CO2}$ is approximately $\pu{1680 N/m}$[^4] and thus $\omega \approx \pu{251.47 THz}$. Substituting these values, we find that the spectral lines are given by:

| Transition                   | Spectral line | Spectrum       |
| ---------------------------- | ------------- | -------------- |
| $\|1\rangle \to \|0\rangle$  | 7596 nm       | Mid-infrared   |
| $\|2 \rangle \to \|0\rangle$ | 3748 nm       | Mid-infrared   |
| $\|3\rangle \to \|0\rangle$  | 2499 nm       | Near-infrared  |
| $\|4\rangle \to \|0\rangle$  | 1874 nm       | Near-infrared  |
| $\|5\rangle \to \|0\rangle$  | 1499 nm       | Near-infrared  |
| $\|6\rangle \to \|0\rangle$  | 1249 nm       | Near-infreared |

> **Note:** all of these transitions are vibrational transitions, and they all occur in the _infrared spectrum_. This has great physical significance; it means that carbon dioxide (just like other greenhouse gases) is very good at absorbing and re-emitting infrared light, which is (one of) the mechanisms that leads to the greenhouse effect, which in turn drives climate change.

### Example 2: hydrogen atom

We will now produce a computational example to solve for the **hydrogen atom**. We use the normalized Chebyshev polynomials as our basis for $R(r), \Theta(\theta)$, and $\Phi(\phi)$ (that is, each of these is approximated by a particular Chebyshev polynomial). We code this all with python, using SciPy for the special functions.

First, we import out libraries and set up our basis:

```python
from scipy.special import legendre
from scipy.differentiate import derivative
from scipy.constants import hbar, c, mp, me, elementary_charge
import numpy as np
```

Then, we prepare our Hamiltonian:

```python
# TODO convert to spherical coords
def Hamiltonian(psi, x, y, z, mu=None, eps=1E-5):
	# mu is reduced mass
	if not mu:
		mu = (mp * me)/(mp + me)
	laplacian = 
	K = -hbar**2 / (2*mu) * derivative(psi, )
	r2 = x**2 + y**2 + z**2
	# smoothed coulomb potential to avoid divide by zero
	# similar to the Plummer potential
	potential = -k*elementary_charge**2 / np.sqrt(r2 + eps**2)
	return K + potential
```

### Example 3: helium atom

Let us now consider a case of a system that does not possess an analytic solution - the helium atom. Since a (neutral) helium atom is composed of two electrons around a nucleus, the atomic Hamiltonian (we ignore spin, vibrational, and rotational degrees of freedom) becomes:

$$
\hat H_\ce{He} = \underbrace{-\dfrac{\hbar^2}{2m}(\nabla_1^2 + \nabla_2^2)}_\text{electron kinetic energy} -\underbrace{\dfrac{Z}{4\pi \varepsilon_0}\left(\dfrac{e^2}{r_1} + \dfrac{e^2}{r_2}\right)}_\text{nucleus-electron attraction} + \underbrace{\dfrac{1}{4\pi \varepsilon_0}\dfrac{e^2}{|r_2 - r_1|}}_\text{electron-electron repulsion}
$$

Where here we assumed that the nucleus moves so slowly that we can effectively consider it non-moving (as with the solution to the hydrogen atom). The third term (interaction term between different electrons) means that the solution to the helium atom _cannot_ be written as a linear superposition of the solutions of the hydrogen atom.

To be able to solve for the energy levels, since we don't know the exact eigenstates, we will use the eigenstates of the _hydrogen atom_ instead as our orthonormal basis. Recall that the hydrogen atom's eigenstates are parametrized by quantum numbers $n, \ell, m$ and are given by:

$$
\psi_{n, \ell, m}(r,\theta ,\varphi )={\sqrt {{\left({\frac {2}{na_{0}^{*}}}\right)}^{3}{\frac {(n-\ell -1)!}{2n(n+\ell )!}}}}\mathrm {e} ^{-\rho /2}\rho ^{\ell }L_{n-\ell -1}^{2\ell +1}(\rho )Y_{\ell }^{m}(\theta ,\varphi )
$$

Where $a_0^*$ is the reduced Bohr radius, $\rho = 2r / n a_0^*$, $L(\rho)$ is a generalized Laguerre polynomial, and $Y(\theta, \varphi)$ is a spherical harmonic. To be able to find the energy levels requires computing the diagonals of the matrix $\langle \psi_k| \hat H |\psi_k\rangle$, which, in this case, becomes:

$$
E_k = \langle \psi_k| \hat H |\psi_k\rangle = \int_V \psi_{n, \ell, m} ~\hat H_\text{He} ~\psi_{n, \ell, m}^* dV
$$

These integrals are considerably simplified by the orthogonality of the solutions to the hydrogen atom (since they form a complete orthonormal basis).

[^3]: https://quantummechanics.ucsd.edu/ph130a/130_notes/node258.html
[^4]: https://chemistry.stackexchange.com/questions/70858/how-do-i-determine-the-molecular-vibrations-of-linear-molecules
[^5]: https://www.quora.com/Is-there-any-way-to-calculate-reduced-mass-for-more-than-two-atoms-in-a-molecule