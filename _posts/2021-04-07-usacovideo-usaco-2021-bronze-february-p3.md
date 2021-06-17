---
title: USACO 2021 Bronze February P3. Clockwise Fence
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2021 Bronze February P3. Clockwise Fence](http://usaco.org/index.php?page=viewproblem2&cpid=1109)  

{% include video id="Xjp7lq2aXJs" provider="youtube" %}


{% highlight python linenos %}
def cross_product(p1, p2):
    return p1[0] * p2[1] - p2[0] * p1[1]

for i in range (int(input())):
    p0 = (0, 0)
    sum = 0
    direction  = input()
    for d in direction:
        if d == 'N':
            p1 = (p0[0], p0[1] + 1)
        elif d == 'E':
            p1 = (p0[0] + 1, p0[1])
        elif d == 'S':
            p1 = (p0[0], p0[1] - 1)
        else:
            p1 = (p0[0] - 1, p0[1])
        sum += cross_product(p1, p0)
        p0 = p1

    if sum > 0:
        print("CW")
    else:
        print("CCW")
{% endhighlight %}  
