---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
mystnb:
  remove_code_source: true
  remove_code_outputs: false
  render_image_options:
    align: center
---

# Algebra


We will begin by going through a review of basic algebra. If seems too easy, feel free to skip to the next section; otherwise, continue here.

We will assume you know what negative numbers and fractions are, and how to do basic arithmetic. If not, review at <https://www.khanacademy.org/math/pre-algebra>.

## The fundamentals of algebra


Algebra is a system of mathematics where we do computations using symbols rather than numbers. Symbols are usually denoted with roman or greek letters.


For instance, consider the following equation:


$$
\Box - 3 = 5
$$


It's clear that the "missing number" in the box has to be 8 for the equation to be true. We can now replace the box with a symbol called $x$:


$$
x - 3 = 5
$$


Where:


$$
x = 8
$$


## The rules of algebra


Every unknown in algebra is denoted by a **different symbol** such as $x, y, z$, etc. For example, we could write:


$$
x + y = 3
$$


Which would be true if $x = 1$ and $y = 2$.


Multiplication in algebra is written like this:


$$
x \times 3 = 3x = x + x + x
$$


This means that:


$$
1x = x \times 1 = x
$$


And:


$$
0x = x \times 0 = 0
$$


Division in algebra is almost always written as a fraction:


$$
\frac{x}{4} = x \div 4
$$


We can move the $x$ to the left of a fraction and it would be equivalent:


$$
\frac{1}{4} x = \frac{x}{4}
$$


If we multiply a fraction by the same value as the bottom of the fraction, we get rid of the fraction:


$$
\frac{a}{b} \times b = a
$$


If we have the same thing on the top and on the bottom of the fraction, we can remove the same thing - this is called "cancelling":


$$
\frac{ax}{ay} = \frac{x}{y}
$$


The fraction of anything over one is itself:


$$
\frac{a}{1} = a
$$


We can move the bottom part of a fraction out of the fraction to get rid of the fraction:


$$
x = \frac{a}{b} \Rightarrow xb = a
$$


We can have negative symbols as well as positive symbols:


$$
-x = -1 \times x
$$


A negative sign to the left of a fraction is equal to a negative numerator or a negative denominator:


$$
-\frac{2}{5} = \frac{-2}{5} = \frac{2}{-5}
$$


Algebraic expressions are collections of numbers and symbols:


$$
3x^2 + 5xy + 6
$$


Equations are expressions that are related by an equal sign:


$$
xyz = 5
$$


Parts of algebraic expressions and equations separated by operators ($+-\times \div$) or placed inside brackets are called **terms**. For example, $5x + 3y + 2z = 5$ has the terms $5x$, $3y$ and $2z$.


If we change the order of an equation, the equation remains the same:


$$
x + 1 = 1 + x
$$


Brackets are equivalent to multiplication when a number or symbol is placed to the left of a bracket:


$$
3(x + 1) = 3 \times (x + 1)
$$


We can **expand** brackets by multiplying the number (or symbol) in front of the bracket by everything inside the bracket:


$$
3(x + 1) = 3 \times x + 3 \times 1 = 3x + 3
$$


And in the same way, we can **factorize** an expression into one that has brackets:


$$
ab + ac = a(b + c)
$$


For more complicated brackets expansions, we use this formula:


$$
(a + b)(c + d) = ac + ad + bc + bd
$$


To factorize this, we'll need a tool called the quadratic formula, which we'll explore later in this chapter.


We can write powers like this:


$$
x^3 = x \times x \times x
$$


Where $x^3$ is equal to $x$ multiplied by $x$ 3 times.


Putting a negative sign in front of brackets is equal to multiplying everything inside the brackets by $-1$:


$$
-(a + b) = -a + -b
$$


A double negative is a positive:


$$
-(-a) = a
$$


Sometimes, we use symbols to represent a number rather than an unknown - these are called **constants**. To avoid confusing symbols that represent numbers and symbols that represent unknowns, we usually use special letters (especially greek letters) to denote constants, and we will always say beforehand that the expression or equation contains a constant. For example, a common constant is $\pi$, which is a number that starts with the digits $3.14159$. This means that:


$$
\pi x = 3.14159 \times x
$$


