---
title: "USACO 2019 Feb Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - BFS
  - BiPartite
---

# USACO 2019 Feb Silver


## Problem 1. Sleepy Cow Herding

[Sleepy Cow Herding](http://usaco.org/index.php?page=viewproblem2&cpid=918)

Farmer John's N cows are always wandering off to the far reaches of the farm! He needs your help herding them back together.  
The main field in the farm is long and skinny -- we can think of it as a number line, on which a cow can occupy any integer location. The N cows are currently situated at different integer locations, and Farmer John wants to move them so they occupy consecutive locations (e.g., positions 3, 4, 5, 6, 7, and 8).  

Unfortunately, the cows are rather sleepy, and Farmer John has trouble getting their attention to make them move. At any point in time, he can only make a cow move if she is an "endpoint" (either the minimum or maximum position among all the cows). When he moves a cow, he can instruct her to move to any unoccupied integer location as long as in this new location she is no longer an endpoint. Observe that over time, these types of moves tend to push the cows closer and closer together.  

Please determine the minimum and maximum number of moves possible before the cows become grouped in N consecutive locations.  

INPUT FORMAT (file herding.in):  
The first line of input contains N (3≤N≤105). Each of the next N lines contains the integer location of a single cow, in the range 1…109.  
OUTPUT FORMAT (file herding.out):  
The first line of output should contain the minimum number of moves Farmer John needs to make to group the cows together. The second line of output should contain the maximum number of such moves he could conceivably make before the cows become grouped together.  
SAMPLE INPUT:  
```
3
7
4
9
```
SAMPLE OUTPUT:
```
1
2
```
The minimum number of moves is 1 --- if Farmer John moves the cow in position 4 to position 8, then the cows are at consecutive locations 7, 8, 9. The maximum number of moves is 2. For example, the cow at position 9 could be moved to position 6, then the cow at position 7 could be moved to position 5.

Problem credits: Matthew Fahrbach

{% highlight c++ linenos %}
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
    ifstream cin("herding.in");
    ofstream cout("herding.out");
    int N;
    cin >> N;
    vector<int> cows (N);

    for (int i = 0; i < N; i++) {
        cin >> cows[i];
    }

    sort(cows.begin(), cows.end());
    int j = 0;
    int maxA = 0;


    for (int i = 0; i < N; i++) {
        while (j < N && cows[i] - cows[j] >= N) {
            j++;
        }
        maxA = max(maxA, i - j + 1);

    }
    int ansMin = N - maxA;

    if ( ( (cows[N - 2] - cows[0] == N - 2) && (cows[N - 1] - cows[N - 2] > 2) )  || ( (cows[N - 1] - cows[1] == N - 2) && (cows[1] - cows[0] > 2) )) {
            ansMin = 2;
        } 

    int ansMax = 0;
    if (cows[N - 1] - cows[N - 2] > cows[1] - cows[0]) {
        ansMax = cows[N - 1] - cows[1] + 1 - (N - 1);
    } else {
        ansMax = cows[N - 2] - cows[0] + 1 - (N - 1);
    } 

    if (cows[N - 1] - cows[0] == N - 1) {
        ansMin = 0;
        ansMax = 0;
    }

    cout << ansMin << endl << ansMax << endl;
}
{% endhighlight %}


## Problem 2. Painting the Barn

