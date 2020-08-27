---
title: "USACO 2020 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2020 Jan Silver

## Problem 3. Wormhole Sort

[Wormhole Sort](http://www.usaco.org/index.php?page=viewproblem2&cpid=992)
Farmer John's cows have grown tired of his daily request that they sort themselves before leaving the barn each morning. They have just completed their PhDs in quantum physics, and are ready to speed things up a bit  
This morning, as usual, Farmer John's N cows (1≤N≤105), conveniently numbered 1…N, are scattered throughout the barn at N distinct locations, also numbered 1…N, such that cow i is at location pi. But this morning there are also M wormholes (1≤M≤105), numbered 1…M, where wormhole i bidirectionally connects location ai with location bi, and has a width wi (1≤ai,bi≤N,ai≠bi,1≤wi≤109).  

At any point in time, two cows located at opposite ends of a wormhole may choose to simultaneously swap places through the wormhole. The cows must perform such swaps until cow i is at location i for 1≤i≤N.  

The cows are not eager to get squished by the wormholes. Help them maximize the width of the least wide wormhole which they must use to sort themselves. It is guaranteed that it is possible for the cows to sort themselves.  

SCORING  
Test cases 3-5 satisfy N,M≤1000.  
Test cases 6-10 satisfy no additional constraints.  
INPUT FORMAT (file wormsort.in):  
The first line contains two integers, N and M.  
The second line contains the N integers p1,p2,…,pN. It is guaranteed that p is a permutation of 1…N.  

For each i between 1 and M, line i+2 contains the integers ai, bi, and wi.   

OUTPUT FORMAT (file wormsort.out):  
A single integer: the maximum minimal wormhole width which a cow must squish itself into during the sorting process. If the cows do not need any wormholes to sort themselves, output −1  
SAMPLE INPUT:
```
4 4
3 2 1 4
1 2 9
1 3 7
2 3 10
2 4 3
```
SAMPLE OUTPUT:
```
9
```
Here is one possible way to sort the cows using only wormholes of width at least 9:

Cow 1 and cow 2 swap positions using the third wormhole.
Cow 1 and cow 3 swap positions using the first wormhole.
Cow 2 and cow 3 swap positions using the third wormhole.
SAMPLE INPUT:
4 1
1 2 3 4
4 2 13
SAMPLE OUTPUT:
-1
No wormholes are needed to sort the cows.

Problem credits: Dhruv Rohatgi

{% highlight c++ linenos %}
struct edge {
        int e;
        int w;
        bool on;
};

const int MN = 1e5+1;
int N, M;
int maxW = -1;
int th, wM = INT_MIN;

vector<edge> adj_list[MN];
vector<int> order(MN);
vector<int> visited(MN);
vector<int> opp(MN);

void floodFill(int curr, int color) {
    visited[curr] = color;
    for (edge i : adj_list[curr]) {
        if (i.w >= th && visited[i.e] == 0) {
            floodFill(i.e, color);
        }
    }

}

bool check(int threshold) {
    th = threshold;
    dbg(th);
    fill(visited.begin(), visited.end(), 0);
    int color = 0;
    FOR(i, 1, N + 1) {
        if (visited[i] == 0) {
            color++;
            floodFill(opp[i], color);
        }
    }

    FOR(i, 1, N + 1) {
        if (visited[order[i]] != visited[i]) {
            return false;
        }
    }
    return true;
}

int binary_search() {

    int max = wM;
    int p = 0;
    for (int a = max; a >= 1; a /= 2) {
        while ((p + a) <= wM && check(p + a)) {
            p += a;
        }
    }
    return p;
}


int main() {
    setIO("wormsort");
    cin >> N >> M;

    F0R(i, N) {
        cin >> order[i + 1];
        opp[i + 1] = order[i + 1];
    }

    F0R(i, M) {
        int A, B, C;
        cin >> A >> B >> C;
        adj_list[A].push_back({B, C, true});
        adj_list[B].push_back({A, C, true});
        wM = max(wM, C);
    }

    int ans = binary_search();

    if (ans >= wM) {
        cout << -1;
    }
    else {
        cout << ans;
    }


}
{% endhighlight %}
