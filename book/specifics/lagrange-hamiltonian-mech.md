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

# Classical mechanics, Part 2


Newton's laws and conservation of energy are two approaches to solving for the equations of motion of an object. We can make Newtonian mechanics more elegant by extending them to fields and potentials. But ultimately, Newtonian mechanics is still cumbersome to use. Here is an alternate, more beautiful approach - Lagrangian mechanics.


## Lagrangian Mechanics


The **Lagrangian** is the difference of an object's kinetic and potential energies, and is denoted by:


$$
\mathcal{L(x, \dot x)} = K(\dot x) - U(x)
$$


Note that the dots are used for the time derivatives - that is, $\dot x = \frac{dx}{dt}$.


The **action** is the time integral of the Lagrangian:


$$
S = \int_{t_1}^{t_2} \mathcal{L}(x, \dot x)~dt
$$


The **principle of stationary action** is one of the most fundamental and profound laws of physics, and states that for any given system, the action is stationary. What does stationary mean? Recall the idea of stationary _points_ in calculus - which include minima and maxima. For the action to be stationary, that means the Lagrangian must be a stationary _function_, which are analogous to stationary points, just for the action, which is a function of functions.


But what form does that Lagrangian have to take to obey the principle of stationary action? The short answer is that it must obey the following equation, known as the **Euler-Lagrange equation**:  


$$
\frac{\partial \mathcal{L}}{\partial x} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x} = 0
$$


We will derive this differential equation in the following section - if this section is too math-heavy, feel free to skip this section.


To begin our derivation, we first go back to single-variable calculus, where we are often told to find the stationary points - such as the maxima or minima - of a function. Both maxima and minima are called **stationary points** - points where the derivative of a function is zero. But what exactly defines a stationary point? Let's take a step back first. We know that the derivative is defined as the limit as $\epsilon \to 0$ of:


$$
f'(x) = \frac{f(x + \epsilon) - f(x)}{\epsilon}
$$


We can rearrange that equation to form:


$$
f(x + \epsilon) = f(x) + \epsilon f'(x)
$$


For a point to be stationary, we know that $f'(x)$ must be zero. Thus:


$$
f(x + \epsilon) = f(x)
$$


which means that at a stationary point, the function remains the same so long as you remain within a small distance $\epsilon$ away from the point. We denote a new notation, $\delta$, which we call the **variation**, and which we define as:


$$
\delta f = f(x + \epsilon) - f(x)
$$


Normally, since $f(x + \epsilon) = f(x) + \epsilon f'(x)$, it would be true that:


$$
\delta f = [f(x) + \epsilon f'(x)] - f(x) = \epsilon f'(x)
$$


But because $f(x + \epsilon) = f(x)$ at a _stationary_ point, $f(x + \epsilon) - f(x) = 0$, so at any stationary point, it is true that:


$$
\delta f = 0
$$


```{note}
$\delta f = \epsilon f'(x)$ is still true at a stationary point, but since $f'(x) = 0$ at a stationary point, $\delta f = \epsilon \cdot 0 = 0$. So you can arrive at the result $\delta f = 0$ at all stationary points using either method.
```


Now, we return to the action:


$$
S = \int \limits_a^b \mathcal{L}(x, \dot x)~dt
$$


We demand that the action must be stationary:


$$
\delta S = 0
$$


Which also means that:


$$
\int \limits_a^b \delta \mathcal{L}(x, \dot x)~dt = 0
$$


Recall that in the single-variable case, we have:


$$
\delta f = \epsilon f'(x)
$$


In the multivariable case, the derivative is replaced by partial derivatives. So we can rewrite the variation of $\mathcal{L}$ as:


$$
\int \limits_a^b \delta \mathcal{L}(x, \dot x)~dt = \int \limits_a^b \epsilon \frac{\partial \mathcal{L}}{\partial x} + \dot \epsilon \frac{\partial \mathcal{L}}{\partial \dot x}~dt
$$


We can split apart this integral to get:


$$
\int \limits_a^b \epsilon \frac{\partial \mathcal{L}}{\partial x}~dt + \int \limits_a^b \frac{\partial \mathcal{L}}{\partial \dot x} \frac{d\epsilon}{dt}~dt
$$


We now can use integration by parts on the second integral. Set:


$$
u = \frac{\partial \mathcal{L}}{\partial \dot x}
$$

$$
dv = \frac{d\epsilon}{dt}
$$

$$
v = \epsilon
$$


Therefore:


$$
du = \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x} dt
$$

