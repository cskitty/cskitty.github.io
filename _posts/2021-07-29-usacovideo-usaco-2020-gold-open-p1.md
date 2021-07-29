---
title: USACO 2020 Gold Open P1: Cow Haircut  
categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## [USACO 2020 Gold Open P1: Cow Haircut  ](http://www.usaco.org/index.php?page=viewproblem2&cpid=1041)

{% include video id="iFVaRcot24Y&t" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll N;
vector<ll> hairs, tree;

void update(ll i, ll x) {
    while (i < tree.size()) {
        tree[i] += x;
        i = i + (i & (-i));
    }
}

ll query(ll i) {
    ll ans = 0;
    while (i > 0) {
        ans += tree[i];
        i = i - (i & (-i));
    }
    return ans;
}

int main() {
    ifstream cin("haircut.in");
    ofstream cout("haircut.out");

    cin >> N;

    hairs.resize(N + 1);
    tree.resize(N + 2);

    vector<int> inverse(N + 1);
    for (int i = 1; i < N + 1; i++) {
        cin >> hairs[i];
        hairs[i]++;
        // i - 1 = values before, also query(N + 1)
        inverse[i] = i - 1 - query(hairs[i]);
        update(hairs[i], 1);
    }

    vector<int> order(N);
    // get new order
    iota(order.begin(), order.end(), 1);
    sort(order.begin(), order.end(), [](int a, int b) {return hairs[a] < hairs[b];});

    ll ans = 0;
    int i = 0;
    cout << ans << endl;
    for(int j = 1; j < N; j++) {
        while (i < N && hairs[order[i]] <= j) {
            ans += inverse[order[i]];
            i++;
        }
        cout << ans << endl;
    }
}
{% endhighlight %}  
