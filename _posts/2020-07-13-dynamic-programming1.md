---
title: "Dynamic Programming Examples"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Dynamic Programming
---

## Dynamic Programming Examples

Explanation

* Solving problems using recursion (using solutions to subproblems) and storing solutions of subproblems to avoid recomputation.
* Key is to figure out the recursion relationship.
* Sometimes need to define subproblems with more inputs.

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

##  Unique Paths II

[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/).

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:  

Input:  
[  
  [0,0,0],  
  [0,1,0],  
  [0,0,0]  
]  
Output: 2  
Explanation:  
There is one obstacle in the middle of the 3x3 grid above.  
There are two ways to reach the bottom-right corner:  
1. Right -> Right -> Down -> Down  
2. Down -> Down -> Right -> Right  

{% highlight java linenos %}
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[][] graph = new int[obstacleGrid.length][obstacleGrid[0].length];


        for (int i = 0; i < obstacleGrid.length; i++) {
            if (obstacleGrid[i][0] == 0) {
                graph[i][0] = 1;
            }
            else{
                break;
            }
        }

        for (int j = 0; j < obstacleGrid[0].length; j++) {
            if (obstacleGrid[0][j] == 0) {
                graph[0][j] = 1;
            }
            else{
                break;
            }
        }

        for (int i = 1; i < obstacleGrid.length; i++) {
            for (int j = 1; j < obstacleGrid[i].length; j++) {
                if (obstacleGrid[i][j] == 0) {
                    graph[i][j] = graph[i - 1][j] + graph[i][j - 1];
                }
            }
        }

        return graph[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
    }
}
{% endhighlight %}


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