$$
v = \int dv = \epsilon
$$


And using the integration by parts formula:


$$
\int \limits_a^b  u~dv = uv \bigg |_a^b - \int \limits_a^b  v~du
$$


The second term becomes:


$$
\epsilon \frac{\partial \mathcal{L}}{\partial \dot x} \bigg |_a^b - \int \limits_a^b \epsilon \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x}~dt
$$


But remember, since we are evaluating at a stationary function (not stationary point, stationary function, as the action is a function of functions), all the derivatives of $\mathcal{L}$ go to zero, so $\epsilon \frac{\partial \mathcal{L}}{\partial \dot x} \bigg |_a^b$ is zero and can be cancelled out. Therefore, the second term is just:


$$
- \int \limits_a^b \epsilon \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x}~dt
$$


Let's put the second term and the first term back together:


$$
\int \limits_a^b \epsilon \frac{\partial \mathcal{L}}{\partial x}~dt - \int \limits_a^b \epsilon \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot x}~dt
$$


Since they are with respect to the same variable, we can recombine these two integrals:


$$
\int \limits_a^b \epsilon \frac{\partial \mathcal{L}}{\partial x}~dt - \epsilon \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x}~dt
$$


And we can factor out the epsilon:


$$
\int \limits_a^b \left(\frac{\partial \mathcal{L}}{\partial x} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x} \right) \epsilon~dt
$$


But remember, $\delta S = 0$, so:


$$
\int \limits_a^b \left(\frac{\partial \mathcal{L}}{\partial x} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x} \right) \epsilon~dt = 0
$$


And the only way for the equation to be true is if:


$$
\frac{\partial \mathcal{L}}{\partial x} - \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot x} = 0
$$


This is the **Euler-Lagrange equation**, and it can be used to solve for the equations of motion as long as the Lagrangian is known.


Note that for a more general set of coordinate systems, where the system is not one-dimensional motion along the $x$ axis, the Euler-Lagrange equation takes the form:


$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot q_i} - \frac{\partial \mathcal{L}}{\partial q_i} = 0
$$


And specifically when we are interested in solving for the motion of a system, and not just of one individual object, it should be noted that the kinetic and potential energies are those of the **system** - that is, the sum of the kinetic and potential energies of every object in the system:


$$
K = \sum_i K_i = K_1 + K_2 + K_3 + \dots + K_n
$$

$$
U = \sum_i U_i = U_1 + U_2 + U_3 + \dots + U_n
$$


Note that the Euler-Lagrange equations apply primarily to closed systems, i.e. systems with no external force acting on them. If there is an external applied force on the system that does work $W$, then the Euler-Lagrange equations become:


$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot q_i} - \frac{\partial \mathcal{L}}{\partial q_i} = \frac{\partial W}{\partial q_i}
$$


### Using Lagrangian mechanics to solve the harmonic oscillator


```{image} ../images/raster/simple-oscillator.png
:alt: Simple oscillator
:width: 400px
:align: center
```


For the single pendulum problem, we first find the equations $x(t)$ and $y(t)$ given our coordinate system. Our coordinate system is based on the point $(0, 0)$ located at the point where the pendulum is attached to the ceiling. Using basic trigonometry, we find that:


$$
x(t) = \ell \sin \theta (t)
$$

$$
y(t) = -\ell \cos \theta (t)
$$


Where $y(t)$ is negative because the pendulum is at a negative height relative to our origin. Using our expressions for $x(t)$ and $y(t)$, we want to find the expression for the kinetic energy $K$. We know that:


$$
K = \frac{1}{2} mv^2
$$


And that:


$$
v = \sqrt{v_x^2 + v_y^2} = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}
$$


To do this, we solve for $\frac{dx}{dt}$ and $\frac{dy}{dt}$. This takes a bit of care, because we need to implicitly differentiate $x(t)$ and $y(t)$ with respect to $t$, where:


