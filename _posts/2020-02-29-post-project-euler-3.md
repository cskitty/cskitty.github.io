---
title: "Project Euler in Python Series 3"
categories:
  - Math
tags:
  - Python
  - Euler
  - Math
---

# Project Euler in Python Series 3

![](/assets/images/snowbunny2.jpg)

## Problem 16 Power digit sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number $$21^{1000}$$?

{% highlight python linenos %}
def problem_16():
    num = 2**1000
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
print(problem_16())
{% endhighlight %}


{% highlight python linenos %}

{% endhighlight %}