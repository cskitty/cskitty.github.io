---
title: "Climbing Stairs"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Dynamic Programming
---

## Climbing Stairs

[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/).

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps  

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


{% highlight java linenos %}
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];

        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n - 1];
    }

}

{% endhighlight %}

## Min Cost Climbing Stairs

[Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/).

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:  
Input: cost = [10, 15, 20]  
Output: 15  
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.  
Example 2:  
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  
Output: 6  
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].  


Let A(n) be the answer, i.e., minimum cost to climb to step n.  
* Consider the last step (or, equivalently the first step), do a case analysis.  What are the possible cases?
* Case one: last step is 1.  
* Case two: last step is 2.
* Thus A(n) = cost[n] + min(A(n-1), A(n-2)).


{% highlight java linenos %}
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] minCost = new int[cost.length + 1];

        minCost[0] = cost[0];
        minCost[1] = cost[1];

        for (int i = 2; i < cost.length; i++) {
            minCost[i] = Math.min(minCost[i - 1], minCost[i - 2]) + cost[i];
        }

        minCost[minCost.length - 1] = Math.min(minCost[minCost.length - 2], minCost[minCost.length - 3]);

        return minCost[minCost.length - 1];
    }
}
{% endhighlight %}
