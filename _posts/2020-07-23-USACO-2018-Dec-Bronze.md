---
title: "USACO 2018 Dec Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Python
---

# USACO 2018 Dec Bronze

## Problem 1. Mixing Milk  


[Mixing Milk](http://www.usaco.org/index.php?page=viewproblem2&cpid=855)  

Farming is competitive business -- particularly milk production. Farmer John figures that if he doesn't innovate in his milk production methods, his dairy business could get creamed!  
Fortunately, Farmer John has a good idea. His three prize dairy cows Bessie, Elsie, and Mildred each produce milk with a slightly different taste, and he plans to mix these together to get the perfect blend of flavors.  

To mix the three different milks, he takes three buckets containing milk from the three cows. The buckets may have different sizes, and may not be completely full. He then pours bucket 1 into bucket 2, then bucket 2 into bucket 3, then bucket 3 into bucket 1, then bucket 1 into bucket 2, and so on in a cyclic fashion, for a total of 100 pour operations (so the 100th pour would be from bucket 1 into bucket 2). When Farmer John pours from bucket a into bucket b, he pours as much milk as possible until either bucket a becomes empty or bucket b becomes full.  

Please tell Farmer John how much milk will be in each bucket after he finishes all 100 pours.  

INPUT FORMAT (file mixmilk.in):   
The first line of the input file contains two space-separated integers: the capacity c1 of the first bucket, and the amount of milk m1 in the first bucket. Both c1 and m1 are positive and at most 1 billion, with c1≥m1. The second and third lines are similar, containing capacities and milk amounts for the second and third buckets.   

OUTPUT FORMAT (file mixmilk.out):  
Please print three lines of output, giving the final amount of milk in each bucket, after 100 pour operations.   

SAMPLE INPUT:  
```
10 3
11 4
12 5
```
SAMPLE OUTPUT:  
```
0
10
2
```
In this example, the milk in each bucket is as follows during the sequence of pours:  
```
Initial State: 3  4  5  
1. Pour 1->2:  0  7  5  
2. Pour 2->3:  0  0  12
3. Pour 3->1:  10 0  2
4. Pour 1->2:  0  10 2
5. Pour 2->3:  0  0  12
(The last three states then repeat in a cycle ...)
```


Problem credits: Brian Dean  


{% highlight python linenos %}
fin = open("mixmilk.in", "r")
fout = open("mixmilk.out", "w")

c = []

for x in range(3):
    c.append(list(map(int, fin.readline().split())))

bucket = [0] + [c[x - 1][1] for x in range(1, 4)]


for x in range( 100):
    one = x % 3 + 1
    two = ( x + 1) % 3 +1

    spaceLeftInTwo = c[two  - 1][0] - bucket[two]

    actualMilkPoured = min(bucket[one], spaceLeftInTwo)

    bucket[one] -= actualMilkPoured

    bucket[two] += actualMilkPoured



for x in range(1,4):
    fout.write(str(bucket[x]) + "\n")
{% endhighlight %}

## Problem 2. Mixing Milk    


[The Bucket List](http://www.usaco.org/index.php?page=viewproblem2&cpid=856)   

Farmer John is considering a change in how he allocates buckets for milking his cows. He thinks this will ultimately allow him to use a small number of total buckets, but he is not sure how many exactly. Please help him out!  
Farmer John has N cows (1≤N≤100), conveniently numbered 1…N. The ith cow needs to be milked from time si to time ti, and requires bi buckets to be used during the milking process. Several cows might end up being milked at the same time; if so, they cannot use the same buckets. That is, a bucket assigned to cow i's milking cannot be used for any other cow's milking between time si and time ti. The bucket can be used for other cows outside this window of time, of course. To simplify his job, FJ has made sure that at any given moment in time, there is at most one cow whose milking is starting or ending (that is, the si's and ti's are all distinct).  

FJ has a storage room containing buckets that are sequentially numbered with labels 1, 2, 3, and so on. In his current milking strategy, whenever some cow (say, cow i) starts milking (at time si), FJ runs to the storage room and collects the bi buckets with the smallest available labels and allocates these for milking cow i.  

Please determine how many total buckets FJ would need to keep in his storage room in order to milk all the cows successfully.  

INPUT FORMAT (file blist.in):  
The first line of input contains N. The next N lines each describe one cow, containing the numbers si, ti, and bi, separated by spaces. Both s_i and t_i are integers in the range 1…1000, and bi is an integer in the range 1…10.  
OUTPUT FORMAT (file blist.out):  
Output a single integer telling how many total buckets FJ needs.  
SAMPLE INPUT:  
```
3  
4 10 1  
8 13 3  
2 6 2
```  
SAMPLE OUTPUT:  
```
4
```
In this example, FJ needs 4 buckets: He uses buckets 1 and 2 for milking cow 3 (starting at time 2). He uses bucket 3 for milking cow 1 (starting at time 4). When cow 2 arrives at time 8, buckets 1 and 2 are now available, but not bucket 3, so he uses buckets 1, 2, and 4.  

Problem credits: Brian Dean  


{% highlight python linenos %}  
fin, fout = open('blist.in'), open('blist.out', 'w')  

N = int(fin.readline())  
events = []

for _ in range(N):
    f = fin.readline().split()
    events.append((int(f[0]), 0, int(f[2])))
    events.append((int(f[1]), 1, int(f[2])))

events.sort()
curBuckets = 0
storedBuckets = 0

for event in events:
    if event[1] == 0:
        if event[2] - storedBuckets >= 0:
            curBuckets += event[2]
            storedBuckets = 0

        elif storedBuckets - event[2] > 0:
            curBuckets += event[2]
            storedBuckets -= event[2]

    else:
        curBuckets -= event[2]
        storedBuckets += event[2]

fout.write(str(storedBuckets))
{% endhighlight %}