## Solving algebraic equations


To be able to solve algebraic equations, the key rule is that **we do to the left-hand side of the equals sign as we do to the right**.


For example, take the example:


$$
x + 5 = 10 - x
$$


Here, we first need to add $x$ to both sides of the equation, giving us:


$$
x + 5 (+ x) = 10 - x (+ x)
$$


This will become:


$$
x + x + 5 = 10
$$


Which simplifies to:


$$
2x + 5 = 10
$$


We then subtract 5 from both sides of the equation:


$$
2x = 5
$$


And then divide both sides by 2 to get the answer:


$$
\frac{2x}{2} = \frac{5}{2}
$$


$$
\frac{2}{2} x = \frac{5}{2}
$$


Because $\frac{2}{2} = 1$:


$$
x = \frac{5}{2}
$$


Sometimes, we need to solve an equation that uses entirely symbols. Yes, that can seem scary, but going slowly, every step becomes easier. For example, presume we have the equation:


$$
\frac{p (a + 2x)}{q^2} = b
$$


The first step is to multiply by $q^2$ on both sides:


$$
\frac{p (a + 2x)}{q^2} \times q^2 = b \times q^2
$$


Since we know that we can remove the $\times$ sign and just write symbols next to each other to show multiplication, this becomes:


$$
\frac{p(a + 2x)}{q^2} q^2 = bq^2
$$


We use one of the rules of algebra, which says that $\frac{a}{b} \times b = a$, to simplify:


$$
\frac{p(a + 2x)}{q^2} \times q^2 = p(a + 2x)
$$


This means our original equation becomes:


$$
p(a + 2x) = bq^2
$$


Now, we need to divide $p$ from both sides. Recall that we write divisions as fractions, so we have:


$$
\frac{p(a + 2x)}{p} = \frac{bq^2}{p}
$$


Using the rule that $\frac{px}{p} = x$, we can cancel the $p$:


$$
(a + 2x) = \frac{bq^2}{p}
$$


Now, we can subtract $a$ from both sides to get rid of it:


$$
(a + 2x) - a = \frac{bq^2}{p} - a
$$


Which gives:


$$
2x = \frac{bq^2}{p} - a
$$


We still unfortunately have the 2, which is more annoying to deal with. We have to divide the 2 from both sides:


$$
\frac{2x}{2} = \frac{\frac{bq^2}{p} - a}{2}
$$


Because $\frac{2x}{2} = x$ (it makes sense; multiplying something by a number then diving by that same number should give you that original something), we can simplify to:


$$
x = \frac{\frac{bq^2}{p} - a}{2}
$$


Remember that anything multiplied by 1 is itself:


$$
x = \frac{1 \times \left(\frac{bq^2}{p} - a\right)}{2}
$$


And that we can move parts of a fraction off the fraction:


$$
x = \frac{1}{2} \left(\frac{bq^2}{p} - a \right)
$$


Congratulations, we've solved it!


## Graphs and coordinates


A graph is a visual way of representing data. To plot a graph, need two values: an $x$ value, and a $y$ value. We represent these values as **ordered pairs** like this:


$$
(x, y)
$$


