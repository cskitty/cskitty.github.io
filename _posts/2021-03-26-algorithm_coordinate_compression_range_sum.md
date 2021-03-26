---
title: "Coordinate Compression: Range Sum"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Coordinate Compression
---

## Coordinate Compression: Range Sum

Suppose there is an infinite number line, and the number on each coordinate on the number line is 0.

Now we first proceed n operations, each operation will be add c on a certain position x.

Next, proceed m queries, each query contains two integers l with r, You need to find for the interval [l, r], the sum of all the numbers between index l and index r.

Input format
The first line contains two integers n with m.

Next n rows, each row contains two integers x and c.

Next m rows, each row contains two integers l and r.

Output format
Total m Line, each line outputs the sum of the numbers in the interval sought in the query.

data range
−109≤ x≤109,
1 ≤ n , m ≤105,
−109≤ l≤ r≤109,
− 10000 ≤ c ≤ 10000

Sample Input:
```
3 3
1 2
3 6
7 5
1 3
4 6
7 8
```
Sample Output:
```
8
0
5
```

### Solution

{% highlight C++ linenos %}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pi;
const int N = 300010;
int a[N], s[N];
int n, m;

vector<int> alls;
vector<pi> add, query;

int find(int x)
{
    /*
    int l = 0, r = alls.size() - 1;
    while(l < r)
    {
        int mid = l + r >> 1;
        if(alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return r + 1;
    */
    return upper_bound(alls.begin(), alls.end(), x) - alls.begin();
}

int main()
{

    cin >> n >> m;

    for(int i = 0; i < n; i ++ )
    {
        int x, c;
        cin >> x >> c;
        add.push_back({x, c});
        alls.push_back(x);
    }

    for(int i = 0; i < m; i ++ )
    {
        int l, r;
        cin >> l >> r;
        query.push_back({l, r});

        alls.push_back(l);
        alls.push_back(r);
    }

    sort(alls.begin(), alls.end());
    alls.erase( unique( alls.begin(), alls.end() ), alls.end());

    for(auto item : add)
    {
        int x = find(item.first);
        a[x] += item.second;
    }

    for(int i = 1; i <= alls.size(); i ++ ) s[i] = s[i - 1] + a[i];

    for(auto item : query)
    {
        int l = find(item.first), r = find(item.second);
        cout << s[r] - s[l - 1] << endl;
    }

    return 0;
}
{% endhighlight %}
