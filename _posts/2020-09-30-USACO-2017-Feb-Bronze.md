---
title: "USACO 2017 Feb Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - Python
  - USACO
---

# USACO 2017 Feb Bronze                    

## Problem 1. Why Did the Cow Cross the Road  

[Why Did the Cow Cross the Road](http://usaco.org/index.php?page=viewproblem2&cpid=711)    

While the age-old question of why chickens cross roads has been addressed in great depth by the scientific community, surprisingly little has been published in the research literature on the related subject of cow crossings. Farmer John, well-aware of the importance of this issue, is thrilled when he is contacted by a local university asking for his assistance in conducting a scientific study of why cows cross roads. He eagerly volunteers to help.
As part of the study, Farmer John has been asked to document the number of times each of his cows crosses the road. He carefully logs data about his cows' locations, making a series of N observations over the course of a single day. Each observation records the ID number of a cow (an integer in the range 1…10, since Farmer John has 10 cows), as well as which side of the road the cow is on.  

Based on the data recorded by Farmer John, please help him count the total number of confirmed crossings. A confirmed crossing occurs when a consecutive sightings of a cow place it on different sides of the road.  

INPUT FORMAT (file crossroad.in):  
The first line of input contains the number of observations, N, a positive integer at most 100. Each of the next N lines contains one observation, and consists of a cow ID number followed by its position indicated by either zero or one (zero for one side of the road, one for the other side).  
OUTPUT FORMAT (file crossroad.out):  
Please compute the total number of confirmed crossings.  
SAMPLE INPUT:  
```
8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
```
SAMPLE OUTPUT:
```
3
```
In this example, cow 3 crosses twice -- she first appears on side 1, then later appears on side 0, and then later still appears back on side 1. Cow 4 definitely crosses once. Cows 2 and 6 do not appear to cross.

Problem credits: Brian Dean

{% highlight python linenos %}
fin, fout = open('crossroad.in'), open('crossroad.out', 'w')

n = int(fin.readline())

sightings = []

dic = {}
for x in range(n):
    sightings.append( fin.readline().split())


for cow, val in sightings:
    try:
        dic[cow] += val
    except:
        dic[cow] = val


def find(x):
    count = 0
    for f in range(len(x) - 1):
        if x[f] + x[f + 1] == '01' or x[f] + x[f + 1] == '10':
            count += 1

    return count


count = 0
for k in dic:
    val = dic[k]
    count += find(val)


fout.write(str(count))
{% endhighlight %}

## Problem 3. Why Did the Cow Cross the Road III  

[Why Did the Cow Cross the Road III](usaco.org/index.php?page=viewproblem2&cpid=713)  

Farmer John, in his old age, has unfortunately become increasingly grumpy and paranoid. Forgetting the extent to which bovine diversity helped his farm truly flourish over the years, he has recently decided to build a huge fence around the farm, discouraging cows from neighboring farms from visiting, and completely prohibiting entry from a handful of neighboring farms. The cows are quite upset by this state of affairs, not only since they can no longer visit with their friends, but since it has caused them to cancel participation in the International Milking Olympiad, an event to which they look forward all year.
Neighboring cows that still have the ability to enter Farmer John's property find the process has become more arduous, as they can enter only through a single gate where each cow is subject to intense questioning, often causing the cows to queue up in a long line.  

For each of the N cows visiting the farm, you are told the time she arrives at the gate and the duration of time required for her to answer her entry questions. Only one cow can be undergoing questioning at any given time, so if many cows arrive near the same time, they will likely need to wait in line to be processed one by one. For example, if a cow arrives at time 5 and answers questions for 7 units of time, another cow arriving at time 8 would need to wait until time 12 to start answering questions herself.  

Please determine the earliest possible time by which all cows are able to enter the farm.  

INPUT FORMAT (file cowqueue.in):  
The first line of input contains N, a positive integer at most 100. Each of the next N lines describes one cow, giving the time it arrives and the time it requires for questioning; each of these numbers are positive integers at most 1,000,000.  
OUTPUT FORMAT (file cowqueue.out):  
Please determine the minimum possible time at which all the cows could have completed processing.  
SAMPLE INPUT:
```
3
2 1
8 3
5 7
```
SAMPLE OUTPUT:
```
15
```
Here, first cow arrives at time 2 and is quickly processed. The gate remains briefly idle until the third cow arrives at time 5, and begins processing. The second cow then arrives at time 8 and waits until time 5+7=12 to start answering questions, finishing at time 12+3 = 15.

Problem credits: Brian Dean

{% highlight python linenos %}
fIn, fOut = open("cowqueue.in"), open("cowqueue.out", "w")

n = int(fIn.readline())
cows = []

for cow in range(n):
    cows.append(tuple(map(int, fIn.readline().strip().split())))

cows.sort(key=lambda x: (x[0], x[1]))
cowsinline = []

time = 0

for cow in cows:
    if cow[0] > time:
        time = cow[0]
    time += cow[1]

fOut.write(str(time))
{% endhighlight %}
