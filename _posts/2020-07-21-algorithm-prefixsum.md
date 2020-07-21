---
title: "Prefix Sum"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - PrefixSum
---

## Subarray Sums Divisible by K

[Leetcode  Subarray Sums Divisible by K] (https://leetcode.com/problems/subarray-sums-divisible-by-k/)  

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
