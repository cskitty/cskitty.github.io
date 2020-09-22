---
title: "Binary Search"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Binary Search
---

# Binary Search

## Minimum Possible

Binary search with false false true true.

{% highlight c++ linenos %}

int binary_search() {
    int l = 0;
    int r = 1e9 + 1;
    while (l != r) {
        int mid = (l + r)/2;
        if (check(mid)) {
            r = mid;
        }
        else {
            l = mid + 1;
        }
    }
    return l;
}

{% endhighlight %}

## Maximum Possible

Binary search with true true false false.

{% highlight c++ linenos %}

  int binary_search(vector<ll> x) {

      int l = 0;
      int r = 1e9 + 1;
      while (l != r) {
          int mid = (l + r + 1)/2;
          if (check(x, mid)) {
              l = mid;
          }
          else {
              r = mid - 1;
          }
      }
      return l;
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
