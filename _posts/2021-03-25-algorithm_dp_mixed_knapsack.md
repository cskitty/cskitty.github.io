---
title: "DP Mixed Knapsack"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Knapsack
  - Multiple Knapsack
---

## DP Mixed Knapsack Problem

Have N Kinds of items and a capacity V Backpack.

There are three categories of items:

Items of the first category can only be used once (01 backpack);
The second type of items can be used unlimited times (complete backpack);
The third type of items can only be used at most si Times (multiple backpacks);
Each volume is vi, The value is wi.

Solve which items are loaded into the backpack, so that the total volume of the items does not exceed the capacity of the backpack, and the total value is the largest.
Output the maximum value.

Input format
Two integers in the first line, N, V, Separated by spaces, respectively indicate the number of objects and the volume of the backpack.

Next there are N Lines, three integers per line vi,wi,si, separated by spaces, indicating the i-th item's volume, value, and quantity.

si = − 1 Represents the first i This item can only be used once;
si = 0 Represents the first i This item can be used unlimited times;
si > 0 Represents the first i Kinds of items can be used si Times

Output format
Output an integer that represents the maximum value.

data range
0 < N, V≤ 1000
0 <vi,wi≤ 1000
− 1 ≤si≤ 1000

Sample Input:
```
4 5
1 2 -1
2 4 1
3 4 0
4 5 2
```
Sample Output:
```
8
```

### Solution
{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;
int n,m,v[100010],w[100010],dp[100010];

int main()
{
    cin>>n>>m;
    int cnt=1;
    for(int i=1;i<=n;i++)
    {
        int a,b,s;
        cin>>a>>b>>s;

        int k=1;
        //convert 0/1 to multiple knapsack with quantity = 1
        if(s<0)
           s=1;
        else
           //convert unbounded knapsack to multiple knapsack with quantity = m/a
           //since this item can have at most m/a
          if(s==0)
            s= m/a;

        //now that we already converted all three types of knapsack to multiple knapsack
        //we then solve multiple knapsack using binary optimation
        //to do that, we create new items by packaging multiple items(0 to 2^log(2,s))
        while(k<=s)
        {
            v[cnt]=a*k;
            w[cnt]=b*k;
            s-=k;
            k*=2;
            cnt++;
        }

        if(s>0)
        {
            v[cnt]=s*a;
            w[cnt]=s*b;
            cnt++;
        }
    }


    //solve the problem using 0/1 knapsack
    for(int i=1;i<=cnt;i++)
    {
        for(int j=m;j>=v[i];j--)
        {
            dp[j]=max(dp[j],dp[j-v[i]]+w[i]);
        }
    }

    cout<<dp[m]<<endl;
    return 0;
}

{% endhighlight %}
