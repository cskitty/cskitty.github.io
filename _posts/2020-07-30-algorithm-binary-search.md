---
title: "Binary Search"
categories:
  - Programming
tags:
  - Algorithms
  - C++
---

## Binary Search

Explanation

A search algorithm that splits the decision in half every time. If larger, "l" becomes the mid + 1, and if smaller, "r" becomes mid -1, changing the range to the smaller/larger halves.


{% highlight c++ linenos %}

int binarySearch(vector<ll> cities, vector<ll> towers) {
    int ans = 0;
    ll l = 0;
    ll r = max(cities.back(), towers.back()) - min(cities[0], towers[0]);
    while (l <= r) {
        ll mid = (r + l)/2;
        if (possible(mid, cities, towers)) {
            // greater
            ans = mid;
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }

    }
    return ans;
}

{% endhighlight %}
