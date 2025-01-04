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

# Introduction to calculus


> Calculus is the most powerful weapon of thought yet devised by the wit of man.
>
> **Wallace B. Smith**

Calculus is the study of continuous change: a simple set of concepts that can be applied to the most complex of systems. Nearly all of modern-day science is built on calculus, especially physics; it is quite the tool to have in your engineer's toolbox!

Over its nearly 400-year history, calculus has evolved into perhaps the most versatile and broad field of mathematics. There is multivariable calculus, vector calculus, stochastic calculus, the calculus of variations, tensor calculus, fractional calculus...we could go on and on...

However, a lifelong journey through calculus begins with monovariable calculus (or just "calculus"). In monovariable calculus, we're concerned with developing the fundamental ideas of calculus. These ideas will carry over to all the more advanced forms of calculus. Through them, you're realize how calculus has such versatility and power.


## Limits


The **limit** is the value a function approaches as $x$ approaches a given value.

For instance:


$$
f(x) = \frac{x^2 - 1}{x - 1}
$$


While the function is not defined at $x = 1$, it approaches 2 as $x$ approaches 1, thus we can say:


$$
\lim_{x \rightarrow 1} f(x) = 2
$$


Sometimes, limits are the same regardless of the direction $x$ approaches $c$. At other times, the limit is different, and dependent on the direction. For instance, take:


$$
f(x) = \frac{1}{x - 3}
$$


As $x$ approaches 3 from the right-hand side, $f(x)$ approaches infinity, and as $x$ approaches 3 from the left-hand side, $f(x)$ approaches **negative** infinity. Thus, we can say there are separate left-hand and right-hand limits, where:


$$
\lim_{x \rightarrow 3^+} f(x) = \infty = DNE
$$

$$
\lim_{x \rightarrow 3^-} f(x) = -\infty = DNE
$$


(DNE means "does not exist")


Notice that as the limit is infinite, and infinity is not a real number, we do not say that the limit of the function is infinity. Rather, we say that the limit does not exist.

The limit of a function does not exist in one of three cases:

- If the function’s left- and right-hand limits are not equal at that x-value
- If the function oscillates in value around an x-value
- If the function becomes indefinitely large around an x-value


## Derivatives


The equation for the slope of a line is defined as:


$$
m = \frac{\Delta f(x)}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}
$$


However, the slope equation only works for straight lines. How, then, could we find the slope of a curve?

Well, we can first take advantage of the fact that if you zoom _really_ close in to a curve, it looks like a straight line:


```{image} img/Calculus-curve-zoom.jpg
:alt: Zooming into a curve
:width: 600px
:align: center
```


_Notice how, as we zoom into the curve, the curve looks more and more like a straight line, and the curvature becomes less and less noticeable._


The **derivative** is a function that tells you the slope of another function at _any_ point. You can think of it as an "upgraded" version of the slope formula. We find the derivative by taking two points, $(x, f(x))$ and $((x + a), f(x+a))$, and calculating the slope from them:


```{image} img/Derivative-illustration.png
:alt: Illustration of the derivative
:width: 400px
:align: center
```


As we shrink $a$ and make it smaller and smaller, $a$ will approach zero, and the slope becomes:


$$
m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{f(x+a) -f(x)}{(x+a) -x} = \frac{f(x+a) -f(x)}{a}
$$


So, for a function $f$, the derivative $\frac{df}{dx}$ is defined as the limit by taking $a$ smaller and smaller:


$$
\frac{df}{dx} = \lim_{a \rightarrow 0} \frac{f(x+a) -f(x)}{a}
$$


### An alternative understanding of the derivative


A more intuitive, but less mathematically rigorous, definition of the derivative is to look at the slope formula once again:


$$
m = \frac{\Delta y}{\Delta x}
$$


Now, let's imagine making the change $\Delta$ smaller and smaller. The eventual result is that $\Delta y$, a small change, becomes a tiny change $dy$, and $\Delta x$, a small change, becomes a tiny change $dx$:


