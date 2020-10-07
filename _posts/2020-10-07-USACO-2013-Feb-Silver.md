---
title: "USACO 2013 Feb Silver"
categories:
  - USACO
tags:
  - Algorithms
  - C++
  - USACO
---

# USACO 2013 Feb Silver                  

## Problem 2. Tractor
[Clumsy Cows](http://www.usaco.org/index.php?page=viewproblem2&cpid=245)  

Problem 2: Tractor [Kalki Seksaria and Brian Dean, 2013]

One of Farmer John's fields is particularly hilly, and he wants to purchase
a new tractor to drive around on it.  The field is described by an N x N
grid of non-negative integer elevations (1 <= N <= 500).  A tractor capable
of moving from one grid cell to an adjacent cell (one step north, east,
south, or west) of height difference D costs exactly D units of money.  

FJ would like to pay enough for his tractor so that, starting from some
grid cell in his field, he can successfully drive the tractor around to
visit at least half the grid cells in the field (if the number of total
cells in the field is odd, he wants to visit at least half the cells
rounded up).  Please help him compute the minimum cost necessary for buying
a tractor capable of this task.  

PROBLEM NAME: tractor  

INPUT FORMAT:

* Line 1: The value of N.  

* Lines 2..1+N: Each line contains N space-separated non-negative
        integers (each at most 1 million) specifying a row of FJ's
        field.  

SAMPLE INPUT (file tractor.in):  
```
5
0 0 0 3 3
0 0 0 0 3
0 9 9 3 3
9 9 9 3 3
9 9 9 9 3
```
INPUT DETAILS:

FJ's farm is a 5 x 5 grid.  The elevations in the first row are 0, 0, 0, 3,
and 3, and so on.  

OUTPUT FORMAT:

* Line 1: The minimum cost of a tractor that is capable of driving
        around at least half of FJ's field.  

SAMPLE OUTPUT (file tractor.out):  
```
3
```
OUTPUT DETAILS:

A tractor of cost 3 is capable of moving between elevation 0 and elevation
3, so it can visit the block of cells at zero elevation as well as the
block of cells at elevation 3.  Together, these represent at least half of
FJ's farm.  



{% highlight C++ linenos %}
int N, M;
const int MaX = 501;
int g[MaX][MaX];
int halfV;
int xv[] = {0, 0, -1, 1};
int yv[] = {-1, 1, 0, 0};
vector<pi> starting;
int currSize = 0;

bool visited[MaX][MaX];

void ff(int r, int c, int diff) {
    if (currSize >= halfV) {
        return;
    }

    visited[r][c] = 1;
    currSize++;
    F0R(i, 4) {
        int nX = r + xv[i], nY = c + yv[i];
        if (nX >= N || nX < 0 || nY >= N || nY < 0 || visited[nX][nY]) {
            continue;
        }
        if (abs(g[r][c] - g[nX][nY]) <= diff) {
            ff(nX, nY, diff);
        }

        if (currSize >= halfV) {
            return;
        }
    }
}


bool check(int diff) {

    memset(visited, 0, MaX * MaX * sizeof(bool));
    for (pi startV : starting) {
        // VERY IMPORTANT LINE
        int x = startV.f, y = startV.s;
        if (! visited[x][y]) {
            currSize = 0;
            ff(x, y, diff);
            if (currSize >= halfV) {
                return true;
            }
        }
    }
    return false;
}


int binary_search() {
    int l = 0;
    int r = 1e7;

    while (l != r) {
        int mid = (l + r)/2;
        bool checkResult = check(mid);
        if (checkResult) {
            r = mid;
        }
        else {
            l = mid + 1;
        }
    }
    return l;
}

int main() {
    setIO("tractor");

    cin >> N;

    F0R(i, N) {
        F0R(j, N) {
            cin >> g[i][j];
            if (j > 0 && g[i][j] == g[i][j - 1] || i > 0 && g[i - 1][j] != g[i][j]) {
                continue;
            }
            starting.pb({i, j});
        }
    }

    int v = N * N;
    if (v % 2 == 0) {
        halfV = v/2;
    }
    else {
        halfV = v/2 + 1;
    }


    cout << binary_search();
}
{% endhighlight %}



## Problem 3. Milk Scheduling
[Clumsy Cows](http://www.usaco.org/index.php?page=viewproblem2&cpid=246)  
Problem 3: Milk Scheduling [Kalki Seksaria, 2013]

Farmer John's N cows (1 <= N <= 10,000) are conveniently numbered 1..N.
Each cow i takes T(i) units of time to milk.  Unfortunately, some cows
must be milked before others, owing to the layout of FJ's barn.  If cow A
must be milked before cow B, then FJ needs to completely finish milking A
before he can start milking B.  

In order to milk his cows as quickly as possible, FJ has hired a large
number of farmhands to help with the task -- enough to milk any number of
cows at the same time.  However, even though cows can be milked at the same
time, there is a limit to how quickly the entire process can proceed due to
the constraints requiring certain cows to be milked before others.  Please
help FJ compute the minimum total time the milking process must take.  

PROBLEM NAME: msched  

INPUT FORMAT:  

* Line 1: Two space-separated integers: N (the number of cows) and M
        (the number of milking constraints; 1 <= M <= 50,000).  

* Lines 2..1+N: Line i+1 contains the value of T(i) (1 <= T(i) <= 100,000).  

* Lines 2+N..1+N+M: Each line contains two space-separated integers A
        and B, indicating that cow A must be fully milked before one
        can start milking cow B.  These constraints will never form
        a cycle, so a solution is always possible.  

SAMPLE INPUT (file msched.in):  
```
3 1
10
5
6
3 2
```
INPUT DETAILS:

There are 3 cows.  The time required to milk each cow is 10, 5, and 6,
respectively.  Cow 3 must be fully milked before we can start milking cow 2.   

OUTPUT FORMAT:  

* Line 1: The minimum amount of time required to milk all cows.  

SAMPLE OUTPUT (file msched.out  
```
11
```
OUTPUT DETAILS:

Cows 1 and 3 can initially be milked at the same time.  When cow 3 is
finished with milking, cow 2 can then begin.  All cows are finished milking
after 11 units of time have elapsed.  


{% highlight C++ linenos %}

int N;
const int maxV = 1e4 + 1;

int main() {
    // unsyncIO();
    setIO("msched");

    cin >> N;
    vector<pi> cows(N);

    F0R(i, N) {
        cin >> cows[i].s >> cows[i].f;
    }

    sort(all(cows), [](pi a, pi b) {if (a.f == b.f) {return a.s < b.s;} return a.f < b.f;});

    int ans = 0;
    priority_queue<int> currCows;
    int i = N - 1;
    int globalTime = 1;
    while (globalTime > 0) {
        if (i>=0 && currCows.empty()) {
            globalTime = cows[i].f;
        }

        while (i >= 0 && cows[i].f == globalTime) {
            currCows.push(cows[i].s);
            i--;
        }

        if(currCows.size() > 0) {
            ans += currCows.top();
            currCows.pop();
        }

        globalTime--;
        dbg(globalTime, i, ans);
    }

    cout << ans;
}

{% endhighlight %}
