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

# Programming with Python

> "Science is what we understand well enough to explain to a computer; art is everything else."
> 
> **Donald Knuth**

Having gone through an extensive amount of math and physics, we now arrive at the last topic in Chapter 1: scientific programming with the Python programming language. While programming is not a _required_ skill to do research for Project Elara, it is a very _useful_ skill, and in general, knowledge of programming is tremendously helpful for solving many problems in math and physics.

## The theory of programming

In this section, we will be discussing programming using the **Python programming language**. A programming language is like an instructions sheet for a computer; a computer reads code written in a programming language, and runs according to the code's instructions. For instance, the following code in Python results in a message being shown ("printed") by the computer:

```{code-cell} ipython3
print("Hi!")
```

By nature, computers are not very smart; they can do arithmetic, read electronic data, and write electronic data, and that's about it. The exact process of "reading" and "writing" data is a bit more sophisticated - for instance, they can read data from a computer mouse that outputs electrical signals when it is moved, or write data to a hard drive (we call this a _filesystem_), or send data into a monitor that translates electrical signals into pixels on a screen. But computers fundamentally do not know what to _do_. The job of programming is for a person to write code that the computer can execute to _do things_, which is what allows computers to perform incredibly complex tasks, incredibly quickly.

Now, code is a broad category for a lot of things that share the common property of storing some form of information. Computer code, also called _source code_, is a specific type of code that can be understood by a computer (there is more nuance, but this is a place to start). Computer code is in many ways similar to mathematical notation; it is made of words and symbols that are arranged in a special way, designed to be human-readable, but following strict rules that encode meaning. 

Computer code has different varieties; each of these is called a _programming language_. There are general-purpose programming languages and domain-specific programming languages; there are very old programming languages (some are more than 50 years old!) and very new programming languages; there are programming languages that are simpler to use, and programming languages that are _much_ harder to use.

The Python programming language that we'll use is one of the **two main** programming languages used by Project Elara. It is designed for simplicity and user-friendliness, and is very popular and used by scientists worldwide. For this reason, Python is a _very_ good language to start programming in. We will now introduce the basics of programming in Python.

```{note}
Have experience in Python, but want a refresher? We recommend reading the [Learn X in Y minutes guide to Python](https://learnxinyminutes.com/python) to review how to write and use Python.
```

## Using Python

There are two ways to be able to use Python: either by installing its specialized software tools from <https://www.python.org/>, which can take quite a bit of time and troubleshooting, or by using an _online code sandbox_ such as [Python Sandbox](https://pythonsandbox.com/). We _highly_ recommend using an online code sandbox to avoid the difficulties of setting up a computer for Python, which is an infamously error-prone process.

If you do choose to install Python on your computer instead of using the online sandbox option, the Python programming language requires that you write code in files with the extension `.py`, which can then be run using the specialized `python yourcode.py` command (replace `yourcode.py` with the actual filename of your code file) in your operating system's terminal (Powershell for Windows, the Terminal app on Macs, your personal terminal on Linux). There are other ways to work with Python on your computer that we will cover later. Again, running Python on your computer is _not recommended_ if you are just starting out and don't have experience with Python.

## Variables and data types

The fundamental building blocks of any programming language, including Python, are _variables_ and _data types_. In Python, variables are names you assign to a value. For instance, we may write:

```{code-cell} ipython3
myvariable = 42
```

We have now created a variable called `myvariable` whose value is the number 42. Variables can be modified (by assigning another value to them), and can be used later in your code wherever you'd like:

```{code-cell} ipython3
# note: the hashtag (#) starts a comment, meaning that
# anything after a hashtag on the same line is not
# considered code and not run by the computer

myvariable = 35 # modify variable
newvariable = 3 # create new variable
myvariable + newvariable # use variable
```

Variables can store different types of data. We can give them descriptive names, like `number_one = 1` or `pi = 3.14159`. In Python, the most common basic types of data are strings, integers, floats, and booleans. We describe each of these below:

| Data type     | What it's for                                               | Example usage                                                                                      |
| ------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| String        | Anything involving characters, words, or text               | `mystringvariable = "Hiii"`                                                                        |
| Integer (int) | Any whole number (positive or negative)                     | `myintvariable = 20`                                                                               |
| Floats        | Any decimal number (we call these _floating-point numbers_) | `myfloatvariable = 1.414`                                                                          |
| Booleans      | A value that is either true or false                        | `is_sunny = True` or `is_rainy = False`, both `True` and `False` **must be capitalized** in Python |

We can also perform _operations_ on variables. For instance, we can do arithmetic on variables:

```{code-cell} ipython3
my_number = 3
my_number = my_number * 5
my_number = my_number - 1
my_number += 30 # this is shorthand for my_number = my_number + 30
my_number -= 12 # this is shorthand for my_number = my_number - 12
divisor = 5
my_number = my_number / divisor
my_number *= 15 # this is shorthand for my_number = my_number * 15
my_number += my_number ** 2 # here ** raises a number to a power
my_number
```

For certain types of variables, we can also _compare_ between two variables:

```{code-cell} ipython3
a = True
b = False
# Check if a is same as b
a == b
```

```{code-cell} ipython3
# Check if a is NOT same as b
a != b
```

```{code-cell} ipython3
# "is" and "not" can also be used for comparisons

# Check if a is true
a is True
```

```{code-cell} ipython3
# Check if a is not true
a is not True
```

```{code-cell} ipython3
# Check a is false
a is False
```

We can also use the `>` (greater than), `<` (less than), `>=` (greater or equal to), `<=` (less or equal to) operations:

```{code-cell} ipython3
num_one = 5
num_two = 3
# Check if 5 is greater than 3
num_one > num_two
```

```{code-cell} ipython3
# Check if 5 is less than 3
num_one < num_two
```

```{code-cell} ipython3
# Check if 5 is less than or equal to 3
num_one <= num_two
```

## Functions

We often want to be able to repeat certain lines of code at different places in our code. We can use _functions_ to do this. Functions contain a block of code that can be _called_ (run) at some later point. In Python, functions are written with the `def` special keyword, the function name followed by `():`, and then an _indented block_ containing the code, like this:

```{code-cell} ipython3
# create a function named perform_one_plus_one
def perform_one_plus_one():
	print(1 + 1)

# call (run) the function
perform_one_plus_one()
```

```{note}
Indentation is very important in Python! Consistency in indentation - that is, indenting by the same amount for code in the same block - makes sure that your code is valid Python code and can be run properly. 
```

Putting a `return` keyword inside the function allows us to be able to save the output of a function to a variable, like this:

```{code-cell} ipython3
# create a function called ten_add_one
# that outputs one added to 10
def ten_add_one():
	return 1 + 10

# run the function and save its
# output to a variable
my_function_output = ten_add_one()
my_function_output
```

We can also specify _arguments_ to a function, which allow it to take one or more variables as inputs:

```{code-cell} ipython3
# create a function called add_numbers
# that adds two numbers and returns 
# (outputs) the results
def add_numbers(a, b):
	return a + b

number_1 = 5
number_2 = 8
# save output of function to variable
sum = add_numbers(number_1, number_2)
sum
```

Python (unlike some other programming languages) also allows defining _default arguments_, where one of a function's arguments can be omitted, and the function will substitute in the pre-set default value instead:

```{code-cell} ipython3
# create a function called circle_area
# that takes in an argument (the radius
# of the circle) and has a default argument 
# for the circle constant pi
def circle_area(radius, pi=3.1415):
	return pi * radius ** 2
```

```{code-cell} ipython3
my_circle_area = circle_area(5)
print("Circle area with default argument for pi:")
print(my_circle_area)
```

```{code-cell} ipython3
# let's now compute the area using a more precise
# value of pi. Although not required, we set the
# variable name in uppercase to show it's a constant
PRECISE_PI = 3.14159265358979

alternative_circle_area = circle_area(5, pi=PRECISE_PI)
print("Circle area with specified value for pi:")
print(alternative_circle_area)
```