$$
\lim_{\Delta \to 0} \frac{\Delta y}{\Delta x} = \frac{dy}{dx}
$$


### (Opinionated) derivative notation

Calculus was invented at roughly the same time by two brilliant mathematicians - Gottlieb Leibniz and Isaac Newton. Unfortunately, each of them published their work at the same time with differing notations. Leibniz wrote the derivative with the notation $\frac{df}{dx}$; Newton used the notation $\dot f$. Lagrange and Euler, not long after, came up with the notation $f'(x)$. In any case, Leibniz and Newton...got into a fight, which became a political controversy, and other mathematicians decided to develop *other* notations as well. So, sadly, there is not a unified notation around calculus.


The most common form of notation is Leibniz's notation, where the derivative of $f(x)$ is written like this:


$$
\frac{df}{dx}
$$


The _nth_-derivative is written as:


$$
\frac{d^n f}{dx^n}
$$


```{important}
**Note:** Even though this looks like a fraction, and can be manipulated similar to fractions, the derivative in Leibniz's notation is **absolutely not** the same as a fraction!
```


The second most common notation is Langrange's notation, where the derivative of $f(x)$ is written like this:


$$
f'(x)
$$


Here, the _nth_-derivative is written as:


$$
f^n (x)
$$


In Project Elära, derivatives of a single-variable function use Leibniz notation most commonly to minimize confusion. The derivative of a function $f(x)$ in Project Elära is _preferred_ to be written as:


$$
\frac{df}{dx}
$$


If we have a function $v(t)$, the derivative with respect to $t$ would be written as:


$$
\frac{dv}{dt}
$$


A higher order derivative (e.g. second derivative) is written like this:


$$
\frac{d^2 f}{dx^2}
$$


The derivative evaluated at a certain point $x = a$ is written as:


$$
\left.\frac{df}{dx} \right |_{x = a}
$$


However, there are some alternate notations that will sometimes be used. Note that these are **all** equivalent:


$$
\frac{d}{dx} f(x) = f'(x)
$$


You will also see $\dot f$ and $\ddot f$ sometimes for first and second time derivatives respectively. This is recommended not to be used as it is easily notationally confused.


### Differentiation


The derivative is a very powerful function, but finding the derivative of a function unfortunately requires a bit of time and patience. This is because there is no universal formula for finding the derivative of a certain function - instead, we have general *rules* for finding the derivatives of a certain type of function, which we use in the process of **differentiation**.


Let's start with the easiest derivative - the derivative of any constant function is zero. Why? Because the slope of any constant function is always zero, and remember, the derivative is a function that tells you the slope at every point. So if the slope at every point is zero, the derivative will always be zero.

We call this the **constant rule**, and we write it out like this:


$$
\frac{dC}{dx} = 0 
$$


Where $n$ can be any constant. For instance, the derivative of 2 with respect to $x$ (the same as finding the rate of change of $f(x) = 2$) would be:


$$
\frac{d(2)}{dx} = 0
$$


This also means that if you have a function $f(x) = c$, where $c$ is a constant, then:


$$
\frac{df}{dx} = c
$$


That should be simple enough, right?

Now, let's do the second-easiest derivative. The derivative of the exponential function $f(x) = e^x$ is itself. We call this the **exponential rule**, and we write it out like this:


$$
\frac{d(e^x)}{dx} = e^x
$$


The exponential rule can also be more generally written as this:


$$
\frac{d(a^x)}{dx} = \ln(a) a^x
$$


For trigonometric functions, the derivatives unfortunately have to be memorized, but you just have to memorize two of them to find the derivatives of all trigonometric functions:


$$
\frac{d(\sin x)}{dx} = \cos x
$$

$$
\frac{d(\cos x)}{dx} = -\sin x
$$


And for polynomial functions, we can use the **power rule**:


$$
\frac{d(x^n)}{dx} = nx^{n - 1}
$$


The power rule applies to linear functions in the form $y = mx +c$:


$$
\frac{df}{dx} = \frac{d(mx + c)}{dx} = \frac{d(mx)}{dx} = 1 m \left(x^{1-0}\right) = m
$$


