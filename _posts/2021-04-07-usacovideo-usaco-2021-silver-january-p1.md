---
title: USACO 2021 Silver January P1. Dance Mooves
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2021 Silver January P1: Dance Mooves  

{% include video id="WaumFVLE6Dc" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define f first
#define s second

ll N, K;

vector<pair<int, int>> swaps;
vector<int> jumpTable;

vector<int> myGroup;
vector<vector<int>> groups;
vector<vector<int>> trace;
vector<int> ans;

// STEP 1: simulate to get the trace for each node
void simulation(vector<ll> &a) {
    // include itself
    for (int i = 1; i <= N; i++) {
        trace[i].push_back(i);
    }

    // simulate first K cycles
    for(int i = 0; i < swaps.size(); i++) {

        int l = swaps[i].f;
        int r = swaps[i].s;

        trace[a[l]].push_back(r);
        trace[a[r]].push_back(i);

        swap(a[l], a[r]);
    }
}

// STEP 2: create jump table
void make_table(vector<ll> &a) {
    // create jumpTable
    for (int i = 1; i < a.size(); i++) {
        jumpTable[a[i]] = i;
    }
}


// STEP 3: find groups of cows using DFS
void findCycles(vector<ll> &a) {
    int currentID = 0;

    for(int i = 1; i <= N ; i++) {
        if (myGroup[i] != -1) {
            continue;
        }

        vector<int> groupIds;
        myGroup[i] = currentID;
        groupIds.push_back(i);
        int j = jumpTable[i];
        int currPhase = 0;
        while (j != i) {
            currPhase++;
            myGroup[j] = currentID;
            groupIds.push_back(j);
            j = jumpTable[j];
        }

        groups.push_back(groupIds);
        currentID++;
    }
}



int main() {
    cin >> N >> K;

    swaps.resize(K);
    trace.resize(N+1);
    jumpTable.resize(N+1);
    myGroup.resize(N+1, -1);
    ans.resize(N+1, 0);

    for (int i = 0; i < K; i++) {
        int a, b;
        cin >> a >> b;
        swaps[i].f = a;
        swaps[i].s = b;
    }

    vector<ll> a(N+1);
    iota(a.begin(), a.end(), 0);

    simulation(a);
    make_table(a);

    findCycles(a);

    map<int, int> finAns;
    for(int groupId = 0; groupId < groups.size(); groupId++) {
        // everything
        unordered_set<int> currSet;
        for (int j = 0; j < groups[groupId].size(); j++) {
            // merge
            for (auto k : trace[groups[groupId][j]]) {
                currSet.insert(k);
            }
        }
        finAns[groupId] = currSet.size();
        continue;
    }

    for (int i = 1; i <= N; i++) {
        cout << max(finAns[myGroup[i]], 1) << endl;
    }

}
{% endhighlight %}  
