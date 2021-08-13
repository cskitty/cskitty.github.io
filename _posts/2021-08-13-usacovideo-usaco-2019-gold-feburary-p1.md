---
title: USACO 2020 Gold Open P1. Cow Haircut
categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## [USACO 2019 February Contest, Gold P1. Cow Land](http://www.usaco.org/index.php?page=viewproblem2&cpid=921)

{% include video id="6_qNZ62uSFY" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;
#define ll long long
vector<vector<int>> adj;

int N, Q;
vector<int> st, ed;
vector<int> enjoy;
vector<int> depth;
#ifdef SIMPLE_LCA
vector<int> parent;
#else
vector<vector<int>> up(2e5 + 1, vector<int> (20));
#endif
int T = 1;

class BIT {
    vector<long long> tree;
public:
    void init(int x) {
        tree.resize(x);
    }
    void update(ll i, ll x) {
        while (i < tree.size()) {
            tree[i] ^= x;
            i = i + (i & (-i));
        }
    }
    ll query(ll i) {
        ll ans = 0;
        while (i > 0) {
            ans ^= tree[i];
            i = i - (i & (-i));
        }
        return ans;
    }
};

// euler tour
void dfs(int c, int p) {
    st[c] = T++;
    depth[c] = depth[p] + 1;
#ifdef SIMPLE_LCA
    parent[c] = p;
#else
    up[c][0] = p;
    for (int i = 1; i < 20; i++) {
        up[c][i] = up[up[c][i-1]][i-1];
    }
#endif
    for (int n : adj[c]) {
        if (n != p) {
            dfs(n, c);
        }
    }
    ed[c] = T - 1;
}

#ifdef SIMPLE_LCA
int lca(int a, int b) {
    // lca
    if (depth[a] > depth[b]) {
        swap (a, b);
    }
    while (depth[a] < depth[b]) {
        b = parent[b];
    }
    while (a != b) {
        a = parent[a];
        b = parent[b];
    }
    return a;
}
#else
int lca(int a, int b) {
    if (depth[a] > depth[b]) {
        swap (a, b);
    }

    // binary jumping
    int d = depth[b] - depth[a];
    for (int i = 0; i < 20; i++) {
        if((d >> i) & 1) {
            b = up[b][i];
        }
    }

    if(a == b) return a;

    //lca using binary jumping
    for (int i = 19; i >= 0; i--) {
        int ap = up[a][i];
        int bp = up[b][i];
        if(ap != bp) a = ap, b = bp;
    }
    return up[a][0];
}
#endif

int main() {
    ifstream cin("cowland.in");
    ofstream cout("cowland.out");
    cin >> N >> Q;
    cin >> N >> Q;
    enjoy.resize(N + 1);
    adj.resize(N + 1);
    st.resize(N + 1); ed.resize(N + 1);
#ifdef SIMPLE_LCA
    parent.resize(N + 1);
#endif
    depth.resize(N + 1);
    depth[0] = 0;
    BIT tree;
    tree.init(N + 1);
    for (int i = 1; i < N + 1; i++) {
        cin >> enjoy[i];
    }
    for (int i = 0; i < N - 1; i++) {
        int a, b; cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    depth[0] = -1;
    dfs(1, 0);

    for (int i = 1; i < N + 1; i++) {
        tree.update(st[i], enjoy[i]);
        tree.update(ed[i] + 1, enjoy[i]);
    }
    for (int i = 0; i < Q; i++) {
        int t;
        cin >> t;
        if (t == 1) {
            int a, b;
            cin >> a >> b;
            tree.update(st[a], enjoy[a]);
            tree.update(ed[a] + 1, enjoy[a]);

            tree.update(st[a], b);
            tree.update(ed[a] + 1, b);
            enjoy[a] = b;
        }
        else {
            int a, b;
            cin >> a >> b;
            int pathsuma = tree.query(st[a]);
            int pathsumb = tree.query(st[b]);

            a = lca(a, b);
            int ans = pathsuma ^ pathsumb ^ enjoy[a];
            cout << ans << endl;
        }
    }
}
{% endhighlight %}  
