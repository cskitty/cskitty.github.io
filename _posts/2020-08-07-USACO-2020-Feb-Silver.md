---
title: "USACO 2020 Feb Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2020 Feb Silver

## Problem 1. Swapity Swapity Swap

Farmer John's N cows (1≤N≤105) are standing in a line. The ith cow from the left has label i for each 1≤i≤N.  
Farmer John has come up with a new morning exercise routine for the cows. He has given the cows M pairs of integers (L1,R1)…(LM,RM), where 1≤M≤100. He then tells the cows to repeat the following M-step process exactly K (1≤K≤109) times:   

For each i from 1 to M:  
The sequence of cows currently in positions Li…Ri from the left reverse their order.
After the cows have repeated this process exactly K times, please output the label of the ith cow from the left for each 1≤i≤N.  

SCORING:  
Test case 2 satisfies N=K=100.  
Test cases 3-5 satisfy K≤103.  
Test cases 6-10 satisfy no additional constraints.  
INPUT FORMAT (file swap.in):  
The first line contains N, M, and K. For each 1≤i≤M, line i+1 line contains Li and Ri, both integers in the range 1…N, where Li<Ri.  
OUTPUT FORMAT (file swap.out):  
On the ith line of output, print the ith element of the array after the instruction string has been executed K times.  
SAMPLE INPUT:  
```
7 2 2
2 5
3 7
```
SAMPLE OUTPUT:
```
1
2
4
3
5
7
6
```
Initially, the order of the cows is [1,2,3,4,5,6,7] from left to right. After the first step of the process, the order is [1,5,4,3,2,6,7]. After the second step of the process, the order is [1,5,7,6,2,3,4]. Repeating both steps a second time yields the output of the sample.  


Problem credits: Brian Dean

{% highlight C++ linenos %}
void setIn(str s) { freopen(s.c_str(),"r",stdin); }
void setOut(str s) { freopen(s.c_str(),"w",stdout); }
void unsyncIO() { ios_base::sync_with_stdio(0); cin.tie(0); }
void setIO(str s = "") {
    unsyncIO();
    if (sz(s)) { setIn(s+".in"), setOut(s+".out"); } // for USACO
}

vector<ll> simulation(vector<pair<ll, ll>> swaps, ll N, vector<ll> a) {

    vector<ll> b = a;
    F0R(i, swaps.size()) {
        // current swap
        int l = swaps[i].f;
        int r = swaps[i].s;
        FOR(j, l, r + 1) {
            b[j] = a[l + r - j];
        }
        a = b;
    }
    return b;
}

vector<ll> group(MX, 0);
vector<ll> phase(MX, 0);
map<ll, vector<ll>> groups;

void cycles(int N, vector<ll> a, vector<ll> b) {

    int currentID = 1;
    FOR(i, 1, N) {
        if(group[i] != 0) {
            continue;
        }
        vector<ll> cycleVec;
        group[i] = currentID;
        cycleVec.push_back(i);
        int j = b[i];
        int currPhase = 0;
        while (j != i) {
            currPhase++;
            phase[j] = currPhase;
            group[j] = currentID;
            cycleVec.push_back(j);
            j = b[j];
        }
        groups[currentID] = cycleVec;
        currentID++;
    }
}

int main() {
    setIO("swap");

    ll N, M, K;
    cin >> N >> M >> K;
    N++;

    vector<pair<ll, ll>> swaps(M);

    F0R(i, M) {
        int a, b;
        cin >> a >> b;
        swaps[i].f = a;
        swaps[i].s = b;
    }

    vector<ll> a(N);
    FOR(i, 1, N) {
        a[i] = i;
    }

    vector<ll> b = simulation(swaps, N, a);

    cycles(N, a, b);

    FOR(i, 1, N) {
        cout << groups[group[i]][(K + phase[i]) % groups[group[i]].size()] << endl;
    }

}
{% endhighlight %}
