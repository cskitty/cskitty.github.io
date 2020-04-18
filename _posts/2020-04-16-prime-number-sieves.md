---
title: "Prime Numbers with Sieve of Eratosthenes"
date: 2020-04-13T15:34:30-04:00
categories:
  - Programming
tags:
  - Python
  - Algorithms
  - Math
---

## Generating Prime Numbers using Sieve of Eratosthenes algorithm


Explanation

Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
For example, if n is 10, the output should be “2, 3, 5, 7”. If n is 20, the output should be “2, 3, 5, 7, 11, 13, 17, 19”.


{% highlight python linenos %}
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            print p,

# driver program
if __name__=='__main__':
    n = 30
    print "Prime numbers less than ", n
    SieveOfEratosthenes(n)
{% endhighlight %}
