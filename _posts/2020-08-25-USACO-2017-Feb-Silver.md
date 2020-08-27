---
title: "USACO 2017 Feb Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2017 Feb Silver

## Problem 1. Why Did the Cow Cross the Road

[Why Did the Cow Cross the Road](http://www.usaco.org/index.php?page=viewproblem2&cpid=714)

Farmer John's cows are trying to learn to cross the road effectively. Remembering the old "why did the chicken cross the road?" joke, they figure the chickens must be experts on crossing the road, and go off in search of chickens to help them.  
As it turns out, chickens are very busy creatures and have limited time to help the cows. There are C chickens on the farm (1≤C≤20,000), conveniently numbered 1…C, and each chicken i is only willing to help a cow at precisely time Ti. The cows, never in a hurry, have more flexibility in their schedules. There are N cows on the farm (1≤N≤20,000), conveniently numbered 1…N, where cow j is able to cross the road between time Aj and time Bj. Figuring the "buddy system" is the best way to proceed, each cow j would ideally like to find a chicken i to help her cross the road; in order for their schedules to be compatible, i and j must satisfy Aj≤Ti≤Bj.  

If each cow can be paired with at most one chicken and each chicken with at most one cow, please help compute the maximum number of cow-chicken pairs that can be constructed.  

INPUT FORMAT (file helpcross.in):  
The first line of input contains C and N. The next C lines contain T1…TC, and the next N lines contain Aj and Bj (Aj≤Bj) for j=1…N. The A's, B's, and T's are all non-negative integers (not necessarily distinct) of size at most 1,000,000,000.  
OUTPUT FORMAT (file helpcross.out):  
Please compute the maximum possible number of cow-chicken pairs.

SAMPLE INPUT:
```
5 4
7
8
6
2
9
2 5
4 9
0 3
8 13
```

SAMPLE OUTPUT:
```
3
```
Problem credits: Brian Dean  

{% highlight c++ linenos %}

int C, N;

int main() {
    setIO("helpcross");
    cin >> C >> N;

    vector<int> chickens(C);
    vector<pair<int, int>> cows(N);

    F0R(i, C) cin >> chickens[i];
    F0R(i, N) cin >> cows[i].f >> cows[i].s;

    int ans = 0;
    sort(all(chickens));
    sort(all(cows), [](pair<int, int> a, pair<int, int> b) {if (a.s == b.s) {return a.f < b.f;} else {return a.s < b.s;}});

    F0R(i, N) {
        auto a = lower_bound(all(chickens), cows[i].s);
        if (a != chickens.end() && cows[i].f <= * a) {
            ans++;
            chickens.erase(a);
        }
    }

    /* vector<bool> usedCows(N, false);
     F0R(i, C) {
       F0R(j, N) {
             if (! usedCows[j] && cows[j].f <= chickens[i] && cows[j].s >= chickens[i]) {
                 usedCows[j] = true;
                 ans++;
                 break;
             }
         }
     }

    int pD = 0, pB = 0;
    int ans = 0;
    while (pD < C && pB < N) {
        if (cows[pB].f <= chickens[pD] && cows[pB].s >= chickens[pD]) {
            dbg(pB, pD, cows[pB].f, cows[pB].s, chickens[pD]);
            // yes
            ans++;
            pB++;
            pD++;
        }
        else if (cows[pB].f > chickens[pD]) {
            pD++;
        }
        else {
            pB++;
        }
    } * /

    cout << ans;
}

{% endhighlight %}

## Problem 2. Why Did the Cow Cross the Road II

[Why Did the Cow Cross the Road II](http://www.usaco.org/index.php?page=viewproblem2&cpid=715)

The long road through Farmer John's farm has N crosswalks across it, conveniently numbered 1…N (1≤N≤100,000). To allow cows to cross at these crosswalks, FJ installs electric crossing signals, which light up with a green cow icon when it is ok for the cow to cross, and red otherwise. Unfortunately, a large electrical storm has damaged some of his signals. Given a list of the damaged signals, please compute the minimum number of signals that FJ needs to repair in order for there to exist some contiguous block of at least K working signals.

INPUT FORMAT (file maxcross.in):  
The first line of input contains N, K, and B (1≤B,K≤N). The next B lines each describe the ID number of a broken signal.  

OUTPUT FORMAT (file maxcross.out):  

Please compute the minimum number of signals that need to be repaired in order for there to be a contiguous block of K working signals somewhere along the road.
SAMPLE INPUT:
```
10 6 5
2
10
1
5
9
```
SAMPLE OUTPUT:
```
1
```
Problem credits: Brian Dean
{% highlight c++ linenos %}

int N, K, B;

int main() {
    setIO("maxcross");

    cin >> N >> K >> B;

    vector<int> prefixLights(N + 1, 0);
    vector<int> signals(N, 0);

    F0R(i, B) {
        int I;
        cin >> I;
        signals[I - 1]++;
    }

    FOR(i, 1, N + 1) {
        prefixLights[i] = prefixLights[i - 1] + signals[i - 1];
    }

    int ans = B;
    F0R(i, N - K + 1) {
        dbg(i, i + K + 1, prefixLights[i + K], prefixLights[i]);
        ans = min(ans, prefixLights[i + K] - prefixLights[i]);
    }

    cout << ans;
}

{% endhighlight %}


## Problem 3. Why Did the Cow Cross the Road III

[Cow Dance Show](http://www.usaco.org/index.php?page=viewproblem2&cpid=716)

Why did the cow cross the road? Well, one reason is that Farmer John's farm simply has a lot of roads, making it impossible for his cows to travel around without crossing many of them.  
FJ's farm is arranged as an N×N square grid of fields (2≤N≤100), Certain pairs of adjacent fields (e.g., north-south or east-west) are separated by roads, and a tall fence runs around the external perimeter of the entire grid, preventing cows from leaving the farm. Cows can move freely from any field to any other adjacent field (north, east, south, or west), although they prefer not to cross roads unless absolutely necessary.  

There are K cows (1≤K≤100,K≤N2) on FJ's farm, each located in a different field. A pair of cows is said to be "distant" if, in order for one cow to visit the other, it is necessary to cross at least one road. Please help FJ count the number of distant pairs of cows.  

INPUT FORMAT (file countcross.in):  
The first line of input contains N, K, and R. The next R lines describe R roads that exist between pairs of adjacent fields. Each line is of the form r c r′ c′ (integers in the range 1…N), indicating a road between the field in (row r, column c) and the adjacent field in (row r′, column c′). The final K lines indicate the locations of the K cows, each specified in terms of a row and column.  
OUTPUT FORMAT (file countcross.out):  
Print the number of pairs of cows that are distant.  
SAMPLE INPUT:  
```
3 3 3
2 2 2 3
3 3 3 2
3 3 2 3
3 3
2 2
2 3
```
SAMPLE OUTPUT:
```
2
```
Problem credits: Brian Dean  

{% highlight c++ linenos %}

const int MaX = 101;
int grid[MaX][MaX];
int N, K, R;
bool visited[MaX][MaX];
set<pair<pair<int, int>, pair<int, int>>> roads;

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

bool valid(int oldX, int oldY, int newX, int newY) {
    return roads.find(make_pair(make_pair(oldX, oldY), make_pair(newX, newY))) == roads.end();
}

void floodfill(int r, int c, int color) {
    // GRID IS ONE BASED !!!
    if (r < 1 || r > N|| c < 1 || c > N || visited[r][c]) {
        return;
    }

    visited[r][c] = true;
    grid[r][c] = color;

    F0R(i, 4) {
        int newX = r + dx[i];
        int newY = c + dy[i];
        if (valid(r, c, newX, newY)) {
            floodfill(newX, newY, color);
        }
    }
}

int main() {
    setIO("countcross");

    cin >> N >> K >> R;

    F0R(i, R) {
        int X1, Y1, X2, Y2;
        cin >> X1 >> Y1 >> X2 >> Y2;

        roads.insert(make_pair(make_pair(X1,Y1), make_pair(X2, Y2)));
        roads.insert(make_pair(make_pair(X2,Y2), make_pair(X1, Y1)));
    }

    vector<pair<int, int>> cows(K);

    F0R(i, K) {
        cin >> cows[i].f >> cows[i].s;
    }

    int colors = 0;
    F0R(i, K) {
        if (! visited[cows[i].f][cows[i].s]) {
            colors++;
            floodfill(cows[i].f, cows[i].s, colors);
        }
    }

    int ans = 0;
    F0R(i, K) {
        F0R(j, i) {
            if (grid[cows[i].f][cows[i].s] != grid[cows[j].f][cows[j].s]) {
                ans++;
            }
        }
    }

    cout << ans;
}


{% endhighlight %}
