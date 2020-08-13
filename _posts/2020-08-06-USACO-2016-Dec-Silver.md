---
title: "USACO 2016 Dec Silver"
categories:
  - USACO
tags:
  - Algorithms
  - Python
  - USACO
  - FloodFill
---

# USACO 2016 Dec Silver

## Problem 1.  Counting Haybales

[Counting Haybales](http://www.usaco.org/index.php?page=viewproblem2&cpid=666)

Farmer John has just arranged his N haybales (1≤N≤100,000) at various points along the one-dimensional road running across his farm. To make sure they are spaced out appropriately, please help him answer Q queries (1≤Q≤100,000), each asking for the number of haybales within a specific interval along the road.
INPUT FORMAT (file haybales.in):
The first line contains N and Q.
The next line contains N distinct integers, each in the range 0…1,000,000,000, indicating that there is a haybale at each of those locations.

Each of the next Q lines contains two integers A and B (0≤A≤B≤1,000,000,000) giving a query for the number of haybales between A and B, inclusive.

OUTPUT FORMAT (file haybales.out):
You should write Q lines of output. For each query, output the number of haybales in its respective interval.
SAMPLE INPUT:
```
4 6
3 2 7 5
2 3
2 4
2 5
2 7
4 6
8 10
```
SAMPLE OUTPUT:
```
2
2
3
4
1
0
```
Problem credits: Nick Wu

{% highlight c++ linenos %}

// USACO Input & Output
void setIO(string name) {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen((name+".in").c_str(),"r",stdin);
    freopen((name+".out").c_str(),"w",stdout);
}

int myLowerBound(int l, int r, vector<int> arr, int needed) {
    while(l<r)
    {
        int mid=(l+r)>>1;
        mid++;
        //dbg(l, r, mid);
        // switch to < if upper bound
        if(arr[mid] < needed) {
            l = mid;
        }
        else r=mid-1;
    }
    return l + 1;
}

int main() {
    setIO("haybales");

    int N, Q;
    cin >> N >> Q;

    vector<int> bales(N);

    F0R(i, N) {
        int x;
        cin >> bales[i];
    }

    sort(bales.begin(), bales.end());

    F0R(i, Q) {
        int S, E;
        cin >> S >> E;


        //dbg( lower_bound(bales.begin(), bales.end(), E) - bales.begin());
        //dbg( myLowerBound(0, N - 1, bales, E) );
        cout << upper_bound(bales.begin(), bales.end(), E) - bales.begin() - myLowerBound(0, N - 1, bales, S) << endl;
    }

}
{% endhighlight %}
