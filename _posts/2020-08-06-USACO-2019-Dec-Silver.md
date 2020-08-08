---
title: "USACO 2019 Dec Silver"
categories:
  - USACO
tags:
  - Algorithms
  - C++
  - USACO
---

# USACO 2019 Dec Silver

## Problem 1. MooBuzz

[MooBuzz](http://usaco.org/index.php?page=viewproblem2&cpid=966)

Farmer John's cows have recently become fans of playing a simple number game called "FizzBuzz". The rules of the game are simple: standing in a circle, the cows sequentially count upward from one, each cow saying a single number when it is her turn. If a cow ever reaches a multiple of 3, however, she should say "Fizz" instead of that number. If a cow reaches a multiple of 5, she should say "Buzz" instead of that number. If a cow reaches a multiple of 15, she should say "FizzBuzz" instead of that number. A transcript of the first part of a game is therefore:  
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16  

Having a slightly more limited vocabulary, the version of FizzBuzz played by the cows involves saying "Moo" instead of Fizz, Buzz, and FizzBuzz. The beginning of the cow version of the game is therefore  

1, 2, Moo, 4, Moo, Moo, 7, 8, Moo, Moo, 11, Moo, 13, 14, Moo, 16  

Given N (1≤N≤109), please determine the Nth number spoken in this game.  

SCORING  
Test cases 2-5 satisfy N≤106.  

INPUT FORMAT (file moobuzz.in):  
The input consists of a single integer, N.  

OUTPUT FORMAT (file moobuzz.out):  
Please print out the Nth number spoken during the game.  
SAMPLE INPUT:  
```
4
```
SAMPLE OUTPUT:  
```
7
```
The 4th number spoken is 7. The first 4 numbers spoken are 1, 2, 4, 7, since we skip over any time a cow says "Moo".  

Problem credits: Brian Dean  

{% highlight c++ linenos %}
int main() {
    ifstream cin ("moobuzz.in");
    ofstream cout ("moobuzz.out");

    int N;

    cin >> N;

    int a = 0;
    while (a != N) {
        int five = N / 5 - (a / 5);
        int three = N / 3 - (a / 3);
        int fifteen = N / 15 - (a / 15);

        a = N;
        N = (N + (five) + (three)) - (fifteen);
    }
    cout << N;
}

{% endhighlight %}


## Problem 2. Meetings

Two barns are located at positions 0 and L (1≤L≤109) on a one-dimensional number line. There are also N cows (1≤N≤5⋅104) at distinct locations on this number line (think of the barns and cows effectively as points). Each cow i is initially located at some position xi and moving in a positive or negative direction at a speed of one unit per second, represented by an integer di that is either 1 or −1. Each cow also has a weight wi in the range [1,103]. All cows always move at a constant velocity until one of the following events occur:  
If cow i reaches a barn, then cow i stops moving.  
A meeting occurs when two cows i and j occupy the same point, where that point is not a barn. In this case, cow i is assigned cow j's previous velocity and vice versa. Note that cows could potentially meet at points that are not integers.  
Let T be the earliest point in time when the sum of the weights of the cows that have stopped moving (due to reaching one of the barns) is at least half of the sum of the weights of all cows. Please determine the total number of meetings between pairs of cows during the range of time 0…T (including at time T).    

SCORING:  
Test cases 2-4 satisfy N≤102 and wi=1 for all i.  
Test cases 5-7 satisfy N≤102.  
INPUT FORMAT (file meetings.in):  
The first line contains two space-separated integers N and L.   
The next N lines each contain three space-separated integers wi, xi, and di. All locations xi are distinct and satisfy 0<xi<L.  

OUTPUT FORMAT (file meetings.out):  
Print a single line containing the answer.  
SAMPLE INPUT:  
```
3 5
1 1 1
2 2 -1
3 3 -1
```
SAMPLE OUTPUT:   
```
2
```
The cows in this example move as follows:  

The first and second cows meet at position 1.5 at time 0.5. The first cow now has velocity −1 and the second has velocity 1.
The second and third cows meet at position 2 at time 1. The second cow now has velocity −1 and the third has velocity 1.
The first cow reaches the left barn at time 2.
The second cow reaches the left barn at time 3.
The process now terminates since the sum of the weights of the cows that have reached a barn is at least half of the sum of the weights of all cows. The third cow would have reached the right barn at time 4.
Exactly two meetings occurred.

Problem credits: Benjamin Qi  

{% highlight c++ linenos %}
#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define f first
#define s second

void setIO(string name) {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen((name+".in").c_str(),"r",stdin);
    freopen((name+".out").c_str(),"w",stdout);
}


struct ant {
    int w;
    int x;
    int d;
};

int N,L;
vector<ant> ants;

int getTime () {
    vector<int> left, right;
    F0R(i,N) {
        if (ants[i].d == -1)
            left.push_back(ants[i].x);
        else
            right.push_back(L - ants[i].x);
    }

    vector<pair<int, int>> v;
    F0R(i,left.size())
        v.push_back({left[i], ants[i].w});

    //since the cow never cross each other
    //we need to reverse the right side cows, use right most weight also
    reverse(right.begin(), right.end());
    F0R(i,right.size())
        v.push_back({right[i], ants[ N - 1 - i ].w});

    sort(v.begin(), v.end());

    int total = 0;
    for(auto t: v) total += t.s;

    int curr = 0;
    for(auto t: v) {
        curr += t.s;
        if (curr * 2 >= total) {
            return t.f;
        }
    }

    return 0;
}

int main() {
    setIO("meetings");
    cin >> N >> L;
    ants.resize(N);
    F0R(i,N) {
        cin >> ants[i].w >> ants[i].x >> ants[i].d;
    }

    sort(ants.begin(), ants.end(), [](ant a, ant b) {return a.x < b.x;});

    int Time = getTime();
    int collisions = 0;

    vector<int> leftAnts;
    vector<int> rightAnts;

    F0R(i, N) {
        if (ants[i].d == -1) {
            leftAnts.push_back(ants[i].x);
        }
        else {
            rightAnts.push_back(ants[i].x);
        }
    }

    F0R(i, leftAnts.size()) {
        int end = lower_bound(rightAnts.begin(), rightAnts.end(), leftAnts[i]) - rightAnts.begin();
        int start = lower_bound(rightAnts.begin(), rightAnts.end(), leftAnts[i] - 2 * Time) - rightAnts.begin();

        collisions += end - start;
/*        if (ants[i].d == -1) {
            F0R(j, ants.size()) {
                if (ants[j].d == 1) {
                    if ((ants[j].x <= ants[i].x) && ((ants[j].x + Time) >= (ants[i].x - Time))) {
                        collisions ++;
                    }
                }
            }
        }*/
    }
    cout << collisions;
 }
{% endhighlight %}



## Problem 3. Milk Visits

[Milk Visits](http://usaco.org/index.php?page=viewproblem2&cpid=968)

Farmer John is planning to build N (1≤N≤105) farms that will be connected by N−1 roads, forming a tree (i.e., all farms are reachable from each-other, and there are no cycles). Each farm contains a cow, whose breed is either Guernsey or Holstein.  
Farmer John's M friends (1≤M≤105) often come to visit him. During a visit with friend i, Farmer John will walk with his friend along the unique path of roads from farm Ai to farm Bi (it may be the case that Ai=Bi). Additionally, they can try some milk from any cow along the path they walk. Since most of Farmer John's friends are also farmers, they have very strong preferences regarding milk. Some of his friends will only drink Guernsey milk, while the remainder will only drink Holstein milk. Any of Farmer John's friends will only be happy if they can drink their preferred type of milk during their visit.  

Please determine whether each friend will be happy after visiting.  

SCORING:
Test cases 2-5 satisfy N≤103,M≤2⋅103.
INPUT FORMAT (file milkvisits.in):
The first line contains the two integers N and M.
The second line contains a string of length N. The ith character of the string is 'G' if the cow in the ith farm is a Guernsey, or 'H' if the cow in the ith farm is a Holstein.

The next N−1 lines each contain two distinct integers X and Y (1≤X,Y≤N), indicating that there is a road between farms X and Y.  

The next M lines contain integers Ai, Bi, and a character Ci. Ai and Bi represent the endpoints of the path walked during friend i's visit, while Ci is either G or H if the ith friend prefers Guernsey milk or Holstein milk.  

OUTPUT FORMAT (file milkvisits.out):  
Print a binary string of length M. The ith character of the string should be '1' if the ith friend will be happy, or '0' otherwise.  

SAMPLE INPUT:
```
5 5
HHGHG
1 2
2 3
2 4
1 5
1 4 H
1 4 G
1 3 G
1 3 H
5 5 H
```
SAMPLE OUTPUT:
```
10110
```
Here, the path from farm 1 and farm 4 involves farms 1, 2, and 4. All of these contain Holsteins, so the first friend will be satisfied while the second one will not.

Problem credits: Spencer Compton  


{% highlight c++ linenos %}

{% endhighlight %}
