---
title: USACO 2020 Silver US Open P2. Cereal
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2020 Silver US Open P2: Cereal  

{% include video id="FcCdPu9Yz70" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
int N, M;

const int MaX = 100001;
vector<int> occ(MaX, 0);
int ans = 0;
vector<pair<int, int>> cows(MaX);

int main() {
    ifstream cin("cereal.in");
    ofstream cout("cereal.out");
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        int F, S;
        cin >> F >> S;
        cows[i].f = F;
        cows[i].s = S;
    }

    vector<int> ansVec(N);

    for (int i = N - 1; i >= 0; i--) {
        int pos = cows[i].f;
        int j = i;

        while (true) {
            if (occ[pos] == 0) {
                occ[pos] = j;
                ans++;
                break;
            }
            else if (occ[pos] < j) {
                break;
            }
            else {
                int next = occ[pos];
                occ[pos] = j;
                if (pos == cows[next].s) {
                    break;
                }
                j = next;
                pos = cows[next].s;
            }
        }
        ansVec[i] = ans;

    }

    for (int i = 0; i < N; i++) {
        cout << ansVec[i] << endl;
    }
}  
{% endhighlight %}  
