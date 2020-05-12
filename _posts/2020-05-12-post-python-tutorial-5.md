---
title: "Introduction to Python Lesson 5: Collections and Functions"
categories:
  - Projects
  - Tutorials
tags:
  - Python
---

## Introduction to Python Lesson 5: Collections and Functions

## Python Collections  

There are four collection data types in the Python programming language:

* List is a collection which is ordered and mutable (can add/delete elements to a list). Duplicate members are allowed.
* Tuple is a collection which is ordered and immutable (can not change once created). Duplicate members are allowed.
* Set is a collection which is unordered and unindexed. It is mutable (can add/delete elements to a set). No duplicate members.
* Dictionary is a collection which is unordered, mutable (can add/delete elements to a dictionary) and indexed. No duplicate members.

| Data Type       | Ordered? | Mutable ? | Indexed ?  |Allow Duplicate Member ? |
| -------------   | ---------------------| -----------|-------------------------|
| List            | Yes      | Yes       | Yes        |Yes                      |
| Tuple           | Yes      | No        | Yes        |Yes                      |
| Set             | No       | Yes       | No         |No                       |
| Dictionary      | No       | Yes       | Yes        |No                       |


When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


### Python List

List is an ordered sequence of items. The list is a most versatile datatype available in Python and is very flexible. Python List can be written as a list of comma-separated items between square brackets: [item1, item2, item3]. Please note that items in a list need not be of the same type, for example:

{% highlight python linenos %}
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

print(list1)
print(list2)
print(list3)
{% endhighlight %}


You access the list items by referring to the index number:

{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000]

print(list[1])
print(list[2])
{% endhighlight %}


List is a mutable collection, to change the value of a specific item, refer to the index number:

{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000];
print(list)

list[1] = 'math'
print(list)

{% endhighlight %}

To determine if a specified item is present in a list use the in keyword:
{% highlight python linenos %}
list = ['physics', 'chemistry', 1997, 2000]

a = 'physics'
print(a in list)
{% endhighlight %}

To add an item to the end of the list, use the append() method:
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

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().
{% highlight python linenos %}
list = ["apple", "banana", "cherry"]
list2 = list.copy()
print(list2)
{% endhighlight %}

We can join, or concatenate, two or more lists in Python using the + operator.
There are ways to make a copy, one way is to use the built-in List method copy().

{% highlight python linenos %}
list1 = [1,2,3]
list2 = [3,4,5]

list3 = list1 + list2
print(list3)
{% endhighlight %}


### Python Tuple

Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.  In Python tuples are written with round brackets () where items are separated by commas, for example:

{% highlight python linenos %}
fruits = ("apple", "banana", "orange")
print(fruits)
{% endhighlight %}


You can access tuple items by referring to the index number, inside square brackets:

{% highlight python linenos %}
fruits = ("apple", "banana", "orange")

#print out the second item in the tuple
print(fruits[1])
{% endhighlight %}

### Negative Indexing

In Python, negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
Negative indexing can be used both in List and Tuple, for example:

{% highlight python linenos %}
primes = [2,3,5,7,11,13,17]
#print out the last number in the list
print(primes[-1])

fruits = ("apple", "banana", "orange")

#print out the second last item
print(fruits[-2])
{% endhighlight %}


### Python Set

Set is an unordered collection of unique items. In Python sets are items written with curly brackets { }. Different from List and Tuple, items in a set are not ordered, that means items in a set can not be accessed by referring to an index.

We can check if a specified variable is present in a set by using the in keyword.

{% highlight python linenos %}
fruits = {'apple', 'banana', 'orange'}

a = 'carrot'
if a in fruits:
    print(a, " is a fruit")
else:
    print(a, " is not a fruit")
{% endhighlight %}

We can also iterate through the set items using a for loop, as shown below:

{% highlight python linenos %}
fruits = {'apple', 'banana', 'orange'}

for a in fruits:
   print(a)
{% endhighlight %}

Set is mutable, which means we can add/delete items to an existing set, as shown below.
Please note that if the item to remove does not exist, remove() will raise an error.

{% highlight python linenos %}
fruits = {'apple', 'banana', 'orange'}

fruits.add('watermelon')
print(fruits)

fruits.remove('banana')
print(fruits)
{% endhighlight %}


There are several ways to operate on two or more sets in Python.

* \| or union() for union.
* & or intersection() for intersection.
* – or difference() for difference
* ^ or symmetric_difference() for symmetric difference


You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another, as shown in the example below:

{% highlight python linenos %}
# Program to perform different set operations
# as we do in  mathematics

# sets are define
A = {0, 2, 4};
B = {1, 2, 3};

# union
print("Union :", A | B)
print("Union :", A.union(B))

# intersection
print("Intersection :", A & B)
print("Intersection :", A.intersection(B))

# difference
print("Difference :", A - B)
print("Difference :", A.difference(B))

# symmetric difference
print("Symmetric difference :", A ^ B)
print("Symmetric difference :", A.symmetric_difference(B))

{% endhighlight %}


## Python Dictionary

In Python, Dictionary is an unordered collection of key-value pairs. Dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.


{% highlight python linenos %}
# empty dictionary
myDict = {}
print(myDict)

# empty dictionary
myDict = dict()
print(myDict)

# dictionary with integer keys
myDict = {1: 'blue', 2: 'ball'}
print(myDict)

# dictionary with mixed keys
myDict = {'color': 'blue', 1: 'orange'}
print(myDict)

# from list of tuples
myDict = dict([('color','red'), (1,'apple')])
print(myDict)
{% endhighlight %}
