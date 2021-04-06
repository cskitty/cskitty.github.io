---
title: "USACO 2018 Gold December Q3. Teamwork"
categories:
  - USACOVIDEO
tags:
  - USACO Gold
---

## USACO 2018 Gold December Q3. Teamwork

{% include video id="boiC5NQCtlc" provider="youtube" %}    

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, K;


int main() {
    ifstream cin("teamwork.in");
    ofstream cout("teamwork.out");

    cin >> N >> K;

    vector<int> cows(N);
    vector<int> dp(N);
    for (int i = 0; i < N; i++) {
        cin >> cows[i];
        dp[i] = cows[i];
    }

    for (int i = 1; i < N; i++) {
        int currMax = cows[i];
        for (int k = 0; k < K; k++) {
            // range from j --> i
            int j = i - k;
            if (j < 0) {
                break;
            }
            currMax = max(currMax, cows[j]);
            dp[i] = max(dp[i], dp[j - 1] + (currMax * (k + 1)));
        }
    }

    cout << dp[N - 1];
}
{% endhighlight %}     
