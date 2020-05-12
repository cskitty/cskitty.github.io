---
title: "Introduction to Python Lesson 3: List and Loops"
categories:
  - Projects
  - Tutorials
tags:
  - Python
---

# Introduction to Python Lesson 3: List and Loops

## Python List

List is an ordered sequence of items. The list is a most versatile datatype available in Python and is very flexible. Python List can be written as a list of comma-separated items between square brackets: [item1, item2, item3]. Please note that items in a List need not be of the same type, for example:

{% highlight python linenos %}
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

print(list1)
print(list2)
print(list3)
{% endhighlight %}


You access the list items by referring to the index number. Please note that similar to string indexing, List indexing in Python starting with 0 and ending with length of List -1.

{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000]
print(list[0))
print(list[1])
print(list[2])
print(list[3])
{% endhighlight %}


List can be modified, we call List a mutable collection (which we will go over in Lesson 5).
To change the value of a specific item in a List, we use the assignment operator and put the indexed List item on the left side of the assignment operator and the new value on the right side.
In the following example, we want to change the second time (index 1) from 'chemistry' to 'math':

{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000];
print(list)

list[1] = 'math'
print(list)
{% endhighlight %}

To determine if a specified item is present in a list use the ***in*** keyword:
{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000]

a = 'physics'
print(a in list)
{% endhighlight %}

To add an item to the end of a list, use the append() method:
{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000]
print(list)

list.append("orange")
print(list)
{% endhighlight %}

There are several methods to remove items from a list:

{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000]
print(list)

list.remove("chemistry")
print(list)

del list[0]
print(list)

#clear the entire list3
list.clear()
print(list)
{% endhighlight %}

### Copy a List

You cannot copy List simply by typing list2 = list1, because: list2 will only be a reference to list1, which means list2 actually is only a pointer to list1.
So changes made in list1 will automatically also be made in list2.

There are many ways to make a copy, the most frequently used way is to use the built-in List method copy(). As shown in the example below:

{% highlight python linenos %}
list = ["apple", "banana", "cherry"]
list2 = list.copy()
print(list2)
{% endhighlight %}

### List concatenation

Similar to string concatenation, we can join, or concatenate, two or more lists in Python using the + operator.

{% highlight python linenos %}
list1 = [1,2,3]
list2 = [3,4,5]

list3 = list1 + list2
print(list3)
{% endhighlight %}


### The build-in range(...) function
In Python, there is a build in function range(...) that gives back a list of sequential numbers.

Syntax of the range(...) function

```
range(start, stop, step)
```

Parameter Values

| PARAMETER        | DESCRIPTION           |  
| -------------   | ---------------------| -----|
| start             | Optional. An integer number specifying at which position to start. Default is 0 |
| stop              | Required. An integer number specifying at which position to end. |
| step             |Optional. An integer number specifying the incrementation. Default is 1 |

The returned number sequence  starts from value ***start***, and increments by ***step***, and ends at ***stop-1***.  
Please note that ***start*** and ***step*** can be omitted if their value is 0 and 1.  
Also the last number of the sequence is ***stop - 1*** instead of ***stop***.  

In the following example, we create a List of numbers from 0 to 9:  

{% highlight python linenos %}
x = range(0, 10, 1)
print(x)

# We can omit the last parameter 1, as it is the default value
y = range(0, 10)
print(y)

# We can omit the first parameter 0 and last parameter 1, as both of them have default values
z = range(10)
print(z)
{% endhighlight %}



## Python Loops

There are two types of loops in Python, for loop and while loop.


### The For loop

For loops tell the computer to do something for a bunch of numbers. They're particularly useful when we want the same "thing" done several times in succession.
Let's say, for example, we wanted to print out the numbers 0-5 in sequence. We could write print statements:

<iframe src="https://trinket.io/embed/python/8eede7897b" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

But that seems tedious!

We could put all the numbers we want to print in a list and then use a for loop to print each thing in the list:
<iframe src="https://trinket.io/embed/python/1dc272e36d" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

That seems a little better.

