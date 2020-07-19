---
title: "House Robber"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Dynamic Programming
---

## House Robber

[leetcode: House Robber](https://leetcode.com/problems/house-robber/).

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.  



Example 1:  

Input: nums = [1,2,3,1]  
Output: 4  
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).  
             Total amount you can rob = 1 + 3 = 4.  
Example 2:  

Input: nums = [2,7,9,3,1]  
Output: 12  
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).  
             Total amount you can rob = 2 + 9 + 1 = 12.  


Constraints:  

0 <= nums.length <= 100  
0 <= nums[i] <= 400  

{% highlight java linenos %}
class Solution {
    public int rob(int[] nums) {
        if (nums.length <= 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = nums[1];

        for (int i = 2; i < nums.length; i++) {
            int x = 0;
            for (int j = 0; j < i - 1; j++) {
                x = Math.max(x, dp[j] + nums[i]);
            }
            dp[i] = x;
        }

        int max = 0;
        for (int i = 0; i < dp.length; i++) {
            max = Math.max(dp[i], max);
        }
        return max;
    }
}
{% endhighlight %}


## House Robber II

[leetcode: House Robber](https://leetcode.com/problems/house-robber-ii/).

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.  

Example 1:  

Input: [2,3,2]  
Output: 3  
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),  
             because they are adjacent houses.  
Example 2:  

Input: [1,2,3,1]  
Output: 4  
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).  
             Total amount you can rob = 1 + 3 = 4.  

{% highlight java linenos %}  
class Solution {  
    public int rob(int[] nums) {  

        if (nums.length == 0) {
            return 0;
        }

        if (nums.length == 1) {
            return nums[0];
        }

        int[] dp = new int[nums.length];

        dp[0] = nums[0];
        int max = dp[0];

        // first not end
        for (int i = 1; i < nums.length - 1; i++) {
            // i = current house being robbed
            dp[i] = nums[i];
            for (int j = 0; j < i - 1; j++) {
                dp[i] = Math.max(nums[i] + dp[j], dp[i]);
            }
            max = Math.max(dp[i], max);
        }

        // end not first
        dp = new int[nums.length];
        dp[1] = nums[1];
        int secondMax = dp[1];
        for (int i = 2; i < nums.length; i++) {
            dp[i] = nums[i];
            for (int j = 1; j < i - 1; j++) {
                dp[i] = Math.max(nums[i] + dp[j], dp[i]);
            }
            secondMax = Math.max(dp[i], secondMax);
        }

        return Math.max(max, secondMax);
    }
}
{% endhighlight %}