For example, if we want to plot the value $x = 1, y = 3$, then $(x, y) = (1, 3)$. We can plot this on a graph by traveling 1 unit to the right, then 3 units up, like this:

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
# matplotlib-specific customizations
%matplotlib inline
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["axes.grid"] = True
```

```{code-cell} ipython3
plt.plot(1, 3, "ro")
plt.title("The point $(1, 3)$")
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.show()
```

## Functions


Functions take in a number and output another number. We denote a function with a symbol with the input as another symbol - for instance, a function $f$ with the input $x$ is written as $f(x)$. A simple function could be:


$$
f(x) = 2x
$$


This means that any input $x$ value would have an output value of twice that $x$ value. We can make a table for values of this function:


| $x$ (input) | $f(x)$ (output) |
|-----|-----|
| 0 | 0 |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |


We can visualize this table of values by plotting it as $(x, y)$ pairs, where $y = f(x)$:

```{code-cell} ipython3
x = np.linspace(0, 5)
plt.plot(x, 2 * x)
plt.title("$f(x) = 2x$")
plt.show()
```

Since we plot the value of $f(x)$ on the y-axis, we say that $y = f(x)$. This means we could've called the above function $f(x) = 2x$, or $y = 2x$ - it doesn't really matter.


### Polynomial functions


Linear functions are in the form $f(x) = ax + b$, such as $f(x) = 5x$, where $a$ and $b$ can be equal to zero. They are called linear because they are "line-like" - they are straight lines. We've already seen this.


Quadratic functions are in the form $f(x) = ax^2 + bx + c$, such as $f(x) = x^2 + 2x + 3$, where $b$ and $c$ can be equal to 0. They look like this:

```{code-cell} ipython3
x = np.linspace(-5, 5)
plt.plot(x, x ** 2)
plt.title("$f(x) = x^2$")
plt.show()
```

We can solve any quadratic function in the form $ax^2 + bx + c = 0$ using the quadratic formula:


$$
x = \frac{-b + \sqrt{b^2 - 4ac}}{2a} \text{ and } x = \frac{b + \sqrt{b^2 - 4ac}}{2a}
$$


Cubic functions are similar, but they are just in the form $f(x) = ax^3 + bx^2 + cx + d$, such as $f(x) = 3x^3 + 5x^2 + 4x + 6$. They look like this:

```{code-cell} ipython3
x = np.linspace(-5, 5)
plt.plot(x, x ** 3 + 3 * x ** 2)
plt.title("$f(x) = x^3 + 3x^2$")
plt.show()
```

The absolute value function $f(x) = |x|$ takes in any negative or positive value and returns a positive value. It looks like this:

```{code-cell} ipython3
x = np.linspace(-5, 5)
plt.plot(x, np.abs(x))
plt.title("$f(x) = |x|$")
plt.show()
```

### Rational functions


The rational function is in the form $f(x) = \frac{1}{x}$. It looks like this:

```{code-cell} ipython3
def f(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return 1/x
fx_name = r'$f(x)=\frac{1}{x}$'

x=np.linspace(-10,10,101)
y=f(x)
plt.plot(x, y, label=fx_name)
plt.legend(loc='upper left')
plt.show()
```

## Trigonometry


## Angles


An **angle** is the space between two lines that meet. We often represent angles using the symbol $\theta$, pronounced "theta".


There are 2 main measurement systems we can use to define angles. The first measurement system is called degrees, denoted with the degree symbol $^\circ$, where you can think of $360^\circ$ as one full circle. Thus, one angle of 1 degree is like slicing a circle into 360 pieces, and just taking one of those pieces.

The second measurement system is called radians, where one full circle is $2\pi$. This is a bit more abstract to understand, but you can use the same way to imagine: imagine taking a circle and cutting it into $2\pi$ (that's around 6.283) pieces. What? Who would _ever_ cut a circle into 6.283 pieces? Yes, it doesn't make a lot of sense, but if you just think of one of those pieces, you would have an angle of 1 radian. We can convert between degrees and radians with:


$$
\begin{align}
1 \mathrm{\ radian} &= 1^\circ \cdot \left(\frac{\pi}{180}\right) \\
1^\circ &= 1 \mathrm{\ radian} \cdot \left(\frac{\pi}{180}\right)
\end{align}
$$


### Right-angled triangles


Trigonometry is the study of **right-angled triangles** - triangles that have one right angle and one other angle $\theta$.


The longest side of a right-angled triangle is called the **hypotenuse**. The **opposite** side is the the side that, well, is _opposite_ the angle $\theta$. Finally, the **adjacent** side is the side between the right angle and the angle $\theta$.

```{figure} https://www.onlinemathlearning.com/image-files/trigonometry-hypotenuse-opposite-adjacent.png
:alt: Right angled triangles diagram
:width: 300
```


But wait, doesn't a triangle have three angles? Yes, that is true, and so the choice of which angle you call $\theta$ doesn't matter. You can define either one of the two other angles (the non-right-angle angles) as your $\theta$ angle, you just have to stick with one angle in your calculations.


Every right-angled triangle obeys the rule that:


$$
\text{Adjacent}^2 + \text{Opposite}^2 = \text{Hypotenuse}^2
$$


### Trigonometric functions


Trigonometric functions are oscillating functions that form a constant repeating pattern. The main, sine ($\sin$), cosine ($\cos$), and tangent ($\tan$), are defined by:


$$
\begin{align}
\sin \theta &= \frac{\mathrm{opposite}}{\mathrm{adjacent}} \\
\cos \theta &= \frac{\mathrm{adjacent}}{\mathrm{hypotenuse}} \\
\tan \theta &= \frac{\mathrm{opposite}}{\mathrm{hypotenuse}} = \frac{\sin \theta}{\cos \theta}
\end{align}
$$


The _reciprocal trigonometric functions_ are the normal trig functions but "flipped over", and they look like this:


$$
\begin{align}
\csc \theta = \frac{1}{\sin} \\
\sec \theta = \frac{1}{\cos} \\
\cot \theta = \frac{1}{\tan}
\end{align}
$$


You can imagine taking a right-angled triangle and slowly making its angle $\theta$ bigger and bigger and bigger. The ratio between the sides is the value of the trigonometric functions.


The graph of $f(\theta) = \sin(\theta)$, where $\theta$ is in units of radians, looks like this:

```{code-cell} ipython3
from matplotlib.ticker import FuncFormatter, MultipleLocator
```

```{code-cell} ipython3
f, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi)
ax.plot(x, np.sin(x))
ax.set_ylim(-1, 1)
ax.grid(True)
ax.set_title(r"$f(x) = \sin(x)$")
ax.xaxis.set_major_formatter(FuncFormatter(
   lambda val, pos: f"{val/np.pi:.0g}" + r"$\pi$" if val !=0 else '0'
))
ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))

