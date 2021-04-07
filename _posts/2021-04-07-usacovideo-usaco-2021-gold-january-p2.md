---
title: USACO 2021 Gold January P2. Telephone
categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## USACO 2021 Gold January P2: Telephone  

{% include video id="wad17BQD8n8" provider="youtube" %}
  

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;


int N, K;
const ll MAX_DIST = 2500000000l;

vector<ll>  cowBreed;
bool reachable[60][60];
vector<bool> visited;
vector<ll> distanceFromOne;
vector<vector<ll>> cowBreedLists;

ll ans = LONG_MAX;

priority_queue<pll, vector<pll>, greater<pll>> pq;

inline void insert(int v, int n) {
    if (!visited[v]) {
        ll d = distanceFromOne[n] + abs(v - n);
        if (d < distanceFromOne[v]) {
            distanceFromOne[v] = d;
            pq.push(make_pair(distanceFromOne[v], v));
        }
    }
}

int main() {
    cin >> N >> K;
    cowBreed.resize(N + 1);
    visited.resize(N + 1, false);
    cowBreedLists.resize(K + 1, vector<ll>());
    distanceFromOne.resize(N + 1, MAX_DIST);

    for (int i = 1; i <= N; i++) {
        cin >> cowBreed[i];
        cowBreedLists[cowBreed[i]].push_back(i);
    }

    for (int i = 1; i <= K; i++) {
        for (int j = 1; j <= K; j++) {
            char c;
            cin >> c;
            reachable[i][j] = (c == '1');
        }
    }


    pq.push({0, 1});
    distanceFromOne[1] = 0;

    while (!pq.empty()) {
        ll n = pq.top().second;
        pq.pop();

        if (visited[n]) {
            continue;
        }

        if (n == N) {
            ans = min(ans, distanceFromOne[n]);
        }

        // special handling
        if (reachable[cowBreed[n]][cowBreed[N]]) {
            ans = min(ans, distanceFromOne[n] + N - n);
        }


        visited[n] = true;
        for (int kk = 1; kk < K + 1; kk++) {
            if (reachable[cowBreed[n]][kk]) {
                int left = 0;

                auto it = upper_bound(cowBreedLists[kk].begin(), cowBreedLists[kk].end(), n);

                if (it != cowBreedLists[kk].end()) {
                    // insert right
                    insert(*it, n);
                }

                // insert left
                if (kk == cowBreed[n]) {
                    // special case if same breed, don't push self again
                    if (it - cowBreedLists[kk].begin() >= 2) {
                        left = *(it - 2);
                    }
                }
                else {
                    if (it != cowBreedLists[kk].begin()) {
                        left = *(it - 1);
                    }
                }

                if (left != 0) {
                    insert(left, n);
                }

            }
        }

    }

    if (ans == LONG_MAX) {
        cout << "-1";
    }
    else {
        cout << ans;
    }
    return 0;
}
{% endhighlight %}  
