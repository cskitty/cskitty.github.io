---
title: USACO 2021 Gold Open Q2. Portals
categories:
  - video
tags:
  - USACO Gold
  - VIDEO
---

## USACO 2021 Gold Open Q2. Portals

{% include video id="FusSjc7Gx_w" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N;

const int mx = 1e5;
const int shift = mx*2;
const int mxsz = shift*2;

vector<pair<int, int>> cost;
vector<vector<pair<int, int>>> neighbors;
vector<bool> visited;
set<int> nodes;
vector<int> parent;
vector<int> found;

int shiftover(int a) {return a+shift;}

int getRoot(int a) {
  if (parent[a] == a) return a;
  return parent[a] = getRoot(parent[a]);
}

vector<int> opt;
void join (int a, int b) {
  a = getRoot(a); b = getRoot(b);
  if (a == b) return;

  if (opt[a] < opt[b]) {
      parent[a] = b;
      opt[b] += opt[a];
  }
  else {
      parent[b] = a;
      opt[a] += opt[b];
  }
}

void dfs(int node) {
  if (visited[node]) return;

  visited[node] = true;
  for(int i = 0; i < 2; i++) {
      nodes.insert(neighbors[node][i].second);

      int child = neighbors[node][i].first;
      dfs(child);
  }
}

inline int makestart() {
  int start = *nodes.begin(); int prev = start;
  if (found[start] > 0) start = shiftover(start);
  found[prev]++;
  return start;
}

inline void runjoin(int start, int val) {
  if (found[val] != 0) {
      join(start, shiftover(val));
  }
  else {
      join(start, val);
  }
}

inline int runp() {
  int g = 0;
  for (int i = 1; i < 2*N + 1; i++) {
      if (! visited[i]) {
          dfs(i);
          // start set
          int start = makestart();
          // loop through
          auto j = nodes.begin();
          j++;
          while (j != nodes.end()) {
              int val = *j;
              runjoin(start, val);
              found[val]++;
              j++;
          }
          nodes.clear();
          g++;
      }
  }
  return g;
}


void make(int szv) {
  opt.resize(szv, 1);
  parent.resize(szv);
  found.resize(shift+1, 0);
  neighbors.resize(shift+1);
  visited.resize(shift+1);
  iota(parent.begin(), parent.end(), 0);
}

inline int unionfind(int numofgroups) {
  int ans = 0;
  for (int ind = 0; ind < cost.size() && numofgroups > 1; ind++) {
      // find smallest value
      int val = cost[ind].second;

      if (found[val] == 1) {
          continue;
      }

      int r1 = getRoot(val); int r2 = getRoot(shiftover(val));

      if (r1 != r2) {
          ans += cost[ind].first;
          join(r1, r2);
          numofgroups--;
      }
  }
  return ans;
}

int main() {
  cin >> N;
  cost.resize(N);
  make(mxsz + 1);

  for (int i = 0; i < N; i++) {
      int p1, p2, p3, p4;
      cin >> cost[i].first >> p1 >> p2 >> p3 >> p4;
      cost[i].second = i + 1;

      for (int j = 0; j < 2; j++) {
          neighbors[(j%2==0)?p1:p2].push_back({(j%2==0)?p2:p1, i + 1});
          neighbors[(j%2==0)?p3:p4].push_back({(j%2==0)?p4:p3, i + 1});
      }
  }
  sort(cost.begin(), cost.end());

  int numofgroups = runp();

  int ans = unionfind(numofgroups);

  cout << ans;

}
{% endhighlight %}  
