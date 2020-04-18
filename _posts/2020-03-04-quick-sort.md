---
title: "Quick Sort"
date: 2020-04-13T15:34:30-04:00
categories:
  - Programming
tags:
  - Python
  - Algorithms
---

## Quick Short


![](/assets/images/girlprogrammer3.jpg)

Explanation

Quick Sort is in fact one of the hardest types of sorting. Let’s suppose you want to sort the numbers [3, 10, 6, 1, 2, 4]. First, you pick a pivot number to compare the rest of the numbers with. In the program, we can pick the last number (in this case 4) to compare the rest of the numbers with. We can put them into two different arrays, lessThan and greaterThan. Diviying it up, we get 1 and 3 in lessThan, and the rest in greaterThan. Quick Sort uses recursion to work. If we call the function quick_sort again, it goes through the two arrays in the same manner. Finally, if the length of the array is less than or equal to one, we can just add it back to the original array.

Steps
![](../img/QuickSort2.png)

{% highlight python linenos %}
def quick_sort(array):
   if len(array) <= 1:
       return array
   lessThan = []
   greaterThan = []
   equalTo = []
   pivot = len(array) - 1
   equalTo.append(array[pivot])
   for index in range(len(array) - 1):
       if array[index] < array[pivot]:
           lessThan.append(array[index])
       elif array[index] > array[pivot]:
           greaterThan.append(array[index])
       else:
           equalTo.append(array[index])
   lessThan = quick_sort(lessThan)
   greaterThan = quick_sort(greaterThan)
   array = lessThan + equalTo + greaterThan
   return array

myArray = [4, 2, 7, 5, 1, 11, 74, 889, 25, 4, 4, 4, 2, 5, 27, 45]
print (quick_sort(myArray))
{% endhighlight %}
