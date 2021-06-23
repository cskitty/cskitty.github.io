---
title: USACO 2014 Gold December P1. Guard Mark
tags:
  - USACO Platinum
---

## [USACO 2014 Gold December P1. Moovie Mooving](http://www.usaco.org/index.php?page=viewproblem2&cpid=494)

##Bitmask DP

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, H;
const int INF = INT_MAX;
vector<vector<int>> cows;


int bitmask(int original, int add) {
    original |= 1UL << add;
    return original;
}

int unbit(int n, int k) {
    return (n & ( 1 << k )) >> k;
}

int height(int n) {
    int ans = 0;
    for (int i = 0; i < N; i++) {
        if (unbit(n, i)) {
            ans += cows[i][0];
        }
    }
    return ans;
}

signed main() {
    ifstream cin("guard.in");
    ofstream cout("guard.out");
    cin >> N >> H;

    cows.resize(N);
    for (int i = 0; i < N; i++) {
        vector<int> cowinfo(3);
        cin >> cowinfo[0] >> cowinfo[1] >> cowinfo[2];
        cows[i] = cowinfo;
    }
    // dp[subset of cows used] = maxweight
    vector<int> dp(pow(2, N));

    int ans = 0;
    dp[0] = INF;
    for (int i = 0; i < pow(2, N); i++) {
        for (int j = 0; j < N; j++) {
            // see if you can add j
            if (! unbit(i, j) && dp[i] - cows[j][1] >= 0) {
                // subset including j
                int subset = bitmask(i, j);
                dp[subset] = max(dp[subset], min(cows[j][2], dp[i] - cows[j][1]));
                // if height > , add to ans
                if (height(subset) >= H) {
                    ans = max(ans, dp[subset]);
                }
            }
        }
    }
    if (ans == 0) {
        cout << "Mark is too tall";
        return 0;
    }
    cout << ans;
}
{% endhighlight %}  
