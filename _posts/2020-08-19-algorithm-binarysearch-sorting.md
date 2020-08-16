---
title: "Binary Search and Sorting"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Binary Search
  - Sorting
---

# Binary Search and Sorting

## Sorting with C++ struct

C++ struct can be sorted using lamda functions.

{% highlight c++ linenos %}

struct P {
  int x, y;
};

vector<P> ants(N);

sort(ants.begin(), ants.end(), [](P a, P b) {return p.x < p.x;});
{% endhighlight %}


## Binary Search implementation 1

{% highlight c++ linenos %}

bool binary_search(int l, int r, vector<int> x, int k) {

    while (l <= r) {
        int m = (l+r)/2;
        if (x[m] == k) return true;
        if (x[m] < k) l = m+1; else r = m-1;
    }
    return false;
}

{% endhighlight %}

## Binary Search implementation 2

There are often bugs in binary search implementations. How exactly to update the search bounds and what is the condition when the search should stop?
Here is an alternative binary search implementation that is shorter and should be easier to get correct:

{% highlight c++ linenos %}

ll binary_search(vector<pair<ll, ll>> x) {

    ll max = x.end() - x.begin();
    ll p = 0;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p + a) >= 0 && check(x, p + a)) p += a;
    }
    return p;
}

ll binary_search(vector<ll> x) {

    ll max = x.end() - x.begin();
    ll p = max;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p - a) >= 0 && check(x, p - a)) p -= a;
    }
    return p;
}


{% endhighlight %}

## C++ Functions for Binary Search

* lower_bound returns a pointer to the first array element whose value is at
least x.
*  upper_bound returns a pointer to the first array element whose value is
larger than x.
*  equal_range returns both above pointers.

{% highlight c++ linenos %}

auto a = lower_bound(array, array+n, x);
auto b = upper_bound(array, array+n, x);
cout << b-a << "\n";

auto r = equal_range(array, array+n, x);
cout << r.second-r.first << "\n";
{% endhighlight %}
