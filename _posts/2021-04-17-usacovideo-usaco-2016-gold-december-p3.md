---
title: USACO 2016 Gold December P3. Lasers and Mirrors
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2016 Gold December P3. Lasers and Mirrors

{% include video id="OX7gKUgL5wA" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, xL, yL, xB, yB;

unordered_map<int, vector<int>> xSame;
unordered_map<int, vector<int>> ySame;
set<pair<int, int>> v;

// 1: horizontal
// 0: vertical
const int ISX = 1, ISY = 0;

queue<array<int, 3>> pq;

int main() {
    ifstream cin("lasers.in");
    ofstream cout("lasers.out");

    cin >> N >> xL >> yL >> xB >> yB;

    // update xSame/ySame for laser
    xSame[xL].push_back(yL);
    ySame[yL].push_back(xL);
    xSame[xB].push_back(yB);
    ySame[yB].push_back(xB);

    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        xSame[a].push_back(b);
        ySame[b].push_back(a);
    }

    pq.push({0, ISX, xL});
    pq.push({0, ISY, yL});

    while (! pq.empty()) {
        array<int, 3> node = pq.front();
        pq.pop();
        int isanX = node[1], coord = node[2], val = node[0];

        if ((isanX && coord == xB) || (! isanX && coord == yB)) {
            cout << val;
            return 0;
        }

        v.insert({isanX, coord});

        if (isanX) {
            // it is an X
            for (int y : xSame[coord]) {
                if (! v.count({ISY,y})) {
                    pq.push({val + 1, ISY, y});
                }
            }

        }
        else {
            // it is a Y
            for (int x : ySame[coord]) {
                if (! v.count({ISX,x})) {
                    pq.push({val + 1, ISX, x});
                }
            }
        }
    }

}
{% endhighlight %}  
