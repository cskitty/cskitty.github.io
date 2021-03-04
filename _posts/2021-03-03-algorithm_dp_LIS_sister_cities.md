---
title: "Dynamic Programming: Sister Cities "
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Dynamic Programming: Sister Cities

Palmia has a large river that runs from east to west. The river has straight north and south banks, and there are N cities with different locations on each bank.

Each city on the North Bank has one and only one sister city on the South Bank, and the sister cities of different cities are different.

Each pair of sister cities applied to the government to open a straight waterway on the river to connect the two cities, but due to the fog on the river, the government decided to avoid any two waterway crossings to avoid accidents.

Programming helps the government to make some decisions to approve and reject applications, so that as many applications as possible are approved while ensuring that any two routes do not intersect.

Input format
In the first line, an integer N represents the number of cities.

From line 2 to line n+1, each line contains two integers, separated by a space, indicating the coordinates of a pair of friendly cities on the south bank and the north bank.

Output format
Only one line, output an integer, indicating the maximum number of applications that the government can approve.

data range
1 ≤ N ≤ 5000,
0 ≤ xi ≤ 10000

Sample Input:
```
7
22 4
2 6
10 3
15 12
9 8
17 17
4 2
```
Sample Output:
```
4
```

## Solution  

We sort the city coordinates on one side from small to large, and we can find that the way to keep the routes from interlacing is to find the longest ascending subsequence of the city coordinates on the other side. Then it was converted into a LIS naked question.

{% highlight C++ linenos %}
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
typedef pair<int, int> PII;

const int N = 5010;
int f[N], n;

int main()
{
    cin >> n;
    vector<PII> cities;

    for(int i = 1; i <= n; i ++)
    {
        int a, b;
        cin >> a >> b;
        cities.push_back({a, b});
    }

    //sort on one bank
    sort(cities.begin(), cities.end());

    for(int i = 0; i <= n; i ++)
      f[i] = 1;

    //find LIS on another bank
    for(int i = 1; i <= n; i ++)
        for(int j = 1; j < i; j ++)
            if(cities[j - 1].second < cities[i - 1].second)
                f[i] = max(f[i], f[j] + 1);

    int maxn = -1;
    for(int i = 1; i <= n; i ++)
      maxn = max(maxn, f[i]);
    cout << maxn;
}

{% endhighlight %}