plt.show()
```

The values of $f(x) = \sin(x)$ can be deduced by reading off the graph:


$$
\begin{align}
\sin(0) &= 0
\sin(\pi / 2) &= \sin (3\pi / 2) = 1
\sin(\pi) &= \sin(2\pi) = 0
\end{align}
$$


Where $\pi \approx 3.14159$.


The graph of $f(x) = \cos x$ looks like the a shifted sine graph:

```{code-cell} ipython3
f, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi)
ax.plot(x, np.cos(x))
ax.set_ylim(-1, 1)
ax.grid(True)
ax.set_title(r"$f(x) = \cos(x)$")
ax.xaxis.set_major_formatter(FuncFormatter(
   lambda val, pos: f'{val/np.pi:.0g}' + r"$\pi$" if val !=0 else '0'
))
ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))

plt.show()
```

Whereas the graph of $f(x) = \tan x$ looks a little different:

```{code-cell} ipython3
def f_tan(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.tan(x)

f, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x) / np.cos(x)
tol = 100
y[y > tol] = np.nan
y[y < -tol] = np.nan
ax.plot(x, y)
ax.grid(True)
ax.set_ylim(-10, 10)
ax.set_title(r"$f(x) = \tan(x)$")
ax.xaxis.set_major_formatter(FuncFormatter(
   lambda val, pos: f'{val/np.pi:.0g}' + r"$\pi$" if val !=0 else '0'
))
ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))

