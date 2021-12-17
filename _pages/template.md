---
title: "Competitive Coding Algoritms"
layout: archive
permalink: /template949/
taxonomy: USACO
author_profile: true
---

![](/assets/images/USACObessieheader.PNG)

## Dijkstra
{% highlight C++ linenos %}
int dijkstraM(int start, int end, vector<vector<pi>> adj, vector<int> &dist) {
    vector<bool> visited(N);

    priority_queue<pi, vector<pi>, greater<pi>> pq;

    pq.push({0, start});
    dist[start] = 0;

    while (pq.size()) {
        pi value = pq.top(); pq.pop();
        ll node = value.s;
        if (visited[node]) {
            continue;
        }
        visited[node] = true;

        for (auto to : adj[node]) {
            int newWeight = to.f + dist[node];

            if (newWeight < dist[to.s]) {
                // nodeInfo[to.s] = nodeInfo[node] + cows[to.s];
                prevV[to.s] = node;

                dist[to.s] = newWeight;
                pq.push({dist[to.s], to.s});
            }
        }

        //dbg(node, dist[node]);
    }

    return dist[end];
}
{% endhighlight %}

## BIT
{% highlight C++ linenos %}
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

BIT  allColors;
allColors.query(j);
allColors.upd(j, x);
{% endhighlight %}


## Normal Segment Tree
{% highlight C++ linenos %}
vector<int> arr;
vector<int> tree;
arr.resize(N + 1);
tree.resize(4*N);

void build(int p, int l, int r) {
    if (l == r) {tree[p] = arr[l]; return;}

    int mid = (l + r)/2;
    build(2*p, l, mid);
    build(2*p + 1, mid + 1, r);

    tree[p] = min(tree[2*p], tree[2*p + 1]);
}

void update(int p, int l, int r, int x, int y) {
    // turn arr[x] into y
    if (l == r) { tree[p] = y; return; }

    int mid = (l + r)/2;
    if (x <= mid) {
        update(2*p, l, mid, x, y);
    }
    else {
        update(2*p + 1, mid + 1, r, x, y);
    }

    tree[p] = min(tree[2*p], tree[2*p + 1]);
}

int query(int p, int l, int r, int x, int y) {
    if (l == r) { return tree[p]; }

    int mid = (l + r)/2;
    int ans = INT_MAX;
    if (x <= mid) {
        ans = min(ans, query(2 * p, l, mid, x, y));
    }
    if (y >= mid + 1) {
        ans = min(ans, query(2 * p + 1, mid + 1, r, x, y));
    }

    return ans;
}


{% endhighlight %}

## Lazy Segment Tree
{% highlight C++ linenos %}

template<class T, int MX> struct LazySeg {
    T treesum[MX], treemin[MX], lazy[MX];

    void build(int n, int tl, int tr) {
        if (tl == tr) {
            treesum[n] = arr[tl];
            treemin[n] = arr[tl];
            return;
        }
        int mid = (tl + tr)/2;
        build(n << 1, tl, mid);
        build((n << 1) + 1, mid + 1, tr);
        // change me
        treesum[n] = (treesum[n << 1] + treesum[(n << 1) + 1]);
        treemin[n] = min(treemin[2*n], treemin[2*n + 1]);
    }

    void pushdown(int n, int tl, int tr) {
        if (lazy[n] > 0) {
            // change me
            treesum[n] += (tr - tl + 1) * lazy[n];
            treemin[n] += lazy[n];

            if (tl != tr) {
                lazy[2*n] += lazy[n];
                lazy[2*n+1] += lazy[n];
            }
            lazy[n] = 0;
        }
    }

    void upd(int n, int tl, int tr, int st, int ed, T v) {
        pushdown(n, tl, tr);
        if (tl > tr || tl > ed || tr < st) return;
        if (tl >= st && tr <= ed) {
            // change me: only for min/max
            treesum[n] += (tr - tl + 1) * v;
            treemin[n] += v;

            // only for min
            if (tl != tr) {
                lazy[2*n] += v;
                lazy[2*n + 1] += v;
            }
            return;
        }
        else {
            int mid = (tl + tr)/2;
            upd(2*n, tl, mid, st, ed, v);
            upd(2*n+1, mid+1, tr, st, ed, v);

            // change me
            treesum[n] = (treesum[2*n] + treesum[2*n+1]);
            treemin[n] = min(treemin[2*n+1], treemin[2*n]);
        }
    }

    T querySum(int n, int tl, int tr, int st, int ed) {
        // change me
        if (tl > tr || ed < tl || st > tr) return 0;

        pushdown(n, tl, tr);

        // segment completely inside query
        if (st <= tl && tr <= ed) {
            return treesum[n];
        }
        else {
            int mid = (tl + tr)/2;
            T a = querySum(2*n, tl, mid, st, ed);
            T b = querySum(2*n + 1, mid + 1, tr, st, ed);

            // change me
            return a+b;
        }
    }

    T queryMin(int n, int tl, int tr, int st, int ed) {
        // change me
        if (tl > tr || ed < tl || st > tr) return MAX;
        pushdown(n, tl, tr);

        // segment completely inside query
        if (st <= tl && tr <= ed) {
            return treemin[n];
        }

        int mid = (tl + tr)/2;
        T a = queryMin(2*n, tl, mid, st, ed);
        T b = queryMin(2*n + 1, mid + 1, tr, st, ed);

        // change me
        return min(a, b);
    }
};

