---
title: "0/1 Knapsack and UnBounded Knapsack Problem"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Knapsack
  - Backtracking
---

## 0/1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the items such that sum of the weights of those items of given subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

### Solution  1: DP

{% highlight C++ linenos %}
int knapSack(int W, int wt[], int val[], int n)
{
    int i, w;
    int K[n + 1][W + 1];

    // Build table K[][] in bottom up manner
    for (i = 0; i <= n; i++)
    {
        for (w = 0; w <= W; w++)
        {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]],
                          K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }

    return K[n][W];
}
{% endhighlight %}

### Solution  2: Backtrack
With little modification, backtrack algorithm can be used to solve 0/1 knapsack Problem

{% highlight C++ linenos %}
int knapSack(int W, int wt[], int val[], int n)
{

    // Base Case
    if (n == 0 || W == 0)
        return 0;

    // If weight of the nth item is more than Knapsack capacity W, then
    // this item cannot be included  in the optimal solution
    if (wt[n - 1] > W)
        return knapSack(W, wt, val, n - 1);

    // Return the maximum of two cases:
    // (1) nth item included
    // (2) not included
    else
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1));
}
{% endhighlight %}



##  Unbounded Knapsack Problem

Given a knapsack weight W and a set of n items with certain value val[i] and weight wt[i], we need to calculate the maximum amount that could make up this quantity exactly.  
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.

{% highlight C++ linenos %}
int unboundedKnapsack(int W, int n, int val[], int wt[])
{
    // dp[i] is going to store maximum value with knapsack capacity i.
    int dp[W+1];
    memset(dp, 0, sizeof dp);

    // Fill dp[] using above recursive formula
    for (int i=0; i<=W; i++)
      for (int j=0; j<n; j++)
         if (wt[j] <= i)
            dp[i] = max(dp[i], dp[i-wt[j]] + val[j]);

    return dp[W];
}
{% endhighlight %}
