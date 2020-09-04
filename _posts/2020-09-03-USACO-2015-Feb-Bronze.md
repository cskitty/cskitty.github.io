---
title: "USACO 2015 Feb Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Python
---

# USACO 2018 Open Bronze  

## Problem 2. COW  


[COW](http://www.usaco.org/index.php?page=viewproblem2&cpid=527)    

Bessie the cow has stumbled across an intriguing inscription carved into a large stone in the middle of her favorite grazing field. The text of the inscription appears to be from a cryptic ancient language involving an alphabet with only the three characters C, O, and W. Although Bessie cannot decipher the text, she does appreciate the fact that C, O, and W in sequence forms her favorite word, and she wonders how many times COW appears in the text.  

Bessie doesn't mind if there are other characters interspersed within COW, only that the characters appear in the correct order. She also doesn't mind if different occurrences of COW share some letters. For instance, COW appears once in CWOW, twice in CCOW, and eight times in CCOOWW.  

Given the text of the inscription, please help Bessie count how many times COW appears.  

INPUT FORMAT: (file cow.in)  
The first line of input consists of a single integer N <= 10^5. The second line contains of a string of N characters, where each character is either a C, O, or W.  

OUTPUT FORMAT: (file cow.out)  
Output the number of times COW appears as a subsequence, not necessarily contiguous, of the input string.  

Note that the answer can be very large, so make sure to use 64 bit integers ("long long" in C++, "long" in Java) to do your calculations.  

SAMPLE INPUT:
```
6
COOWWW
```
SAMPLE OUTPUT:
```
6
```
[***Problem credits:*** Ben Cousins and Brian Dean, 2015]


{% highlight python linenos %}
fin, fout = open('cow.in'), open('cow.out', 'w')

n = int(fin.readline())
s = fin.readline()

cCount = 0
coCount = 0
cowCount = 0

for i in range(n):
    if s[i] == 'C':
        cCount += 1

    elif s[i] == 'O':
        coCount += cCount

    elif s[i] == 'W':
        cowCount += coCount

fout.write(str(cowCount))
{% endhighlight %}
