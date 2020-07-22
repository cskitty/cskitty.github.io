---
title: "Prefix Sum"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - PrefixSum
---

[Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)  

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.


{% highlight java linenos %}
class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        int half = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        for (int j = 0; j < nums.length; j++) {
            if (half + half + nums[j] == sum) {
                return j;
            }
            half += nums[j];
        }
        return -1;
    }
}
{% endhighlight %}



## Subarray Sums Divisible by K

[Leetcode  Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)  

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.  



Example 1:  

Input: A = [4,5,0,-2,-3,1], K = 5  
Output: 7  
Explanation: There are 7 subarrays with a sum divisible by K = 5:  
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]  


{% highlight java linenos %}
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] P = new int[A.length + 1];
        P[0] = 0;

        for (int i = 0; i < A.length; i++) {
            P[i + 1] = P[i] + A[i];
        }

        Map<Integer, Integer> remainders = new HashMap<Integer, Integer>();
        for (int i = 0; i < P.length; i++) {
            // if diff %k == 0, diff divisible
            int key = P[i] % K;
            if (key < 0) {
                key += K;
            }
            if (remainders.containsKey(key)) {
                remainders.put(key, remainders.get(key) + 1);
            }
            else {
                remainders.put(key, 1);
            }
        }

        int sum = 0;
        for (int i : remainders.values()) {
            sum += (i * (i - 1)) / 2 ;
        }
        return sum;
    }
}
{% endhighlight %}
