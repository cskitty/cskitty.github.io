---
title: "Dynamic Programming: Longest Increasing Subsequence O(NlogN) Algorithm"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Longest Increasing Subsequence O(NlogN) Algorithm

Longest Increasing Subsequence (LIS) problems find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.

Sample Input:
```
8
186 186 150 200 160 130 197 220
```
Sample Output:
```
4
```

## Solution  

Maintain a set of active lists of varying length, each list is an increasing sequence, lists are sorted by their length.
Scan through input array and insert A[i] to these lists. We scan the lists (for end elements) in decreasing order of their length.

We will use the end elements of all the lists to find a list whose end element is smaller than A[i].

* If A[i] is smallest among all end candidates of active lists, we will start new active list of length 1.
* If A[i] is largest among all end candidates of active lists, we clone the list and extend the largest list by A[i].
* If A[i] is in between, we will find a list with largest end element that is smaller than A[i]. Clone and extend the cloned list by A[i]. If there's another list with the same size as this extended list, remove that list. So for each list length, we only keep the list with the smallest end elements.  

As we can use binary search to find the list based on  A[i], the complexitiy is N (A[i] loop) * log(N) (binary search).

{% highlight C++ linenos %}
int lengthOfLIS(vector<int>& nums)
{
  //we only need to store end element of each list in a sorted set
  set<int> s;
  for (auto a : nums) {
    //do nothing if a list end element is same as a
    if (s.find(a) != s.end())
      continue;

    //this works for smallest a, biggest a, and also work for middle a
    s.insert(a);

    auto it = s.upper_bound(a);

    //upper_bound equals it only means we have two lists with same size
    //remove list with biggest end element
    if (it != s.end())
      s.erase(it);
  }
  return s.size();
};
{% endhighlight %}
