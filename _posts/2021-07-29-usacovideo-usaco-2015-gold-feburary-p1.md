---
title: USACO 2015 Gold February P1. Cow Hopscotch
categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2015 Gold February P1: Cow Hopscotch](http://www.usaco.org/index.php?page=viewproblem2&cpid=532)

{% include video id="6blXS6g39iU" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

const int N = 752, M=1e9+7;
int K, R, C, grid[N][N];
vector<map<int, int>> m;
vector<vector<int>> colorVector;

#ifdef NEW_SEGMENT_TREE
//https://usaco.guide/gold/PURS?lang=cpp
template<class T> struct Seg {
    const T ID = 0; T comb(T grid, T b){ return (grid+b+M)%M; }

    int n=0; vector<T> seg;
    void init(int _n) { n = _n; seg.assign(2*n,ID); }

    void pull(int p) { seg[p] = comb(seg[2*p],seg[2*p+1]); }
    void upd(int p, T val) {
        seg[p += n] += val; seg[p] %= M; for (p /= 2; p; p /= 2) pull(p); }

    T query(int l, int r) {
        T ra = ID, rb = ID;
        for (l += n, r += n+1; l < r; l /= 2, r /= 2) {
            if (l&1) ra = comb(ra,seg[l++]);
            if (r&1) rb = comb(seg[--r],rb);
        }
        return comb(ra,rb);
    }
};
#else
struct BIT {
    vector<int> tree;
    void init(int _n) { tree.resize(_n); }

    void upd(int i, int x) {
        while (i < tree.size()) {
            tree[i] = (tree[i] + x);
            //if (tree[i] < 0) tree[i] += M;
            if (tree[i] > M) tree[i] -= M;
            tree[i] = (tree[i] + M) % M;
            i += (i & (-i));
        }
    }

    long long query(int i) {
        long long ans = 0;
        while (i > 0) {
            ans += tree[i];
            //if (ans < 0) ans += M;
            if (ans > M) ans -= M;
            ans = (ans + M) % M;
            i -= (i & (-i));
        }
        return ans;
    }
};
#endif

long long ans[N];

int main() {
    ifstream cin("hopscotch.in");
    ofstream cout("hopscotch.out");

    cin >> R >> C >> K;

    colorVector.resize(K + 1);
    m.resize(K + 1);

#ifdef NEW_SEGMENT_TREE
    Seg<long long> colors[K+3],allColors;
#else
    BIT colors[K + 3], allColors;
#endif
    allColors.init(C+1);

    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            int c;
            cin >> c;
            c--;
            grid[i][j] = c;
            colorVector[c].push_back(j);
        }
    }

    for(int i = 0; i < colorVector.size(); i++) {
        sort(colorVector[i].begin(), colorVector[i].end());
        for (auto j : colorVector[i]) {
            if (! m[i][j]) m[i][j] = m[i].size() + 1;
        }
    }

    for (int i = 0; i < m.size(); i++)
        colors[i].init(m[i].size()+2);

    allColors.upd(1,1);
    colors[grid[1][1]].upd(m[grid[1][1]][1],1);

    for(int i=2; i<=R; i++){
        for(int j=C; j>=2; j--){
            int x = grid[i][j];
#ifdef NEW_SEGMENT_TREE
            ans[j] = allColors.query(1,j-1) - colors[x].query(1, m[x][j]-1) + M;
#else
            ans[j] = allColors.query(j-1) - colors[x].query(m[x][j]-1) + M;
#endif
            ans[j] %= M;
            allColors.upd(j, ans[j]);
            colors[x].upd(m[x][j], ans[j]);
        }
    }
    cout << ans[C];
}
{% endhighlight %}  
