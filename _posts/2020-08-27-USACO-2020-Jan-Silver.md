---
title: "USACO 2020 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2020 Jan Silver

## Problem 1. Berry Picking

[Berry Picking](http://www.usaco.org/index.php?page=viewproblem2&cpid=990)

Bessie and her little sister Elsie are picking berries in Farmer John's berry patch. Farmer John's patch has exactly N berry trees (1≤N≤1000); tree i contains exactly Bi berries (1≤Bi≤1000). Bessie has exactly K baskets (1≤K≤1000, K even). Each basket can hold as many berries from a single tree as Bessie wants, but cannot contain berries from two different trees as their flavors will clash with each other. Baskets may remain empty.  
Bessie wants to maximize the number of berries she collects. However, Farmer John wants Bessie to share with her little sister, and so Bessie will have to give Elsie the K/2 baskets with the largest number of berries. This means that Elsie may even end up with more berries than Bessie, which is very unfair, but unfortunately, sibling dynamics are not always fair.  

Help Bessie figure out the maximum number of berries she can collect.  

SCORING:   
Test cases 1-4 satisfy K≤10.  
Test cases 5-11 satisfy no additional constraints.  
INPUT FORMAT (file berries.in):  
The first line of input contains space-separated integers N and K.  
The second line contains N space-separated integers B1,B2,…,BN.  

OUTPUT FORMAT (file berries.out):  
A single line with the answer.  
SAMPLE INPUT:  
```
5 4
3 6 8 4 2
```
SAMPLE OUTPUT:
```
8
```
If Bessie fills  

one basket with 6 berries from tree 2  
two baskets, each with 4 berries from tree 3  
one basket with 4 berries from tree 4  
then she receives two baskets each with 4 berries, giving her 8 berries in total.  

Problem credits: Nathan Pinsker
{% highlight c++ linenos %}

{% endhighlight %}

## Problem 2. Loan Repayment

[Berry Picking](http://www.usaco.org/index.php?page=viewproblem2&cpid=991)

Farmer John owes Bessie N gallons of milk (1≤N≤1012). He has to give her the milk within K days. However, he doesn't want to give the milk away too quickly. On the other hand, he has to make forward progress on the loan, so he must give Bessie at least M gallons of milk each day (1≤M≤1012).  
Here is how Farmer John decides to pay back Bessie. He first picks a positive integer X. He then repeats the following procedure every day:  

Assuming that Farmer John has already given Bessie G gallons, compute N−GX rounded down. Call this number Y.  
If Y is less than M, set Y to M.  
Give Bessie Y gallons of milk.  
Determine the largest X such that if Farmer John follows the above procedure, Farmer John gives Bessie at least N gallons of milk after K days (1≤K≤1012).  

SCORING:  
Test cases 2-4 satisfy K≤105.  
Test cases 5-11 satisfy no additional constraints.  
INPUT FORMAT (file loan.in):  
The only line of input contains three space-separated positive integers N, K, and M satisfying K⋅M<N.  
OUTPUT FORMAT (file loan.out):  
Output the largest positive integer X such that Farmer John will give Bessie at least N gallons using the above procedure.  
SAMPLE INPUT:  
```
10 3 3
```
SAMPLE OUTPUT:
```
2
```

For the first test case, when X=2 Farmer John gives Bessie 5 gallons on the first day and M=3 gallons on each of the next two days.  

Note that the large size of integers involved in this problem may require the use of 64-bit integer data types (e.g., a "long long" in C/C++).  

Problem credits: Nick Wu  

{% highlight c++ linenos %}
ll N;
ll M, K, Kv;

bool check(ll target) {
    K = Kv;
    ll G = 0;

    dbg(target);
    while (K > 0 && G < N) {
        ll Y = (N - G)/target;
        if (Y <= M) {
            return (G + M * K) >= N;
        }
        ll days = (N - G - (target * Y))/Y + 1;
        if (days > K) {
            days = K;
        }
        G += Y * days;
        K-= days;
    }
    return G >= N;
}

ll binary_search() {

    ll max = 1e12;
    ll p = 0;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p + a) > 0 && check(p + a)) {
            p += a;
        }
    }
    return p;
}

int main() {
    setIO("loan");

    cin >> N >> K >> M;
    Kv = K;

    cout << binary_search();

}
{% endhighlight %}



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
