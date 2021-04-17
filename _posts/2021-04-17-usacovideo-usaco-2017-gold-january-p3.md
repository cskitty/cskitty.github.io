---
title: USACO 2017 Gold January P3. Cow Navigation
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2017 Gold January P3. Cow Navigation

{% include video id="i386-OEo53I" provider="youtube" %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N;
const int maxV = 21;
int grid[maxV][maxV];
int dist[maxV][maxV][4][maxV][maxV][4];
queue<array<int, 6>> pq;

int Nd = 0, Ed = 1, Sd = 2, Wd = 3;
int dirX[] = {-1, 0, 1, 0};
int dirY[] = {0, 1, 0,-1};

inline bool valid(int x, int y, int d) {
    if (x + dirX[d] < N && x + dirX[d] >= 0 && y + dirY[d] < N && y + dirY[d] >= 0) {
        if (grid[x + dirX[d]][y + dirY[d]] == 1) {
            return false;
        }
        return true;
    }
    return false;
}

int main() {
    ifstream cin("cownav.in");
    ofstream cout("cownav.out");

    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            char a;
            cin >> a;
            if (a == 'H') {
                grid[i][j] = 1;
            }
            else {
                grid[i][j] = 0;
            }
        }
    }

    pq.push({N - 1, 0, Nd, N - 1, 0, Ed});
    dist[N - 1][0][Nd][N - 1][0][Ed] = 1;

    while (pq.size()) {
        array<int, 6> node = pq.front();
        int x1 = node[0], y1 = node[1], d1 = node[2], x2 = node[3], y2 = node[4], d2 = node[5];
        pq.pop();

        if (x1 == 0 && x1 == x2 && y1 == N - 1 && y1 == y2) {
            cout << dist[x1][y1][d1][x2][y2][d2] - 1;
            return 0;
        }

        // forward
        int newX1 = x1, newY1 = y1, newD1 = d1, newX2 = x2, newY2 = y2, newD2 = d2;
        if (valid(x1, y1, d1) && (!(x1 == 0 && y1 == N - 1))) {
            newX1 = x1 + dirX[d1];
            newY1 = y1 + dirY[d1];
        }
        if (valid(x2, y2, d2) && (!(x2 == 0 && y2 == N - 1))) {
            newX2 = x2 + dirX[d2];
            newY2 = y2 + dirY[d2];
        }

        if (dist[newX1][newY1][newD1][newX2][newY2][newD2] == 0) {
            dist[newX1][newY1][newD1][newX2][newY2][newD2] = dist[x1][y1][d1][x2][y2][d2] + 1;
            pq.push({newX1, newY1, newD1, newX2, newY2, newD2});
        }

        // left/right
        for(int direction = -1; direction <= 1; direction += 2) {
            newD1 = (d1 + 4 + direction) % 4;
            newD2 = (d2 + 4 + direction) % 4;

            if (dist[x1][y1][newD1][x2][y2][newD2] == 0) {
                dist[x1][y1][newD1][x2][y2][newD2] = dist[x1][y1][d1][x2][y2][d2] + 1;
                pq.push({x1, y1, newD1, x2, y2, newD2});
            }
        }
    }

}
{% endhighlight %}  