const int SEGSZ = 4*MXV;
LazySeg<long long, SEGSZ> seg;

{% endhighlight %}


## Fast Segment Tree

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

template<class T> struct Seg { // comb(ID,b) = b
	const T ID = 1e18; T comb(T a, T b) { return min(a,b); }
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

Seg<int> st;

int main() {
	int n, q; cin >> n >> q;
  //Note that st.init(n+1) allows us to update and query indices in the range [0,n+1)=[0,n].
	st.init(n+1);
	for(int i=1; i<=n; i++) {
		int a; cin >> a;
		st.upd(i, a);
	}
	for(int i=1; i<=q; i++) {
		int t, a, b; cin >> t >> a >> b;
		if (t==1) st.upd(a,b);
		else cout << st.query(a,b) <<"\n";
	}
}

Seg<int> st;
st.upd(i, x);
int a = st.query(x, y);

bool ckmin(int& a, int b){ return b < a ? a = b, true : false; }
template<class T> struct Seg { // comb(ID,b) = b
    const T ID = 0; T comb(T a, T b) { return min(a,b); }
    int n; vector<T> seg;
    void init(int _n) { n = _n; seg.assign(2*n,ID); }
    void pull(int p) { seg[p] = comb(seg[2*p],seg[2*p+1]); }
    void upd(int p, T val) { // set val at position p
        ckmin(seg[p += n],val); for (p /= 2; p; p /= 2) pull(p); }
    T query(int l, int r) {	// sum on interval [l, r]
        T ra = ID, rb = ID;
        for (l += n, r += n+1; l < r; l /= 2, r /= 2) {
            if (l&1) ra = comb(ra,seg[l++]);
            if (r&1) rb = comb(seg[--r],rb);
        }
        return comb(ra,rb);
    }
};
{% endhighlight %}

## LCA

{% highlight C++ linenos %}
int T = 1;
vector<int> st, ed, depth;
vector<vector<int>> up(2e5 + 1, vector<int> (20));

//euler tour to flattern the tree
void dfs(int n, int p) {
    st[n] = T;
    depth[n] = depth[p] + 1;

    //jump table for node n
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

//dfs to get depth and initialize jump table
depth[0] = -1;
dfs(1, 0);

//lca
int l = lca(a, b);
{% endhighlight %}

## HLD

{% highlight C++ linenos %}
//dfs1 to get depth, parent and sz of each node
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
//dfs2 to flatten and get index T of node, head of node
void dfs2(int n, int h, int p) {
    st[n] = T++;

    //do some calculation.e.g    seg.upd(st[n], values[n]);
    head[n] = h;
    int hv = -1;
    for (auto i : adj[n]) {
        if (i != p) {
            if (hv == -1 || sz[i] > sz[hv]) {
                hv = i;
            }
        }
    }

    // leaf node, then return
    if (hv == -1) return;

    // heavy edge = inherit
    dfs2(hv, h, n);

    // other eddge, start a new segment
    for (auto i : adj[n]) {
        if (i != p && i != hv) {
            // light edge = new segment
            dfs2(i, i, n);
        }
    }
}

//do something for 2 nodes ...
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
{% endhighlight %}

### Union Find
{% highlight C++ linenos %}
int parent[N]; // initialize parent[i] = i

#ifndef PATH_COMPRESSION
int findRoot (int a) {
    if (parent[a] == a) {
      return a;
    }

    return findRoot(parent[a]);
}
#else
//Path Compression - O(log N) per query:
int findRoot (int a) {
  if (parent[a] == a) {
    return a;
  }
    return parent[a] = findRoot(parent[a]);
}
#endif

bool isConnected (int a, int b) {
  return findRoot(a) == findRoot(b);
}

#ifdef KEEP_SIZE_SMALL
int size[N]; // initialize size[i] = 1

void join (int a, int b) {
  a = findRoot(a);
  b = findRoot(b);

  if (a == b) {
    return;
  }

  if (size[a] < size[b]) {
  parent[a] = b;
    size[b] += size[a];
  }
  else {
    parent[b] = a;
    size[a] += size[b];
  }
}
#elseif KEEP_DEPTH_SMALL
int depth[N]; // initialize depth[i] = 1

void join (int a, int b) {
  a = findRoot(a);
  b = findRoot(b);

  if (a == b) {
    return;
  }

  if (depth[a] < depth[b]) {
    parent[a] = b;
  }
  else {
    parent[b] = a;
    depth[a] = max(depth[a], depth[b] + 1);
  }
}
#else
void join (int a, int b) {
  parent[ findRoot(a) ] = findRoot(b);
}

#endif
{% endhighlight %}

## KMP

{% highlight C++ linenos %}
typedef vector<int> VI;

void buildTable(string& w, VI& t)
{
  t = VI(w.length());
  int i = 2, j = 0;
  t[0] = -1; t[1] = 0;

  while(i < w.length())
  {
    if(w[i-1] == w[j]) {
       t[i] = j+1;
       i++;
       j++;
    }
    else if(j > 0) {
      j = t[j];
    }
    else {
      t[i] = 0;
      i++;
    }
  }
}

int KMP(string& s, string& w)
{
  int m = 0, i = 0;
  VI t;

  buildTable(w, t);
  while(m+i < s.length())
  {
    if(w[i] == s[m+i])
    {
      i++;
      if(i == w.length()) return m;
    }
    else
    {
      m += i-t[i];
      if(i > 0) i = t[i];
    }
  }
  return s.length();
}

{% endhighlight %}


## Math  

### Fast Power

{% highlight C++ linenos %}
int mul(int x,int n,int p)
{
   int ans=0;
   while(n) {
       if (n&1)ans=ans+x%p;
       x=x+x%p;
       n>>=1;
   }
   return ans%p;
}

int fpow(int x,int n,int p)
{
   int ans=1;
   while (n) {
       if (n&1) ans=mul(ans,x,p);
       x=mul(x,x,p);
       n>>=1;
   }
   return ans%p;
}
{% endhighlight %}  

### GCD

{% highlight C++ linenos %}
int gcd(int x,int y){
    return y==0?x:gcd(y,x%y);
}

int exgcd(int a,int b,int &x,int &y)
{
    if (b==0) {
        x=1;y=0;
        return a;
    }
    int g=exgcd(b,a%b,x,y);
    int t=x;x=y;y=t-a/b*x;
    return g;
}
{% endhighlight %}

## Data Structure

### Unordered Map Custom Comparitor
{% highlight C++ linenos %}
struct hashPi {
    size_t operator()(const pair<int, int>& p) const { return (p.first*100001) + p.second; }
};
unordered_map<pair<int, int>, int, hashPi> findlca;
{% endhighlight %}

### Priority queue

{% highlight C++ linenos %}
priority_queue<int> q;                           //biggest on top
priority_queue<int,vector<int>,less<int> > q;    //biggest on top

priority_queue<int,vectot<int>,greater<int> > q; //smallest on top

struct cmp{
    bool operator () (pair<int,int> &a, pair<int,int> &b){
        if (a.first!= b.first) return a.first<b.first;
        else return a.second<b.second;
    }
};
priority_queue<rec,vector<rec>,cmp>q;  

{% endhighlight %}

## Sorting

### Quick Sort
{% highlight C++ linenos %}
void quick_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    while (i < j)
    {
        do i ++ ; while (q[i] < x);
        do j -- ; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    quick_sort(q, l, j), quick_sort(q, j + 1, r);
}
{% endhighlight %}

### Merge Sort
{% highlight C++ linenos %}
void merge_sort(int q[], int l, int r)
{
    if (l >= r) return;

    int mid = l + r >> 1;
    merge_sort(q, l, mid);
    merge_sort(q, mid + 1, r);

    int k = 0, i = l, j = mid + 1;
    while (i <= mid && j <= r)
        if (q[i] <= q[j]) tmp[k ++ ] = q[i ++ ];
        else tmp[k ++ ] = q[j ++ ];

    while (i <= mid) tmp[k ++ ] = q[i ++ ];
    while (j <= r) tmp[k ++ ] = q[j ++ ];

    for (i = l, j = 0; i <= r; i ++, j ++ ) q[i] = tmp[j];
}
{% endhighlight %}

## Binary Search  
{% highlight C++ linenos %}
bool check(int x) {/* ... */}  

int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;    
        else l = mid + 1;
    }
    return l;
}

