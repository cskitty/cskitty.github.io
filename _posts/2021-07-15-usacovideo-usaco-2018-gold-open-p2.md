---
title: USACO 2018 Gold US Open P2. Milking Order
categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## [USACO 2018 Gold US Open P2. Milking Order](http://www.usaco.org/index.php?page=viewproblem2&cpid=838)

{% include video id="OaL9vEkShyk" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<int>> inputV;
vector<int> ans;

bool check(int x) {
    vector<vector<int>> adj(N + 1);
    vector<int> inDegree(N + 1, 0);

    for(int i = 0; i < x; i++) {
        for(int j = 1; j < inputV[i].size(); j++) {
            adj[inputV[i][j - 1]].push_back(inputV[i][j]);
            inDegree[inputV[i][j]]++;
        }
    }

    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 1; i < N + 1; i++) {
        if (! inDegree[i]) {
            pq.push(i);
        }
    }

    if (pq.empty()) {
        return false;
    }

    int turns = 0;
    while (! pq.empty()) {
        turns++;
        int node = pq.top(); pq.pop();
        ans[turns] = node;

        for (int child : adj[node]) {
            inDegree[child]--;

            if (inDegree[child] == 0) {
                pq.push(child);
            }
        }
    }

    if (turns != N) {
        return false;
    }
    return true;
}

int binary_search() {
    int l = 0;
    int r = M - 1;
    while (l != r) {
        int mid = (l + r + 1)/2;
        if (check(mid)) {
            l = mid;
        }
        else {
            r = mid - 1;
        }
    }
    // make sure to double check l!
    check(l);
    return l;
}

int main() {
    ifstream cin("milkorder.in");
    ofstream cout("milkorder.out");

    cin >> N >> M;

    ans.resize(N + 1);
    inputV.resize(M);

    // read in input
    for (int i = 0; i < M; i++) {
        int v;
        cin >> v;
        for (int j = 0; j < v; j++) {
            int val;
            cin >> val;
            inputV[i].push_back(val);
        }
    }

    // run binary search
    binary_search();

    // print answer
    for (int i = 1; i < N; i++) {
        cout << ans[i] << " ";
    }
    cout << ans[N];
    cout << endl;
}
{% endhighlight %}  
