---
title: "Introduction to Python Lesson 1: Variables and Print"
categories:
  - Projects
  - Tutorials
tags:
  - Python
---

# Introduction to Python Lesson 1: Variables and Print
{% include video id="AEY_B1MSGTw" provider="youtube" %}

If you’ve gone to search up the word “Python”, chances are, you get a definition like this:
py·thon ˈpīˌTHän,ˈpīTHən/
noun
a large heavy-bodied nonvenomous constrictor snake occurring throughout the Old World tropics.
 But that’s not the only thing it says, and that’s not what we mean. If you continue reading, the second definition should pop up:
2. a high-level general-purpose programming language.
 That’s the one we’re talking about. Python is a programming language, one of the easier ones too. So let’s start with some basics.

{% highlight python linenos %}
print("Hello Python!")
{%endhighlight%}
## Numbers
Numbers in Python work like what you've learned from your math class including but not limit to counting numbers, negative numbers, decimals so on and so force.

To show you what I mean, type a few more numbers into the console below, pressing return after each one. You can also use operators.

  For example, try type 11 * 11 below.

<iframe src="https://trinket.io/embed/console/8c94ebd6bf" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Variables

### Integer

* int - integers: ..., -3, -2, -1, 0, 1, 2, 3, ...

While in other languages (C, java), there's limitation on the size of Integers. In Python, there is no limit to how long an integer value can be. It is only constrained by the amount of memory your system has. 111, 222, -232301231231 are examples of integers in Python.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
x=5
y=-3
print(x)
print(y)
print(x+y)
{% endhighlight %}

### String

* str - character strings, text: "hello world!", "CS50", 'python', 'bunnies are awesome'

Strings are sequences of character data. The string type in Python is called str.
String literals may be delimited using either single or double quotes. All the characters between the opening delimiter and matching closing delimiter are part of the string: "hello word" or 'hello world'.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
x = "Hello Word!"
print(x)

y = "I love "
z = "Python!"
print(y + z)
{% endhighlight %}

String is one of the six build-in sequence data type in Python. Each element of a sequence data type is assigned a position number or index. The first index is zero, the second index is one, and so forth.  In addition to string type, the others most common ones are lists and tuples, which we would see in next tutorial.

There are certain things you can do with all sequence types. These operations include indexing, slicing, adding, and checking for existence. In addition, Python has built-in functions for finding the length of a sequence and for finding its largest and smallest elements.


| Operation       | Result               | Example  |
| -------------   | ---------------------| -----|
| x in s          | True if an item of s is equal to x, else False | 'e' in "help" is True  |
| s + t           |	the concatenation of s and t |  'Good '+'Morning' is 'Good Morning' |
| s[i]            | i'th item of s, origin 0 | 'help'[3] is 'p'  |  
| s[i:j]          | slice of s from i to j |  'help'[1:3] is 'el' |  
| len(s)          | length of s | len(help) is 4  |  
| min(s)          | smallest item of s | min('help') is 'e'  |  
| max(s)          | largest item of s |  max('help') is 'h' |  



### Float (decimals)

* float - floating point numbers, decimal point fractions: -3.14, 1.2, 1e-8, 3.2e5

The float type in Python designates a decimal number. float values are specified with a decimal point. Scientific notation can be used here.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
pi = 3.14159
print(x)
print(2*pi)
{% endhighlight %}

### Boolean

* bool - boolean values: True and False

Boolean value in Python may have one of two values, True or False.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
i_love_python = True
python_loves_me = False
print(i_love_python)
print(python_loves_me)
{% endhighlight %}

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
| <=              | Less than or equal to: True if left operand is less than or equal to the right | x <= y |

### Logical operators

Logical operators perform Logical AND, Logical OR and Logical NOT operations.

| OPERATOR        | DESCRIPTION           | SYNTAX  |
| -------------   | ---------------------| -----|
| and             | Logical AND: True if both the operands are true | x and y |
| or              | Logical OR: True if either of the operands is true | x or y |
| not             | Logical NOT: True if operand is false | not x |


Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
i = 10
j = 9
print(i == j)
print(i > 9)
print(i < j)
print(i * j)
print(i * j * j)
{% endhighlight %}

##  Conversions

In Python, we can use the build in functions int(), float(), and str() to convert between types.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
x = "5"
print(x, type(x))
x = int("5")
print(x, type(x))
pi = float("3.141")
print(pi, type(pi))
print(str(4))

apples = "I have" + str(2) + "apple"
print(apples)
{% endhighlight %}

## The print() function

Type print("Hello World") in the above console and see what happens.
Try another example print('foo\tbar').
