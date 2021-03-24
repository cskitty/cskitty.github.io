---
title: "DP Finite Automata with Compression: Treasure Hunt"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Finite Automata
---

## DP Finite Automata with Compression: Treasure Hunt

Bessie, who participated in the archaeological excavation, got a treasure map, and the treasure map marked n under ground treasure houses. There are total m possible roads available for development.

Bessie is determined to go personally to dig out the treasures in all the treasure houses.

However, each treasure house is very far from the ground, that is to say, it is very difficult to open a road from the ground to a certain treasure house, and it is relatively easy to develop a road between the treasure houses.

Bessie's determination moved the sponsor of the archaeological excavation. The sponsor decided to sponsor her to open up a passage from the ground to a certain treasure house for free. Bessie can choose any of the n places to open a passage from the ground to that treasure house.

Based on this, Bessie also needs to consider how to dig the road between the treasure houses.

The roads that have been excavated can be used at will without cost.

Every time a new road is excavated, Bessie will work with the archaeological team to unearth the treasures of the treasure house that can be reached by that road.

In addition, Bessie does not want to develop useless roads, that is, the road between two treasure houses that have been excavated does not need to be developed.

The cost of developing a new road is:  

The length of the road × The number of treasure houses that have passed from the treasure house that the sponsor helped her to open to the treasure house at the beginning of the road (including the treasure house that the sponsor helped her open and the treasure house at the beginning of the road). 

Please write a program for Bessie to select the treasure house opened by the sponsor and the road to be excavated afterwards, so as to minimize the total cost of the project, and output this minimum value.

Input format

Two positive integers separated by spaces on the first line n with m, Represents the number of treasure houses and the number of roads.

Next m Line, each line has three positive integers separated by spaces, which are the numbers of the two treasure houses connected by a road (the numbers are 1 ∼ n ), and the length of the road v.

Output format
The output is a line, a positive integer, which represents the smallest total cost.

data range
1 ≤ n ≤ 12,
0 ≤ m ≤ 1000,
v ≤ 5 ∗ 105


Sample Input:
```
4 5
1 2 1
1 3 3
1 4 1
2 3 4
3 4 1
```
Sample Output:
```
4
```

### Solution

Basically this question is to find a MST for all treasure houses and make the minimal cost to build MST.  
* We use a bit vector to represent a subset of currently connected treasure houses.  
* A 1 bit in position i means the i-th treasure house is included in the subsets
* dp[i][k] represents the minimal cost to build MST for subset i (bit vector), and the maximal depth of the MST is j.  
* State transition:
```
  for j in subset(i):
     get the remaining set of j from i: remain = i ^ j
     get the minimal cost to expand to all nodes in remain from any node in set j
     dp[i][k] = min (dp[i][k], dp[j][k - 1] + min_cost_to_remain * k)
```


{% highlight C++ linenos %}
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 12, M = 1 << 12, INF = 0x3f3f3f3f;

int n, m;
int d[N][N];
int f[M][N], reachable[M];

int main()
{
    scanf("%d%d", &n, &m);

    memset(d, 0x3f, sizeof d);
    for (int i = 0; i < n; i ++ )
      d[i][i] = 0;

    while (m -- )
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        a --, b --;
        d[a][b] = d[b][a] = min(d[a][b], c);
    }

    //pre-calculate the reachable set reachable[i] for given set i
    for (int i = 1; i < 1 << n; i ++ )
        for (int j = 0; j < n; j ++ )
            if (i >> j & 1)
            {
                for (int k = 0; k < n; k ++ )
                    if (d[j][k] != INF)
                      reachable[i] |= 1 << k;
            }

    //initialization. minimal cost to set of 1 nodes is 0
    memset(f, 0x3f, sizeof f);
    for (int i = 0; i < n; i ++ )
      f[1 << i][0] = 0;

    //iterate through all possible subsets of n nodes
    for (int i = 1; i < 1 << n; i ++ )
        //iterate through all subsets of set i
        for (int j = i - 1; j; j = (j - 1) & i)
            //validness check: subset j's reachable set must be inside set i
            //otherwise, j is an invalid subset
            if ((reachable[j] & i) == i)
            {
                //remain is the set of nodes not in j but in i
                int remain = i ^ j;
                //calculate the minimal cost of building roads to reach all nodes in set remain
                int cost = 0;
                for (int k = 0; k < n; k ++ )
                    if (remain >> k & 1)
                    {
                        int t = INF;
                        for (int u = 0; u < n; u ++ )
                            if (j >> u & 1)
                                t = min(t, d[k][u]);
                        cost += t;
                    }

                //iterate through all possible depth of the MST of set i
                for (int k = 1; k < n; k ++ )
                  f[i][k] = min(f[i][k], f[j][k - 1] + cost * k);
            }

    int res = INF;
    for (int i = 0; i < n; i ++ )
      res = min(res, f[(1 << n) - 1][i]);

    printf("%d\n", res);
    return 0;
}
{% endhighlight %}
