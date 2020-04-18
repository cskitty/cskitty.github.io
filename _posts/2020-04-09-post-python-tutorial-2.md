---
title: "Python for Beginner Lesson 2: Flow Control"
date: 2020-04-17 
categories:
  - Projects
  - Tutorials
tags:
  - Python
  - Beginner
  - Turtle
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

## Loops

There are two types of loops in Python, for and while.

### The For loop

For loops tell the computer to do something for a bunch of values. They're particularly useful when we want the same "thing" done several times in succession.
Let's say, for example, we wanted to print out the numbers 0-5 in sequence. We could write print statements:

<iframe src="https://trinket.io/embed/python/8eede7897b" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

But that seems tedious!

For loop and a listPermalink
We could also put the numbers we want in a list and then print each thing in the list:
<iframe src="https://trinket.io/embed/python/1dc272e36d" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

That seems a little better.

* On the first line, we make a list, called numbers, and fill it with the numbers we wish to print: [0, 1, 2, 3, 4, 5].
* On the second line, we write for n in numbers: This is the for loop part, and converted into English, it says "Look at the list called numbers. For each element in it, grab the element and temporarily call it n. Then .. "
* On the third line, we write print just once, and ask Python to print n. That's the same as asking Python to print out the value in the variable container n – which we know is one of the elements in the list from the second line!

## For loop and range( .. ) function

There's a special range( .. ) function built into Python that gives back a range of numbers.
Try running the code below:

```python
print(range(0, 6))
for n in range(0, 6):
    print(n)
```

Here we get the same result, though we didn't have to make a list ourselves. The range(0, 6) function returns a list that went from 0 (inclusive) to 6 (exclusive.)

## Doing things with for loops

The general form of a for loop looks like this:

```python
for temp_variable in some_sort_of_list:
  do_something
```

For loops end up being pretty useful. Take a look at the code below; when you think you know what it does,
open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

```python
sum = 0
for x in range(0, 101):
    sum = sum + x

print(sum)
```

### The While loop

While loops repeat as long as a certain boolean condition is met. For example:

```python
count = 0
sum   = 0
while count < 5:
    print(count)
    count = count + 1  # count += 1 also works!
    sum = sum + count
print(sum)
```


## "break" and "continue" statements

break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. A few examples:

```python
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
```

## Exercise

Can you create a program to add all odd numbers that are less than 100?
