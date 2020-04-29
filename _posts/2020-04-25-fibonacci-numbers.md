---
title: "Basic Math in Programming"
categories:
  - Programming
tags:
  - Python
  - Algorithms
  - Math
---

## Basic Math in Programming

### Fibonacci Sequence

The Fibonacci sequence in math is defined as

$$F_n = F_{n-1} + F_{n-2}$$

In Python, we can easily generate a series of Fibonacci numbers up to a certain number $$N$$. One way to do this is with dynamic programming:


{% highlight python linenos %}

def fibonacci_numbers(N):
  if (N < 3):
    return 1
  p1 = 1
  p2 = 1
  for i in range(3, N+1):
    temp = p1
    p1 = p2
    p2 = temp + p2
  return p2

fibonacci_list = [fibonacci_numbers(x) for x in range(1, 10)]

print(fibonacci_list)

{% endhighlight %}

As the numbers get larger, the values of the Fibonacci sequence increases exponentially. What if we want to only get the last digit of the value?

{% highlight python linenos %}

def fibonacci_numbers(N):
  if (N < 3):
    return 1
  p1 = 1
  p2 = 1
  for i in range(3, N+1):
    temp = p1
    p1 = p2 % 10
    p2 = (temp + p2) % 10
  return p2


print(fibonacci_numbers(331))

{% endhighlight %}

By modding every value by 10, we make sure that we only keep the last digit of the values. This not only saves space, but also speeds up the program.

### LCM and GCD

GCD can be found using Euclid's GCD algorithm.

{% highlight python linenos %}

def GCD(x, y):
  if (x < y):
    x, y = y, x
  diff = x % y
  while (diff > 0):
    diff = x % y
    x = y
    y = diff
  return x

GCD(120, 200)
{% endhighlight %}


LCM can be found with the property that $$GCD * LCM = x * y$$.

{% highlight python linenos %}

def LCM(x, y):
  mult = x * y
  if (x < y):
    x, y = y, x
  diff = x % y
  while (diff > 0):
    diff = x % y
    x = y
    y = diff
  return mult//x

LCM(120, 200)
{% endhighlight %}
