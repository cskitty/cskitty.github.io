---
title: "USACO 2020 Open Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Binary Search
---

# USACO 2020 Open Silver

## Problem 1. Social Distancing

[Social Distancing](http://usaco.org/index.php?page=viewproblem2&cpid=1038)  

Farmer John is worried for the health of his cows after an outbreak of the highly contagious bovine disease COWVID-19.  
In order to limit transmission of the disease, Farmer John's N cows (2≤N≤105) have decided to practice "social distancing" and spread themselves out across the farm. The farm is shaped like a 1D number line, with M mutually-disjoint intervals (1≤M≤105) in which there is grass for grazing. The cows want to locate themselves at distinct integer points, each covered in grass, so as to maximize the value of D, where D represents the distance between the closest pair of cows. Please help the cows determine the largest possible value of D.

INPUT FORMAT (file socdist.in):  
The first line of input contains N and M. The next M lines each describe an interval in terms of two integers a and b, where 0≤a≤b≤1018. No two intervals overlap or touch at their endpoints. A cow standing on the endpoint of an interval counts as standing on grass.  
OUTPUT FORMAT (file socdist.out):  
Print the largest possible value of D such that all pairs of cows are D units apart. A solution with D>0 is guaranteed to exist.  
SAMPLE INPUT:  
```
5 3
0 2
4 7
9 9
```
SAMPLE OUTPUT:
```
2
```
One way to achieve D=2 is to have cows at positions 0, 2, 4, 6 and 9.  

SCORING:   
Test cases 2-3 satisfy b≤105.  
Test cases 4-10 satisfy no additional constraints.  
Problem credits: Brian Dean  

{% highlight C++ linenos %}  
int N;
ll M;

bool check(vector<pair<ll, ll>> v, ll target) {
    // target = max distancing

    ll pos = v[0].f;
    ll i = 0;
    if (target == 3) {
        // cout << ('x');
    }
    dbg(target);
    ll amt = 0;
    while (amt < N) {
        if (v[i].f >= pos) {
            pos = v[i].f;
        }
        if (v[i].f <= (pos) && v[i].s >= (pos)) {
            amt++;
            pos += target;
        }
        else {
            i++;

        }

        if (i >= v.size()) {
            return false;
        }
    }

    dbg(target, "true");
    return true;
}

ll binary_search(vector<pair<ll, ll>> x) {

    dbg(x);

    //ll max = x.end() - x.begin();
    ll max = x[x.size() - 1].s - x[0].f;
    ll p = 0;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p + a) >= 0 && check(x, p + a)) p += a;
    }
    return p;
}

int main() {

    setIO("socdist");

    cin >> N >> M;

    vector<pair<ll, ll>> nums(M);

    F0R(i, M)
    cin >> nums[i].f >> nums[i].s;

    sort(all(nums));

    cout << binary_search(nums);

}
{% endhighlight %}

## Problem 2. Cereal

