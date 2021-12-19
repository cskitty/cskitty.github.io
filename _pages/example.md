---
title: "Competitive Coding Algoritms"
layout: archive
permalink: /example949/
taxonomy: USACO
author_profile: true
---

## Lazy Segment Tree
{% highlight C++ linenos %}  
#include <bits/stdc++.h>  
using namespace std;  

using ll = long long;

const int MXV = 1e5*2;
const int MAX = 1e9, MN = -1e9;
vector<ll> arr;

template<class T> struct LSegTree {
    int N;
    vector<T> t, lz;
    T U=-1e18;

    // change me
    T F(T i, T j) { return max(i,j); } LSegTree() {}

    LSegTree(int N) : N(N), t(4*(N+1),U), lz(4*(N+1),0) {}

    void pull(int i) { t[i] = F(t[i*2],t[i*2+1]); }

    void push(int i, int l, int r) {
        t[i]+=lz[i];
        if(l!=r) lz[i*2]+=lz[i], lz[i*2+1]+=lz[i];
        lz[i]=0;
    }

    void build(vector<ll> &v) { build(v,1,0,N); }

    void build(vector<ll> &v, int i, int l, int r) {
        if(l==r) { t[i]=v[l]; return; } int m=(l+r)/2;
        build(v,i*2,l,m); build(v,i*2+1,m+1,r); pull(i);
    }

    void upd(int L, int R, T v) { upd(L,R,v,1,0,N); }

    void upd(int L, int R, T v, int i, int l, int r) {
        push(i,l,r); if(R<l || L>r) return;
        if(L<=l && R>=r) { lz[i]+=v; push(i,l,r); return; }
        int m=(l+r)/2; upd(L,R,v,i*2,l,m);
        upd(L,R,v,i*2+1,m+1,r); pull(i);
    }

    T qry(int L, int R) { return qry(L,R,1,0,N); }

    T qry(int L, int R, int i, int l, int r) {
        push(i,l,r); if(R<l || L>r) return U;
        if(L<=l && R>=r) return t[i]; int m=(l+r)/2;
        return F(qry(L,R,i*2,l,m), qry(L,R,i*2+1,m+1,r));
    }
};

vector<ll> v;

int main() {
    int N, Q;
    cin >> N >> Q;

    arr.resize(N + 1);
    v.resize(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> v[i];
        arr[i] = arr[i-1] + v[i];
        //cout << arr[i] << " ";
    }
    //cout << endl;

    LSegTree<long long> seg(N);
    seg.build(arr);
    /*for (int k = 1; k <= N; k++) {
        cout << seg.qry(k, k) << "[" << seg.qry(k-1, k) << "] ";
    }
    cout << endl;*/
    for (int i = 0; i < Q; i++) {
        int t, a, b;
        cin >> t >> a >> b;
        if (t == 1) {
            // upd
            seg.upd(a, N, b - v[a]);
            v[a] = b;


        }
        else {
            long long ans = seg.qry(a, b) - seg.qry(a-1, a-1);
            cout << max(0LL,ans) << endl;
        }
    }
}
{% endhighlight %}


## Modified Segment Tree
{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

const int N = 200010;
const int S = 1 << 18;

int n, q, a[N];

struct node {
    long long sum, pref;
    node(long long sum, long long pref) : sum(sum), pref(pref) {}
    node(long long x = 0) : sum(x), pref(max(0LL, x)) {}
    friend node operator+(const node& a, const node& b) {
        return {a.sum + b.sum, max(a.pref, a.sum + b.pref)};
    }
} tt[S << 1];

void build(int k = 1, int l = 1, int r = n) {
    if (l == r) { tt[k] = node(a[l]); return; }
    int m = (l + r) >> 1;
    build(k << 1, l, m);
    build(k << 1 | 1, m + 1, r);
    tt[k] = tt[k << 1] + tt[k << 1 | 1];
}

void update(int i, int x, int k = 1, int l = 1, int r = n) {
    if (l == r) { tt[k] = node(x); return; }
    int m = (l + r) >> 1;
    if (i <= m) update(i, x, k << 1, l, m);
    else update(i, x, k << 1 | 1, m + 1, r);
    tt[k] = tt[k << 1] + tt[k << 1 | 1];
}

node query(int ql, int qr, int k = 1, int l = 1, int r = n) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && qr >= r) return tt[k];
    int m = (l + r) >> 1;
    node q1 = query(ql, qr, k << 1, l, m);
    node q2 = query(ql, qr, k << 1 | 1, m + 1, r);
    return q1 + q2;
}

