---
title: "Introduction to Python Lesson 2: Statement and Flow Control"
categories:
  - Tutorials
tags:
  - Python
---

# Introduction to Python Lesson 2: Statement and Flow Control           
{% include video id="3m4C3hfEPLc" provider="youtube" %}

## [Click to Download Lesson 2 Slides](/assets/docs/intro_python_2.pdf)  
## Python Statement

In Python, a statement is an instruction that the Python interpreter can execute. For example, a = 11 is an assignment statement. There are other more complex statements such as if statement, for statement, while statement, etc.

### Multi-line statement and explicit line continuation.

In Python, usually the end of a statement is marked by a newline character (carriage return). In case we need multiple lines for a statement, we can use the line continuation character (\). For example:

{% highlight python linenos %}
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
{% endhighlight %}


### Implicit Line continuation

In Python, expressions in parentheses (), square brackets [] or curly braces {} can be split over more than one physical line without using backslashes. For example:

{% highlight python linenos %}
weekdays = ['Mon','Tus','Wed',
            'Thur', 'Fri','Sat','Sun']
{% endhighlight %}

The following code will raise an error as the last line is not indented.

{% highlight python linenos %}
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
{% endhighlight %}


We can also put multiple statements in a single line using semicolons, as follows:
{% highlight python linenos %}
a = 1; b = 2; c = 3
{% endhighlight %}


## Python Indentation

While many other programming languages like Java and C,  use braces { } wrapping around multiple statements to define a block of code, code indentation is used in Python to define code blocks.

A code block consists of statements start with same level indentation and ends with the first unindented line. The amount of indentation is up to the programmer to decide, as long as it is consistent throughout that block.

Usually we use four whitespaces for indentation, as shown in the example below:

{% highlight python linenos %}
if a > 0:
    #four space identation is used here
    if a % 2 == 1
        #another four space identation is used
        print("positive odd number")
    else:
        #another four space identation is used
        print("positive even number")
else:
    #four space identation is used here
    print("negative")
{% endhighlight %}

## Python Comments

In Python, comments can be used to explain Python code and can be used to make the code more readable. They describe what is going on inside a program.  In Python, the hash (#) symbol is used to start writing a comment and the comment extends to the end of the line. Python Interpreter will not execute any thing inside comments.

Programmers can use comments to disable certain lines of code instead of deleting them. This will be very helpful during development stage.

{% highlight python linenos %}
# let's print hello world
print("hello world!")

# the following line will not be executed
# a = 1
{% endhighlight %}

### Multi-line comments

If the comments are long and require multiple lines. We can use triple quotes, either ''' or """.

{% highlight python linenos %}
"""I am a multiline comments which
continues here and here
and ends here"""
{% endhighlight %}


## Conditions and If ... Else statements

In Python, If Statement is used for decision making. It will run the body of code only when If statement is true.
The Else keyword catches anything which isn't caught by the preceding conditions.

Python supports the usual logical conditions from mathematics:

* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

Example:

{% highlight python linenos %}
a = 33
b = 44
if b > a:
  print("b is greater than a")
else:
  print("b is less or equal than a")
{% endhighlight %}

In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 44, we know that 44 is greater than 33, and so we print to screen that "b is greater than a".


### Nested if statements

Additional elif statement can be added to introduce more comparisons.
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

We can use if..elif..else to execute different statements based on various conditions.

    if *condition*:
        *statement*
        *statement*
        ...
    elif *condition*: # 0 or more elif clauses
        *statement*
        *statement*
        ...    
    else:             # optional
        *statement*
        *statement*

Example:

* Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.
* After running, you can modify the variable today to "Tuesday" or "Sunday" and try again.

{% highlight python linenos %}
today = "Monday"
hiking = "N"
my_recitation = "Tuesday"

if today == "Sunday":
    print("Todoay is " + today)
    if hiking == "Y":
        print("Go hiking")
    else:
        print("Stay home")
elif today == "Wednesday":
    print("I have homework due today!")
elif today == my_recitation:
    print("Go to recitation!")
else:
    print("No plan for today")
{% endhighlight %}
