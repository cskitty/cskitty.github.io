---
title: "USACO 2015 Feb Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Python
---

# USACO 2015 Feb Bronze  

## Problem 1. Censoring (Bronze)   
[Censoring (Bronze)](http://www.usaco.org/index.php?page=viewproblem2&cpid=526)  

Farmer John has purchased a subscription to Good Hooveskeeping magazine for his cows, so they have plenty of material to read while waiting around in the barn during milking sessions. Unfortunately, the latest issue contains a rather inappropriate article on how to cook the perfect steak, which FJ would rather his cows not see (clearly, the magazine is in need of better editorial oversight).  

FJ has taken all of the text from the magazine to create the string S of length at most 10^6 characters. From this, he would like to remove occurrences of a substring T of length <= 100 characters to censor the inappropriate content. To do this, Farmer John finds the _first_ occurrence of T in S and deletes it. He then repeats the process again, deleting the first occurrence of T again, continuing until there are no more occurrences of T in S. Note that the deletion of one occurrence might create a new occurrence of T that didn't exist before.  

Please help FJ determine the final contents of S after censoring is complete.  

INPUT FORMAT: (file censor.in)  
The first line will contain S. The second line will contain T. The length of T will be at most that of S, and all characters of S and T will be lower-case alphabet characters (in the range a..z).  

OUTPUT FORMAT: (file censor.out)  
The string S after all deletions are complete. It is guaranteed that S will not become empty during the deletion process.  
SAMPLE INPUT:  
```
whatthemomooofun
moo
```
SAMPLE OUTPUT:
```
whatthefun
```
[Problem credits: Mark Gordon, 2015]


{% highlight python linenos %}
fin, fout = open('censor.in'), open('censor.out', 'w')
s = fin.readline().strip()
t = fin.readline().strip()
news = ''
lt = len(t)
newslen = 0

for char in s:
    news += char
    newslen += 1
    if newslen >= lt and news[-lt:] == t:
        news = news[0:newslen - lt]
        newslen -= lt
fout.write(news)
{% endhighlight %}

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
Problem credits: Ben Cousins and Brian Dean, 2015

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
