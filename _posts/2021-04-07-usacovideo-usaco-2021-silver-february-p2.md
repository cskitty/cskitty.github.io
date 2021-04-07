---
title: USACO 2021 Silver February P2. Year of the Cow
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2021 Silver February P2. Year of the Cow  

{% include video id="MY5Ait0AcmE" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> cows(N);
    for (int i = 0; i < N; i++) {
        cin >> cows[i];
    }

    sort(cows.begin(), cows.end());

    int k = 0, d = 12;
    vector<int> floor(N);
    vector<int> jumps;

    floor[0] = cows[0] - (cows[0] % 12);
    if (floor[0] != 0) {
        k++;
        jumps.push_back(floor[0]);
    }
    for (int i = 1; i < N; i++) {
        floor[i] = cows[i] - (cows[i]%12);
        if (floor[i] - floor[i - 1] >= 24) {
            jumps.push_back(floor[i] - floor[i - 1] - 12);
            d += 12;
            k++;
        }
        else if (floor[i] - floor[i - 1] == 12) {
            d += 12;
        }
        else {
            continue;
        }
    }

    sort(jumps.begin(), jumps.end());

    int i = 0;
    while (k >= K) {
        k--;
        d += jumps[i];
        i++;
    }

    cout << d;

}  
{% endhighlight %}  