[Painting the Barn](http://usaco.org/index.php?page=viewproblem2&cpid=919)

Farmer John is not good at multitasking. He gets distracted often, making it hard to complete long projects. Currently, he is trying to paint one side of his barn, but he keeps painting small rectangular areas and then getting sidetracked by the needs of tending to his cows, leaving some parts of the barn painted with more coats of paint than others.  
We can describe the side of the barn as a 2D x-y plane, on which Farmer John paints N rectangles, each with sides parallel to the coordinate axes, each described by the coordinates of its lower-left and upper-right corner points.  

Farmer John wants to apply several coats of paint to the barn so it doesn't need to be repainted again in the immediate future. However, he doesn't want to waste time applying an excessive number of coats of paint. It turns out that K coats of paint is the optimal amount. Please help him determine how much area of the barn is covered with exactly K coats of paint after he paints all his rectangles.  

INPUT FORMAT (file paintbarn.in):
The first line of input contains N and K (1≤K≤N≤105). Each of the remaining N lines contains four integers x1,y1,x2,y2 describing a rectangular region being painted, with lower-left corner (x1,y1) and upper-right corner (x2,y2). All x and y values are in the range 0…1000, and all rectangles have positive area.
OUTPUT FORMAT (file paintbarn.out):
Please output the area of the barn that is covered by exactly K coats of paint.
SAMPLE INPUT:
```
3 2
1 1 5 5
4 4 7 6
3 3 8 7
```
SAMPLE OUTPUT:
```
8
```
Problem credits: Nick Wu


{% highlight c++ linenos %}

int main() {
    setIO("paintbarn");

    cin >> N >> M;

    vector<vector<int>> dp(1001, vector<int> (1001, 0));

    F0R(i, N) {
        int r1, c1, r2, c2;
        cin >> r1 >> c1 >> r2 >> c2;

      FOR(j, r1, r2) {
            dp[j][c1]++;
            dp[j][c2]--;
        }
    }
    int ans = 0;
    F0R(r, 1001) {
        FOR(c, 1, 1001) {
            dp[r][c] += dp[r][c - 1];
            if (dp[r][c] == M) {
                ans++;
            }
        }
    }


    cout << ans;
}

{% endhighlight %}


## Problem 3. The Great Revegetation

[The Great Revegetation](http://usaco.org/index.php?page=viewproblem2&cpid=920)

A lengthy drought has left Farmer John's N pastures devoid of grass. However, with the rainy season arriving soon, the time has come to "revegetate". In Farmer John's shed, he has two buckets, each with a different type of grass seed. He wants to plant grass in each of his N pastures, choosing exactly one type of grass to plant in each.
Being a dairy farmer, Farmer John wants to make sure he manages the somewhat particular dietary needs of his M cows. Each of his M cows has two favorite pastures. Some of his cows have a dietary restriction that they should only eat one type of grass consistently --- Farmer John therefore wants to make sure the same type of grass is planted in the two favorite fields of any such cow. Other cows have a very different dietary restriction, requiring them to eat different types of grass. For those cows, Farmer John of course wants to make sure their two favorite fields contain different grass types.

Please help Farmer John determine the number of different ways he can plant grass in his N pastures.

INPUT FORMAT (file revegetate.in):
The first line of input contains N (2≤N≤105) and M (1≤M≤105). Each of the next M lines contains a character that is either 'S' or 'D', followed by two integers in the range 1…N, describing the pair of pastures that are the two favorites for one of Farmer John's cows. If the character is 'S', this line represents a cow that needs the same type of grass in its two favorite pastures. If the character is 'D', the line represents a cow that needs different grass types.
OUTPUT FORMAT (file revegetate.out):
Output the number of ways Farmer John can plant grass in his N pastures. Please write your answer in binary.
SAMPLE INPUT:
```
3 2
S 1 2
D 3 2
```
SAMPLE OUTPUT:
```
10
```
Problem credits: Dhruv Rohatgi and Brian Dean

{% highlight c++ linenos %}
#define SAME 0
#define DIFF 1
vector<pair<int, int>> a[MX];
vector<int> vis(MX);
vector<int> coloring(MX);
bool impossible = false;
int N, M;

void dfs(int n, int g, int c) {
    coloring[n] = c;
    vis[n] = g;
    for(pair<int, int> u : a[n]) {
            if (coloring[u.f] != 0) {
                if (u.s == SAME && coloring[u.f] != coloring[n]) {
                    impossible = true;
                    return;
                }
                if (u.s == DIFF && coloring[u.f] == coloring[n]) {
                    impossible = true;
                    return;
                }
            }
            else if (vis[u.f] == 0) {

                 if (u.s == DIFF) {
                    dfs(u.f, g, 3 - c);
                }
                else if (u.s == SAME) {
                    dfs(u.f, g, c);
                }
            }
    }
}

int main() {
    setIO("revegetate");
    cin >> N >> M;

    F0R(i, M) {
        char T;
        int A, B;
        cin >> T >> A >> B;

        if (T == 'S') {
            a[A].push_back(make_pair(B, SAME));
            a[B].push_back(make_pair(A, SAME));
        }
        else {
            a[A].push_back(make_pair(B, DIFF));
            a[B].push_back(make_pair(A, DIFF));
        }
    }

    int groups = 0;
    FOR(i, 1, N + 1) {
        if (vis[i] == 0) {
            groups++;
            dfs(i, groups, 1);
        }
    }

    if (impossible) {
        cout << 0;
    }
    else {
        cout << 1;
        F0R(i, groups) {
            cout << 0;
        }
    }

}
{% endhighlight %}
