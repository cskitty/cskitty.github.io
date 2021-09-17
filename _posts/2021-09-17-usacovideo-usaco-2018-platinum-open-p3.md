---
title: USACO 2018 US Open P3 Disruption

categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2018 Platinum US Open P3 Disruption](http://www.usaco.org/index.php?page=viewproblem2&cpid=842)
{% include video id="rUOiklqcysk" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, M;
const int SZ = 50001;
vector<vector<int>> adj(SZ);
vector<pair<int, int>> edges(SZ);
vector<set<pair<int, int>>> nodeset(SZ);
vector<int> parent(SZ);
vector<int> ans(SZ);

int dfs(int n, int p) {
    // merge small 2 large alg
    for (auto c : adj[n]) {
        if (c != p) {
            parent[c] = n;
            int csz = dfs(c, n);
            if (csz > nodeset[n].size()) swap(nodeset[n], nodeset[c]);
            for (auto s : nodeset[c]) {
                if (nodeset[n].count(s)) {
                    // disruption question specialty
                    // if the same edge in both sets,
                    // the edge is internal to tree (therefore remove)
                    nodeset[n].erase(s);
                }
                else {
                    nodeset[n].insert(s);
                }
            }
        }
    }

    if (nodeset[n].size() == 0) {
        ans[n] = -1;
    }
    else {
        ans[n] = nodeset[n].begin()->first;
    }
    return nodeset[n].size();
}

int main() {
    ifstream cin("disrupt.in");
    ofstream cout("disrupt.out");
    cin >> N >> M;

    adj.resize(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int p, q;
        cin >> p >> q;
        edges[i] = {p, q};
        adj[p].push_back(q);
        adj[q].push_back(p);
    }

    for (int i = 0; i < M; i++) {
        int p, q, r;
        cin >> p >> q >> r;
        nodeset[p].insert({r, i});
        nodeset[q].insert({r, i});
    }
    dfs(1, -1);
    for (int i = 0; i < N - 1; i++) {
        int fv = edges[i].first, sv = edges[i].second;
        if (parent[sv] == fv) swap(sv, fv);

        cout << ans[fv] << endl;
    }
}
{% endhighlight %}  