int main() {
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; ++i)
        scanf("%d", a + i);
    build();
    for (int i = 0, t, x, y; i < q; ++i) {
        scanf("%d%d%d", &t, &x, &y);
        if (t == 1) {
            update(x, a[x] = y);

            for (int ii = 1; ii <= n; ii++) {
                cout << query(ii, ii).sum << ", ";
            }
            cout << endl;
        }
        else printf("%lld\n", query(x, y).pref);
    }
}
{% endhighlight %}

## HLD, Heavy Light Decomposition
{% highlight C++ linenos %}
#include "bits/stdc++.h"
using namespace std;

const int N = 2e5+5;
const int D = 19;
const int S = (1<<D);

int n, q, v[N];
vector<int> adj[N];

int sz[N], p[N], dep[N];
int st[S], id[N], tp[N];

void update(int idx, int val) {
	st[idx += n] = val;
	for (idx /= 2; idx; idx /= 2)
		st[idx] = max(st[2 * idx], st[2 * idx + 1]);
}

int query(int lo, int hi) {
	int ra = 0, rb = 0;
	for (lo += n, hi += n + 1; lo < hi; lo /= 2, hi /= 2) {
		if (lo & 1)
			ra = max(ra, st[lo++]);
		if (hi & 1)
			rb = max(rb, st[--hi]);
	}
	return max(ra, rb);
}

int dfs_sz(int cur, int par) {
	sz[cur] = 1;
	p[cur] = par;
	for(int chi : adj[cur]) {
		if(chi == par) continue;
		dep[chi] = dep[cur] + 1;
		p[chi] = cur;
		sz[cur] += dfs_sz(chi, cur);
	}
	return sz[cur];
}

int ct = 1;

void dfs_hld(int cur, int par, int top) {
	id[cur] = ct++;
	tp[cur] = top;
	update(id[cur], v[cur]);
	int h_chi = -1, h_sz = -1;
	for(int chi : adj[cur]) {
		if(chi == par) continue;
		if(sz[chi] > h_sz) {
			h_sz = sz[chi];
			h_chi = chi;
		}
	}
	if(h_chi == -1) return;
	dfs_hld(h_chi, cur, top);
	for(int chi : adj[cur]) {
		if(chi == par || chi == h_chi) continue;
		dfs_hld(chi, cur, chi);
	}
}

int path(int x, int y){
	int ret = 0;
	while(tp[x] != tp[y]){
		if(dep[tp[x]] < dep[tp[y]])swap(x,y);
		ret = max(ret, query(id[tp[x]],id[x]));
		x = p[tp[x]];
	}
	if(dep[x] > dep[y])swap(x,y);
	ret = max(ret, query(id[x],id[y]));
	return ret;
}

