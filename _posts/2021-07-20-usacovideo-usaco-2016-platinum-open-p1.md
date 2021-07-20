---
title: USACO 2016 2016 Platinum Open P1. 262144
categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2016 2016 Platinum Open P1. 262144](http://www.usaco.org/index.php?page=viewproblem2&cpid=648)

{% include video id="XyBF7vhwVbs" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> nums;

int main() {
    ifstream cin("262144.in");
    ofstream cout("262144.out");

    cin >> N;
    nums.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int sz = 60;
    int maxsize = 0;
    vector<vector<int>> dp(N, vector<int>(sz, -1));
    for (int i = 0; i < N; i++) {
        dp[i][nums[i]] = i;
    }

    for (int val = 1; val < sz; val++) {
        for (int i = N - 1; i >= 0; i--) {
            if (dp[i][val - 1] == -1 || dp[i][val - 1] + 1 >= N || val - 1 < 0) {
                continue;
            }
            dp[i][val] = max(dp[i][val], dp[dp[i][val - 1] + 1][val - 1]);
            if (dp[i][val] != -1) {
                maxsize = max(maxsize, val);
            }
        }
    }
    cout << maxsize;
}
{% endhighlight %}  
