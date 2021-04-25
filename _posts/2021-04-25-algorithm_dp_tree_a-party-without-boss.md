---
title: "A Party Without a Boss"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - DP on a Tree
---

## A Party Without a Boss

Description

A university has N Employees, numbered from 1 ∼ N.

Their workplace relation is like a tree rooted by the principal, where the parent node is the direct boss of the child node.

Each employee has a happiness index, using integers H_i Given, where 1 ≤ i ≤ N.

Now there is an anniversary party, but no staff is willing to attend the meeting with their direct boss (their parent node).

Under the premise that this condition is met, the organizer hopes to invite some employees to participate in the conference, so that the sum of the happiness index of all participating employees is the largest. Find the maximum value.

Input format

The first line contains the integer N.
The next N lines contain the value i where Line i contains the happiness index H_i of staff number i.  
The next N− 1 lines have the integers L and K where K is the direct boss of L.


Output format
Output the largest happiness index.

Restrictions:
1 ≤ N≤ 6000,
−128 ≤ H_i ≤ 127

Sample Input  
```
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
```

Sample Output
```
5
```

Solution  

We can create a dp array with state dp[i][j] where i represents the employee and j represents 0 if the employee doesn't go to the party, and 1 if the employee does.

* Employee doesn't go: We can choose between the maximum of the children (people working under the employee) going, or the children not going. dp[i][0] = max(dp[x][0], dp[x][1]) + max(dp[x + 1][0], dp[x + 1][1]) + ... max(dp[y][0], dp[y][1])
* Employee does go: The children cannot go, thus it can only be dp[i][1] = dp[x][0] + dp[x + 1][0] + ... + dp[y][0]

### Solution  

{% highlight C++ linenos %}
#include <iostream>
#include <cstdio>
using namespace std;

int dp[6010][2];
int f[6010][2];
int ind[6010];
int vis[6010];
int root;

// dfs from leaf node up
void dfs(int u) {
    if(!u) return;
    vis[u] = 1;
    root = u;
    dp[f[u][0]][0] += max(dp[u][1] + f[u][1], dp[u][0]);
    dp[f[u][0]][1] += dp[u][0];
    ind[f[u][0]]--;
    if(! ind[f[u][0]]) {
      dfs(f[u][0]);
    }
}

int main() {
    int n = 0;
    cin >> n;

    // f[i][0] = parent
    // f[i][1] = happiness index

    for(int i=1;i<=n;i++) {
        cin >> f[i][1];
    }
    int a,b;

    for(int i=1;i<n;i++) {
        cin >> a >> b;
        f[a][0] = b;
        // ind keeps child #
        ind[b]++;
    }

    for(int i=1;i<=n;i++)
        if(!vis[i]&&!ind[i]) // is a leaf node, has not been visited and no children
            dfs(i);

    printf("%d\n",max(dp[root][0], dp[root][1]+f[root][1]));
}

{% endhighlight %}
