---
title: "USACO 2020 Jan Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2020 Jan Bronze

## Problem 1. Word Processor

[Word Processor](http://usaco.org/index.php?page=viewproblem2&cpid=987)

Bessie the cow is working on an essay for her writing class. Since her handwriting is quite bad, she decides to type the essay using a word processor.  
The essay contains N words (1≤N≤100), separated by spaces. Each word is between 1 and 15 characters long, inclusive, and consists only of uppercase or lowercase letters. According to the instructions for the assignment, the essay has to be formatted in a very specific way: each line should contain no more than K (1≤K≤80) characters, not counting spaces. Fortunately, Bessie's word processor can handle this requirement, using the following strategy:  

If Bessie types a word, and that word can fit on the current line, put it on that line.  
Otherwise, put the word on the next line and continue adding to that line.  
Of course, consecutive words on the same line should still be separated by a single space. There should be no space at the end of any line.  

Unfortunately, Bessie's word processor just broke. Please help her format her essay properly!  

INPUT FORMAT (file word.in):  
The first line of input contains two space-separated integers N and K.  
The next line contains N words separated by single spaces. No word will ever be larger than K characters, the maximum number of characters on a line.  

OUTPUT FORMAT (file word.out):  
Bessie's essay formatted correctly.  
SAMPLE INPUT:  
```
10 7
hello my name is Bessie and this is my essay
```
SAMPLE OUTPUT:
```
hello my
name is
Bessie
and this
is my
essay
Including "hello" and "my", the first line contains 7 non-space characters. Adding "name" would cause the first line to contain 11>7 non-space characters, so it is placed on a new line.
```
Problem credits: Nathan Pinsker

{% highlight python linenos %}
fin = open("word.in", "r")
fout = open("word.out", "w")


nk = fin.readline().split()
n = nk[0]
k = int(nk[1])

text = fin.readline().split()
output = []

line = ''
for x in text:
    if len(x.replace(" ", '') + line.replace(' ', '')) <= k:
        line += x + ' '
        dsf = 1
    else:
        output.append(line)

        line = x + " "

        dsf = 0
output.append(line)


for x in range(len(output) - 1):
    fout.write(output[x].strip() + '\n')
    {% endhighlight %}

## Problem 2. Photoshoot

[Photoshoot](http://usaco.org/index.php?page=viewproblem2&cpid=988)

Farmer John is lining up his N cows (2≤N≤$$10^3$$), numbered 1…N, for a photoshoot. FJ initially planned for the i-th cow from the left to be the cow numbered ai, and wrote down the permutation a1,a2,…,aN on a sheet of paper. Unfortunately, that paper was recently stolen by Farmer Nhoj!
Luckily, it might still possible for FJ to recover the permutation that he originally wrote down. Before the sheet was stolen, Bessie recorded the sequence b1,b2,…,bN−1 that satisfies bi=ai+ai+1 for each 1≤i<N.

Based on Bessie's information, help FJ restore the "lexicographically minimum" permutation a that could have produced b. A permutation x is lexicographically smaller than a permutation y if for some j, xi=yi for all i<j and xj<yj (in other words, the two permutations are identical up to a certain point, at which x is smaller than y). It is guaranteed that at least one such a exists.

SCORING:
Test cases 2-4 satisfy N≤8.
Test cases 5-10 satisfy no additional constraints.
INPUT FORMAT (file photo.in):
The first line of input contains a single integer N.
The second line contains N−1 space-separated integers b1,b2,…,bN−1.

OUTPUT FORMAT (file photo.out):
A single line with N space-separated integers a1,a2,…,aN.
SAMPLE INPUT:
5
4 6 7 6
SAMPLE OUTPUT:
3 1 5 2 4
a produces b because 3+1=4, 1+5=6, 5+2=7, and 2+4=6.

Problem credits: Benjamin Qi and Chris Zhang

{% highlight python linenos %}
fin, fout = open('photo.in'), open('photo.out', 'w')

n = int(fin.readline())
b = list(map(int, fin.readline().split()))

a = []
count = 0

for a1 in range(1, n-1):

    off = False

    a = []
    a.append(a1)
    a.append(b[0] - a1)

    cur = b[0] - a1

    for x in range(1, n-1):
        cur = b[x] - cur

        if cur not in a and cur > 0 and cur <= n:
            a += [cur]
        else:
            off = True
            break

    if not off:
        break


fout.write(' '.join(list(map(str, a))))
{% endhighlight %}
