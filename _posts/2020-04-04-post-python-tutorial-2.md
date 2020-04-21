---
title: "Python for Beginner Lesson 2: Flow Control"
categories:
  - Projects
  - Tutorials
tags:
  - Python
---

# Python for Beginner Lesson 2:  Flow Control

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

```python
a = 33
b = 44
if b > a:
  print("b is greater than a")
else:
  print("b is less or equal than a")
```

In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 44, we know that 44 is greater than 33, and so we print to screen that "b is greater than a".

## Indentation

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
The following code will raise an error as the last line is not indented.

```python
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
```

## Nested if statements

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

```python
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
```