int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}
{% endhighlight %}

## Math

### Binary Search for Equation Solving
{% highlight C++ linenos %}
bool check(double x) {/* ... */}  

double bsearch_3(double l, double r)
{
    const double eps = 1e-6;   
    while (r - l > eps)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;
}
{% endhighlight %}

### Big Integer  

{% highlight C++ linenos %}
// C = A + B, A >= 0, B >= 0
vector<int> add(vector<int> &A, vector<int> &B)
{
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ )
    {
        t += A[i];
        if (i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
    }

    if (t) C.push_back(t);
    return C;
}

// C = A - B, A >= B, A >= 0, B >= 0
vector<int> sub(vector<int> &A, vector<int> &B)
{
    vector<int> C;
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        t = A[i] - t;
        if (i < B.size()) t -= B[i];
        C.push_back((t + 10) % 10);
        if (t < 0) t = 1;
        else t = 0;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

// C = A * b, A >= 0, b > 0
vector<int> mul1(vector<int> &A, int b)
{
    vector<int> C;

    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        if (i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();

    return C;
}

// C = A * B
vector<int> mul2(vector<int> &A, vector<int> &B) {
    vector<int> C(A.size() + B.size(), 0);  

    for (int i = 0; i < A.size(); i++)
        for (int j = 0; j < B.size(); j++)
            C[i + j] += A[i] * B[j];

    int t = 0;
    for (int i = 0; i < C.size(); i++) {  
        t += C[i];
        C[i] = t % 10;
        t /= 10;
    }

    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

// A / b = C ... r, A >= 0, b > 0
vector<int> div(vector<int> &A, int b, int &r)
{
    vector<int> C;
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];
        C.push_back(r / b);
        r %= b;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

{% endhighlight %}


## Prefix Sum

### 1D Prefix Sum
{% highlight C++ linenos %}

for (int i=1; i<=N; i++) {
  pre[i] = val[i] + pre[i-1];
}

//sum from a to b inclusive
pre[b] - pre[a-1]
{% endhighlight %}

### Reverse 1D Prefix Sum
{% highlight C++ linenos %}
val[a] += x;
val[b+1] -= x;

for (int i=1; i< N; i++) {
  val[i] += val[i-1];
}
{% endhighlight %}

### 2D Prefix Sum
{% highlight C++ linenos %}
for (int i=1; i<=N; i++) {
  for (int j=1; j<=N; j++) {
    pre[i][j] = val[i][j] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1];
  }
}

//sum of the range from (x1, y1) to (x2, y2) is:
pre[x2][y2] - pre[x1-1][y2] - pre[x2][y1-1] + pre[x1-1][y1-1]
{% endhighlight %}

### Reverse 2D Prefix Sum
{% highlight C++ linenos %}

// add v to the range from (x1, y1) to (x2, y2), inclusive
val[x1][y1] += v;
val[x1][y2+1] -= v;
val[x2+1][y1] -= v;
val[x2+1][y2+1] += v;

// get value at (i,j)
for (int i=1; i<=N; i++) {
  for (int j=1; j<=N; j++) {
    val[i][j] += + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1];
  }
}
{% endhighlight %}


## Bit Operation

### The k-th bit of an integer n
{% highlight C++ linenos %}
n >> k & 1
{% endhighlight %}

### The first LSB 1 and it's trailing 0s
{% highlight C++ linenos %}
lowbit(n) = n & -n
{% endhighlight %}


## 2 Pointers

{% highlight C++ linenos %}
for (int i = 0, j = 0; i < n; i ++ )
{
    while (j < i && check(i, j)) j ++ ;

    // your code
}
{% endhighlight %}

## Coordinate Compression

{% highlight C++ linenos %}
vector<int> alls; // store all input values
sort(alls.begin(), alls.end());
alls.erase( unique( alls.begin(), alls.end() ), alls.end()); // remove duplicates

// use binary search to find coordinate of value x
// can also be done using upper_bound(alls.begin(), all.end(), x)
int find(int x)
{
    return upper_bound(alls.begin(), alls.end(), x) - alls.begin();
}

//add is array of pairs, first is the uncompressed index, second is the operation to add
//a is the compressed array, each index is compressed from original index
map<int, int> a;
for(auto item : add)
{
    int compressed_index = find(item.first);
    a[compressed_index] += item.second;
}
{% endhighlight %}

## Segments Merger

{% highlight C++ linenos %}
// combine the over lapping ranges
void merge(vector<pair<int,int>> &segs)
{
    vector<pair<int,int>> res;

    sort(segs.begin(), segs.end());

    int st = -2e9, ed = -2e9;

    //[st, ed]: the last range
    for (auto seg : segs)
        //case 1: can't merge new range
        if (ed < seg.first)
        {
            if (st != -2e9)
              res.push_back({st, ed});

            st = seg.first, ed = seg.second;
        }
        else
          //case 2: the new range's end is smaller than last range's end
          //case 3: the new range's end is bigger than last range's end
          //in both cases, extend the new end for the last range
          ed = max(ed, seg.second);

    if (st != -2e9)
      res.push_back({st, ed});

    segs = res;
}
{% endhighlight %}



## Monotonous Stack

{% highlight C++ linenos %}
//Open a stack and decrease monotonically.
//For the top element on the stack, what you can see is the number of elements behind
	stack<int>s;
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;

		//When the input is bigger, remove the smaller from the stack
		while (!s.empty() && temp >= s.top())s.pop();

		s.push(temp);
	}
{% endhighlight %}


