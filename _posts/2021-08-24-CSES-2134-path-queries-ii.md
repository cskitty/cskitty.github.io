---
title: CSES 2134 Path Queries II
tags:
  - CSES
---

## [Path Queries II](https://cses.fi/problemset/task/2134)

* Heavy-Light Decomposition
* Segment Tree

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, Q;
vector<vector<int>> adj;
vector<int> st, sz, values;
vector<int> parent, depth;
vector<int> head;

template<class T> struct Seg { // comb(ID,b) = b
    const T ID = -1; T comb(T a, T b) { return max(a,b); }
    int n; vector<T> seg;
    void init(int _n) { n = _n; seg.assign(2*n,ID); }
    void pull(int p) { seg[p] = comb(seg[2*p],seg[2*p+1]); }
    void upd(int p, T val) { // set val at position p
        seg[p += n] = val; for (p /= 2; p; p /= 2) pull(p); }
    T query(int l, int r) {	// min on interval [l, r]
        T ra = ID, rb = ID;
        for (l += n, r += n+1; l < r; l /= 2, r /= 2) {
            if (l&1) ra = comb(ra,seg[l++]);
            if (r&1) rb = comb(seg[--r],rb);
        }
        return comb(ra,rb);
    }
};

Seg<int> seg;

void dfs(int n, int p) {
    // make trees
    depth[n] = depth[p] + 1;
    sz[n] = 1;
    for (auto i : adj[n]) {
        if (i != p) {
            parent[i] = n;
            dfs(i, n);
            sz[n] += sz[i];
        }
    }
}

int T = 1;

void dfs2(int n, int h, int p) {
    st[n] = T++;
    seg.upd(st[n], values[n]);
    head[n] = h;
    int hv = -1;
    for (auto i : adj[n]) {
        if (i != p) {
            if (hv == -1 || sz[i] > sz[hv]) {
                hv = i;
            }
        }
    }
    if (hv == -1) return;
    // heavy edge = inherit
    dfs2(hv, h, n);
    for (auto i : adj[n]) {
        if (i != p && i != hv) {
            // light edge = new segment
            dfs2(i, i, n);
        }
    }
}

int hldquery(int a, int b) {
    int ans = 0;
    while (head[a] != head[b]) {
        if (depth[head[a]] < depth[head[b]]) swap(a, b);
        int q1 = seg.query(st[head[a]], st[a]);
        a = parent[head[a]];
        ans = max(ans, q1);
    }
    if (depth[a] < depth[b]) swap(a, b);
    int q2 = seg.query(st[b], st[a]);
    ans = max(ans, q2);
    return ans;
}

int main() {
    cin >> N >> Q;
    seg.init(N + 1);
    st.resize(N + 1); sz.resize(N + 1); values.resize(N + 1);
    parent.resize(N + 1); depth.resize(N + 1); head.resize(N + 1);
    adj.resize(N + 1);

    for (int i = 1; i <= N; i++) {
        cin >> values[i];
    }
    for (int i = 0; i < N - 1; i++) {
        int a, b; cin >> a >>  b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    depth[0] = -1;
    dfs(1, 0);
    dfs2(1, 1, 0);
    for (int i = 0; i < Q; i++) {
        int t; cin >> t;
        if (t == 1) {
            int s, x;
            cin >> s >> x;
            seg.upd(st[s], x);
        }
        else {
            int a, b;
            cin >> a >> b;
            cout << hldquery(a, b) << " ";
        }
    }
}
{% endhighlight %}  
