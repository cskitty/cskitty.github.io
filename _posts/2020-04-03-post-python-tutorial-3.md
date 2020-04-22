---
title: "Python for Beginner Lesson 3: Loops"
categories:
  - Projects
  - Tutorials
tags:
  - Python
---

# Python for Beginner Lesson 3:  Loops

There are two types of loops in Python, for loop and while loop.

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

{% highlight python linenos %}
print(range(0, 6))
for n in range(0, 6):
    print(n)
{% endhighlight %}

Here we get the same result, though we didn't have to make a list ourselves. The range(0, 6) function returns a list that went from 0 (inclusive) to 6 (exclusive.)

## Doing things with for loops

The general form of a for loop looks like this:

{% highlight python linenos %}
for temp_variable in some_sort_of_list:
  do_something
{% endhighlight %}

For loops end up being pretty useful. Take a look at the code below; when you think you know what it does,
open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
sum = 0
for x in range(0, 101):
    sum = sum + x

print(sum)
{% endhighlight %}

### The While loop

While loops repeat as long as a certain boolean condition is met. For example:

{% highlight python linenos %}
count = 0
sum   = 0
while count < 5:
    print(count)
    count = count + 1  # count += 1 also works!
    sum = sum + count
print(sum)
{% endhighlight %}


## "break" and "continue" statements

break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. A few examples:

{% highlight python linenos %}
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
{% endhighlight %}

## Exercise

Can you create a program to add all odd numbers that are less than 100?