Lastly, we should mention that Python has a number of _built-in_ functions. Some of these allow inter-conversion of data types - for instance, `str(yourvar)` converts a variable to a string, `int(yourvar)` converts a variable to an integer, `float(yourvar)` converts a variable to a float, and `bool(yourvar)` converts a variable to a boolean (substitute `yourvar` with the variable to convert). Others allow for basic input-output, such as the `print()` function we've already seen. We will introduce a number of other built-in functions later.

## Control flow

Now that we know how to create, use, and modify variables, as well as creating functions to run a block of code wherever we want it, we can cover the last important component of a programming language: **control flow**.

Control flow allows us to control the order in which our code is executed. For instance, we can choose to run or skip a block of code based on a condition. This is called a _conditional_, and the first type of conditional we will examine is an _if-statement_.

An **if-statement** in Python is comprised of the `if` keyword, followed by a condition (remember the boolean and comparison operations), followed by an indented block of code to run _if_ the condition is true, as shown below:

```{code-cell} ipython3
my_number = 5

# Run our block of code ONLY if the condition
# `my_number > 3` is true

if my_number > 3:
	print("My number is greater than 3!")
```

We can also use the `not` keyword in if-statements, allowing us to express a block of code to run _if_ the condition is false, as shown:

```{code-cell} ipython3
sunny_today = False

# Run our block of code ONLY if the boolean
# variable `sunny_today` is NOT true

if not sunny_today:
	print("Today isn't a sunny day.")
```

We can add an _else_ block after an if-statement to immediately run a block of code if the condition in the if-statement is not satisfied, like this:

```{code-cell} ipython3
sky = "Blue"

if sky == "Purple":
	print("Sky is purple!")
else:
	print("The color of the sky is:")
	print(sky)
```

We often to run another if-statement following an else-statement. We _could_ write this by nesting (placing) our second if-statement in our first if-statement, like this:

```{code-cell} ipython3
name = "John"

if name == "David":
	print("Name is David")
else:
	if name == "John":
		print("Name is John")
```

But if we have multiple if-statements to run after, this becomes very tedious to write and hard to read. Instead, Python offers an `elif` key word (short for "else if"), that simplifies the above code to:

```{code-cell} ipython3
name = "John"

if name == "David":
	print("Name is David")
elif name == "John":
	# runs code if the name is not David
	# and the name is also John
	print("Name is John")
```

Python also allows us to re-execute a line of code multiple times - these are called _loops_. The first type of loop is called a **while loop**. While loops are formed with a `while` keyword, followed by some condition, and then an indented block of code, like this:

```{code-cell} ipython3
x = 1
while x < 3:
	# code in this block is re-run
	# as long as x is less than 3
	print("X is", x)
	x += 1
	print("Added one to x, continuing to loop...")

print("Loop finished")
```

The block of code within the while loop repeats as long as the condition is satisfied, but once the condition is _no longer satisfied_, the while loop exits. In our previous example, our condition was that $x < 3$, and so long as this was true, the code block within the while loop repeats. But we add 1 to $x$ on every loop - that's what `x += 1` does - and so after running twice, the value of $x$ is 3. This means that $x < 3$ is _no longer true_, and so the loop is ended, and we say we have _exited_ the loop.

While loops are good for certain tasks, but they have one major issue - you must carefully keep track of the condition to make sure that the loop _actually_ exits. It is easy to accidentally write a loop that never exits (that is, until either your operating system force-shutdowns your running Python or you get a computer crash). Here is an example:

```python
while True:
	print("Looping forever...")
```

Do _not_ actually try to run this code for the reasons just mentioned! But since `True` is always true, this while loop never exits, and runs forever. This makes while-loops a potential source of issues, so there is another type of loop that is often used instead. This is the **for-loop**.

Instead of exiting only on a certain condition, a for-loop _iterates_ (loops) through a finite number of items, which means that unless if you do something really really hacky, for-loops always exit and won't run forever. A for-loop can take several different forms, and we will show the most common of them here. The first is iterating across a range of numbers. The for loop starts with the `for` keyword, then defines a variable to hold the current number in the range, then defines the range, and finally, there is an indented code block that runs on every iteration. We show this below:

```{code-cell} ipython3
# We run a block of code once
# for every number less than 10,
# starting from 0 (i.e. all numbers
# between 0 and 9)

for number in range(10):
	# the `number` variable holds the
	# current number
	print("Current number is", number)
	# the for loop runs for every number
	# until 9
```

There are other types of for-loops that we will cover shortly, once we reach the next section.

## Objects, lists, and dicts

By this point, we have covered the most basic Python functionalities. These functionalities - variables, arithmetical and logical operations, functions, and control flow - are not unique to Python; almost every programming language has them, and a programming language is basically _required_ to have them in order to be considered a programming language (this is called _Turing completeness_, although that is a far more vast topic). But Python extends these functionalities with an extensive _standard library_ that provides more features.

To understand the Python standard library, let's first discuss what a _software library_ is. A software library is a collection of software code that can be used by other code to provide additional functionality. Python's standard library is an example of a software library, with the special property that it is _distributed with_ the Python language tools when you install it - that's why we call it a _standard_ library. Other libraries are typically downloaded, and we call these libraries _extenal libraries_.

Python's standard library includes more complex data-types called _objects_ (this is technically an oversimplification but will do for now). Objects are data-types that have properties and have their own specialized functions, which we call _methods_. Among the two most common objects in Python are lists and dictionaries.

Lists are Python's way to, unsurprisingly, make sense of a group of things. For instance, we can make a list of numbers, or a list of integers:

```{code-cell}
ls1 = [1, 2, 3, 4, 5] # our first list
ls2 = ["a", "b", "c", "d", "e"] # our second list
```

You can put any data type you want in a list:

```{code-cell}
ls3 = [1, "a", 2, "b", 3, 3.78592, True, False]
```

You can put lists inside of lists:

```{code-cell}
ls4 = [[5, 7, 9], ["a", "b", "c"], [3, "vedant", True]]
```

We can put variables inside lists as well:

```{code-cell}
ls5 = [ls1, ls2, ls3, ls4]
```

To find the size of a list, we use `len()`:

```{code-cell}
len(ls1)
```

To access the elements of the list, we use bracket syntax. However, note that in Python, we start counting from zero, so the first element is index 0:

```{code-cell}
print(ls1)
print("First element:", ls1[0])
```

Similarly, the second element is index 1, the fifth element is index 4, and the 100th element is index 99:

```{code-cell}
print(ls2)
print("Second element:", ls2[1])
```

We can also count backwards, in which case the last element is index -1:

```{code-cell}
print(ls1)
print("Last element:", ls1[-1])
```

```{code-cell}
print(ls3)
print(ls3[-1])
```

The usefulness of a list is that we can store a collection of different pieces of information together, and operate on them all simultaneously. This is where **iterators** come in - they allow us to apply an operation on every element in a list. One type of iterator is our familiar **for-loop**, and now we will see how it is perfectly suited to working with lists.

For instance, suppose we wanted to increase every element in a list by one. We could always do this:

```{code-cell}
numbers_ls = [1, 25, 389, 1578, 12903]

numbers_ls[0] += 1
numbers_ls[1] += 1
numbers_ls[2] += 1
numbers_ls[3] += 1
numbers_ls[4] += 1

print(numbers_ls)
```

But for any longer example, it would be exhausting to write every single case. Instead, we could write a **for loop**:

```{code-cell}
numbers_ls = [1, 25, 389, 1578, 12903]

for i in range(len(numbers_ls)):
    numbers_ls[i] += 1

print(numbers_ls)
```

Let's take a closer look at this for-loop. In that loop, `range(len(numbers_ls))` returns 5, which tells us we're going to repeat the for loop's operation 5 times. Each time, we have a variable `i` - the first time, `i` will be equal to 0 (remember Python counts from 0), the second time, `i` will be equal to 1, the third, `i` will be equal to 2, and so on, until `i` is equal to 4.

Our operation then takes the ith element of the list and adds one to itself. For example, if `i = 0`, then we're really doing `numbers_ls[0] += 1`; if `i = 1`, then we're doing `numbers_ls[1] += 1`; and so on and so forth.

What if we just wanted to print out all the elements of our list? We could write that with a for-loop as well:

```{code-cell}
# here we don't have to use range()
# just the list itself
for number in numbers_ls:
	print(number)
```

Aside from iterating over lists with for loops, Python has some standard defined functions for lists. For example, we can add to a list:

```{code-cell}
numbers_ls2 = [4, 5, 6, 7]
numbers_ls2.append(8)
numbers_ls2
```

We can remove elements from a list:

```{code-cell}
numbers_ls2_clone = numbers_ls2.copy() # make a copy of a list
numbers_ls2_clone.pop() # remove last element
numbers_ls2_clone.pop(1) # remove element at index 1
numbers_ls2_clone
```

And most usefully, we can slice a list. A slice of a list `[a:b]` returns a list **starting** from index a and **ending before** index b:

```{code-cell}
numbers_ls2 = [4, 5, 6, 7, 8]

# Slice with n: returns list STARTING from index n
numbers_ls2[2:]
# [6, 7, 8]
numbers_ls2[3:]
# [7]

# Slice with :n returns list ENDING before index n
numbers_ls2[:2]
# [4, 5]

# Double slice returns list STARTING from
# index n and ENDING before index n
numbers_ls2[1:3]
# original: [4, | 5, 6, | 7,]
# sliced: [5, 6]
```

Finally, we can use `index()` to find the index of an element within a list:

```{code-cell}
fruits = ["apples", "oranges", "pears"]
fruits.index("apples") # returns index 0
```

After lists, we have tuples, which are like lists, but unmodifiable, meaning that you **cannot** change elements within a tuple. We write tuples using rounded brackets:

```{code-cell}
tup1 = (1, 2, 3, 4)
# So this doesn't work:
# tup1.pop()
```

We can find the number of elements in a tuple in the same way as a list:

```{code-cell}
len(tup1)
```

We can't change tuples but we can slice them and save the result to a **new** tuple:

```{code-cell}
tup2 = tup1[1:-1]
print("original:", tup1)
print("sliced:", tup2)
```

We can unpack tuples (this works for lists as well):

```{code-cell}
coords = (3.5, -8.0, 10.3)
x, y, z = coords
print(x)
```

Finally, the last of the commonly-used collection types is the dictionary. Dictionaries are used to store **structured** data. In more technical terms, they map keys (entries) to values (definition of each entry).

We make a dictionary by entering keys with their corresponding values. Note keys for dictionaries have to be fixed-memory types (for technical reasons). Fixed-memory types include ints, floats, strings, and tuples. In the below example, we create a dictionary with two keys, `name` and `age`:

```{code-cell}
our_ages_dict = { "name": "John", "age": 30 }
# we can add a key-value pair like this:
our_ages_dict["nationality"] = "United States"

print(our_ages_dict)
```

We access dictionary values with `[]` where the key is inside the brackets:

```{code-cell}
our_ages_dict["name"]
```

The other way to get a key is to use the `get()` function:

```{code-cell}
our_ages_dict.get("name")
```

If you try to find an invalid key, it will return `None`:

```{code-cell}
# the only keys are "name", "age", and "nationality",
# and "home" is not one of them
our_ages_dict.get("home")
```

To get all the keys, use the `keys()` function, which will return the keys as a list:

```{code-cell}
list(our_ages_dict.keys())
```

Use the `values()` function to do the same thing with the values:

```{code-cell}
list(our_ages_dict.values())
```

We can use "in" to check if a key is in a dict:

```{code-cell}
"name" in our_ages_dict
```

## Using external libraries

While the abilities of Python with just its standard library are already extensive, the real power of Python is its ease of using _external_ libraries. There exists a Python library for almost anything, and you can browse through them on https://pypi.org/, the official site for Python libraries. Many Python libraries are so extensively used that they have become industry-standard and you will rarely find a research publication that involve some sort of computational science that _don't_ use them. 

At Elara, we make extensive use of Python and its libraries. We will cover the scientific computing libraries used in Project Elara in the next chapter, as well as more advanced programming techniques such as object-oriented programming, list comprehensions, lambda functions, decorators, and vectorized operations. But a working knowledge of Python programming is already enough to get you far.