## Sliding Window

Use monotonous queue to find minimal in a sliding window.   

{% highlight C++ linenos %}
deque<int> dq;

//find the minimal number in the sliding window
for(int i = 0; i < n; i ++)
{
     //keep the front of the deque always inside sliding window of size k
     if( !dq.empty() && k < i - dq.front() + 1)
         dq.pop_front();

     //maintain monotonous queue
     //if the queue is not empty and the tail element is not smaller than a[i]
     //pop all the bigger elements until it is smaller than a[i]
     while( !dq.empty() && a[dq.back()] >= a[i])
         dq.pop_back();

     dq.push_back(i);

     if(i + 1 >= k)
         cout << a[dq.front()] << " ";
}
{% endhighlight %}


## KMP

{% highlight C++ linenos %}
//ne: based on pattern string p
//ne[i] = j, j the maximal length of prefix: ne[1:j] == ne[i-j+1:i]
for (int i = 2, j = 0; i <= m; i ++ )
{
    while (j && p[i] != p[j + 1])
      j = ne[j];

    if (p[i] == p[j + 1])
      j ++ ;

    ne[i] = j;
}

for (int i = 1, j = 0; i <= n; i ++ )
{
    while (j && s[i] != p[j + 1])
      j = ne[j];

    if (s[i] == p[j + 1])
      j++;

    if (j == m)
    {
        j = ne[j];
    }
}
{% endhighlight %}