As well as for rational functions in the form $f(x) = \frac{1}{x^n}$:


$$
\frac{d\left(\frac{1}{x^n}\right)}{dx} = \frac{d(x^{-n})}{dx} = -nx^{-n -1} = -\frac{n}{x^{n + 1}}
$$


And nth root functions (e.g. square root, cube root, etc.) in the form $f(x) = \sqrt[n]{x}$:


$$
\frac{d\left(\sqrt[n]{x}\right)}{dx} = \frac{d\left(x^\frac{1}{n}\right)}{dx} = \frac{1}{n} x^{\frac{1 - n}{n}}
$$


Combining the power rule and exponential rule gives us the derivatives of logarithms:


$$
\frac{d(\ln x)}{dx} = \frac{1}{x}
$$

$$
\frac{d(\log_a x)}{dx} = \frac{1}{x \ln a}
$$


However, most functions are made from a _combination_ of these functions. For instance, the function $f(x) = 2x^2 + 3x + 5$ is a combination of a constant function, linear function, and power function. To find the derivatives of combinations of functions, we have a few more rules to help us.

First, we have the **sum rule**:


$$
\frac{d(f(x) + g(x))}{x} = \frac{df}{dx} + \frac{dg}{dx}
$$


Then, the **constant coefficient rule:**


$$
\frac{d(c \cdot f(x))}{dx} = c \cdot \frac{df}{dx}
$$


Then, the **product rule**:


$$
\frac{d(f(x)g(x)}{dx} = \frac{df}{dx} g(x) + \frac{dg}{dx} f(x)
$$


From the product rule, we can derive the **quotient rule**:


$$
\frac{d\left(\frac{f(x)}{g(x)}\right)}{dx} = \frac{\frac{df}{dx} g(x) - \frac{dg}{dx} f(x)}{(g(x))^2}
$$


And, most importantly, we have the **chain rule**. The chain rule is used for _composite functions_ - functions that have been nested into each other. For instance, $h(x) = \sin x^2$ is made by nesting the function $g(x) = x^2$ _inside_ of the function $f(x) = \sin x$. So, we can say that $h(x) = f(g(x))$. This is a **composition of functions**.

With that in mind, the **chain rule** is written like this:


$$
\frac{df(g(x))}{dx} = \frac{df}{du}\frac{du}{dx} = \frac{df}{dx} \{g(x)\} \frac{dg}{dx}
$$


This means we nest $g(x)$ in the derivative of $f(x)$ and multiply that by the derivative of $g(x)$. The other rules here are mostly self-explanatory, but I'll go through a worked example with the chain rule: let's try to find the derivative of $h(x) = \cos x^2$.


#### Practicing the chain rule


We use the chain rule for _composite_ functions, like our example, $h(x) = \cos x^2$. We know that we can rewrite $h(x)$ as a composite function $f(g(x))$, where:


$$
h = \cos (u)
$$

$$
u = x^2
$$


We can now use the chain rule. In the first step, we find $\frac{dh}{du}$:


$$
\frac{dh}{du} = -\sin (u) = -\sin (x^2)
$$


Note that we substituted in $x^2$ for $u$. Now, we find $\frac{du}{dx}$:


$$
\frac{du}{dx} = 2x
$$


We now just need to multiply them together:


$$
\frac{dh}{dx} = \frac{dh}{du} \frac{du}{dx}
$$

$$
\frac{dh}{dx} = -2x \sin x^2
$$


That's our answer!


### Reciprocal derivatives


In monovariable calculus _only_, derivatives follow the **reciprocal rule**:


$$
\frac{df}{dx} = \frac{1}{\frac{dx}{df}}
$$

$$
\frac{dx}{df} = \frac{1}{\frac{df}{dx}}
$$


### Tangent to a curve

The tangent to the function $f(x)$ at $x = a$ is given by the function $T(x)$, where:


$$
\sigma(x) = \frac{df}{dx}
$$

$$
T(x) = \sigma \left(a\right)\left(x-a\right)+f\left(a\right)
$$


This is also called the **linear approximation** of a function.


### Higher-order derivatives


Taking a derivative _nth_ times gives you the _nth_ derivative of a function. For example, taking the derivative of the derivative is the second derivative, the derivative of the second derivative is the third derivative, and so on. Going in the other direction, the 0th derivative is not taking the derivative at all - the same as the original function.

The second derivative is the most common higher-order derivative, and it is given by:


$$
\frac{d^2 f}{dx^2} = \frac{d\left(\frac{df}{dx}\right)}{dx}
$$


The _order_ of the derivative is the number of times you take the derivative: for instance, the 7th derivative involves taking the derivative of a function 7 times! (don't do that, please...)


### Finding maxima and minima


We can find the critical points (maxima and minima) of a function $f(x)$ by finding its derivative and setting it to zero:


$$
\frac{df}{dx} = 0
$$


For instance, for the function $f(x) = 2x^2 + 1$:


$$
\frac{df}{dx} = 4x
$$

$$
4x = 0
$$

$$
x = 0
$$


Then, plugging in that x value into the original f(x), we can find the y value of the maximum/minimum point:


$$
f(0) = 2(0^2) + 1 = 1
$$


So the minimum of $f(x)$ is the point $(0, 1)$. How do we know if it's a maximum or minimum though? To find out, we use the **second derivative**, which measures how the slope changes. If a point is a maximum, the slope will change from positive to negative around that point; if a point is a minimum, vice-versa. So:


$$
\begin{cases}
\text{if} \quad \frac{d^2 f}{dx^2} < 0 \quad x = \text{max.} \\
\text{if} \quad \frac{d^2 f}{dx^2} > 0 \quad x = \text{min.}
\end{cases}
$$


The second derivative of $f(x)$ is the derivative of its derivative, which we can find like this:


$$
\frac{d^2 f}{dx^2} = \frac{d(4x)}{dx} = 4
$$


Since $\frac{d^2 f}{dx^2} > 0$, we know that the point $(0, 1)$ has to be a **minimum**.


### Implicit differentiation


Implicit differentiation is when we differentiate with respect to an intermediary variable, often used when the object being differentiated is not a function. For instance, consider the equation of a circle:


$$
x^2 + y^2 = 1
$$


To implicitly differentiate it, we have:


$$
\frac{d}{dx} (x^2 + y^2) = \frac{d}{dx} (1)
$$


The right-hand side is straightforward:

$$
\frac{d}{dx} (x^2 + y^2) = 0
$$


The sum rule can be used for the left-hand side:


$$
\frac{d}{dx}
 x^2 + \frac{d}{dx}
y^2 = 0
$$

$$
2x + \frac{d}{dx}
y^2
 = 0
$$


To implicitly differentiate $y^2$, we can use the chain rule:


$$
\frac{d}{dx}
y^2 = 2y \frac{dy}{dx}
$$


So:

$$
2x + 2y \frac{dy}{dx} = 0
$$


Rearranging the terms, we find that:

$$
2y \frac{dy}{dx} = -2x
$$

$$
\frac{dy}{dx} = - \frac{x}{y}
$$


**Problem:** Suppose that $y = x^2 + 3$. Find $\frac{dy}{dt}$ when $x = 1$, $\frac{dx}{dt} = 2$.

We implicitly differentiate $y$ to find:

$$
\frac{dy}{dt} = 2x \frac{dx}{dt}
$$

Then we plug in the values for $x$ and $\frac{dx}{dt}$ to find that:

$$
\frac{dy}{dt} = 2(1)(2) = 4
$$


## Antiderivatives


The antiderivative is the function $F(x)$ that is the original function of a derivative $f(x)$. For instance, the antiderivative of $2x$ is $x^2$, because if $2x$ is the derivative, then the original function is $x^2$:


$$
\frac{d(x^2)}{dx} = 2x
$$


The **indefinite integral** is another name for the antiderivative. The indefinite integral is written as:


$$
F(x) + C = \int f(x)dx
$$


The $C$ is due to the fact that the integral returns a family of antiderivatives, as any derivative has infinitely many antiderivatives.


Just like derivatives, indefinite integrals follow certain rules:


$$
\int dx = x + C
$$

Constant rule:

$$
\int k  \, dx = kx + C
$$

Inverse power rule:

$$
\int x^n dx = \frac{x^{n + 1}}{n + 1}
$$

Sum and difference rule:

$$
\int [f(x) \pm g(x)] dx = \int f(x) dx \pm \int g(x) dx
$$

Constant factor rule:

$$
\int k f(x) dx = k \int f(x) dx
$$


### An intuitive understanding


Suppose we have the derivative of a function, and that derivative is $f(x)$. We now want to find the original function $F(x)$ that derivative came from. To do so, we notice that:


$$
f(x) = \frac{dF}{dx}
$$


So if we rearrange the terms, we get:


$$
f(x) dx = dF
$$


Now, $dF$ is similar to saying "a tiny tiny change in F". If we add lots of $dF$'s together, it would seem reasonable that we would get $F$:


$$
F(x) = \sum_i dF
$$


Only in integral calculus, we replace the summation symbol with the integral symbol $\int$, so it becomes:


$$
F(x) = \int dF = \int f(x) dx
$$


## Integration


### Area under a curve


Up to this point, we've only seen one type of integral - the indefinite integral, used for finding the original function given its derivative. Now, we will explore another type of integral, the definite integral, which returns an area rather than a function. The definite integral looks like this:


$$
A = \int \limits_a^b f(x) dx
$$


Intuitively, the definite integral gives the area underneath a curve. It does this by creating tiny rectangles under that curve:


```{image} https://www.technologyuk.net/mathematics/integral-calculus/images/integral_calculus_0013.gif
:alt: Integral visualization as rectangles under a curve
:width: 400px
:align: center
```


We can find the area by summing the areas of the rectangles we place under the curve. As more rectangles are used, the approximation becomes closer to the true area. Taking the limit as the number of rectangles approaches infinity, we find the true area underneath the curve:


$$
A = \lim_{n \rightarrow \infty} \sum_{i = 1}^n f(c_i) \Delta x = \int \limits_a^b f(x) dx
$$


Several properties of the definite integral include:


$$
\int_a^a f(x) dx = 0
$$

$$
\int_b^a f(x)dx = -\int_a^b f(x)dx
$$

$$
\int_a^c f(x) dx = \int_a^b f(x)dx + \int_b^c f(x)dx
$$


### Average value of a function

The average (mean) value of a function on $[a, b]$ is given by:

$$
\frac{1}{b-a} \int_a^b f(x)dx
$$


### The fundamental theorem of calculus


Derivatives, indefinite integrals, and definite integrals are related by the **fundamental theorem of calculus (FTC)**. The theorem consists of two parts.


The first part of the FTC states that if you have an original function $F(x)$ whose derivative is $f(x)$, then taking the indefinite integral of the derivative gives you the original function:


$$
f(x) = \frac{dF}{dx} \Rightarrow F(x) = \int f(x) dx
$$


The FTC #1 establishes that differentiation and integration are **inverse operations**. The derivative is the _rate of change_, whereas the integral finds the _accumulated net change_.


Then the second part of the FTC states that the definite integral, which is the area underneath the curve of $f(x)$, is given by evaluating the indefinite integral between the bounds of the curve:


$$
A = \int \limits_a^b f(x) dx = F(b) - F(a)
$$


This means that when we know the indefinite integral of a function, we can use the FTC as a shortcut to evaluating the definite integral.


For instance, let's try to evaluate the area under the curve of $f(x) = x^2$ from $x = 0$ to $x = 3$:


$$
\int \limits_0^3 x^2 dx
$$


We first find the indefinite integral of $f(x)$ - the original function whose derivative is $x^2$. We can use the inverse power rule for this:


$$
\int x^n dx = \frac{1}{n + 1} x^{n + 1} + C
$$


Thus the indefinite integral of $f(x)$ is equal to:


$$
F(x) = \frac{x^3}{3} + C
$$


Now, we just evaluate $F(3) - F(0)$:


$$
F(3) - F(0) = \left(\frac{3^3}{3} + C\right) - \left(\frac{0^3}{3} + C\right)
$$


The two $C$'s cancel and we are simply left with:


$$
F(3) - F(0) = 9
$$


Thus:


$$
\int \limits_0^3 x^2 dx = 9
$$


### U-substitution


Just as we have the chain rule for derivatives, we have a sort of "reverse" chain rule for evaluating indefinite integrals. We begin with a typical integral:


$$
\int f(x) dx
$$


And we want to express the integrand $f(x)$ in terms of another function $g(u)$. To do this, we define:


$$
x = g(u)
$$

$$
f(x) = f(g(u))
$$

$$
\frac{dx}{du} = g'(u)
$$

$$
dx = g'(u) du
$$


Therefore:

$$
\int f(x) dx = \int f(g(u)) g'(u) du
$$


which is essentially a reverse chain rule. Why would we do this though? Doesn't it make integrals more complicated? While the formula may seem scary, the reality is that with clever cancelling, u-substitution can make integrals a lot easier to solve. Take, for instance:


$$
\int \frac{x^{3}}{\sqrt{16-x^{4}}}dx
$$


Here, we identify the part of the integral that we want to make our $u$. Usually, this is an annoyingly complex part of the integral that we want to make simpler with u-substitution. In this case, it would be $u = 16 - x^4$. So:


$$
u = 16 - x^4
$$

$$
\frac{du}{dx} = -4x^3
$$


$$
dx = \frac{du}{-4x^3}
$$


Now, we can substitute $16-x^4$ for $u$:


$$
\int \frac{x^{3}}{\sqrt{16-x^{4}}}dx = \int \frac{x^{3}}{\sqrt{u}}dx
$$


And substitute $\frac{du}{-4x^3}$ for $dx$:


$$
\int \frac{x^{3}}{\sqrt{u}}dx = \int \frac{x^{3}}{\sqrt{u}} \frac{du}{-4x^3}
$$


And magically we find that the $x^3$ and $-4x^3$ cancel, leaving us with an integrand completely in terms of $u$:


$$
\int \frac{x^{3}}{\sqrt{u}} \frac{du}{-4x^3} = \int -\frac{1}{4} \frac{1}{\sqrt{u}} du
$$


We can make the integral even simpler by moving the constant factor outside the integral:


$$
\int -\frac{1}{4} \frac{1}{\sqrt{u}} du = -\frac{1}{4} \int \frac{1}{\sqrt{u}} du
$$


We've successfully greatly simplified the integral!


$$
\int \frac{x^{3}}{\sqrt{16-x^{4}}}dx \Rightarrow -\frac{1}{4} \int \frac{1}{\sqrt{u}} du
$$


Solving this integral in terms of $u$ is easy:


$$
-\frac{1}{4} \int \frac{1}{\sqrt{u}} du = -\frac{1}{2} \sqrt{u} + C
$$


We just need to remember to now replace $u$ with its value in terms of $x$:


$$
-\frac{1}{2} \sqrt{u} + C = -\frac{1}{2} \sqrt{16 - x^4} + C
$$


So we evaluated a difficult integral using u-substitution to find its answer!


### Integration by parts


Integration by parts is given by:


$$
\int u dv = uv - \int v du
$$


It is the integral form of the product rule for derivatives. Unsurprisingly, it is often used for integrating products of functions. To illustrate this, let's consider integrating $f(x) = x \sin (x)$:


$$
\int x\sin(x) dx
$$


To integrate, we first pick our $u$ and $dv$. We generally want $u$ to be a function that is easy to differentiate, and $dv$ to be a function that is easy to integrate. Here, we will pick $u = x$, $dv = \sin(x)$. So:


$$
u = x
$$

$$
\frac{du}{dx} = 1
$$

$$
du = 1dx = dx
$$

$$
dv = \sin x
$$

$$
v = \int dv = -\cos x
$$


Using the integration by parts formula, we have:


$$
\int x\sin(x) dx = -x \cos x - \int (-\cos x) dx
$$


Which simplifies to:


$$
\int x \sin x dx = -x\cos x + \sin x + C
$$


### Other integration rules


There are several other notable integration tricks such as integrating by partial fractions, integrating by trigonometric substitutions, using trig identities, long division, and other algebraic methods for solving indefinite integrals. A full list of them can be found at <https://brilliant.org/wiki/integration-tricks/>. Another way to solve complicated integrals is to refer to integral tables, which contain precomputed tables of common integrals - see <https://en.wikipedia.org/wiki/Lists_of_integrals>.


### Integral calculators


When integrals are too difficult to solve using any known method, consult an online integral calculator! Some very good ones are <https://mathdf.com/int/> and <https://www.wolframalpha.com>. Additionally, for relatively simple expressions (to type in), consult <https://gamma.sympy.org/>. The SymPy Python library is also well worth learning to do symbolic integration on a computer.


## Taylor series


Imagine we had a certain function $f(x)$. We want to approximate that function with a polynomial $T(x)$. So we write the general equation of a polynomial centered at $x = a$:


$$
T(x) = c_0 + c_1 (x - a) + c_2 (x-a)^2 + c_3 (x - a)^3 + c_4 (x - a)^4 + \dots c_n (x - a)^n
$$


Now, for this function to be equal to $f(x)$, then $T(a) = f(a)$. So we compute $T(a)$:


$$
T(a) = c_0 + c_1 (a - a) + c_2 (a-a)^2 + c_3 (a - a)^3 + c_4 (a - a)^4 + \dots c_n (a - a)^n
$$


Since $a - a$ cancels to zero, every term in the equation cancels to zero other than $c_0$, so:


$$
T(a) = c_0
$$


But we know that $T(a) = f(a)$. So we can rewrite $T(x)$ as:


$$
T(x) = f(a) + c_1 (x - a) + c_2 (x-a)^2 + c_3 (x - a)^3 + c_4 (x - a)^4 + \dots c_n (x - a)^n
$$


Alright, but just having two functions be equal at a single point isn't enough to make sure that these two functions are equal. To be more sure that the two functions are equal, we demand $T'(a) = f'(a)$ must be true as well. If we compute $T'(x)$, we'd get:


$$
T'(x) = c_1 + 2c_2(x - a) + 3 c_3(x - a)^2 + 4c_4 (x -a)^3 + \dots nc_n (x - a)^{n - 1}
$$


Once again, if we compute $T'(a)$, the terms all cancel other than the first, so we have:


$$
T'(a) = c_1 + 2c_2 (a - a) + 3c_3(a - a)^2 + 4c_4 (a - a)^3 + \dots nc_n(a - a)^{n - 1}
$$


Again, since all the $a - a$ terms cancel to zero, we are left with just one term, where:


$$
T'(a) = c_1
$$


But again, we know that $T'(a) = f'(a)$, so we can rewrite $T(x)$ as:


$$
T(x) = f(a) + f'(a) (x - a) + c_2 (x-a)^2 + c_3 (x - a)^3 + c_4 (x - a)^4 + \dots c_n (x - a)^n
$$


Still, we can't be certain that $T(x) = f(x)$. We don't just want their values and their first derivatives to match at $x = a$ - we want their second derivatives to match too! So we do the same exercise - take the second derivative of $T(x)$. We get:


$$
T''(x) =2c_2 + 3(2) c_3(x - a) + 4(3)c_4 (x -a)^2 + \dots n (n-1)c_n (x - a)^{n - 2}
$$


Once again, if we solve for $T''(a)$, every term except for the first cancel to yield zero, so we get:


$$
T''(a) = 2c_2
$$


But we said that $f''(a) = T''(a)$, so:


$$
c_2 = \frac{1}{2} f''(a)
$$


So $T(x)$ is now:


$$
T(x) = f(a) + f'(a) (x - a) + \frac{1}{2} f''(a) (x-a)^2 + c_3 (x - a)^3 + c_4 (x - a)^4 + \dots c_n (x - a)^n
$$


You might be noticing a pattern here! In fact, if we take the general expression of $T(x)$:


$$
T(x) = \sum_{n = 0}^\infty c_n (x - a)^n
$$


Then the nth-term of $T(x)$ would be:


$$
c_n (x - a)^n
$$


If we take the derivative of the nth term, using the power rule, we get:


$$
c_n (n)(n-1)(n-2)\dots(3)(2)(1) (x-a)^{n -n}
$$


Here we can write $n(n - 1)(n-2)(n-3) \dots (3)(2)(1)$ as $n!$ (we call that "n-factorial"). For example, $3! = 3 \times 2 \times 1 = 6$. We can also rewrite $n-n = 0$, and anything raised to the power of zero is just one, so we get this expression for the nth-derivative of $T$:


$$
c_n n!
$$


And if we demand that the nth-derivative of $f(x)$ is equal to the nth-derivative of $T(x)$ at $x = a$, then:


$$
f^{(n)}(a) = c_n n!
$$


If we solve for $c_n$, we get:


$$
c_n = \frac{f^{(n)} (a)}{n!}
$$


Then if we plug this back in to the infinite sum representation of $T(x)$, replacing $c_n$ with what we derived:


$$
T(x) = \sum_{n = 0}^\infty \frac{f^{(n)} (a)}{n!}(x - a)^n
$$


This is the formula for the **Taylor series** of a function. For practical purposes, we usually don't let the sum range from 0 to infinity, and instead cap the sum at some number, which we call the **order** of the resulting polynomial. For example, the 7th-order Taylor polynomial is a Taylor series capped at 7 terms.


We can use the Taylor series to compute the values of transcendental functions (the exponential function, logarithmic function, and trigonometric functions), given known values of a function. For example, using a 7th-order Taylor approximation at $a = 0$ and range reduction techniques to rescale any value of the sine function to between $-\frac{\pi}{4}$ and $\frac{\pi}{4}$, you can calculate the value of the sine function to within an error of $\pm 3.6 \times 10^{-6}$ of the correct value. 


The Taylor series is also a method of calculating the precise value of $e$, Euler's number, to use in calculations of the exponential function. To do so, we first need to recognize that $e^0 = 1$, as with any other number raised to the power of zero. We also know that because $\frac{d}{dx} e^x = e^x$, the nth-derivative of $e^x$ will always be $e^x$, and thus the nth-derivative $f^{(n)} (0)$ is always going to be $e^0 = 1$. Plugging that into our Taylor series, and setting $a = 0$ (as our point of reference is $x = 0$), we have:


$$
e^x = T(x) = \sum_{n = 0}^\infty \frac{1}{n!} (x -0)^n
$$


Which becomes:


$$
T(x) = \sum_{n = 0}^\infty \frac{x^n}{n!}
$$


Now, given also that we know that $e^1 = e$, then $T(1) = e$, so:


$$
e = T(1) = \sum_{n = 0}^\infty \frac{1^n}{n!}
$$


And since $1^n = 1$, we have:


$$
e = \sum_{n = 0}^\infty \frac{1}{n!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \dots
$$


Which results in:


$$
e \approx 2.718
$$


You can also find $\pi$ using Taylor series in a similar manner (just with a Taylor approximation of the arctangent or arcsine function instead).


Taylor series are also good for approximating complex functions. For example, the Taylor series for $\sin(x)$ starts with:


$$
\sin (x) \approx x - \frac{1}{3!} x^3 + \frac{1}{5!} x^5 - \frac{1}{7!} x^7 + \dots
$$


Which means the first-order Taylor polynomial for $\sin(x)$ is just:


$$
\sin(x) \approx x
$$


This is called the **small-angle approximation** to the sine function, and it is very powerful - as we'll see later, it allows many complicated differential equations to be simplified and made solvable.
