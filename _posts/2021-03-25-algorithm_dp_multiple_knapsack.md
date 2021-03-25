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

### Solution 1

{% highlight C++ linenos %}
#include <iostream>
using namespace std;

const int N = 510, M = 6010;

int v[N], w[N], s[N];
int dp[N][M];
int n, m;


int main(){

    cin >> n >> m;
    for (int i = 1 ; i <= n ; i ++) cin >> v[i] >> w[i] >> s[i];

    //iterate all items
    for (int i = 1 ; i <= n ; i ++){
        //iterate all weights
        for (int j = 0 ; j <= m ; j ++){
            dp[i][j] = dp[i - 1][j];
            //iterate all item quantity
            for (int k = 1 ; k <= s[i] && j >= k * v[i] ; k ++){
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v[i]] + k * w[i]);
            }
        }
    }

    cout << dp[n][m];

    return 0;
}
{% endhighlight %}

### Solution 2: Optimization through Binary Grouping

For each item, create new items which is equivalent to packing together 2^j (j=0..log2(s[i])) items.
Then solve the original problem with 0-1 knapsack.


{% highlight C++ linenos %}
index = 0;
for (int i = 1; i <= n; i++) {
  int c = 1, v, w, s;
  cin >> v >> w >> s;
  while (s - c > 0) {
    s -= c;
    w[++index] = c * w;
    v[index] = c * v;
    c *= 2;
  }
  w[++index] = k * w;
  v[index] = k * v;
}
{% endhighlight %}
