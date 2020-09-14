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

[Swapity Swapity Swap](http://www.usaco.org/index.php?page=viewproblem2&cpid=1014)

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


## Problem 2. Triangles

[Triangles](http://www.usaco.org/index.php?page=viewproblem2&cpid=1015)

Farmer John would like to create a triangular pasture for his cows.  
There are N fence posts (3≤N≤105) at distinct points (X1,Y1)…(XN,YN) on the 2D map of his farm. He can choose three of them to form the vertices of the triangular pasture as long as one of the sides of the triangle is parallel to the x-axis and another side is parallel to the y-axis.  

What is the sum of the areas of all possible pastures that FJ can form?  

SCORING:  
Test case 2 satisfies N=200.  
Test cases 3-4 satisfy N≤5000.  
Test cases 5-10 satisfy no additional constraints.  
INPUT FORMAT (file triangles.in  
The first line contains N.  
Each of the next N lines contains two integers Xi and Yi, each in the range −104…104 inclusive, describing the location of a fence post.  

OUTPUT FORMAT (file triangles.out):  
As the sum of areas is not necessarily be an integer and may be very large, output the remainder when two times the sum of areas is taken modulo 109+7.  
SAMPLE INPUT:  
```
4
0 0
0 1
1 0
1 2
```
SAMPLE OUTPUT:
```
3
```
Fence posts (0,0), (1,0), and (1,2) give a triangle of area 1, while (0,0), (1,0), and (0,1) give a triangle of area 0.5. Thus, the answer is 2⋅(1+0.5)=3.

Problem credits: Travis Hance and Nick Wu

{% highlight C++ linenos %}

struct P{
    int x;
    int y;
};

map<int, int> xMap;
map<int, int> yMap;

vector<P> XPoints;
vector<P> YPoints;


int YSumForX(int x,  int i) {
    if (xMap.count(XPoints[i].y) > 0) {
        return xMap[x];
    }

    ll sumY = 0;
    auto bounds2 = equal_range(YPoints.begin(), YPoints.end(), XPoints[i], [] (P a, P b) {return a.y < b.y;});
    for (auto k = bounds2.f; k < bounds2.s; k++) {
        sumY += abs(( * k).x - x);
    }

    xMap[XPoints[i].y] = sumY + x;

    return sumY;
}

int XSumForY(int y, int i) {
    if (yMap.count(y) > 0) {
        return yMap[y];
    }

    ll sumX = 0;
    auto bounds = equal_range(XPoints.begin(), XPoints.end(), XPoints[i], [] (P a, P b) {return a.x < b.x;});
    for (auto j = bounds.f; j < bounds.s; j++) {
        sumX += abs((* j).y - y);
    }

    //yMap[y] = sumX;

    return sumX;
}

int main() {
    setIO("triangles");

    ll sum = 0;

    int N;
    cin >> N;
    XPoints.resize(N);

    F0R(i, N) cin >> XPoints[i].x >> XPoints[i].y;

    sort(XPoints.begin(), XPoints.end(), [] (P a, P b) {return a.x < b.x;});

    YPoints.assign(XPoints.begin(), XPoints.end());
    sort(YPoints.begin(), YPoints.end(), [] (P a, P b) {return a.y < b.y;});

    F0R(i, N) {

        ll sumY = YSumForX(XPoints[i].x,  i);
        ll sumX = XSumForY(XPoints[i].y,  i);


        sum += sumX * sumY;
    }

    cout << sum % MOD;

}

{% endhighlight %}


## Problem 3. Clock Tree

[Clock Tree](http://www.usaco.org/index.php?page=viewproblem2&cpid=1016)

Farmer John's new barn has a truly strange design: it consists of N rooms (2≤N≤2500), conveniently numbered 1…N, and N−1 corridors. Each corridor connects a pair of rooms, in such a way that it is possible to walk from any room to any other room along a series of corridors.  
Every room in the barn has a circular clock on the wall with the standard integers 1…12 around its face. However, these clocks only have one hand, which always points directly at one of the integers on the clock face (it never points between two of these integers).  

Bessie the cow wants to synchronize all the clocks in the barn so they all point to the integer 12. However, she is somewhat simple-minded, and as she walks around the barn, every time she enters a room, she moves the hand on its clock ahead by one position. For example, if the clock pointed at 5, it would now point at 6, and if the clock pointed at 12, it would now point at 1. If Bessie enters the same room multiple times, she advances the clock in that room every time she enters.  

Please determine the number of rooms in which Bessie could start walking around the barn such that she could conceivably set all the clocks to point to 12. Note that Bessie does not initially advance the clock in her starting room, but she would advance the clock in that room any time she re-entered it. Clocks do not advance on their own; a clock only advances if Bessie enters its room. Furthermore, once Bessie enters a corridor she must exit through the other end (it is not allowed to walk partially through the corridor and loop back around to the same room).  

SCORING:  
Test cases 2-7 satisfy N≤100.  
Test cases 8-15 satisfy no additional constraints.  
INPUT FORMAT (file clocktree.in):  
The first line of input contains N. The next line contains N integers, each in the range 1…12, specifying the initial clock setting in each room. The next N−1 lines each describe a corridor in terms of two integers a and b, each in the range 1…N, giving the room numbers connected by the corridor.  
OUTPUT FORMAT (file clocktree.out):  
Print the number of rooms in which Bessie could start, such that it is possible for her to set all clocks to point to 12.
SAMPLE INPUT:  
```
4
11 10 11 11
1 2
2 3
2 4
```
SAMPLE OUTPUT:
```
1
```
In this example, Bessie can set all the clocks to point to 12 if and only if she starts in room 2 (for example, by moving to room 1, 2, 3, 2, and finally 4).

Problem credits: Brian Dean

{% highlight C++ linenos %}

ll N;
const int MaX = 2501;
vector<int> ogClock(MaX);
vector<int> clockVal(MaX);
vector<int> adj[MaX];

inline int mod(int val) {
    return (val - 1) % 12 + 1;
}

int dfs(int node, int parent) {

    for (int child : adj[node]) {
        if (child != parent) {
            clockVal[child] = mod(clockVal[child] + 1);
            clockVal[node] += 12 - dfs(child, node);
            clockVal[node] = mod(clockVal[node]);
        }
    }

    if (parent >= 0) clockVal[parent] = mod(clockVal[parent] + 1);

    return (clockVal[node]);
}

int main() {
    setIO("clocktree");

    cin >> N;

    F0R(i, N) {
        cin >> ogClock[i + 1];
    }

    F0R(i, N - 1) {
        int A, B;
        cin >> A >> B;

        adj[A].pb(B);
        adj[B].pb(A);
    }

    vector<int> myL;
    int ans = 0;
    FOR(i, 1, N + 1) {
        clockVal = ogClock;
        int ret = dfs(i, -1);

        if (mod(ret) == 12 || mod(ret) == 1) {
            ans++;
            myL.push_back(i);
        }
    }



    cout << ans;
}
{% endhighlight %}
