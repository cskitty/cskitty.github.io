---
title: "0/1 Knapsack Problem"
categories:
  - Programming
tags:
  - Python
  - Algorithms
---

## 0/1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the items such that sum of the weights of those items of given subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

With little modification, backtrack algorithm can be used to solve 0/1 knapsack Problem


{% highlight python linenos %}
import copy

ans = [0, []]

def backtrack(currentPath, data):
    global ans
    currentWeight = 0
    currentVal = 0
    for i in currentPath:
        currentWeight += data[i][1]
        currentVal += data[i][0]
        if (currentWeight > W):
            return
    # print(currentVal, currentPath, currentWeight, ans)
    if (currentVal >= ans[0]):
        ans = [currentVal, copy.deepcopy(currentPath)]
        # print (ans)
    if (len(currentPath) == len(data)):
        return
    else:
        for i in range(len(data)):
            if (i in currentPath):
                continue
            else:
                # add
                currentPath.append(i)
                # explore
                backtrack(currentPath, data)
                # pop
                currentPath.pop()
                # print (ans)


currentPath = []

val = [40, 100, 50, 60]
wt = [20, 10, 40, 30]
W = 60

data = []
for i in range(len(val)):
    data.append((val[i], wt[i]))
backtrack(currentPath, data)

print(ans)

{% endhighlight %}
