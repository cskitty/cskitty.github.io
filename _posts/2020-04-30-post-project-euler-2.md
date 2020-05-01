---
title: "Project Euler in Python Series 2"
date: 2020-04-30
categories:
  - Math
tags:
  - Python
  - Euler
  - Math
---

# Project Euler in Python Series 2

![](/assets/images/snowbunny2.jpg)

## Problem 11 Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


{% highlight python linenos %}
import sympy
def problem_10():
    sum = 0
    for x in range(3, 2000000, 2):
        if sympy.isprime(x):
            sum += x
    return sum + 2
print(problem_10())
{% endhighlight %}
