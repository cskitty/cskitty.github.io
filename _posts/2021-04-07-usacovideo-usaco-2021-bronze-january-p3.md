---
title: USACO 2021 Bronze January P3. Just Stalling
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2021 Bronze January P3: Just Stalling](http://usaco.org/index.php?page=viewproblem2&cpid=1085)  

{% include video id="w89ku-wpE9I" provider="youtube" %}


{% highlight python linenos %}
N = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))
ans = 1
cows.sort(reverse=True)
stalls.sort(reverse=True)
stallsCanBeIn = [0] * N

for i in range(N):
    for stall in stalls:
        if stall >= cows[i]:
            stallsCanBeIn[i] += 1
i = 0
for stall in stallsCanBeIn:
    ans *= stall - i
    i += 1
{% endhighlight %}  
