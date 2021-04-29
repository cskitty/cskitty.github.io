---
title: "Central Europe 2003: Minimizing maximizer"
categories:
  - USACO
tags:
  - Algorithms
  - State Compression DP
---

# Central Europe 2003: Minimizing maximizer

Description

 [POJ 1769](http://poj.org/problem?id=1769)

 The company Chris Ltd. is preparing a new sorting hardware called Maximizer. Maximizer has n inputs numbered from 1 to n. Each input represents one integer. Maximizer has one output which represents the maximum value present on Maximizer's inputs.

 Maximizer is implemented as a pipeline of sorters Sorter(i1, j1), ... , Sorter(ik, jk). Each sorter has n inputs and n outputs. Sorter(i, j) sorts values on inputs i, i+1,... , j in non-decreasing order and lets the other inputs pass through unchanged. The n-th output of the last sorter is the output of the Maximizer.

 An intern (a former ACM contestant) observed that some sorters could be excluded from the pipeline and Maximizer would still produce the correct result. What is the length of the shortest subsequence of the given sequence of sorters in the pipeline still producing correct results for all possible combinations of input values?

 Task
 Write a program that:

 reads a description of a Maximizer, i.e. the initial sequence of sorters in the pipeline,
 computes the length of the shortest subsequence of the initial sequence of sorters still producing correct results for all possible input data,
 writes the result.


Input

The first line of the input contains two integers n and m (2 <= n <= 50000, 1 <= m <= 500000) separated by a single space. Integer n is the number of inputs and integer m is the number of sorters in the pipeline. The initial sequence of sorters is described in the next m lines. The k-th of these lines contains the parameters of the k-th sorter: two integers ik and jk (1 <= ik < jk <= n) separated by a single space.

Output

The output consists of only one line containing an integer equal to the length of the shortest subsequence of the initial sequence of sorters still producing correct results for all possible data.

SAMPLE INPUT:
```
40 6
20 30
1 10
10 20
20 30
15 25
30 40
```

SAMPLE OUTPUT:
```
4
```

Hint

Huge input data, scanf is recommended.

Solution:

* State: Create a dp state with dp[i][j] where i is the current city and j is the state of remaining tickets
* Use a binary number to represent j, and the tickets used (visualization: 010010010 where 1 represents the remaining tickets). For N tickets, we have 2^N states for j
* State transition: suppose we use ticket k to transfer from city j to city i
for (int j = 0; j < N; j++) {
   if (dist[i][j] >= 0) {
      dp[i][S & ~(1 << k)] = min(dp[i][S & ~(1 << k)], dp[j][S] + dist[i][j]/tickets[k])      
   }
}


{% highlight C++ linenos %}
// not including macros

#include <bits/stdc++.h>
using namespace std;

int t[15];
int dist[35][35];
double dp[1 << 10][35];  

int main()
{
	int n, m, p, a, b;

	while (~scanf_s("%d%d%d%d%d", &n, &m, &p, &a, &b) && (n || m || p || a || b))
	{
		for (int i = 0; i<n; i++)
			scanf_s("%d", &t[i]);
		memset(mp, -1, sizeof(mp));

		while (p--)
		{
			int u, v, w;
			scanf_s("%d%d%d", &u, &v, &w);
			u--, v--;
			if (dist[u][v]<0)
				dist[u][v] = dist[v][u] = w;
			else
				dist[u][v] = dist[v][u] = min(dist[u][v], w);
		}

		memset(dp, 127, sizeof(dp));


		dp[(1 << n) - 1][a - 1] = 0;
		double ans = INF;

		for (int s = (1 << n) - 1; s >= 0; s--)
		{
			for (int v = 0; v<m; v++)
			   for (int i = 0; i<n; i++)
			      if (s >> i & 1)
			          for (int u = 0; u<m; u++)
			             if (dist[v][u] >= 0)
				               dp[s & ~(1 << i)][u] = min(dp[s & ~(1 << i)][u], dp[s][v] + dist[v][u] * 1.0 / t[i]);
		}

		for (int i = 0; i < (1 << n); i++){
			ans = min(ans, dp[i][b - 1]);
		}

		if (ans == INF)
			printf_s("Impossible\n");
		else
			printf_s("%.3lf\n", ans);
	}
	return 0;
}
{% endhighlight %}