## Trie

{% highlight C++ linenos %}
int son[N][26], cnt[N], idx;
// 0 is the root, and empty node  
// son[p][u] stores p's subtree root node
// cnt[p] stores number of words ending with p node

void insert(string str)
{
    int p = 0;

    for (int i = 0; i < str.size(); i ++ )
    {
        int u = str[i] - 'a';

        if (!son[p][u])
          son[p][u] = ++idx;

        p = son[p][u];
    }

    cnt[p]++ ;
}

int query(string str)
{
    int p = 0;
    for (int i = 0; str.size(); i ++ )
    {
        int u = str[i] - 'a';

        if (!son[p][u])
          return 0;

        p = son[p][u];
    }

    return cnt[p];
}

## Geometry 1

{% highlight C++ linenos %}

double INF = 1e100;
double EPS = 1e-12;

template<typename T>
struct Point {
    T x, y;

    Point() : x(0), y(0) {}

    Point(T x0, T y0) : x(x0), y(y0) {}

    Point& operator+=(const Point& p) {
        x += p.x;
        y += p.y;
        return *this;
    }

    Point& operator-=(const Point& p) {
        x -= p.x;
        y -= p.y;
        return *this;
    }

    Point& operator*=(const Point& p) {
        x *= p.x;
        y *= p.y;
        return *this;
    }