[Cereal](http://www.usaco.org/index.php?page=viewproblem2&cpid=1039)  

Farmer John's cows like nothing more than cereal for breakfast! In fact, the cows have such large appetites that they will each eat an entire box of cereal for a single meal.
The farm has recently received a shipment with M different types of cereal (1≤M≤105) .   Unfortunately, there is only one box of each cereal! Each of the N cows (1≤N≤105) has a favorite cereal and a second favorite cereal. When given a selection of cereals to choose from, a cow performs the following process:  

If the box of her favorite cereal is still available, take it and leave.  
Otherwise, if the box of her second-favorite cereal is still available, take it and leave.
Otherwise, she will moo with disappointment and leave without taking any cereal.
The cows have lined up to get cereal. For each 0≤i≤N−1, determine how many cows would take a box of cereal if Farmer John removed the first i cows from the line.  

INPUT FORMAT (file cereal.in):  
The first line contains two space-separated integers N and M.  
For each 1≤i≤N, the i-th line contains two space-separted integers fi and si (1≤fi,si≤M and fi≠si) denoting the favorite and second-favorite cereals of the i-th cow in line.  

OUTPUT FORMAT (file cereal.out):  
For each 0≤i≤N−1, print a line containing the answer for i.  
SAMPLE INPUT:
```
4 2
1 2
1 2
1 2
1 2
```
SAMPLE OUTPUT:
```
2
2
2
1
```
If at least two cows remain, then exactly two of them get a box of cereal.

SCORING:
Test cases 2-3 satisfy N,M≤1000.
Test cases 4-10 satisfy no additional constraints.
Problem credits: Dhruv Rohatgi

{% highlight C++ linenos %}  
const int MaX = 100001;
int N, M;
vector<int> occ(MaX, 0);
int ans = 0;
vector<pair<int, int>> cows(MaX);

int main() {
    setIO("cereal");
    cin >> N >> M;


    F0R(i, N) {
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

    F0R(i, N) {
        cout << ansVec[i] << endl;
    }
}
{% endhighlight %}


## Problem 3. The Moo Particle

[The Moo Particle](http://www.usaco.org/index.php?page=viewproblem2&cpid=1040)

Quarantined for their protection during an outbreak of COWVID-19, Farmer John's cows have come up with a new way to alleviate their boredom: studying advanced physics! In fact, the cows have even managed to discover a new subatomic particle, which they have named the "moo particle".
The cows are currently running an experiment involving N moo particles (1≤N≤105). Particle i has a "spin" described by two integers xi and yi in the range −109…109 inclusive. Sometimes two moo particles interact. This can happen to particles with spins (xi,yi) and (xj,yj) only if xi≤xj and yi≤yj. Under these conditions, it's possible that exactly one of these two particles may disappear (and nothing happens to the other particle). At any given time, at most one interaction will occur.  

The cows want to know the minimum number of moo particles that may be left after some arbitrary sequence of interactions.  

INPUT FORMAT (file moop.in):  
The first line contains a single integer N, the initial number of moo particles. Each of the next N lines contains two space-separated integers, indicating the spin of one particle. Each particle has a distinct spin.  
OUTPUT FORMAT (file moop.out):  
A single integer, the smallest number of moo particles that may remain after some arbitrary sequence of interactions.  
SAMPLE INPUT:
```
4
1 0
0 1
-1 0
0 -1
```
SAMPLE OUTPUT:
```
1
```
One possible sequence of interactions:

Particles 1 and 4 interact, particle 1 disappears.  
Particles 2 and 4 interact, particle 4 disappears.  
Particles 2 and 3 interact, particle 3 disappears.  
Only particle 2 remains.  

SAMPLE INPUT:
```
3
0 0
1 1
-1 3
```
SAMPLE OUTPUT:
```
2
```
Particle 3 cannot interact with either of the other two particles, so it must remain. At least one of particles 1 and 2 must also remain.  

SCORING:  
Test cases 3-6 satisfy N≤1000.  
Test cases 7-12 satisfy no additional constraints.  
Problem credits: Dhruv Rohatgi  

{% highlight C++ linenos %}
int main() {
    setIO("moop");
    cin >> N;

    vector<pi> particles(N);
    vector<int> maxY(N);
    vector<int> minY(N);

    F0R(i, N) {
        cin >> particles[i].f >> particles[i].s;
    }

    sort(all(particles), [](pi a, pi b) {if (a.f == b.f) {return a.s < b.s;} return a.f < b.f;});

    minY[0] = particles[0].s;
    maxY[N - 1] = particles[N - 1].s;
    F0R(i, N) {
        if (i >= 1) {
            minY[i] = min(minY[i - 1], particles[i - 1].s);
        }
        if (N - i - 1 != N - 1) {
            maxY[N - i - 1] = max(particles[N - i - 1].s, maxY[N - i]);
        }
    }

    int ans = N;

    FOR(i, 1, N) {
        if (minY[i] <= maxY[i]) {
            ans--;
        }
    }
    cout << ans;
}

{% endhighlight %}
