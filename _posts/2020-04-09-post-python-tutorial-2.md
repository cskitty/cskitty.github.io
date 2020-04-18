---
title: "Python Tutorial - Lesson 2 : Lists and Loops"
categories:
  - Projects
  - Tutorials
tags:
  - Python
  - Beginner
  - Turtle
---

# Python Tutorial - Lesson 2 : Lists and Loops

## List

## Loop

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
There's a special range( .. ) function built into Python that gives back a range of numbers. Try running the code below:

<iframe src="https://trinket.io/embed/python/3cbdc1f6f3" width="100%" height="210" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here we get the same result, though we didn't have to make a list ourselves. The range(0, 6) function returns a list that went from 0 (inclusive) to 6 (exclusive.)

## Doing things with for loops

The general form of a for loop looks like this:

```python
for temp_variable in some_sort_of_list:
  do_something
```

For loops end up being pretty useful. Take a look at the code below; when you think you know what it does, click 'Run', and take a look:

<iframe src="https://trinket.io/embed/python/7c3769aaed" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
