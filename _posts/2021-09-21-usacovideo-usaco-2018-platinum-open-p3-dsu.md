---
title: USACO 2018 US Open P3 Disruption

categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2018 Platinum US Open P3 Disruption](http://www.usaco.org/index.php?page=viewproblem2&cpid=842)
{% include video id="hMWYvYTDDaU" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, M;
const int MXV = 5e4 + 1;
const int MAX = 1e9;
const int SZ = 50001;
vector<vector<int>> adj(SZ);
vector<pair<int, int>> edges;

struct Edge {
    int a;
    int b;
    int w;
};
vector<Edge> replacements;
int depth[MXV];
vector<int> dsuroot(MXV);
vector<vector<int>> up(MXV, vector<int> (20));


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
//dfs1 to get depth, parent and sz of each node
void dfs(int n, int p) {
    // make trees
    depth[n] = depth[p] + 1;

    //initialize jump table
    up[n][0] = p;
    for (int i = 1; i < 20; i++) {
        up[n][i] = up[up[n][i-1]][i-1];
    }

    for (auto i : adj[n]) {
        if (i != p) {
            up[i][0] = n;
            dfs(i, n);
        }
    }
}

int findRoot (int a) {
    if (dsuroot[a] == a) {
        return a;
    }
    return dsuroot[a] = findRoot(dsuroot[a]);
}


vector<int> ans;

void jump(int node, int lcav, int w) {
    int r = findRoot(node);
    while (depth[r] > depth[lcav]) {
        ans[r] = w;
        // merge r with parent[r]
        dsuroot[r] = up[r][0];

        // jump to the parent's root
        r = findRoot(dsuroot[r]);

    }
}
int main() {
    ifstream cin("disrupt.in");
    ofstream cout("disrupt.out");
    cin >> N >> M;
    adj.resize(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int p, q;
        cin >> p >> q;
        edges.push_back({p, q});
        adj[p].push_back(q);
        adj[q].push_back(p);
    }

    dfs(1, 0);


    for (int i = 0; i < M; i++) {
        Edge e;
        cin >> e.a >> e.b >> e.w;
        replacements.push_back(e);
    }

    sort(replacements.begin(), replacements.end(), [](Edge &a, Edge &b) {
        return a.w < b.w;
    });

    ans.resize(N+1, MAX);
    iota(dsuroot.begin(), dsuroot.end(), 0);

    for (int i = 0; i < M; i++) {
        Edge e = replacements[i];
        int lcav = lca(e.a, e.b);

// #define BRUTE_FORCE
#ifdef BRUTE_FORCE
        for (int n = e.a; depth[n] > depth[lcav]; n = up[n][0]) {
            ans[n] = min(ans[n], e.w);
        }

        for (int n = e.b; depth[n] > depth[lcav]; n = up[n][0]) {
            ans[n] = min(ans[n], e.w);
        }
#else
        jump(e.a, lcav, e.w);
        jump(e.b, lcav, e.w);
#endif
    }

    for (int i = 0; i < N - 1; i++) {
            int a = edges[i].first, b = edges[i].second;
            if (depth[a] < depth[b]) swap(a, b);
            cout << ((ans[a] == MAX) ? -1 : ans[a]) << endl;
    }
}
{% endhighlight %}  
