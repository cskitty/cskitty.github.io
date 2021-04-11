---
title: USACO 2021 Gold Open Q1. United Cows of Farmer John
categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## USACO 2021 Gold Open Q1. United Cows of Farmer John

{% include video id="t0Rc9pU0q4o" provider="youtube" %}


{% highlight C++ linenos %}
#include<bits/stdc++.h>
using namespace std;

int N;
long long ans = 0;
const int MX = 2e5 + 1;
int prevbreedtype[MX];
int cows[MX];
int bit[MX];

void updateBIT(int a, int b) {
    while (a <= N) { bit[a] += b; a += (a & (-a));}
}

int query(int a) {
    int r = 0;
    while (a > 0) {r += bit[a]; a = a - (a & (-a));} return r;
}

inline void runBIT() {
    for (int i = 0; i < N; i++) {
        // last cow of same breed
        int mybreed = cows[i];
        int lastcow = prevbreedtype[mybreed];

        if (lastcow != -1) {
            // reset to 0 so we can update again with 1 so no overcounting
            updateBIT(lastcow + 1, -1);
        }
        // new breed type
        prevbreedtype[mybreed] = i;
        updateBIT(i + 1, 1);

        if (i > 0) {
            int p1 = max(0, lastcow);
            ans += query(i) - query(p1);
        }
    }
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> cows[i];
        prevbreedtype[i] = -1;
    }

    runBIT();

    cout << ans;
}
{% endhighlight %}  
