---
title: "Binary Search and Sorting"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Binary search
  - Sorting
---

## Sorting with C++ struct

C++ struct can be sorted using lamda functions.

{% highlight java linenos %}
struct P {
  int x, y;
};

sort(ants.begin(), ants.end(), [](P a, P b) {return p.x < p.x;});
{% endhighlight %}



## Binary Search

{% highlight java linenos %}
int a = 0, b = n-1;

while (a <= b) {
  int k = (a+b)/2;
  if (array[k] == x) {
  // x found at index k
  }
  if (array[k] > x) b = k-1;
  else a = k+1;
}
{% endhighlight %}

## C++ Functions for Binary Search

* lower_bound returns a pointer to the first array element whose value is at
least x.
*  upper_bound returns a pointer to the first array element whose value is
larger than x.
*  equal_range returns both above pointers.

{% highlight java linenos %}

auto a = lower_bound(array, array+n, x);
auto b = upper_bound(array, array+n, x);
cout << b-a << "\n";

auto r = equal_range(array, array+n, x);
cout << r.second-r.first << "\n";

{% endhighlight %}
