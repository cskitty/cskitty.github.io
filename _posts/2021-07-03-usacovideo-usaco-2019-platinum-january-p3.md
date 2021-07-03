---
title: USACO 2019 Platinum January P3. Train Tracking 2
categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2019 Platinum January P3: Train Tracking 2](http://www.usaco.org/index.php?page=viewproblem2&cpid=902)

{% include video id="ce5emV58Isw" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

#define ll long long
int N, K;
int M = 1e9, MOD = 1e9 + 7;
vector<ll> v;
vector<ll> ansv;

inline ll fast_power(ll base, ll power) {
    ll result = 1;
    while(power > 0) {
        if(power % 2 == 1) { // Can also use (power & 1) to make code even faster
            result = (result*base) % MOD;
        }
        base = (base * base) % MOD;
        power = power / 2; // Can also use power >>= 1; to make code even faster
    }
    return result;
}

ll use_dp(ll val, ll len) {
    vector<ll> dp(len + 2);
    dp[1] = 1, dp[0] = 1;
    ll x = M - val;
    for (int i = 2; i <= len + 1; i++) {
        dp[i] = (dp[i - 1] * (x + 1)) % MOD;
        if (i - K - 1 >= 0) {
            dp[i] = ((dp[i] - (dp[i - K - 1] * fast_power(x, K)) % MOD) + MOD) % MOD;
        }
    }
    return dp[len + 1] % MOD;
}

int main() {
    ifstream cin("tracking2.in");
    ofstream cout("tracking2.out");

    cin >> N >> K;
    v.resize(N + 1);
    for (ll i = 1; i <= N; i++) {
        cin >> v[i];
    }

    ll ans = 1;
    for (int i = 1, j; i <= N - K + 1; i = j + 1) {
        j = i;
        // i is start of new window, j is ending
        while (v[j + 1] == v[i]) {
            j++;
        }
        // len of curr window
        ll len = j - i + 1;
        // add extra K - 1 from next window
        len += K - 1;
        // check against previous window
        // special handling: skip first window
        if (i > 1 && v[i] < v[i - 1]) {
            // already calculated first K values in previous window
            len -= K;
        }
        // check against next window
        // special handling: skip last window
        if (j < N - K + 1 && v[j] < v[j + 1]) {
            // will calculate last K values in next window
            len -= K;
        }
        if (len > 0) {
            ans *= use_dp(v[i], len);
            ans %= MOD;
        }
    }
    cout << ans;
}
{% endhighlight %}  
