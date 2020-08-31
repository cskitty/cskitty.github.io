---
title: "USACO 2020 Feb Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2020 Feb Bronze

## Problem 1. Triangles

[Triangles](http://usaco.org/index.php?page=viewproblem2&cpid=1011)

Farmer John would like to create a triangular pasture for his cows.  
There are N fence posts (3≤N≤100) at distinct points (X1,Y1)…(XN,YN) on the 2D map of his farm. He can choose three of them to form the vertices of the triangular pasture as long as one of the sides of the triangle is parallel to the x-axis and another side is parallel to the y-axis.  

What is the maximum area of a pasture that Farmer John can form? It is guaranteed that at least one valid triangular pasture exists.  

INPUT FORMAT (file triangles.in):  
The first line of the input contains the integer N. Each of the next N lines contains two integers Xi and Yi, each in the range −104…104 inclusive, describing the location of a fence post.  
OUTPUT FORMAT (file triangles.out):  
As the area itself is not necessarily an integer, output two times the maximum area of a valid triangle formed by the fence posts.  
SAMPLE INPUT:  
```
4
0 0
0 1
1 0
1 2
```
SAMPLE OUTPUT:
```
2
```
Posts at (0,0), (1,0), and (1,2) form a triangle of area 1. Thus, the answer is 2⋅1=2. There is only one other triangle, with area 0.5.

Problem credits: Travis Hance

{% highlight c++ linenos %}


{% endhighlight %}

## Problem 2. Mad Scientist

[Mad Scientist](http://usaco.org/index.php?page=viewproblem2&cpid=1012)

Farmer John's cousin Ben happens to be a mad scientist. Normally, this creates a good bit of friction at family gatherings, but it can occasionally be helpful, especially when Farmer John finds himself facing unique and unusual problems with his cows.  
Farmer John is currently facing a unique and unusual problem with his cows. He recently ordered N cows (1≤N≤1000) consisting of two different breeds: Holsteins and Guernseys. He specified the cows in his order in terms of a string of N characters, each either H (for Holstein) or G (for Guernsey). Unfortunately, when the cows arrived at his farm and he lined them up, their breeds formed a different string from this original string.  

Let us call these two strings A and B, where A is the string of breed identifiers Farmer John originally wanted, and B is the string he sees when his cows arrive. Rather than simply check if re-arranging the cows in B is sufficient to obtain A, Farmer John asks his cousin Ben to help him solve the problem with his scientific ingenuity.  

After several months of work, Ben creates a remarkable machine, the multi-cow-breed-flipinator 3000, that is capable of taking any substring of cows and toggling their breeds: all Hs become Gs and all Gs become Hs in the substring. Farmer John wants to figure out the minimum number of times he needs to apply this machine to transform his current ordering B into his original desired ordering A. Sadly, Ben's mad scientist skills don't extend beyond creating ingenious devices, so you need to help Farmer John solve this computational conundrum.  

INPUT FORMAT (file breedflip.in):  
The first line of input contains N, and the next two lines contain the strings A and B. Each string has N characters that are either H or G.  
OUTPUT FORMAT (file breedflip.out):  
Print the minimum number of times the machine needs to be applied to transform B into A.  
SAMPLE INPUT:  
```
7
GHHHGHH
HHGGGHH
```
SAMPLE OUTPUT:
```
2
```
First, FJ can transform the substring that corresponds to the first character alone, transforming B into GHGGGHH. Next, he can transform the substring consisting of the third and fourth characters, giving A. Of course, there are other combinations of two applications of the machine that also work.

Problem credits: Brian Dean

{% highlight c++ linenos %}

fin, fout = open('breedflip.in'), open('breedflip.out', 'w')

n = int(fin.readline())

a = fin.readline()
b = fin.readline()

s = []
for x in range(n):
    if a[x] != b[x]:
        s.append(1)
    else:
        s.append(0)

def count(x,s):
    count = 0
    for f in range(len(s) - 1):
        if s[f] == int(x[0]) and s[f+ 1] == int(x[1]):
            count += 1

    return count

s = [0] + s + [0]
fout.write(str((count('01', s) + count('10', s))//2))

{% endhighlight %}


## Problem 3. Swapity Swap

[Swapity Swap](http://usaco.org/index.php?page=viewproblem2&cpid=1013)

Farmer John's N cows (1≤N≤100) are standing in a line. The ith cow from the left has label i, for each 1≤i≤N.  
Farmer John has come up with a new morning exercise routine for the cows. He tells them to repeat the following two-step process exactly K (1≤K≤109) times:  

The sequence of cows currently in positions A1…A2 from the left reverse their order (1≤A1<A2≤N).  
Then, the sequence of cows currently in positions B1…B2 from the left reverse their order (1≤B1<B2≤N).  
After the cows have repeated this process exactly K times, please output the label of the ith cow from the left for each 1≤i≤N.  

SCORING:  
Test cases 2-3 satisfy K≤100.  
Test cases 4-13 satisfy no additional constraints.  
INPUT FORMAT (file swap.in):  
The first line of input contains N and K. The second line contains A1 and A2, and the third contains B1 and B2.  
OUTPUT FORMAT (file swap.out):  
On the ith line of output, print the label of the ith cow from the left at the end of the exercise routine.  
SAMPLE INPUT:  
```
7 2
2 5
3 7
```
SAMPLE OUTPUT:
```
1
2
4
3
5
7
6
```
Initially, the order of the cows is [1,2,3,4,5,6,7] from left to right. After the first step of the process, the order is [1,5,4,3,2,6,7]. After the second step of the process, the order is [1,5,7,6,2,3,4]. Repeating both steps a second time yields the output of the sample.

Problem credits: Brian Dean  

{% highlight c++ linenos %}
 
{% endhighlight %}
