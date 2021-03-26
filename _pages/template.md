---
title: "Competitive Coding Algoritms"
layout: archive
permalink: /template949/
taxonomy: USACO
author_profile: true
---

![](/assets/images/USACObessieheader.PNG)

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
    for (auto seg : segs)
        if (ed < seg.first)
        {
            if (st != -2e9)
              res.push_back({st, ed});

            st = seg.first, ed = seg.second;
        }
        else
          ed = max(ed, seg.second);

    if (st != -2e9)
      res.push_back({st, ed});

    segs = res;
}
{% endhighlight %}
