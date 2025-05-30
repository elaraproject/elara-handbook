# Differential equations


> "Once you learn the concept of a differential equation, you see [them] all over, no matter what you do..."
>
> **Gian-Carlo Rota**


Differential equations are simultaneously often regarded as some of the coolest and strangest objects in physics. On one hand, they're ubiquitous, and nearly every physics theory is expressed using them. On the other, they have a tendency to be unsolvable and difficult to understand. It is hoped that this chapter will bring all their positive qualities into the limelight, and make differential equations no longer scary or intimidating, but descriptions of nature unrivaled in their beauty.


## What is a differential equation?


Differential equations are any equations that describe a function in terms of how it changes through space or time. For instance, we could have:


$$
\frac{dy}{dt} = ky
$$


The interpretation of this equation is that $y$ increases proportional to its derivative, so as $y$ increases, the rate of change of $y$ increases by a proportional amount.


Differential equations can be of a single-variable function and its derivatives, or a multivariable function and its partial derivatives. For instance, the wave equation is given by:


$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$


Here, $u = u(x, t)$, and is the function describing the wave. The interpretation of the wave equation is that the rate of change of the rate of change of $u$ moving along the $x$ direction is proportional to the rate of change of the rate of change of $u$ as time passes.


Differential equations that only involve single-variable functions are called **ordinary differential equations** (ODEs), while those that involve multivariable functions (and their partial derivatives) are called **partial differential equation** (PDEs).

### Initial-value and boundary-value problems

We are interested in solving differential equations to be able to perform further mathematical analysis of the physics of a given system. There are a myriad number of ways to solve differential equations, and we will cover just a few in the following sections. In general, however, finding an _exact_ solution to a particular system cannot be done with knowledge of just the differential equation; typically, _some_ data must be provided before a solution can be found. 

In the case of ODEs in the form $\dfrac{dy}{dt} = f(t, y)$, this data is called the _initial condition_, the state of $y(t)$ at $t = 0$.  Some physical examples of initial conditions are the initial velocity or initial position. We often denote such an initial condition $y_0$. Once we know that, we can calculate the values of $y$ that the differential equation predicts for all future times $t$.  The combination of an ODE and an initial value is known as an **initial-value problem (IVP)**.

**Boundary-value problems** can be thought of as an extension of initial value problems to partial differential equations (PDEs). Unlike initial counditions, boundary value problems usually specify the _function_ that the solution to the PDE takes at the boundaries. Such functions are called _boundary conditions_ (BCs). A physical example may be some water sloshing in a water tank; a PDE may be solved to find the function describing the distribution of water within the tank. The boundary condition would then be the height of the water at the walls of the tank.

The three main types of boundary conditions are Dirichlet, Neumann, and Robin. You can mix and use different boundary conditions together, especially for boundary-value problems that have different types of boundaries, but individually they are generally in one of these forms:

| Type of BC | Example mathematical form                  |
| ---------- | ------------------------------------------ |
| Dirichlet  | $y = f$                                    |
| Neumann    | $\frac{\partial y}{\partial x} = f$        |
| Robin      | $Ay + B \frac{\partial y}{\partial x} = f$ |
| Cauchy     | Combination of Dirichlet and Neumann       |

#### Physical significance of different types of boundary conditions

The physical intepretation of a Dirichlet boundary condition is that the physical quantity is fixed or constrained at the boundary, that is, it takes a specific constant value. In the special case where $u = 0$ at the boundary, the physical quantity vanishes at the boundary.

Meanwhile, the physical interpretation of a Neumann boundary condition is that the physical quantity is kept within the boundary. This corresponds to insulating or reflecting boundaries that prevent the physical quantity from flowing or radiating outwards.

Robin boundary conditions have more flexible physical interpretations. One specific type of robin boundaries is an _open_ boundary. The physical interpretation of an open boundary condition is that the physical quantity is allowed to flow undisturbed outwards beyond the boundary. This corresponds to boundaries that allow for outward radiation or free propagation through them. It is a specific type of Robin boundary condition.

