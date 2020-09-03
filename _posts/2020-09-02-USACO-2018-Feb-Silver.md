---
title: "USACO 2018 Feb Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2018 Feb Silver

## Problem 1. Rest Stops

[Lifeguards](http://www.usaco.org/index.php?page=viewproblem2&cpid=810)

Farmer John and his personal trainer Bessie are hiking up Mount Vancowver. For their purposes (and yours), the mountain can be represented as a long straight trail of length L meters (1≤L≤106). Farmer John will hike the trail at a constant travel rate of rF seconds per meter (1≤rF≤106). Since he is working on his stamina, he will not take any rest stops along the way.  
Bessie, however, is allowed to take rest stops, where she might find some tasty grass. Of course, she cannot stop just anywhere! There are N rest stops along the trail (1≤N≤105); the i-th stop is xi meters from the start of the trail (0<xi<L) and has a tastiness value ci (1≤ci≤106). If Bessie rests at stop i for t seconds, she receives ci⋅t tastiness units.  

When not at a rest stop, Bessie will be hiking at a fixed travel rate of rB seconds per meter (1≤rB≤106). Since Bessie is young and fit, rB is strictly less than rF.  

Bessie would like to maximize her consumption of tasty grass. But she is worried about Farmer John; she thinks that if at any point along the hike she is behind Farmer John on the trail, he might lose all motivation to continue!  

Help Bessie find the maximum total tastiness units she can obtain while making sure that Farmer John completes the hike.  

INPUT FORMAT (file reststops.in):  
The first line of input contains four integers: L, N, rF, and rB. The next N lines describe the rest stops. For each i between 1 and N, the i+1-st line contains two integers xi and ci, describing the position of the i-th rest stop and the tastiness of the grass there.  
It is guaranteed that rF>rB, and 0<x1<⋯<xN<L. Note that rF and rB are given in seconds per meter!  

OUTPUT FORMAT (file reststops.out):  
A single integer: the maximum total tastiness units Bessie can obtain.  
SAMPLE INPUT:  
```
10 2 4 3
7 2
8 1
```
SAMPLE OUTPUT:  
```
15
```
In this example, it is optimal for Bessie to stop for 7 seconds at the x=7 rest stop (acquiring 14 tastiness units) and then stop for an additional 1 second at the x=8 rest stop (acquiring 1 more tastiness unit, for a total of 15 tastiness units).  

Problem credits: Dhruv Rohatgi

{% highlight C++ linenos %}
ll L, N, rF, rB;


int main() {
    setIO("reststops");

    cin >> L >> N >> rF >> rB;

    vector<pair<ll, ll>> stops(N);
    F0R(i, N) {
        cin >> stops[i].f >> stops[i].s;
    }

    ll ans = 0;
    int currentPos = -1;

    while (currentPos < N - 1) {

        int maxV = currentPos + 1;
        FOR(i, currentPos + 1, N) {
            if (stops[i].s >= stops[maxV].s) {
                maxV = i;
            }
        }

        ans += ((stops[maxV].f - stops[currentPos].f)* (rF - rB)) * stops[maxV].s;

        currentPos = maxV;
    }

    cout << ans;
}
{% endhighlight %}

## Problem 2. Snow Boots

[Snow Boots](http://www.usaco.org/index.php?page=viewproblem2&cpid=811)

It's winter on the farm, and that means snow! There are N tiles on the path from the farmhouse to the barn, conveniently numbered 1…N, and tile i is covered in fi feet of snow.
Farmer John starts off on tile 1 and must reach tile N to wake up the cows. Tile 1 is sheltered by the farmhouse roof, and tile N is sheltered by the barn roof, so neither of these tiles has any snow. But to step on the other tiles, Farmer John needs to wear boots!

In his foul-weather backpack, Farmer John has B pairs of boots, numbered 1…B. Some pairs are more heavy-duty than others, and some pairs are more agile than others. In particular, pair i lets FJ step in snow at most si feet deep, and lets FJ move at most di forward in each step.

Unfortunately, the boots are packed in such a way that Farmer John can only access the topmost pair at any given time. So at any time, Farmer John can either put on the topmost pair of boots (discarding his old pair) or discard the topmost pair of boots (making a new pair of boots accessible).

Farmer John can only change boots while standing on a tile. If that tile has f feet of snow, both the boots he takes off AND the boots he puts on must be able to withstand at least f feet of snow. Intermediate pairs of boots which he discards without wearing do not need to satisfy this restriction.

Help Farmer John minimize waste, by determining the minimum number of pairs of boots he needs to discard in order to reach the barn. You may assume that Farmer John is initially not wearing any boots.

INPUT FORMAT (file snowboots.in):
The first line contains two space-separated integers N and B (2≤N,B≤250).
The second line contains N space-separated integers. The ith integer is fi, giving the depth of snow on tile i (0≤fi≤109). It's guaranteed that f1=fN=0.

The next B lines contain two space-separated integers each. The first integer on line i+2 is si, the maximum depth of snow in which pair i can step. The second integer on line i+2 is di, the maximum step size for pair i. It's guaranteed that 0≤si≤109 and 1≤di≤N−1.

The boots are described in top-to-bottom order, so pair 1 is the topmost pair in FJ's backpack, and so forth.

OUTPUT FORMAT (file snowboots.out):
The output should consist of a single integer, giving the minimum number of boots Farmer John needs to discard. It's guaranteed that it will be possible for FJ to make it to the barn.
SAMPLE INPUT:
```
10 4
0 2 8 3 6 7 5 1 4 0
2 3
4 2
3 4
7 1
```
SAMPLE OUTPUT:
```
2
```
Problem credits: Brian Dean and Dhruv Rohatgi

Problem credits: Jay Leeds  

{% highlight C++ linenos %}
const int MaX = 250 + 1;
ll N, M;
ll ans = 1e9+1;
vector<pair<ll, ll>> boots(MX);
vector<ll> steps(MX);
// vector<bool> visited(MX);

vector<vector<int>> memoization(MaX, vector<int>(MaX));

void find(ll tile, int boot, ll val) {
    memoization[tile][boot] = val;
    dbg(tile, boot, val);
    if (tile == N - 1) {
        ans = min(val, ans);
    }
    else {
        FOR(j, 1, min(boots[boot].s + 1, N - tile + 1)) {
            if (steps[tile + j] <= boots[boot].f && ((memoization[tile + j][boot] == 0))) {
                find(tile + j, boot, val);
            }
        }

        FOR(i, boot + 1, M) {
            if (steps[tile] <= boots[i].f && memoization[tile][i] == 0) {
                find(tile, i, val + 1);
            }
            else {
                val++;
            }
        }
    }
}


int main() {
    setIO("snowboots");

    cin >> N >> M;


    F0R(i, N) cin >> steps[i];

    F0R(i, M) {
        cin >> boots[i].f >> boots[i].s;
    }


    find(0L, 0, 0L);
    cout << ans;
}
{% endhighlight %}


## Problem 3. Teleportation

[Teleportation](http://usaco.org/index.php?page=viewproblem2&cpid=812)

One of the farming chores Farmer John dislikes the most is hauling around lots of cow manure. In order to streamline this process, he comes up with a brilliant invention: the manure teleporter! Instead of hauling manure between two points in a cart behind his tractor, he can use the manure teleporter to instantly transport manure from one location to another.  
Farmer John's farm is built along a single long straight road, so any location on his farm can be described simply using its position along this road (effectively a point on the number line). A teleporter is described by two numbers x and y, where manure brought to location x can be instantly transported to location y.  
Farmer John decides to build a teleporter with the first endpoint located at x=0; your task is to help him determine the best choice for the other endpoint y. In particular, there are N piles of manure on his farm (1≤N≤100,000). The ith pile needs to moved from position ai to position bi, and Farmer John transports each pile separately from the others. If we let di denote the amount of distance FJ drives with manure in his tractor hauling the ith pile, then it is possible that di=|ai−bi| if he hauls the ith pile directly with the tractor, or that di could potentially be less if he uses the teleporter (e.g., by hauling with his tractor from ai to x, then from y to bi).  

Please help FJ determine the minimum possible sum of the di's he can achieve by building the other endpoint y of the teleporter in a carefully-chosen optimal position. The same position y is used during transport of every pile.  

INPUT FORMAT (file teleport.in):  
The first line of input contains N. In the N lines that follow, the ith line contains ai and bi, each an integer in the range −108…108. These values are not necessarily all distinct.  
OUTPUT FORMAT (file teleport.out):  
Print a single number giving the minimum sum of di's FJ can achieve. Note that this number might be too large to fit into a standard 32-bit integer, so you may need to use large integer data types like a "long long" in C/C++. Also you may want to consider whether the answer is necessarily an integer or not...  
SAMPLE INPUT:  
```
3
-5 -7
-3 10
-2 7
```
SAMPLE OUTPUT:
```
10
```
In this example, by setting y=8 FJ can achieve d1=2, d2=5, and d3=3. Note that any value of y in the range [7,10] would also yield an optimal solution.

Problem credits: Brian Dean

{% highlight C++ linenos %}


{% endhighlight %}
