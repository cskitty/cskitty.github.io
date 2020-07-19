---
title: "Longest Increasing Subsequence"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Dynamic Programming
---

## Longest Increasing Subsequence

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence).

Longest Increasing Subsequence finds the longest (not necessarily continuous) sub-sequence given a sequence.

Example:

Input: [1, 4, 2, 5]
Output: 3

(Explanation: The length of the longest increasing subsequence can be found through finding either [1, 2, 5] or [1, 4, 5])


{% highlight java linenos %}
class Solution {

    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int[] dp = new int[nums.length];
        dp[0] = 1;

        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            // nums[i] = current integer
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int max = 0;
        for (int i = 0; i < dp.length; i++) {
            if (dp[i] > max) {
                max = dp[i];
            }
        }
        return max;
    }

}

{% endhighlight %}
