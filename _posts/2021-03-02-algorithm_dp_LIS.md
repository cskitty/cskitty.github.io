---
title: "Dynamic Programming: Longest Increasing Subsequence"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Longest Increasing Subsequence

Longest Increasing Subsequence (LIS) problems find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.

Sample Input:
```
8
186 186 150 200 160 130 197 220
```
Sample Output:
```
4
```

## Solution  


State representation:

* f[i] is the length of LIS in a[1 ~ i] ending with a[i]

State calculation:  

For each element "i", we find the value of the LIS ending with that value. We can do this by finding the maximum LIS of all previous indexes (index "j") where a[j] < a[i]. We can save the value of f[i] as the length of f[j] + 1, being the length of the LIS of j, and adding a[i] to the end of the sequence.

{% highlight C++ linenos %}
#include <iostream>
using namespace std;
const int N = 1010;
int a[N], f[N], n;
int main()
{
    cin >> n;
    for(int i = 1; i <= n; i ++) {
      cin >> a[i];
      f[i] = a[i];
    }
    for(int i = 2; i <= n; i ++)
        for(int j = 1; j < i; j ++)
            if(a[j] < a[i])
                f[i] = max(f[i], f[j] + 1);

    int maxn = -1;
    for(int i = 1; i <= n; i++)
      maxn = max(maxn, f[i]);
    cout << maxn << endl;
    return 0;
}
{% endhighlight %}
