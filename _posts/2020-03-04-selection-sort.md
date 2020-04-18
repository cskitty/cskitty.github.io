---
title: "Selection Sort"
date: 2020-04-13T15:34:30-04:00
categories:
  - Programming
tags:
  - Python
  - Algorithms
---

## Selection Sort


![](/assets/images/girlprogrammer1.jpg)

Explanation

I’m learning Algorithms, so this is a Python Selection Sort. With selection sorting, if we start with an unsorted list (We’ll say 3, 6, 2, 9, 1) we first compare element[0] which in this case is 3, to the other numbers. To do this we first find the least number from element[1] to the last element (in this case element[4]). In the program below, the function find_min(array, start, end) does that.

Next, once we’ve found the smallest element (in this case 1) we compare it to the first number. This is done in the program with an if loop. If it is smaller, we swap it. The swap(array, first, second) function shows how to swap. Going through the list one at a time, we finally can get a sorted list.

### Visual Steps

3, 6, 2, 9, 1

3, 6, 2, 9, 1 (least number is 1)

1, 6, 2, 9, 3 (next least number is 2)

1, 2, 6, 9, 3 (next least number is 3)

1, 2, 3, 9, 6 (next least number is 6)

1, 2, 3, 6, 9 (We’re done!)


{% highlight python linenos %}
def swap(array, first, second):
    number = array[first]
    array[first] = array[second]
    array[second] = number

def find_min(array, start, end):
    least = start
    current = start + 1
    while current < end:
       if array[least] > array[current]:
           least = current
    current += 1
    return least

def selection_sort(array):
    pointer1 = 0
    end = len(array)
    while pointer1 < end - 1:
        pointer2 = find_min(array, pointer1 + 1, end)
        if array[pointer2] < array[pointer1]:
            swap(array, pointer1, pointer2)
        pointer1 += 1

myArray = [18, 6, 66, 44, 9, 2, 6, 6, 6, 12, 22, 14]
selection_sort(myArray)
for x in myArray:
    print x
{% endhighlight %}
