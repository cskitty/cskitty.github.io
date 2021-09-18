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


## Fast Segment Tree
{% highlight C++ linenos %}
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
st.upd(i, x);
int a = st.query(x, y);
{% endhighlight %}

## LCA

{% highlight C++ linenos %}

vector<vector<int>> up(2e5 + 1, vector<int> (20));

//initialize jump table
up[c][0] = p;
for (int i = 1; i < 20; i++) {
    up[c][i] = up[up[c][i-1]][i-1];
}

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
S[i] = a[1] + a[2] + ... a[i]
a[l] + ... + a[r] = S[r] - S[l - 1]
{% endhighlight %}

### Reverse 1D Prefix Sum
{% highlight C++ linenos %}
B[l] += c, B[r + 1] -= c
{% endhighlight %}

### 2D Prefix Sum
{% highlight C++ linenos %}
S[i, j] = sum of first i rows and j columns
S[x2, y2] - S[x1 - 1, y2] - S[x2, y1 - 1] + S[x1 - 1, y1 - 1]
{% endhighlight %}

### Reverse 2D Prefix Sum
{% highlight C++ linenos %}
S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c
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
{% endhighlight %}
