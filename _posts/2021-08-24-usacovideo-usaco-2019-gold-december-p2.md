---
title: USACO 2019 Gold December P2 Milk Visits

categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## [USACO 2019 Gold December P2 Milk Visits](http://www.usaco.org/index.php?page=viewproblem2&cpid=970)

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> type;
vector<vector<int>> adj;
int T = 1;
vector<int> st, ed, depth;
vector<vector<int>> up;
vector<vector<int>> colorval;
vector<vector<pair<int, int>>> colorv2;

void dfs(int n, int p) {
    st[n] = T;
    depth[n] = depth[p] + 1;
    up[n][0] = p;

    for (int i = 1; i < 20; i++) {
        up[n][i] = up[up[n][i - 1]][i - 1];
    }
    T++;
    for (auto c : adj[n]) {
        if (c != p) {
            dfs(c, n);
        }
    }

    ed[n] = T - 1;
}

int lca(int a, int b) {
    if (depth[a] < depth[b]) swap(a, b);

    int diff = depth[a] - depth[b];
    for (int i = 0; i < 20; i++) {
        if ((diff >> i) & 1) {
            a = up[a][i];
        }
    }
    if (a == b) return a;

    for (int i = 19; i >= 0; i--) {
        int ap = up[a][i];
        int bp = up[b][i];
        if (ap != bp) {
            a = ap; b = bp;
        }
    }
    return up[a][0];
}

struct hashPi {
    size_t operator()(const pair<int, int>& p) const { return (p.first*100001) + p.second; }
};
vector<int> ans;
unordered_map<pair<int, int>, int, hashPi> findlca;
unordered_map<int, vector<int>> findquery;
vector<array<int, 3>> queries;

void querydfs(int n, int p) {
    colorval[type[n]].push_back(n);

    for (auto i : findquery[n]) {
        int a = queries[i][0], b = queries[i][1], c = queries[i][2];

        int d = colorval[c].size() ? colorval[c].back() : 0;

        if (depth[d] >= depth[findlca[{a, b}]]) {
            ans[i] = 1;
        }
    }

    for (auto x : adj[n]) {
        if (x != p) {
            querydfs(x, n);
        }
    }

    colorval[type[n]].pop_back();
}


int main() {
    ifstream cin("milkvisits.in");
    ofstream cout("milkvisits.out");

    cin >> N >> M;
    type.resize(N + 1);
    adj.resize(N + 1);
    st.resize(N + 1); ed.resize(N + 1);
    up.resize(N + 1, vector<int>(20));
    depth.resize(N + 1);
    colorval.resize(N + 1); colorv2.resize(N + 1);
    ans.resize(M);

    for (int i = 1; i < N + 1; i++) {
        cin >> type[i];
    }
    for (int i = 1; i < N; i++) {
        int a, b; cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    depth[0] = -1;
    dfs(1, 0);

    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        queries.push_back({a, b, c});
        findquery[a].push_back(i);
        findquery[b].push_back(i);

        if (findlca.count({a, b}) == 0) {
            int l = lca(a, b);
            findlca[{a, b}] = l;
            findlca[{b, a}] = l;
        }
    }

    querydfs(1, 0);
    for (int i = 0; i < M; i++) {
        cout << ans[i];
    }
}
{% endhighlight %}  
