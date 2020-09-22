---
title: "Floodfill"
categories:
  - Programming
tags:
  - Algorithms
  - C++
---

## Floodfill (Recursive)

{% highlight c++ linenos %}
int visited[MaxX][MaxY];
int currSize = 0;

int xv[] = {0, 0, -1, 1};
int yv[] = {-1, 1, 0, 0};
void ff(int r, int c, int color) {
    // >= N or >? Does M exist?
    if (r >= N || r < 0 || c >= M || c < 0 || visited[r][c]) {
        return;
    }

    currSize++;
    visited[r][c] = color;

    F0R(i, 4) {
        int nX = r + xv[i], nY = c + yv[i];
        ff(nX, nY, color);
    }
}

int floodfill() {

    memset(visited, 0, MaxX * MaxY * sizeof(bool));

    int color = 0;
    F0R(i, N) {
      F0R(j, M) {
        if (! visited[i][j]) {
          currSize = 0;
          color++;
          ff(i, j, color);
        }
      }
    }

    return color;
}
{% endhighlight %}
