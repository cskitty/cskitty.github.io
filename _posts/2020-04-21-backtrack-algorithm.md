---
title: "Backtrack Algorithm"
categories:
  - Programming
tags:
  - Python
  - Algorithms
---

## Backtrack Algorithm

Backtrack algorithms are used to solve a lot of brute force based DFS search problems.

Let's take a look at Leetcode problem [46](https://leetcode.com/problems/permutations/)

Explanation

Given a collection of distinct integers, return all possible permutations.

Example

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

{% highlight python linenos %}
import copy

def backtrack(answer,  track, nums):
    if len(track) == len(nums):
        # python only: use deepcopy to create a duplicate of track and push to answer
        answer.append( copy.deepcopy(track))
        return
    else:
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            else:
                #push
                track.append(nums[i])
                #explore
                backtrack(answer, track, nums)
                #pop
                track.pop(len(track) - 1)

answer = []
track = []
nums = [1, 2, 3]
backtrack(answer, track, nums)
print(answer)

{% endhighlight %}
