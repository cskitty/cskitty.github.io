---
title: USACO 2017 Platinum January P1. Promotion Counting
tags:
  - USACO Platinum
---

## [USACO 2017 Platinum January P1. Promotion Counting](http://usaco.org/index.php?page=viewproblem2&cpid=696)
{% include video id="XNLA58yFNkU" provider="youtube" %}

## Bitmask DP

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N;
vector<vector<int>> adj;
vector<int> prevnum, rating, ans, parent;
int countval = 0;
vector<int> bit;

// bit functions
void updateBIT(int a, int b) {
    while (a <= N) { bit[a] += b; a += (a & (-a));}
}

int query(int a) {
    int r = 0;
    while (a > 0) {r += bit[a]; a = a - (a & (-a));} return r;
}

void dfs(int node) {
    prevnum[node] = query(N) - query(rating[node]);
    for (auto child : adj[node]) {
        countval++;
        dfs(child);
    }
    ans[node] = query(N) - query(rating[node]) - prevnum[node];
    updateBIT(rating[node], 1);
}

int main() {
    ifstream cin("promote.in");
    ofstream cout("promote.out");

    cin >> N;
    adj.resize(N + 1);
    rating.resize(N + 1);
    bit.resize(N + 1);
    parent.resize(N + 1, -1);
    prevnum.resize(N + 1);
    ans.resize(N + 1);

    vector<pair<int, int>> old(N + 1);
    for (int i = 1; i < N + 1; i++) {
        cin >> old[i].first;
        old[i].second = i;
    }

    for (int i = 2; i < N + 1; i++) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    // compression
    sort(old.begin(), old.end());
    for (int i = 1; i < N + 1; i++) {
        rating[old[i].second] = i;
    }
    dfs(1);
    for (int i = 1; i <= N; i++) {
        cout << ans[i] << endl;
    }
}
{% endhighlight %}  