$$
\frac{dx}{dt} = \frac{dx}{d\theta} \frac{d\theta}{dt}
$$


$$
\frac{dy}{dt} = \frac{dy}{d\theta} \frac{d\theta}{dt}
$$


Implicitly differentiating, we have:


$$
v_x = \frac{dx}{dt} = \ell \cos \theta \frac{d\theta}{dt}
$$

$$
v_y = \frac{dy}{dt} = \ell \sin \theta \frac{d\theta}{dt}
$$


Now, we plug our values for $v_x$ and $v_y$ into the kinetic energy equation, which gives us:


$$
K = \frac{1}{2} m \left(\ell^2 \cos^2 \theta \frac{d\theta}{dt} + \ell^2 \sin^2 \theta \frac{d\theta}{dt}\right)
$$


If we do a little simplification by factoring and remembering that $\cos^2 \theta + \sin^2 \theta = 1$, we get:


$$
K = \frac{1}{2} m \ell^2 \left(\frac{d\theta}{dt}\right)^2
$$


Now we find the potential energy. Remember that close to Earth, the potential energy is determined by and only by the vertical distance between the origin (which is the reference height of zero) and the measured point. This means that:


$$
U = mgh
$$


The height in this case is negative (because it's below the origin) and we're only taking the vertical component of the height (hence $\cos \theta$) so:


$$
U = -mg \cos \theta \ell
$$


Putting it all together, our Lagrangian is:


$$
\mathcal{L} = \frac{1}{2} m \ell^2 \left(\frac{d\theta}{dt}\right)^2 + mg \cos \theta \ell
$$


Here, our coordinates are determined in terms of the angle $\theta$ only, so the Euler-Lagrange equations take the form:


$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot \theta} - \frac{\partial \mathcal{L}}{\partial \theta} = 0
$$


If we plug this into the Euler-Lagrange equation, we get:


$$
m \frac{d^2 \theta}{dt^2} \ell^2 + mg \sin \theta \ell = 0
$$


We can rewrite this as:


$$
m \frac{d^2 \theta}{dt^2} \ell^2 = - mg \sin \theta \ell
$$


And cancel out the common factors to yield:


$$
\frac{d^2 \theta}{dt^2} = - \frac{g}{\ell} \sin \theta
$$


We have arrived at our answer. This is the differential equation of the simple pendulum. Note that while this equation is impossible to solve analytically directly, we can use the small-angle approximation of $\sin \theta \approx \theta$ to get:


$$
\frac{d^2 \theta}{dt^2} = -\frac{g}{\ell} \theta
$$


Of which the solution is:


$$
\theta(t) = \theta_{max} \sin \left(\sqrt{\frac{g}{\ell}}t + \phi_0 \right)
$$


### Using Lagrangian mechanics to solve the orbit equation


We want to derive the orbit of Earth around the Sun. To do so, we again first derive the expressions for $x(t)$ and $y(t)$ in terms of the solar-earth system:


$$
x(t) = r(t) \cos \theta(t)
$$

$$
y(t) = r(t) \sin \theta(t)
$$


Differentiating both (and remembering to use the product rule), we find that:


$$
v_x(t) = \cos \theta(t) \frac{dr}{dt} - r(t) \sin \theta (t) \frac{d\theta}{dt}
$$

$$
v_y(t) = \sin \theta(t) \frac{dr}{dt} + r(t) \cos \theta \frac{d\theta}{dt}
$$


Which we can use to find the kinetic energy (after lots of algebra and several passes at using the identity $\sin^2 \theta + \cos^2 \theta = 1$):


$$
K = \frac{1}{2} m \left[\left(\frac{dr}{dt}\right)^2 + r^2 \left(\frac{d\theta}{dt}\right)^2\right]
$$


The potential energy is given by $U = -\frac{GMm}{r}$, so the Lagrangian is:


$$
\mathcal{L} = \frac{1}{2} m (\dot r^2 + r^2 \dot \theta^2) + \frac{GMm}{r}
$$


Applying the Euler-Lagrange equations to each coordinate, $r$ and $\theta$, present in the Lagrangian, we have:


