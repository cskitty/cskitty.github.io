---
title: "Japan 2005 Domestic: Traveling by Stagecoach"
categories:
  - USACO
tags:
  - Algorithms
  - State Compression DP
---

# Japan 2005 Domestic: Traveling by Stagecoach

Description

 [POJ 2686](http://poj.org/problem?id=2686)

Once upon a time, there was a traveler.

He plans to travel using stagecoaches (horse wagons). His starting point and destination are fixed, but he cannot determine his route. Your job in this problem is to write a program which determines the route for him.

There are several cities in the country, and a road network connecting them. If there is a road between two cities, one can travel by a stagecoach from one of them to the other. A coach ticket is needed for a coach ride. The number of horses is specified in each of the tickets. Of course, with more horses, the coach runs faster.

At the starting point, the traveler has a number of coach tickets. By considering these tickets and the information on the road network, you should find the best possible route that takes him to the destination in the shortest time. The usage of coach tickets should be taken into account.

The following conditions are assumed.
A coach ride takes the traveler from one city to another directly connected by a road. In other words, on each arrival to a city, he must change the coach.
Only one ticket can be used for a coach ride between two cities directly connected by a road.
Each ticket can be used only once.
The time needed for a coach ride is the distance between two cities divided by the number of horses.
The time needed for the coach change should be ignored.


Input

The input consists of multiple datasets, each in the following format. The last dataset is followed by a line containing five zeros (separated by a space).

n m p a b
t1 t2 ... tn
x1 y1 z1
x2 y2 z2
...
xp yp zp

Every input item in a dataset is a non-negative integer. If a line contains two or more input items, they are separated by a space.

n is the number of coach tickets. You can assume that the number of tickets is between 1 and 8. m is the number of cities in the network. You can assume that the number of cities is between 2 and 30. p is the number of roads between cities, which may be zero.

a is the city index of the starting city. b is the city index of the destination city. a is not equal to b. You can assume that all city indices in a dataset (including the above two) are between 1 and m.

The second line of a dataset gives the details of coach tickets. ti is the number of horses specified in the i-th coach ticket (1<=i<=n). You can assume that the number of horses is between 1 and 10.

The following p lines give the details of roads between cities. The i-th road connects two cities with city indices xi and yi, and has a distance zi (1<=i<=p). You can assume that the distance is between 1 and 100.

No two roads connect the same pair of cities. A road never connects a city with itself. Each road can be traveled in both directions.

Output

For each dataset in the input, one line should be output as specified below. An output line should not contain extra characters such as spaces.

If the traveler can reach the destination, the time needed for the best route (a route with the shortest time) should be printed. The answer should not have an error greater than 0.001. You may output any number of digits after the decimal point, provided that the above accuracy condition is satisfied.

If the traveler cannot reach the destination, the string "Impossible" should be printed. One cannot reach the destination either when there are no routes leading to the destination, or when the number of tickets is not sufficient. Note that the first letter of "Impossible" is in uppercase, while the other letters are in lowercase.


SAMPLE INPUT:
```
3 4 3 1 4
3 1 2
1 2 10
2 3 30
3 4 20
2 4 4 2 1
3 1
2 3 3
1 3 3
4 1 2
4 2 5
2 4 3 4 1
5 5
1 2 10
2 3 10
3 4 10
1 2 0 1 2
1
8 5 10 1 5
2 7 1 8 4 5 6 3
1 2 5
2 3 4
3 4 7
4 5 3
1 3 25
2 4 23
3 5 22
1 4 45
2 5 51
1 5 99
0 0 0 0 0
```
SAMPLE OUTPUT:  
```
30.000
3.667
Impossible
Impossible
2.856
```
Hint

Since the number of digits after the decimal point is not specified, the above result is not the only solution. For example, the following result is also acceptable.

30.0

3.66667

Impossible

Impossible

2.85595

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