    Point& operator/=(const Point& p) {
        x /= p.x;
        y /= p.y;
        return *this;
    }

    Point operator+(const Point& p) const {
        return Point(*this) += p;
    }

    Point operator-(const Point& p) const {
        return Point(*this) -= p;
    }

    Point operator*(const Point& p) const {
        return Point(*this) *= p;
    }

    Point operator/(const Point& p) const {
        return Point(*this) /= p;
    }

    Point operator*(const T& p) const {
        return {x*p, y*p};;
    }

    bool operator < (const Point &p) const {
        if (x != p.x) return x < p.x;
        return y < p.y;
    }
};

template<typename T>
Point<T> operator+(T a, Point<T> p) { return p + a; }

template<typename T>
Point<T> operator*(T a, Point<T> p) { return p * a; }

template<typename T>
T dot(Point<T> p, Point<T> q) { return p.x * q.x + p.y * q.y; }

template<typename T>
T norm(Point<T> p) { return dot(p, p); }

template<typename T>
T dist(Point<T> a, Point<T> b) { return norm(a - b); }

template<typename T>
double abs(Point<T> p) { return sqrt(norm(p)); }

template<typename T>
double proj(Point<T> p, Point<T> q) { return dot(p, q) / abs(q); }

template<typename T>
double angle(Point<T> p, Point<T> q) { return acos(dot(p, q) / abs(p) / abs(q)); }

template<typename T>
T cross(Point<T> p, Point<T> q) { return p.x * q.y - p.y * q.x; }

template<typename T>
Point<T> intersect(Point<T> a1, Point<T> a2, Point<T> d1, Point<T> d2) {
    return a1 + (a2 - a1)*(cross(d1-a1, d1-d2)/cross(a2-a1, d1-d2));
}

template<typename T>
bool segments_parallel(Point<T> a1, Point<T> a2, Point<T> d1, Point<T> d2) {
    return abs(cross(a1-a2,d1-d2)) < EPS; // sin(x) = 0
}

template<typename T>
bool point_on_segment(Point<T> p, Point<T> a, Point<T> b){ // p belongs to (a,b) or not - gives false for a and b
    if (segments_parallel(p,a,p,b) && dot(p-a,p-b) < 0) return true; // to check
    return false;
}

template<typename T>
bool operator==(const Point<T> &p, const Point<T> &q) {
    return p.x == q.x && p.y == q.y;
}

template<typename T>
istream& operator>>(istream &is, Point<T> &p) {
    return is >> p.x >> p.y;
}

template<typename T>
ostream& operator<<(ostream &os, const Point<T> &p) {
    return os << '(' << p.x << ',' << p.y << ')';
}

template<typename T>
bool segments_intersect(Point<T> a, Point<T> b, Point<T> c, Point<T> d){
    if (dist(a,c) < EPS || dist(a,d) < EPS || dist(b,c) < EPS || dist(b,d) < EPS) return true;
    if (dist(a,b) < EPS && dist(c,d) < EPS) return false;
    if (dist(a,b) < EPS) return point_on_segment(a,c,d);
    if (dist(c,d) < EPS) return point_on_segment(c,a,b);

    if (segments_parallel(a,b,c,d) && segments_parallel(a,c,b,d) && segments_parallel(a,d,b,c)){
        if (point_on_segment(a,c,d) || point_on_segment(b,c,d) || point_on_segment(c,a,b) || point_on_segment(d,a,b)) return true;
        return false;
    }

    if (cross(a-b,a-c) * cross(a-b,a-d) > 0) return false; // c and d are one side of (a,b)
    if (cross(c-d,c-a) * cross(c-d,c-b) > 0) return false; // a and b are one side of (c,d)
    return true;
}
{% endhighlight %}


## Geometry 2

{% highlight C++ linenos %}
// Geometry part
double INF = 1e100;
double EPS = 1e-12;