plt.show()
```

## Radicals


If we know a number, say, 4, can we find two equal numbers that multiply to form that number? Actually, we can! In the case of 4, we know that:


$$
4 = 2 \times 2
$$


So we can say that the "square root" of 4 is 2, and we use the $\sqrt{}$ symbol to show this:


$$
\sqrt{4} = 2
$$


We can expand this idea. If we knew a number, say 8, can we find three equal numbers that multiply to form that number? Yes, we can! In the case of 8, we know that:


$$
8 = 2 \times 2 \times 2
$$


So we can say that the "cube root" of 8 is 2, and we use the $\sqrt[3]{}$ symbol to show this:


$$
\sqrt[3]{8} = 2
$$


The same goes for 4 equal numbers that multiply to form a number, 5, 6, and so on. These roots, from the square root and cube root to that 4th and 5th and 6th root, are called **radicals**. Radicals follow these rules:


$$
\begin{align}
\sqrt{1} &= 1 \\
\sqrt{0} &= 0 \\
\sqrt{a} \times \sqrt{a} &= a \\
\sqrt{ab} &= \sqrt{a} \times \sqrt{b}
\end{align}
$$


## Exponentials and Logarithms


### The rules of exponents


Exponents are every time we multiply one number by itself a certain number of times. For example, $2^2$, pronounced "2 squared" or "2 to the power of 2" is two multiplied by itself, two times - that is $2 \times 2$. $2^3$, pronounced "2 cubed" or "2 to the power of 3" is two multiplied by itself, three times - that is $2 \times 2 \times 2$. Exponents follow these rules:


$$
\begin{align}
1^a &= 1 \\
0^a &= 0 \\
a^0 &= 1 \\
a^1 &= a \\
a^m + a^n &= a^{(m + n)} \\
a^m / a^n &= a^{(m - n)} \\
(a^b)^c &= a^{(b \times c)}
\end{align}
$$


Fractional exponents are the same as a radical:


$$
\begin{align}
a^{\frac{1}{2}} &= \sqrt{a} \\
a^{\frac{1}{3}} &= \sqrt[3]{a}
\end{align}
$$


Finally, negative exponents are equal to one over the positive exponent of that number:


$$
a^{-n} = \frac{1}{a^n}
$$


### Exponential and logarithmic functions


All exponential functions are in the form $f(x) = b^x$ where $b > 0$ and $b \neq 1$. Note that if $x$ is negative, then $b^{-x} = \left(\frac{1}{b}\right)^x$. The most commonly-used exponential function is $f(x) = e^x$, also confusingly called "the exponential function", where $e$ is a special number that is around 2.718:

```{code-cell} ipython3
x = np.linspace(-5, 5)
plt.grid(True)
plt.plot(x, np.exp(x))
plt.title(r"$f(x) = e^x$")
plt.show()
```

What if we want to "undo" the exponential function? We would need to find an **inverse function**, a function that does the opposite thing as another function. In the case of an exponential function, the inverse is called a **logarithmic function**. The basic logarithmic function is given by:


$$
y = \log_b x
$$


where $b^y = x$. To remember this mapping between exponential functions, you can remember that $b$ is the "basement" (because of its subscript), and it's raised to the "answer" of $y$ to get $x$. Several common logarithmic functions have shorthand notations:


$$
\begin{align}
\ln x &= \log_e x
\log x &= \log_{10} x
\end{align}
$$


The $\ln$ function is also called the "natural logarithm", and it looks like this:

```{code-cell} ipython3
x = np.linspace(0.01, 5)
plt.grid(True)
plt.plot(x, np.log(x))
plt.title(r"$f(x) = \ln x$")
plt.show()
```

Just as with exponents, logarithms follow certain rules:


$$
\begin{align}
\log_b (xy) &= \log_b x + \log_b y \\
\log_b (x^n) &= n \log_b x \\
\log_b \left(\frac{x}{y}\right) &= \log_b x - \log_b y \\
\log_b x &= \frac{\ln x}{\ln b}
\end{align}
$$

```{important}
Be careful! Note that $(\log_b x)^r \neq r \log_b x$!!!
```

## Factorials


A factorial is when you multiply a number by all whole numbers smaller than it, and is denoted with $!$. For example, $2! = 2 \times 1$, $3! = 3 \times 2 \times 1$, and $4! = 4 \times 3 \times 2 \times 1$.


## Sums


Sometimes, we want to add up a lot of numbers:


$$
1 + 2 + 3 + 4 + 5 + 6 + 7 + \dots
$$


How do we compactly write this out? One way is to assign each number a symbol, with its position in the list of numbers to add as an index on the bottom. So 1, which is the first number, would be $a_1$. This becomes:


$$
a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7 + \dots
$$


A compact way of writing this out is with the **summation symbol**:


$$
\sum_{i = 1}^n a_i = a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7
$$


where $i$ is the index on the bottom, $i = 1$ means the indices start from 1, and $n$ means the indices end at $n$. $n$ can be infinity sometimes:


$$
\sum_{i = 1}^\infty a_i = a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7 + \dots
$$


Summation is very useful for shortening long formulas. For example, the **binomial expansion formula**:


$$
(a + b)^n = \sum_{i = 0}^n \frac{n!}{(n - i)! i!} a^{n - i} b^i
$$