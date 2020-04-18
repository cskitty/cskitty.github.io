---
title: "Binary Search"
date: 2020-04-13T15:34:30-04:00
categories:
  - Programming
tags:
  - Python
  - Algorithms
---

## Binary Search

![](/assets/images/sleeping.jpg)

Explanation

This is a binary search. It’s a way to find an item. For example, let’s say you’re searching the dictionary for a word. (as an example, queen.) Normal searching would have you start at the A’s, Aardvark and Apple, then go to the B’s and C’s and so on and so forth until you reach the Q’s. However, binary search lets you reduce the amount of steps. If you start in the middle of the dictionary, near, say, M, you can easily see Queen is after Merry and now you’ve eliminated half the dictionary.

If you look in half of that (near the S’s) you can see that Salamander and Swing are before Queen. Now you only have a fourth of the dictionary left. If you keep on going, you will eventually reach Queen.


{% highlight python linenos %}
def binary_search(item, array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) / 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
   return None

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print (binary_search(67, primes))
{% endhighlight %}
