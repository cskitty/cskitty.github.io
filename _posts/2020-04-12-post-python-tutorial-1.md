---
title: "Introduction to Python Lesson 1: Variables and Print"
categories:
  - Tutorials
tags:
  - Python
---                          
# Introduction to Python Lesson 1: Variables and Print                                                                       
{% include video id="AEY_B1MSGTw" provider="youtube" %}

## [Click to Download Lesson 1 Slides](/assets/docs/intro_python_1.pdf)    

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

## 1.1: Variables

Let’s suppose you want to store an object, like a pencil.
In real life, you would probably store it in a container. In Python, or any other programming language, you can do the same. A virtual “container” for objects is known as a variable (abbreviate as var). Variables are one of the fundamental parts of Python or any programming! The only difference between a real container and a variable is that typically, variables only hold one item, like a small ziploc bag or a tiny backpack.
In programming, variables need a name. This is how you can refer to them later. If I want to store my pencil into a bag and take it out later to write, I need to know what bag I stored it in.
For the syntax of creating the variable, we can simply assign the name to the value. The syntax is shown below; run the code!

{% highlight python linenos %}
x = 3
{%endhighlight%}

Variable naming is an important part of any language. For Python, there are words like "For" or ""True" (Both of which will be addressed later!). To make sure we don't accidentally name a variable after a word that already has a meaning, there are a few simple rules to follow.3
Camel Case - start with lowercase letters, and name new words with an uppercase letter. i.e. "firstDogSpot" or "catName"
No spaces!
Avoid keywords; on most python platforms, the keywords will change color. Don't use these words!
Always start with a letter. They can contain numbers though; for example "dog1" or "catName3" work, while "1Dog" and "3CatName" do not.
In this example, the value of the variable is a number. Of course, we can’t store actual items like pencils in python. However, we can store many other things.

## Numbers
Numbers in Python work like what you've learned from your math class including but not limit to counting numbers, negative numbers, decimals so on and so force.

To show you what I mean, type a few more numbers into the console below, pressing return after each one. You can also use operators.

  For example, try type 11 * 11 below.

<iframe src="https://trinket.io/embed/console/8c94ebd6bf" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Variables

### Integer

1.2: Numbers and Operators
 Just like from math, numbers come in many different forms. In programming, they are classified into different types of variables.

print(z)
 In this example, the value of z that will print out is 3 + 2, or 5.
 The most commonly used form of numbers are integers, or abbreviated as int. In Python specifically, they are unlimited; from -31459263 to positive 6283185, any number can be an integer. (This is not true for other programming languages, such as C or Java).

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
x = 3
y = 2
z = x + y
print(x, y, z)
{% endhighlight %}

As shown in the first example, variables can be added. But not only that: they can perform all the operations of a functioning equation!

### Float (decimals)

* float - floating point numbers, decimal point fractions: -3.14, 1.2, 1e-8, 3.2e5

The float type in Python designates a decimal number. float values are specified with a decimal point. Scientific notation can be used here.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
pi = 3.14159
print(x)
print(2*pi)
{% endhighlight %}

What about decimals and numbers that are not whole? These numbers go into a type of variable called a float.

In this example, while b renders as an int, a will save as a float.
{% highlight python linenos %}
a = 1.02
b = 1
{% endhighlight %}
Just like integers, floats can be operated on.

### String

* str - character strings, text: "hello world!", "CS50", 'python', 'starcoder!'

Remember the pencil from earlier? Though we can’t store the actual pencil, we can store the word in the variable. This word can be contained as a string (which can be abbreviated to str)
So that Python can differentiate the string from a Python command, strings have double quotes around them.


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


### Boolean

* bool - boolean values: True and False

The final main type of variable is Boolean, abbreviated into bool. There are only two variables for these: true and false. Though this may not seem interesting right now, they are especially useful in the future (and next lesson!)

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
i_love_python = True
python_loves_me = False
print(i_love_python)
print(python_loves_me)
{% endhighlight %}

##  Operators

These values can usually be operated on; there are a couple main types of operators.

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
