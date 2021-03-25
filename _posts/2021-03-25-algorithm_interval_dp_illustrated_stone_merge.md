---
title: "Interval DP Illustrated: Stone Merger"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Interval DP
---

## What is DP on Interval?

DP on interval is an extension of linear dynamic programming. When dividing the problem in stages, it has a lot to do with the order in which the elements appear in the stage and which elements from the previous stage are merged.

Features of interval DP:  

Merger : that is to integrate two or more parts, of course, it can also be reversed;  
Features : able to decompose the problem into a form that can be combined in pairs;  

Solution : Set the optimal value for the entire problem, enumerate the merge points, decompose the problem into two parts, and finally merge the optimal values ​​of the two parts to get the optimal value of the original problem.  

```
dp(i,j) = max(dp(i,j), dp(i,k) + dp(k+1,j) +cost)
```

## Interval DP Illustrated: Stone Merger


The piles of stones are discharged around the circular playground. Now the stones are to be combined into a pile in an orderly manner. It is stipulated that only two adjacent piles can be selected and merged into a new pile each time, and the number of stones in the new pile is recorded as the combined score.

Please write a program to read the heap count n and the number of stones in each pile, and calculate as follows:

Choose a scheme of merging stones (n-1 times) so that the sum of the combined scores is the largest.
Choose a scheme of merging stones (n-1 times) so that the sum of sub-merged scores is the smallest.


Sample Input:
```
4
4 5 9 4
```
Sample Output:
```
43
54
```

### Solution

Since the question is a ring, we duplicate the array to make an array of size 2xn. Then we can just use normal linear array interval DP.

{% highlight C++ linenos %}
#include<bits/stdc++.h>

using namespace std;

const int N = 420, INF = 0x3f3f3f3f;

int f[N][N];
int g[N][N];
int a[N];

int main()
{
    int n;
    cin >> n;
    memset(f,INF,sizeof f);
    memset(g,-INF,sizeof g);

    for(int i = 1; i <= n; i ++ )
    {
        cin >> a[i];
        a[i+n] = a[i];
    }

    //prefix sum and initialization
    for(int i = 1; i <= 2 * n; i ++ )
    {
        a[i] += a[i-1];
        g[i][i] = 0;
        f[i][i] = 0;
    }    

    //dp on interval: out loop is length, inner loop is the left bound
    for(int len = 2 ; len <= n ;len ++ )
      for(int l = 1; l + len - 1 <= 2 * n ; l ++ )
      {
          int r = l + len - 1;
          for(int k = l - 1 ; k <= r; k ++ )
          {
              f[l][r] = min(f[l][r],f[l][k-1] + f[k][r] + a[r] - a[l - 1] );
              g[l][r] = max(g[l][r],g[l][k-1] + g[k][r] + a[r] - a[l - 1] );
          }
      }

    int minv = INF , maxv = -INF;
    for(int i = 1; i <= n;i++)
        {
            minv = min(minv, f[i][i + n - 1]);
            maxv = max(maxv, g[i][i + n - 1]);
        }
     cout << minv << endl << maxv << endl;

      return 0;
}
{% endhighlight %}