struct point {
  double x, y;
  point() {}
  point(double x, double y) : x(x), y(y) {}
  point(const point &p) : x(p.x), y(p.y) {}
  point operator + (const point &p) const { return point(x+p.x, y+p.y); }
  point operator - (const point &p) const { return point(x-p.x, y-p.y); }
  point operator * (double c) const { return point(x*c, y*c); }
  point operator / (double c) const { return point(x/c, y/c); }
  bool operator < (const point &p) const {
      if (x != p.x) return x < p.x;
      return y < p.y;
  }
};

double dot(point p, point q) { return p.x*q.x + p.y*q.y; } // proportional to cos(x)
double dist(point p, point q) { return sqrt(dot(p-q , p-q)); }
double cross(point p, point q) { return p.x*q.y - p.y*q.x; } // proportional to sin(x) - p to q counterclockwise

bool segments_parallel(point a, point b, point c, point d){ // if (a,b) || (c,d)
    return abs(cross(a-b,c-d)) < EPS; // sin(x) = 0
}

bool point_on_segment(point p, point a, point b){ // p belongs to (a,b) or not - gives false for a and b
    if (segments_parallel(p,a,p,b) && dot(p-a,p-b) < 0) return true; // to check
    return false;
}

bool segments_intersect(point a, point b, point c, point d){    
    if (dist(a,c) < EPS || dist(a,d) < EPS || dist(b,c) < EPS || dist(b,d) < EPS) return true;
    if (dist(a,b) < EPS && dist(c,d) < EPS) return false;
    if (dist(a,b) < EPS) return point_on_segment(a,c,d);
    if (dist(c,d) < EPS) return point_on_segment(c,a,b);
    if (segments_parallel(a,b,c,d) && segments_parallel(a,c,b,d) && segments_parallel(a,d,b,c)){
        if (point_on_segment(a,c,d) || point_on_segment(b,c,d) || point_on_segment(c,a,b) || point_on_segment(d,a,b)) return true;
        return false;
    }
    if (cross(a-b,a-c) * cross(a-b,a-d) > 0) return false; // c and d are one side of (a,b)
    if (cross(c-d,c-a) * cross(c-d,c-b) > 0) return false; // a and b are one side of (c,d)
    return true;
}

point lines_intersection(point a, point b, point c, point d) {
  b=b-a; d=c-d; c=c-a;
  assert(dot(b, b) > EPS && dot(d, d) > EPS);
  return a + b*cross(c, d)/cross(b, d);
}

void print(point a, point b, point c, point d){
    point x[4];
    x[0] = a , x[1] = b, x[2] = c, x[3] = d;
    sort(x,x+4);
    if (dist(x[1],x[2]) < EPS) printf("%.2f %.2f",x[1].x,x[1].y);
    else for (int i=1;i<3;i++) printf("%.2f %.2f ",x[i].x,x[i].y);
    printf("\n");
}

void solve_intersection(point a, point b, point c, point d){
    if (!segments_intersect(a,b,c,d)) cout << "none" << endl; // no intersection
    else if (segments_parallel(a,b,c,d)){ // intersection, includes a=b cases...
        if (dist(a,b) < EPS) printf("%.2f %.2f\n",a.x,a.y);
        else if (dist(c,d) < EPS) printf("%.2f %.2f\n",c.x,c.y);
        else print(a,b,c,d); // prints the two middle points (could be equal)
    }
    else {
        point ans = lines_intersection(a,b,c,d); // normal intersection, when there is one
        printf("%.2f %.2f\n",ans.x,ans.y);            
    }   
}
{% endhighlight %}


## Geometry 3. Sort Points Counter Clockwise using Cross Product

//https://codeforces.com/blog/entry/48122
 a ^ b = a.x * b.y - a.y * b.x = |a||b|sin α.

* if a ^ b > 0, then b points to the left side of d if we're looking in the direction of a;
* if a ^ b = 0, then b lies on d, so it's collinear with a;
* if a ^ b < 0, then b points to the right side of d (as in the picture).

{% highlight C++ linenos %}
inline bool up (point p) {
  return p.y > 0 or (p.y == 0 and p.x >= 0);
}

sort(v.begin(), v.end(), [] (point a, point b) {
  return up(a) == up(b) ? a.x * b.y > a.y * b.x : up(a) < up(b);
});
{% endhighlight %}
