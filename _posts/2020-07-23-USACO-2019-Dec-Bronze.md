---
title: "USACO 2019 Dec Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Python
---

# USACO 2019 Dec Bronze  

## Problem 1. Cow Gymnastics

In order to improve their physical fitness, the cows have taken up gymnastics! Farmer John designates his favorite cow Bessie to coach the N other cows and to assess their progress as they learn various gymnastic skills.
In each of K practice sessions (1≤K≤10), Bessie ranks the N cows according to their performance (1≤N≤20). Afterward, she is curious about the consistency in these rankings. A pair of two distinct cows is consistent if one cow did better than the other one in every practice session.

Help Bessie compute the total number of consistent pairs.

INPUT FORMAT (file gymnastics.in):  
The first line of the input file contains two positive integers K and N. The next K lines will each contain the integers 1…N in some order, indicating the rankings of the cows (cows are identified by the numbers 1…N). If A appears before B in one of these lines, that means cow A did better than cow B.
OUTPUT FORMAT (file gymnastics.out):
Output, on a single line, the number of consistent pairs.
SAMPLE INPUT:  
```
3 4
4 1 2 3
4 1 3 2
4 2 1 3
```
SAMPLE OUTPUT:  
```
4
```
The consistent pairs of cows are (1,4), (2,4), (3,4), and (1,3).

Problem credits: Nick Wu

{% highlight python linenos %}
fin, fout = open('gymnastics.in'), open('gymnastics.out', 'w')

k, n = tuple(map(int, fin.readline().split()))
rankings = [list(map(int, fin.readline().strip().split())) for _ in range(k)]

cows = list(range(1, 1 + n))
ans = 0
for cow1 in cows:
    for cow2 in cows:
        if cow1 != cow2:
            consistent = True
            for ranking in rankings:
                if ranking.index(cow1) < ranking.index(cow2):
                    consistent = False

            if consistent:
                ans += 1

fout.write(str(ans))
{% endhighlight %}

## Problem 2. Where Am I?  

Farmer John has gone out for a walk down the road and thinks he may now be lost!  
Along the road there are N farms (1≤N≤100) in a row. Farms unfortunately do not have house numbers, making it hard for Farmer John to figure out his location along the road. However, each farm does have a colorful mailbox along the side of the road, so Farmer John hopes that if he looks at the colors of the mailboxes nearest to him, he can uniquely determine where he is.    

Each mailbox color is specified by a letter in the range A..Z, so the sequence of N mailboxes down the road can be represented by a string of length N containing letters in the range A..Z. Some mailboxes may have the same colors as other mailboxes. Farmer John wants to know what is the smallest value of K such that if he looks at any sequence of K consecutive mailboxes, he can uniquely determine the location of that sequence along the road.   

For example, suppose the sequence of mailboxes along the road is 'ABCDABC'. Farmer John cannot set K=3, since if he sees 'ABC', there are two possible locations along the road where this consecutive set of colors might be. The smallest value of K that works is K=4, since if he looks at any consecutive set of 4 mailboxes, this sequence of colors uniquely determines his position along the road.  

INPUT FORMAT (file whereami.in):    
The first line of input contains N, and the second line contains a string of N characters, each in the range A..Z.  
OUTPUT FORMAT (file whereami.out):    
Print a line containing a single integer, specifying the smallest value of K that solves Farmer John's problem.  
SAMPLE INPUT:  
```
7
ABCDABC
```
SAMPLE OUTPUT:  
```
4
```
Problem credits: Brian Dean

{% highlight python linenos %}
fin, fout = open('whereami.in'), open('whereami.out', 'w')
n = int(fin.readline())
S = fin.readline().strip()

k = 1


def count(val, S):
    return val.find(S) == val.rfind(S)


while k <= n:
    b = True
    for x in range(0, n - k):
        val = S[x:x + k]

        if not count(S, val):
            b = False

    if b:
        break

    k += 1

fout.write(str(k))
{% endhighlight %}

## Problem 3. Livestock Lineup   

[Livestock Lineup](http://www.usaco.org/index.php?page=viewproblem2&cpid=965)    

Every day, Farmer John milks his 8 dairy cows, named Bessie, Buttercup, Belinda, Beatrice, Bella, Blue, Betsy, and Sue.
The cows are rather picky, unfortunately, and require that Farmer John milks them in an order that respects N constraints (1≤N≤7). Each constraint is of the form "X must be milked beside Y", stipulating that cow X must appear in the milking order either directly after cow Y or directly before cow Y.  

Please help Farmer John determine an ordering of his cows that satisfies all of these required constraints. It is guaranteed that an ordering is always possible. If several orderings work, then please output the one that is alphabetically first. That is, the first cow should have the alphabetically lowest name of all possible cows that could appear first in any valid ordering. Among all orderings starting with this same alphabetically-first cow, the second cow should be alphabetically lowest among all possible valid orderings, and so on.  

INPUT FORMAT (file lineup.in):  
The first line of input contains N. The next N lines each contain a sentence describing a constraint in the form "X must be milked beside Y", where X and Y are names of some of Farmer John's cows (the eight possible names are listed above).  
OUTPUT FORMAT (file lineup.out):  
Please output, using 8 lines, an ordering of cows, one cow per line, satisfying all constraints. If multiple orderings work, output the one that is alphabetically earliest.  
SAMPLE INPUT:
```
3
Buttercup must be milked beside Bella
Blue must be milked beside Bella
Sue must be milked beside Beatrice
```
SAMPLE OUTPUT:
```
Beatrice
Sue
Belinda
Bessie
Betsy
Blue
Bella
Buttercup
```
Problem credits: Brian Dean  

{% highlight python linenos %}
import itertools

fin, fout = open('lineup.in'), open('lineup.out', 'w')

n = int(fin.readline())
restrictions = []

for _ in range(n):
    restrictions.append(fin.readline().strip().split(' must be milked beside '))

cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
cows.sort()
count = 0

for cowOrdering in itertools.permutations(cows):
    passed = True
    for cow1, cow2 in restrictions:
        if abs(cowOrdering.index(cow1) - cowOrdering.index(cow2)) != 1:
            passed = False

    if passed:
        break

for cow in cowOrdering:
    fout.write(cow + '\n')
{% endhighlight %}