$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot r} - \frac{\partial \mathcal{L}}{\partial r} = 0
$$

$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot \theta} - \frac{\partial \mathcal{L}}{\partial \theta} = 0
$$


Solving both equations yields the equations of motion for the Earth:


$$
\frac{d^2 r}{dt^2} = r \left(\frac{d\theta}{dt}\right)^2 - \frac{GM}{r^2}
$$

$$
\frac{d^2 \theta}{dt^2} = - \frac{2}{r} \frac{dr}{dt} \frac{d\theta}{dt} 
$$


These can be solved analytically, but for the sake of simplicity here they will be solved using a numerical differential equation solver:

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
```

```{code-cell} ipython3
def newtonian_d_dt(t, X, G=6.67e-11, M=2e30):
    r, theta, u, v = X
    dr_dt = u
    dtheta_dt = v
    du_dt = r * v ** 2 -(G * M) / (r ** 2) 
    dv_dt = -(2 * u * v) / r
    return dr_dt, dtheta_dt, du_dt, dv_dt
```

```{code-cell} ipython3
r0 = 1.5e11
theta0 = np.pi/2
u0 = 0
v0 = 1.99e-7 # 2pi / 365 days
newtonian_initial = [r0, theta0, u0, v0]
```

```{code-cell} ipython3
tmax = 365 * 24 * 60 * 60 # 1 year
samples = 5000
t = np.linspace(0, tmax, samples)
newtonian = solve_ivp(newtonian_d_dt, (0, tmax), y0=newtonian_initial, dense_output=True)
sol = newtonian.sol(t)
```

```{code-cell} ipython3
fig = plt.figure()
ax = plt.axes()

r = sol[0]
theta = sol[1]

# Convert from polar to cartesian
x1 = r * np.cos(theta)
y1 = r * np.sin(theta)

