---
title: "Japan 2005 Domestic: Traveling by Stagecoach"
categories:
  - USACO
tags:
  - Algorithms
  - DP on digits
---

# Japan 2005 Domestic: Traveling by Stagecoach

Description

Count the number of integers in a given interval [X, Y], which satisfy the following conditions: this number is exactly equal to K sum of powers of integer B.

For example, suppose X= 15 , Y= 20 , K= 2 , B = 2, Then there are and only the following three numbers satisfy the meaning of the question:

17 =24+20
18 =24+21
20 =24+22

Input format
The first line contains two integers X and Y, The next two lines contain integers K and B.

Output format
Contains only an integer, indicating the number of numbers that meet the condition.

data range

1 ≤ X ≤ Y≤ 2^31− 1,
1 ≤ K ≤ 20,
2 ≤ B ≤ 10


SAMPLE INPUT:
```
15 20
2
2
```

SAMPLE OUTPUT:  
```
3
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

{% endhighlight %}