```{admonition} Some supplementary information
Boundary conditions generally do not involve specifying more than the value(s) of the first partial derivatives and the function at the boundaries. This is because the majority of PDEs that govern the universe don't have any higher derivatives of higher than second-order. The main equations we will be solving are either first-order or second-order.
```

#### Solving initial- and boundary-value problems

Initial-value problems can be solved by hand in some cases, but for cases where they cannot be solved by hand, computational methods can be used to solve them numerically (this results in an approximate solution). We will explore how to do so in the numerical methods section in Chapter 3. In addition, there exist online calculators that numerically solve differential equations: see Bluffton University's [free tool at this link](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html) for solving IVPs.

Boundary-value problems can be solved by hand in vastly fewer cases, and even when a solution is possible to find by hand, many simplifying assumptions must be used. For this reason, numerical methods are required for the majority of boundary-value problems. Again, we will explore this further in Chapter 3, but for those interested, the web app  [Visual PDE](https://visualpde.com/) provides an easy-to-use graphical interface for solving PDEs numerically. We recommend you try it out!

## Solving differential equations


When we are told to solve a differential equation, what we are doing is to figure out $y$ from the differential equation. How we can do this depends on the type of differential equation. For example, consider an ODE in the form:


$$
\frac{dy}{dt} = f(y) g(t)
$$


If we can put any ODE in this form, it is considered **separable**. What we can then do is to make sure each side of an equation is expressed only in terms of one variable:


$$
\frac{1}{f(y)} dy = g(t) dt
$$


And finally, to integrate both sides to solve:


$$
\int \frac{1}{f(y)} dy = \int g(t) dt
$$


Partial differential equations are considered separable by a similar criteria: if you can express each side of them only in terms of one variable, then they are separable.


But enough theory! Let's actually try solving two differential equations, one ODE and one PDE. The ODE we will be solving is the exponential growth equation - the reason for that name will become apparent very soon. It is given by:


$$
\frac{dy}{dx} = ky
$$


Here, $k$ is just a constant. By multiplying $dx$ to both sides of the equation, we have:


$$
dy = ky dx
$$


And now, by dividing $y$ from both sides, we have:


$$
\frac{1}{y} dy = k dx
$$


We can now integrate both sides to solve:


$$
\int \frac{1}{y} dy = \int k dx
$$


Which results in:


$$
\ln(y) = kx + C
$$


We raise both with $e^x$, to get:


$$
e^{\ln(y)} = e^{kx + C}
$$


Which becomes:


$$
y = e^{kx + C}
$$


Just one more step! Now that:


$$
e^{kx + C} = e^C e^{kx}
$$


If we define a new constant $C_2 = e^C$, then:


$$
y = C_2 e^{kx}
$$


This is called the **general solution** to the exponential growth equation, because $C_2$ can be any number, and so this general solution encodes all possible solutions each with their own value of $C_2$. 

To actually solve it for a value, we need an **initial value**. For instance, we may be told that $y(0) = 1$. If we plug that in:


$$
1 = C_2 e^{k(0)}
$$


$$
C_2 = 1
$$


So our unique solution given our initial value is now:


$$
y = e^{kx}
$$

We have now solved the **initial value problem** - finding the solution to the differential equation given the provided initial condition.

Note that $C_2$ was the same number as $y(0)$. Therefore, we have a new interpretation of $C_2$ - note that $C_2$ is the **initial value** of a function, so $C_2 = y_0$, and we can rewrite the general solution as:


$$
y = y_0 e^{kx}
$$


The PDE we will be solving is the 1D **heat equation**, given by:


$$
\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2}
$$


This equation models the temperature function $u(x, t)$ of a long, thin rod, where the value of $u$ at a given position $x$ and a given time $t$ is the temperature. Note that $\alpha$ is just a constant. Third nice fact about the equation: it's separable! To separate, we first write $u(x, t)$ as a product of two functions:


