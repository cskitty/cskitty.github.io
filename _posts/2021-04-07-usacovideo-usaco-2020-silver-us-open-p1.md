---
title: USACO 2020 Silver US Open P1. Social Distancing
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2020 Silver US Open P1: Social Distancing  

{% include video id="mt8QhnFOkr0" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define f first
#define s second

int N;
ll M;

bool check(vector<pair<ll, ll>> v, ll target) {
    // target = max distancing

    ll pos = v[0].f;
    ll i = 0;
    ll amt = 0;
    while (amt < N) {
        if (v[i].f >= pos) {
            pos = v[i].f;
        }
        if (v[i].f <= (pos) && v[i].s >= (pos)) {
            amt++;
            pos += target;
        }
        else {
            i++;

        }

        if (i >= v.size()) {
            return false;
        }
    }
    return true;
}

ll binary_search(vector<pair<ll, ll>> x) {

    ll max = x[x.size() - 1].s - x[0].f;
    ll p = 0;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p + a) >= 0 && check(x, p + a)) p += a;
    }
    return p;
}

int main() {
    ifstream cin ("socdist.in");
    ofstream cout ("socdist.out");

    cin >> N >> M;

    vector<pair<ll, ll>> nums(M);

    for (int i = 0; i < M; i++) {
        cin >> nums[i].f >> nums[i].s;
    }


    sort(nums.begin(), nums.end());

    cout << binary_search(nums);

}  
{% endhighlight %}  
