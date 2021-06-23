---
title: USACO 2015 Gold January P2. Moovie Mooving
categories:
  - video
tags:
  - USACO Platinum
  - VIDEO
---

## [USACO 2015 Gold January P2. Moovie Mooving](http://www.usaco.org/index.php?page=viewproblem2&cpid=515)

{% include video id="oKm_GZD9u1E" provider="youtube" %}

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, L;
vector<vector<int>> schedule;
vector<vector<vector<int>>> next_show;
vector<int> D;
vector<pair<int, int>> dp;

//bit operations
inline int pct(int x) { return __builtin_popcount(x); }
inline int setbit(int n, int k) { return (n | (1 << k)); }
inline int getbit(int n, int k) { return (n & ( 1 << k )) >> k; }

int find_show_time(int t, int m) {
    auto it = upper_bound(schedule[m].begin(), schedule[m].end(), t);
    if (it == schedule[m].begin()) {
        return -1;
    }

    int start = *(it - 1);
    if (start + D[m] < t || start > t) {
        return -1;
    }

    return (it - 1) - schedule[m].begin();
}

int main() {
    ifstream cin("movie.in");
    ofstream cout("movie.out");
    cin >> N >> L;

    D.resize(N);
    schedule.resize(N);
    next_show.resize(N, vector<vector<int>>(N, vector<int>(0, -1)));

    for (int i = 0; i < N; i++) {
        int t, v;
        cin >> t >> v;
        D[i] = t;
        int a;
        while(v) {
            cin >> a;
            schedule[i].push_back(a);
            v--;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            for (int ii = 0; ii < schedule[i].size(); ii++) {
                next_show[i][j].push_back(find_show_time(schedule[i][ii] + D[i], j));
            }
        }
    }

    // dp[x] = {last_movie, last_move_schedule_index}
    dp.resize(pow(2, N), {-1, -1});

    int ans = N + 1;
    dp[0] = {0, 0};

    // schedule subset loop
    for (int i = 0; i < pow(2, N); i++) {
        if (dp[i].first == -1) continue;
        for (int j = 0; j < N; j++) {
            // has movie j already been watched?
            if (getbit(i, j)) continue;
            int subset = setbit(i, j);

            int x;
            if (i == 0) {
                x = schedule[j][0] == 0 ? 0:-1;
            }
            else {
                x = next_show[dp[i].first][j][dp[i].second];
            }
            if (x != -1) {
                // subset including j
                if (dp[subset].first == -1 || schedule[dp[subset].first][dp[subset].second] + D[dp[subset].first] < schedule[j][x] + D[j]) {
                    dp[subset] = {j, x};
                }
                if (schedule[dp[subset].first][dp[subset].second] + D[dp[subset].first] >= L) {
                    ans = min(ans, pct(subset));
                }
            }
        }
    }

    if (ans == N + 1) {
        cout << -1;
    }
    else {
        cout << ans;
    }
}
{% endhighlight %}  
