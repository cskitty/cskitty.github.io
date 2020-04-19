---
title: "Python for Beginner Lesson 1: Variables and Print"
date: 2020-04-18
categories:
  - Projects
  - Tutorials
tags:
  - Python
  - Beginner
---

# Python for Beginner Lesson 1: Variables and Print

## Numbers
Numbers in Python work like what you've learned from your math class including but not limit to counting numbers, negative numbers, decimals so on and so force.

To show you what I mean, type a few more numbers into the console below, pressing return after each one. You can also use operators.
For example, try type
<<<<<<< HEAD
11 * 11 below.
=======
$$11\cdot11$$ below.
>>>>>>> a902a4c50bb1ec2148cf394946506560559e71ab

<iframe src="https://trinket.io/embed/console/8c94ebd6bf" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Variables

### Integer

* int - integers: ..., -3, -2, -1, 0, 1, 2, 3, ...

While in other languages (C, java), there's limitation on the size of Integers. In Python, there is no limit to how long an integer value can be. It is only constrained by the amount of memory your system has. 111, 222, -232301231231 are examples of integers in Python.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
x=5
y=-3
print(x)
print(y)
print(x+y)
```

### String

* str - character strings, text: "hello world!", "CS50", 'python', 'bunnies are awesome'

Strings are sequences of character data. The string type in Python is called str.
String literals may be delimited using either single or double quotes. All the characters between the opening delimiter and matching closing delimiter are part of the string: "hello word" or 'hello world'.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
x = "Hello Word!"
print(x)

y = "I love "
z = "Python!"
print(y + z)
```

### Float (decimals)

* float - floating point numbers, decimal point fractions: -3.14, 1.2, 1e-8, 3.2e5

The float type in Python designates a decimal number. float values are specified with a decimal point. Scientific notation can be used here.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
pi = 3.14159
print(x)
print(2*pi)
```

### Boolean

* bool - boolean values: True and False

Boolean value in Python may have one of two values, True or False.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
i_love_python = True
python_loves_me = False
print(i_love_python)
print(python_loves_me)
```

##  Operators

### Arithmetic operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.

| OPERATOR        | DESCRIPTION           | SYNTAX  |
| -------------   | ---------------------| -----|
| +               | Addition: adds two operands | x + y |
| -               | Subtraction: subtracts two operands | x - y |
| *               | Multiplication: multiplies two operands | x * y |
| /               |Division (float): divides the first operand by the second | x / y |
| //              | Division (floor): divides the first operand by the second | x // y |
| %               | Modulus: returns the remainder when first operand is divided by the second | x % y |


### Relational operators

 Relational operators compares the values. It either returns True or False according to the condition.

| OPERATOR        | DESCRIPTION           | SYNTAX  |
| -------------   | ---------------------| -----|
| >               | Greater than: True if left operand is greater than the right | x > y |
| <               | Less than: True if left operand is less than the right | x < y |
| ==              | Equal to: True if both operands are equal | x == y |
| !=              | Not equal to - True if operands are not equal | x != y |
| >=              | Greater than or equal to: True if left operand is greater than or equal to the right | x >= y |
| <-              | Less than or equal to: True if left operand is less than or equal to the right | x <= y |

### Logical operators

Logical operators perform Logical AND, Logical OR and Logical NOT operations.

| OPERATOR        | DESCRIPTION           | SYNTAX  |
| -------------   | ---------------------| -----|
| and             | Logical AND: True if both the operands are true | x and y |
| or              | Logical OR: True if either of the operands is true | x or y |
| not             | Logical NOT: True if operand is false | not x |


Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
i = 10
j = 9
print(i == j)
print(i > 9)
print(i < j)
print(i * j)
print(i * j * j)
```

##  Conversions

In Python, we can use the build in functions int(), float(), and str() to convert between types.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
x = "5"
print(x, type(x))
x = int("5")
print(x, type(x))
pi = float("3.141")
print(pi, type(pi))
print(str(4))

apples = "I have" + str(2) + "apple"
print(apples)
```

## The print() function

Type print("Hello World") in the above console and see what happens.
Try another example print('foo\tbar').
