---
title: "Sorting and Custom Comparators"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Sorting
---

## Sorting with C++ Struct

C++ struct can be sorted using lamda functions.

{% highlight c++ linenos %}

struct P {
  int x, y;
};

vector<P> ants(N);

sort(ants.begin(), ants.end(), [](P a, P b) {return p.x < p.x;});
{% endhighlight %}

C++ struct override operator function example below. Useful for sets and priority queues.

{% highlight c++ linenos %}

struct Point {
    ll x, y;
    int segindex;
    bool start;
};

bool operator< (Point p1, Point p2) { return p1.x==p2.x ? p1.y<p2.y : p1.x<p2.x; }

struct Segment {
    Point p, q;
    int index;
};

bool operator< (Segment s1, Segment s2) { return s1.index != s2.index && eval(s1)<eval(s2); }
bool operator== (Segment s1, Segment s2) { return s1.index == s2.index; }


{% endhighlight %}