ax.plot(x1, y1)
ax.set_title('Plot of Newtonian orbit')
plt.show()
```

As it can be seen, the orbit is a ellipse, and we have arrived at this result using Lagrangian mechanics!


### Using Lagrangians to solve the double pendulum problem


We will now tackle a problem that would be very difficult to solve using Newton's laws, but much easier with Lagrangian mechanics. Here we have a system as follows:


```{image} ../images/raster/double-pendulum.png
:alt: Double pendulum diagram
:width: 400px
:align: center
```


Here, the notable difference is that we have a **system** as opposed to a single object, and we need to find the kinetic and potential energies of the entire system. To do this, we divide the kinetic and potential energies into two parts:


$$
K = K_1 + K_2
$$

$$
U = U_1 + U_2
$$


Where $K_1$ and $K_2$ are respectively the kinetic energies of the first pendulum mass and second pendulum mass, and likewise with $U_1$ and $U_2$ and their potential energies.


We will first derive the kinetic energies, because they are harder :( As we know, we first setup a coordinate system where the point $(0, 0)$ is centered on the point the double pendulum is attached to the ceiling. Then, we write the position functions of the first pendulum:


$$
x_1(t) = \ell_1 \sin \theta_1 (t)
$$

$$
y_1(t) = -\ell_1 \cos \theta_1 (t)
$$


We figure these out from basic trigonometry and the fact that $y_1(t)$ is negative, as it is below the origin. We then take the derivatives to find the $x$ and $y$ components of the velocity:


$$
\frac{dx_1}{dt} = \ell_1 \cos \theta_1 (t) \frac{d\theta_1}{dt}
$$

$$
\frac{dy_1}{dt} = \ell_1 \sin \theta_1 (t) \frac{d\theta_1}{dt}
$$


Using this, we can find $K_1$:


$$
K_1 = \frac{1}{2} m_1 \left(\dot x_1^2 + \dot y_1^2\right)
$$


$$
K_1 = \frac{1}{2} m_1 \left[ \left(\ell_1 \cos \theta_1 (t) \frac{d\theta_1}{dt} \right)^2 + 
\left(\ell_1 \sin \theta_1 (t) \frac{d\theta_1}{dt}\right)^2 \right]
$$


Using the trig identity $\sin^2 \theta + \cos^2 \theta = 1$, this is trivial to simplify into:


$$
K_1 = \frac{1}{2} m_1 \ell_1^2 \left(\frac{d\theta}{dt}\right)^2
$$


Then, we write the position functions of the second pendulum:


$$
x_2 (t) = x_1(t) + \ell_2 \sin \theta_2 (t)
$$

$$
y_2 (t) = y_1(t) + (- \ell_2 \cos \theta_2 (t))
$$


Here, we add the $x$ and $y$ displacement of the second pendulum with the $x$ and $y$ displacement of the first to find the total displacement from the origin, because remember, we're using the _same_ coordinate system for both pendulums. If we sub in the values of $x_1(t)$ and $y_1(t)$, we have:


$$
x_2 (t) = \ell_1 \sin \theta_1 (t) + \ell_2 \sin \theta_2 (t)
$$

$$
y_2 (t) = - \ell_1 \cos \theta_1 (t) - \ell_2 \cos \theta_2 (t))
$$


We compute their derivatives:


$$
\frac{dx_2}{dt} = \ell_1 \cos \theta_1 (t) \frac{d\theta_1}{dt} + \ell_2 \cos \theta_2(t) \frac{d\theta_2}{dt}
$$

$$
\frac{dy_2}{dt} = \ell_1 \sin \theta_1(t) \frac{d\theta_1}{dt} + \ell_2 \sin \theta_2(t) \frac{d\theta_2}{dt}
$$


And then plug them into the kinetic energy formula to find:


$$
K_2 = \frac{1}{2} m_2 \left[
\left(\ell_1 \cos \theta_1 (t) \frac{d\theta_1}{dt} + \ell_2 \cos \theta_2(t) \frac{d\theta_2}{dt}\right)^2 +
\left(\ell_1 \sin \theta_1(t) \frac{d\theta_1}{dt} + \ell_2 \sin \theta_2(t) \frac{d\theta_2}{dt}\right)^2
\right]
$$


Expanding that out, and using $\sin^2 \theta + \cos^2 \theta = 1$ to simplify, we have:


$$
K_2 = \frac{1}{2} m_2 \left[
\ell_1^2 \left(\frac{d\theta_1}{dt}\right)^2 + 2\ell_1 \ell_2 \frac{d\theta_1}{dt} \frac{d\theta_2}{dt}
(\cos \theta_1 \cos \theta_2 + \sin \theta_2 \sin \theta_2) + \ell_2^2 \left(\frac{d\theta_2}{dt}\right)^2
\right]
$$


Here, we can use the identity $\cos x \cos y + \sin x \sin y = \cos (x - y)$ to simplify to:


$$
K_2 = \frac{1}{2} m_2 \left[
\ell_1^2 \left(\frac{d\theta_1}{dt}\right)^2 + 2\ell_1 \ell_2 \frac{d\theta_1}{dt} \frac{d\theta_2}{dt} \cos (\theta_1 - \theta_2) + \ell_2^2 \left(\frac{d\theta_2}{dt}\right)^2
\right]
$$


Now, combining the two kinetic energies together, we end up with:


$$
K = \frac{1}{2} m_1 \ell_1^2 \left(\frac{d\theta}{dt}\right)^2 + \frac{1}{2} m_2 \left[
\ell_1^2 \left(\frac{d\theta_1}{dt}\right)^2 + 2\ell_1 \ell_2 \frac{d\theta_1}{dt} \frac{d\theta_2}{dt} \cos (\theta_1 - \theta_2) + \ell_2^2 \left(\frac{d\theta_2}{dt}\right)^2
\right]
$$


We use a similar approach for the potential energies - we add the potential energy of the first pendulum and the second to find the total system's potential energy:


$$
U = U_1 + U_2
$$


$$
U = m_1 g (-\ell_1 \cos \theta_1 (t) ) + m_2 g (-\ell_1 \cos \theta_1(t) - \ell_2 \cos \theta_2(t))
$$


After factoring, we have:


$$
U = -(m_1 + m_2) g \ell_1 \cos \theta_1(t) - m_2 g \ell_2 \cos \theta_2 (t)
$$


Using $\mathcal{L} = K - U$, we substitute into the two Euler-Lagrange equations (one for $\theta_1$ and one for $\theta_2$):


$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot \theta_1} - \frac{\partial \mathcal{L}}{\partial \theta_2} = 0
$$

$$
\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot \theta_1} - \frac{\partial \mathcal{L}}{\partial \theta_2} = 0
$$


With the Lagrangian:


$$
\mathcal{L} = \frac{1}{2} m_1 \ell_1^2 \left(\frac{d\theta}{dt}\right)^2 + \frac{1}{2} m_2 \left[
\ell_1^2 \left(\frac{d\theta_1}{dt}\right)^2 + 2\ell_1 \ell_2 \frac{d\theta_1}{dt} \frac{d\theta_2}{dt} \cos (\theta_1 - \theta_2) + \ell_2^2 \left(\frac{d\theta_2}{dt}\right)^2
\right]
+ (m_1 + m_2) g \ell_1 \cos \theta_1(t) + m_2 g \ell_2 \cos \theta_2 (t)
$$


To find the equations of motion ([source](https://diego.assencio.com/?index=1500c66ae7ab27bb0106467c68feebc6)):


$$
(m_1 + m_2) l_1 \ddot{\theta}_1 + m_2 l_2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l_2 \dot{\theta}_2^2\sin(\theta_1 - \theta_2) + (m_1 + m_2) g \sin\theta_1 = 0
$$

$$
l_2 \ddot{\theta}_2 + l_1 \ddot{\theta}_1 \cos(\theta_1 - \theta_2)
- l_1 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2)  + g \sin\theta_2 = 0
$$


These equations are completely unsolvable analytically, but they can be solved numerically to yield the position of a double pendulum with time.


### Langrangian to Newtonian mechanics


Let's see how we can recover Newton's 2nd law from the Euler-Lagrange equation. Remember that the equation (in the case of one-dimenional motion along the $x$ axis) is given by:


$$
\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot x} = \frac{\partial \mathcal{L}}{\partial x}
$$


And remember that the Lagrangian is given by:


$$
\mathcal{L} = \frac{1}{2} m \dot x^2 - U(x)
$$


Applying the Euler-Lagrange equations to the general Lagrangian, we get:


$$
m \ddot x = -\frac{dU}{dx}
$$


Recalling that $F = -\frac{dU}{dx}$ and $\ddot x = a$, we have recovered Newton's 2nd law!


$$
F = ma
$$


We can even use Lagrangian mechanics on simple problems and check that it matches with Newtonian mechanics. Let's do our freefall example from earlier. With $K = \frac{1}{2} m \dot y^2$ and $U = mgy$, we use the Euler-Lagrange equations to find:


$$
m \frac{d^2 y}{dt^2} = - mg
$$


Which we can simplify to:


$$
a_y = -g
$$


Which reproduces the Newtonian result!


### Lagrangians to the stars


The Lagrangian formulation of classical mechanics is so powerful, precisely because it relies on a differential equation that can be generalized. Beyond classical mechanics, the Lagrangian isn't always necessarily $\mathcal{L} = K - U$, but the Euler-Lagrange equations still hold true, and so does the principle of stationary action. Thus, just defining a Lagrangian can describe entire theories, as the Euler-Lagrange equations yield the equations of methods for each theory, from which every other result of the theory can be derived. This is the power of Lagrangian mechanics.


We will end with one final thought - one of the most successful theories in all of physics, the **Standard model** of particle physics, is encapsulated in one compact Lagrangian:


$$
\mathcal{L} = -\frac{1}{4} F_{\mu \nu} F^{\mu \nu} + i \overline \psi \gamma_\beta D^\beta + h.c. + \psi_i y_{ij} \psi_j \phi + h.c. + |D_\mu \phi |^2 - V(\phi)
$$


And one of the most mathematically beautiful theories, in fact one we will see very soon, **General Relativity**, is described in another compact Lagrangian:


$$
\mathcal{L} = \frac{1}{2\kappa} R \sqrt{-g}~ ~d^4 x
$$


Who knew that Lagrangians could take us deep into the hearts of atoms, and to the furthest stars...? :)
