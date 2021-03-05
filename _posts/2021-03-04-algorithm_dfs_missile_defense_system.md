---
title: "Missile Defense System"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - DFS
---

## Missile Defense System

In order to counter the threat of malicious countries nearby, Country R has updated their missile defense system.

A missile defense system to intercept highly either been strictly monotonic rise or has been strictly monotonic decline.

For example, if a system intercepts two missiles with a height of 3 and a height of 4, then the system can only intercept missiles with a height greater than 4.

Given the height of a series of upcoming missiles, please find out at least how many sets of defense systems are needed to shoot them all down.

Input format
The input contains multiple sets of test cases.

For each test case, the first line contains the integer n, which represents the number of incoming missiles.

The second line contains n different integers, representing the height of each missile.

When the input test case n=0, it means that the input is terminated, and the test case does not need to be processed.

Output format
For each test case, output an integer that occupies a row to indicate the number of defense systems required.

data range
1 ≤ n ≤ 50

Sample Input:
```
5
3 5 2 4 1
0
```
Sample Output:
```
2
```

## Solution  
In this question, the interception height of a set of defense system’s missiles is either rising or falling, so the straight LIS algorithm is incorrect. In LIS, the core idea is whether an element can be added to the existing sequence, which is only related to the last element of the sequence. This key idea is used in this question.

The algorithm is to use backtrack BFS + LIS: maintain two sets of increasing sequences and decreasing sequences up[k] and down[k] to record the last missile intercepted by the k-th set of ascending (descending) system.  

Algorithm is a backtrack DFS function: dfs(u,su,sd) means that the u-th missile is being processed and we have su ascending sequences and sd descending sequences.

It stands to reason that every time a new number is obtained, all the sequences that can be put into it should be replayed.
However, there is a greedy strategy when expanding nodes, which greatly saves time.
Suppose you want to put a number into an ascending sequence, then it must be the one with the largest last element among all the ascending sequences that can be put into it.

In fact, think about it, since each number must be put in a sequence,
for the ascending sequence, the smaller it is currently, the more useful it is. Since it can be put into the larger one, why waste a small one?
Note that up[i] According to this strategy, the order is already in order, so just find the first one you encounter.

{% highlight C++ linenos %}
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 55;

int n;
int q[N];
int up[N], down[N];
int ans;

//u: index, su: len(up[]), sd: len(down[])
void dfs(int u, int su, int sd) {
    if (su + sd >= ans)
      return;

    if (u == n) {
        ans = su + sd;   
        return;
    }

    // put u to upper sequences
    int k = 0;
    while (k < su && up[k] >= q[u]) k ++;
    int t = up[k];
    up[k] = q[u];
    if (k < su) dfs(u + 1, su, sd);
    else dfs(u + 1, su + 1, sd);
    up[k] = t;

    // put u to down sequences
    k = 0;
    while (k < sd && down[k] <= q[u]) k ++;
    t = down[k];
    down[k] = q[u];
    if (k < sd) dfs(u + 1, su, sd);
    else dfs(u + 1, su, sd + 1);
    down[k] = t;
}

int main() {
    while (cin >> n, n) {
        for (int i = 0; i < n; i ++)
            cin >> q[i];

        ans = n;
        dfs(0, 0, 0);

        cout << ans << endl;
    }
}
{% endhighlight %}