$$
u(x, t) = f(x) g(t)
$$


Therefore, using this definition, we can compute the partial derivatives of $u$:


$$
\frac{\partial u}{\partial t} = f(x) g'(t) 
$$


$$
\frac{\partial^2 u}{\partial x^2} = f''(x) g(t)
$$


So we now have:


$$
f g' = \alpha^2 f'' g
$$


If we rearrange this equation, we get:


$$
\frac{g'}{g \alpha^2} = \frac{f''}{f}
$$


Now, note that the left hand side has derivatives and functions dependent on $t$, but the right hand side has derivatives and functions dependent on $f$. If derivatives with respect to different variables are constant, then the two sides of the equation must be equal to a constant, which we'll call $\lambda$:


$$
\frac{g'}{g \alpha^2} = \frac{f''}{f} = -\lambda
$$


Why the negative sign? Since a negative sign applied to a constant makes it still a constant, so we can technically do what we want to $\lambda$ - scale it, add another constant to it, make it positive or negative, the math still works out. The only difference is that $-\lambda$ makes the resulting differential equations way easier to solve, which is why we're adding a negative sign.


So, we have two ODEs instead of our original PDE to solve:


$$
g' = -\lambda \alpha^2 g 
$$ 

$$
f'' = -\lambda f
$$


The first equation is separable, and, after going through the steps to manually solve the differential equation, the result is:


$$
g(t) = C_1 e^{-\lambda a^2 t}
$$


The second equation requires a little bit more work. Which functions are equal to negative of their second derivative? On inspection, we can guess that the function $\sin x$ would work, and indeed it does work when we compute its second derivative:


$$
\frac{d^2}{dx^2} \sin x = -\sin x
$$


However, we want the second derivative to not be equal to the function, but **proportional** to it. Thus, perhaps a good guess would be $\sin(\lambda x)$. But note that:


$$
\frac{d^2}{dx^2} \sin(\lambda x) = -\lambda^2 \sin(\lambda x)
$$


So to make the proportionality constant agree with our differential equation, we want to square root $\lambda$, instead, so:


$$
\frac{d^2}{dx^2} \sin(\sqrt{\lambda} x) = - \lambda \sin(\sqrt{\lambda} x)
$$


To make this equation more general, since multiplying by a constant does not affect proportionality, we can scale $\sin(\sqrt{\lambda} x)$ by an arbitrary constant $C_2$. So we have solved our second differential equation:


$$
f(x) = C_2 \sin(\sqrt{\lambda} x)
$$


Now, we simply need to combine the two solutions together:


$$
u(x, t) = f(x) g(t) = C_2 \sin(\sqrt{\lambda} x) C_1 e^{-\lambda \alpha^2 t}
$$


Since we have two multiplied constants, we can rewrite them as a third constant where $C_3 = C_2 C_1$:


$$
u(x, t) = C_3 \sin(\sqrt{\lambda} x) e^{-\lambda \alpha^2 t}
$$


This is our general solution of the 1D heat equation!


## Laplace and Fourier transforms


The next category of methods to solve differential equations involves Laplace and Fourier transforms. These are two transforms that take an expression of one variable to be expressed in terms of a different variable. For a given function $f(t)$, the Laplace transform results in a new function $g(s)$:


$$
g(s) = \int_0^\infty f(t) e^{-st} dt
$$


And the Fourier transform also results in a new function $h(s)$:


$$
h(s) = \int_{-\infty}^{\infty} f(t) e^{-2\pi i st} dt
$$


The main idea behind these transforms is that they allow ordinary differential equations in terms of $t$ to become algebraic equations in terms of $s$. They also allow partial differential equations in terms of $t$ to become algebraic or ordinary differential equations in terms of $s$. Then, the unknown function can be algebraically solved for, and an inverse transform can be taken to find the solution in terms of $t$.


## Numerical methods and approximations


While many differential equations can be solved exactly, not all differential equations are so straightforward to solve. Instead, most differential equations are typically not solved directly.


There are three common alternatives if a differential equation is resistant to separation of variables or the Laplace and Fourier transforms:

- "Guess and check"
- Taylor series approximation
- Numerical solving (often using computers)


The "guess and check" approach, also known as the "method of inspired guessing", is literally that - given knowledge of functions and their derivatives, guess a solution to the differential equation. For instance, suppose we had the differential equation:


$$
\frac{d^2 x}{dt^2} = 0
$$


From basic analysis of this differential equation, we know that the original function must be of a degree less than 2, because otherwise its second derivative wouldn't vanish to zero. Thus, we can guess that it is some type of linear function. And indeed, if we take the second derivative of a linear function, it does yield zero. So the solution is:


$$
x(t) = at + b
$$


We can also use a Taylor series to approximate solutions to a differential equation. For instance, we could use it to approximate $r(t)$ from Newton's gravitational force equation:


$$
\frac{d^2 r}{dt^2} = -\frac{GM}{r^2}
$$


We aim to solve this with a 4th-order Taylor series for the Earth and the Sun. We have the initial conditions $r(0) = r_0$ and $r'(0) = v_0$, where $r_0$ is the mean distance from the Earth to the Sun (1 AU), and $r'(0)$ is equal to $\frac{2\pi r_0}{T}$, where $T$ is the Earth's period. A 4th-order Taylor polynomial is given by:


$$
r(t) = r(0) + r'(0) t + \frac{r''(0)}{2} t^2 + \frac{r'''(0)}{6} t^3
$$


We know that $r(0) = r_0$, and $r'(0) = v_0$. We also know that $r''(0) - \frac{GM}{r^2} = -\frac{GM}{r_0^2}$. Finally, $r''' = \frac{d}{dt} r''$, such that:


$$
r''' = \frac{d}{dt} \left( -\frac{GM}{r^2}\right) = \frac{2GM}{r^3} \frac{dr}{dt}
$$


Thus, $r'''(0) = \frac{2GM}{r_0^3} v_0$, so the final Taylor polynomial is:


$$
r(t) = r_0 + v_0 t - \frac{GM}{2r_0^2} t^2 + \frac{2 v_0 GM}{r_0^3} t^3
$$


This is 4th-order Taylor expansion for the solution $r(t)$ of the differential equation, and will successfully approximate the solution, so long as $t$ is close to zero.


The final method of solving differential equations that cannot be easily solved using any other means is by using **numerical methods**. Numerical methods take the initial conditions of a differential equation and calculate a tiny change $dy$ in a function caused by a small step along the function's input $dx$. Then, they add that little change $dy$ to the existing value of $y$. By doing this process many, many times, over and over, an entire solution to a differential equation can be approximated. 


To find the formula for one type of numerical method, the Euler method, consider the definition of the derivative, just with the limit removed:


$$
f'(x) = \frac{f(x + h) - f(x)}{h}
$$


Let's solve for $f(x + h)$ in this equation:


$$
f(x + h) = hf'(x) + f(x)
$$


This means that given a current value of a function $f$, the next value of $f$ is given by:


$$
f_{n + 1} = hf'(x) + f_n
$$


This method is tedious to do by hand, but computers can do it very quickly. More accurate types of numerical methods, including the very popular Runge-Kutta methods, are similar in nature, only they break each step into smaller steps for more precision.


## Summary of Differential Equations


The great paradox of differential equations is that they can be ridiculously easy to solve, or ridiculously hard to solve. Using just pen-and-paper techniques, differential equations require lots of creativity and imaginative approaches to be solved, and often require simplifying the problem or special cases of problems. But with brute-force computer solving, differential equations can be simplified into much easier problems, albeit problems that require a lot of steps and computing power. In Project Elära, the majority of differential equation solving will be done numerically, but knowing the analytic techniques will certainly be helpful as well. That said, enough on differential equations - let's get back into physics!
