---
title: "DP Multiple Knapsack"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Knapsack
  - Multiple Knapsack
---

## DP Multiple Knapsack

Given an array of items, each item has weight, value and quantity and the knapsack's maximum holding weight.
Output the the maximum value that can be obtained for holding these items in knapsack.  

Input format
In the first row, there are two numbers n, m, where n represents the number of items that you want to pick, and m represents the maximum knapsack holding weight.  

In the next n rows, 3 numbers in each row, w, v and q, respectively represent the weight, value and the maximum quantity that can be picked (pick 0 up to q).  

Output format
One line: a number, indicating the maximum value that can be obtained for this purchase.

Sample Input:
```
5 1000
80 20 4
40 50 9
30 50 7
40 30 6
20 20 1
```
Sample Output:
```
1040
```

### Solution 1: 2D Knapsack

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> w(N + 1);
    vector<int> v(N + 1);
    vector<int> amt(N + 1);

    vector<vector<int>> dp(N + 1, vector<int>(M + 1));

    dp[0][0] = 0;
    for (int i = 1; i < N + 1; i++) {
        cin >> w[i] >> v[i] >> amt[i];
        for (int j = 0; j <= M; j++) {
            dp[i][j] = dp[i - 1][j];
            for (int k = 0; k <= amt[i] && k*w[i] <= j; k++) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - (w[i]*k)] + (v[i]*k));
            }
        }
    }
    cout << dp[N][M];
}
{% endhighlight %}

### Solution 2: 1D Knapsack Optimization

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> w(N + 1);
    vector<int> v(N + 1);
    vector<int> amt(N + 1);

    vector<int> dp(M + 1);

    dp[0] = 0;
    for (int i = 1; i < N + 1; i++) {
        cin >> w[i] >> v[i] >> amt[i];
        for (int j = M; j >= 0; j--) {
            for (int k = 0; k <= amt[i] && k*w[i] <= j; k++) {
                dp[j] = max(dp[j], dp[j - (w[i]*k)] + (v[i]*k));
            }
        }
    }
    cout << dp[M];
}
{% endhighlight %}

### Solution 3: Binary Grouping Optimization

There are n[i] items for the i-th item, this n[i] can be expanded to n[i]=2^0+2^1+…+2^k+c (where 2^(k+1) < n[i] < 2^(k+2)). 2^0+2^1+…+2^k can represent the interval [0,2^(k+1)-1 ], by adding the number c, it can represent all the numbers on the interval [0,n[i]])

For each item, create new items which is equivalent to packing together 2^j (j=0..log2(s[i])) items. Then solve the original problem with 0-1 knapsack.

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> w;
    vector<int> v;

    for (int i = 0; i < N; i++) {
        int wi, vi, amti;
        cin >> wi >> vi >> amti;

        for (int j = 1; j <= amti; j*=2) {
            w.push_back(wi * j);
            v.push_back(vi * j);
            amti -= j;
        }
        if (amti > 0) {
            w.push_back(amti*wi);
            v.push_back(amti*vi);
        }
    }

    // turn into 0/1 knapsack
    vector<int> dp(M + 1);
    dp[0] = 0;
    for (int i = 0; i < v.size(); i++) {
        for (int j = M; j >= w[i]; j--) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }

    cout << dp[M];
}

{% endhighlight %}