int main() {
	scanf("%d%d", &n, &q);
	for(int i=1; i<=n; i++) scanf("%d", &v[i]);
	for(int i=2; i<=n; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	dfs_sz(1, 1);
	dfs_hld(1, 1, 1);
	while(q--) {
		int t;
		scanf("%d", &t);
		if(t == 1) {
			int s, x;
			scanf("%d%d", &s, &x);
			v[s] = x;
			update(id[s], v[s]);
		} else {
			int a, b;
			scanf("%d%d", &a, &b);
			int res = path(a,b);
			printf("%d ", res);
		}
	}
}
{% endhighlight %}


## LCA, Centroid Decomposition
{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9+7;
int N, M;
vector<vector<int>> adj, up;
vector<int> parent, dist, dpth, sz;

vector<bool> v;
int find_size(int n, int p) {
    if (v[n]) return 0;
    sz[n] = 1;
    for (auto c : adj[n]) {
        if (c != p) {
            sz[n] += find_size(c, n);
        }
    }
    return sz[n];
}

// centroid tree
int find_centroid(int n, int p, int mx) {
    for (auto c : adj[n]) {
        if (c != p) {
            if (! v[c] && sz[c] * 2 > mx) {
                return find_centroid(c, n, mx);
            }
        }
    }
    return n;
}

void init_centroid(int n, int p) {
    find_size(n, -1);

    int c = find_centroid(n, 0, sz[n]);
    v[c] = true;
    parent[c] = p;

    for (int x : adj[c]) {
        if (! v[x]) {
            init_centroid(x, c);
        }
    }
}


void dfs(int n, int p) {
    dpth[n] = dpth[p] + 1;

    //jump table for node n
    up[n][0] = p;
    for (int i = 1; i < 20; i++) {
        up[n][i] = up[up[n][i - 1]][i - 1];
    }

    for (auto c : adj[n]) {
        if (c != p) {
            dfs(c, n);
        }
    }
}

// lca
int lca(int a, int b) {
    if (dpth[a] < dpth[b]) swap(a, b);

    int diff = dpth[a] - dpth[b];
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

int find_dist(int n, int p) {
    int vlca = lca(n, p);
    int d1 = abs(dpth[n] - dpth[vlca]);
    int d2 = abs(dpth[p] - dpth[vlca]);
    return d1 + d2;
}

// go up ancestors + upd query val
void upd(int n) {
    int p = n;
    dist[n] = 0;
    while (parent[p] != 0) {
        p = parent[p];
        dist[p] = min(dist[p], find_dist(n, p));
    }
}

// go up ancestors + find ans (dist(n, anc) + dist[anc])
int query(int n) {
    int p = n;
    int ans = dist[p];
    while (parent[p] != 0) {
        p = parent[p];
        int s = find_dist(n, p) + dist[p];
        ans = min(ans, s);
    }
    return ans;
}

int main() {
    cin >> N >> M;
    adj.resize(N + 1);
    dist.resize(N + 1, INF);
    parent.resize(N + 1);
    dpth.resize(N + 1);
    v.resize(N + 1);
    sz.resize(N + 1);
    up.resize(N + 1, vector<int>(20));
    for (int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(1, 0);
    init_centroid(1, 0);
    upd(1);

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        if (a == 1) {
            upd(b);
        }
        else {
            cout << query(b) << endl;
        }
    }

}
{% endhighlight %}







## Convex hull

{% highlight C++ linenos %}
#include <bits/stdc++.h>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORE(i, a, b) for (int i = (a); i <= (b); i++)
#define F0R(i, a) for (int i = 0; i < (a); i++)
#define trav(a, x) for (auto &a : x)

#define f first
#define s second
#define bk back()
#define pb push_back

#define sz(x) int((x).size())
#define bg(x) begin(x)
#define all(x) bg(x), end(x)

int N, Q;

const int MX = 2e5 + 5;

using T = long long; // or long long
const T EPS = 1e-9; // might want to change
using P = pair<T,T>; using vP = vector<P>; using Line = pair<P,P>;

T sq(T a) { return a*a; } // square
T norm(const P& p) { return sq(p.f)+sq(p.s); } // x^2 + y^2

// basic operations
P operator-(const P& l, const P& r) {
	return P(l.f-r.f,l.s-r.s);
}

T cross(const P& a, const P& b) { return a.f*b.s-a.s*b.f; } // cross product
T cross(const P& p, const P& a, const P& b) { // cross product
	return cross(a-p,b-p);
}

using vi = vector<int>;
using vP = vector<P>;

int hullInd(const vP& v) {
	int ind = int(min_element(all(v))-begin(v));
	vi cand, hull{ind};
	F0R(i,sz(v)) if (v[i] != v[ind]) cand.pb(i);

	sort(all(cand),[&](int a, int b) { // sort by angle, tiebreak by distance
		P x = v[a]-v[ind], y = v[b]-v[ind];
		T t = cross(x,y);
		return t != 0 ? t > 0 : norm(x) < norm(y);
	});

	trav(c,cand) { // for every point
		while (sz(hull) > 1 && cross(v[end(hull)[-2]],v[hull.bk],v[c]) <= 0) {
			hull.pop_back(); // pop until counterclockwise and size > 1
		}
		hull.pb(c);
	}

    /*cout << "[";
    for (auto i : hull) {
        cout << "[" << v[i].f << ", " << v[i].s << "], ";
    }
    cout << "]" << endl;*/

    long long ans = 0;
    for (int i = 0; i < hull.size(); i++) {
        for (int j = i + 1; j < hull.size(); j++) {
            ans = max(ans, norm(v[hull[i]]-v[hull[j]]));
        }
    }

	return ans;
}


int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int c;
	cin >> c;
	vP pts(c);
    F0R(i, c) {
        long long a, b;
        cin >> a >> b;
        pts[i] = P(a, b);
    }

    int ret = hullInd(pts); // gets hull indices of convex hull

    cout << sqrt(ret) << endl;

}
{% endhighlight %}
