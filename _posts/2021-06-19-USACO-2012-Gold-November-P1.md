---
title: USACO 2014 Gold November P1. Balanced Cow Breeds
categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2014 Gold November P1. Balanced Cow Breeds](http://www.usaco.org/index.php?page=viewproblem2&cpid=193)

### Advanced DP

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int maxV = 1001;
int dp[maxV][maxV];

int main() {
    string s;
    cin >> s;

    dp[1][1] = 1, dp[1][0] = 1;

    int currOpen = 1;
    int i = 0;
    for (auto c : s) {
        i++;
        if (i < 2) {
            continue;
        }
        if (c == '(') {
            currOpen++;
        }
        else {
            currOpen--;
        }
        for (int j = 0; j < currOpen + 1; j++) {
            int k = currOpen - j;
            int l = currOpen - k + 1;
            dp[i][j] = 0;

            if (c == '(') {
                // left bracket, "("

                if (j - 1 >= 0 && dp[i - 1][j - 1] != 0) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
                if (k - 1 >= 0 && dp[i - 1][currOpen - 1 - (k - 1)] != 0) {
                    dp[i][j] += dp[i - 1][currOpen - 1 - (k - 1)];
                }
            }
            else {
                // right bracket, ")"

                if (dp[i - 1][j + 1] != 0) {
                    dp[i][j] += dp[i - 1][j + 1];
                }
                if (dp[i - 1][currOpen + 1 - (k + 1)] != 0) {
                    dp[i][j] += dp[i - 1][currOpen + 1 - (k + 1)];
                }
            }
            dp[i][j] %= 2012;
        }
    }

    cout << dp[i][0] % 2012;
}
{% endhighlight %}  