* On the first line, we make a list, called numbers, and fill it with the numbers we wish to print: [0, 1, 2, 3, 4, 5].
* On the second line, we write for n in numbers: This is the for loop part, and converted into English, it says "Look at the list called numbers. For each element in it, grab the element and temporarily call it n. Then .. "
* On the third line, we write print just once, and ask Python to print n. That's the same as asking Python to print out the value in the variable container n – which we know is one of the elements in the list from the second line!

The syntax of a for loop is:
```
for variable in something_iterable :
    *statement*
    *statement*
    ...
```


### For loop and range( .. ) function

range(...) function can be used in a for loop to generate a list of integers which can be used by the for loop.
Try running the code below:

{% highlight python linenos %}
for n in range(0, 6):
    print(n)
{% endhighlight %}

Here we get the same result, though we didn't have to make a list ourselves. The range(0, 6) function returns a list that went from 0 (inclusive) to 6 (exclusive.)

## Two methods for iterating on items in a list

There are two ways to iterate on items in a list using for loops. Let's go over with two examples.

### Iterate through indexes (i.e. 0, 1, 2...length-1)

This method is useful if you want to know which index is been used for processing the current item.
{% highlight python linenos %}
item_list = [1,3,5,9]
for index in range(len(item_list)):
  item_str = "index = " + str(index) + ", item= " + str(item_list[index])
  print(item_str)
{% endhighlight %}


### Iterate directly on items

This method is useful if you only work on item itself.

{% highlight python linenos %}
item_list = [1,3,5,9]
for item in item_list:
  print(item)
{% endhighlight %}


## Various usage of for loops

### Execute the same code multiple times

A common scenario of using Python for loops is to execute an action a given number of
times. This is can be done with the built-in range() function. The following example
prints out 10 "hello world" string

{% highlight python linenos %}
count = 10
for x in range(count):
    print("hello world!")
{% endhighlight %}


With the % operator, the following example prints out all even numbers less than 20  

{% highlight python linenos %}
count = 20
for x in range(count):
    if x % 2 == 0:
      print(x)
{% endhighlight %}


For loops can be more powerful. Take a look at the code below; when you think you know what it does,
open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
sum = 0
for x in range(0, 101):
    sum = sum + x

print(sum)
{% endhighlight %}



### The While loop

While loops repeat as long as a certain boolean condition is met.   
The syntax of Python while loop is shown below:

```
while boolean_condition_is_true:
    statement
    statement
    ...

```

For example:

{% highlight python linenos %}
counter = 0
sum   = 0
while counter < 10:
    print(counter)
    counter = counter + 1  # counter += 1 also works!
    sum = sum + counter
print(sum)
{% endhighlight %}

In the above program, the test expression will be True as long as our counter variable is less than or equal to 10.  
Please note that we need to increase the value of the counter variable in the body of the loop.  
This is very important (and mostly forgotten). Failing to do so will result in an infinite loop (never-ending loop).

Finally, the sum of counteres (from 0 to 9) is displayed.


## "break" and "continue" statements

The ***break*** statement terminates the loop containing it.  
Control of the program flows to the statement immediately after the body of the loop ().  

If the ***break***  statement is inside a nested loop (loop inside another loop), the ***break***  statement will terminate the innermost only.

Example of using ***break*** inside a while Loop:

{% highlight python linenos %}
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    if count >= 5:
        break
    count += 1
{% endhighlight %}


Example of using ***break*** inside a for Loop:

{% highlight python linenos %}
# the same thing implemented with for loop and break
for i in range(100):
  print(i)
  if i >= 5:
    break
{% endhighlight %}


The ***continue***  statement is used to skip the rest of the code inside a loop for the current iteration only.   
Loop does not terminate but continues on with the next iteration.

Example of using ***continue*** inside a while Loop:  

{% highlight python linenos %}
# Prints out only even numbers 2,4, 6, 8
count = 0
while count < 10:
    count += 1
    if count % 2 == 1:
      continue
    print(count)
{% endhighlight %}


Example of using ***continue*** inside a for Loop:  

{% highlight python linenos %}
# Prints out only odd numbers 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
{% endhighlight %}

## Exercise

Can you create a program to add all odd numbers that are less than 100?
