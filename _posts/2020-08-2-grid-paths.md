---
title: "Grid Paths"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - DFS
---

# Grid Paths  

[Grid Paths](https://cses.fi/problemset/task/1625/)  

There are 88418 paths in a 7×7 grid from the upper-left square to the lower-left square. Each path corresponds to a 48-character description consisting of characters D (down), U (up), L (left) and R (right).  

For example, the path  

![](/assets/images/gridpath.png)  

corresponds to the description DRURRRRRDDDLUULDDDLDRRURDDLLLLLURULURRUULDLLDDDD.   

You are given a description of a path which may also contain characters ? (any direction). Your task is to calculate the number of paths that match the description.  

Input  

The only input line has a 48-character string of characters ?, D, U, L and R.  

Output  

Print one integer: the total number of paths.  

Example  

Input:  
```
??????R??????U??????????????????????????LD????D?
```
Output:  
```
201
```


{% highlight c++ linenos %}

bool visited[7][7];
string path;
int answer = 0;

inline bool valid(int i, int j) {

    if (i < 7 && j < 7 && i >= 0 && j >= 0 && ! visited[i][j]) {
        return true;
    }


    return false;
}

void dfs(int i, int j, int a) {
    //dbg(i, j, a);

    if (i == 6 && j == 0) {
        if (a == 48) {
            answer++;
        }
        return;
    }

    visited[i][j] = true;

    // go up
    if ((path[a] == 'U' || path[a] == '?')) {
        if (i > 0 && valid(i - 1, j)) {
            if (!(!valid(i - 2, j) && valid(i - 1, j - 1) && valid(i - 1, j + 1)) || (i - 1 == 6 && j == 0)) {
                dfs(i - 1, j, a + 1);
            }
        }
    }

    if (path[a] == 'D' || path[a] == '?') {
        if (i < 6 && valid(i + 1, j)) {
            if (!(!valid(i + 2, j) && valid(i + 1, j - 1) && valid(i + 1, j + 1))) {
                dfs(i + 1, j, a + 1);
            }
        }
    }

    if (path[a] == 'L' || path[a] == '?') {
        if (j > 0 && valid(i, j - 1)) {
            if (!(!valid(i, j - 2) && valid(i - 1, j - 1) && valid(i + 1, j - 1))) {
                dfs(i, j - 1, a + 1);
            }
        }
    }

    if (path[a] == 'R' || path[a] == '?') {
        if (j < 6 && valid(i, j + 1)) {
            if (!(!valid(i, j + 2)  && valid(i - 1, j + 1) && valid(i + 1, j + 1))) {
                dfs(i, j + 1, a + 1);
            }
        }
    }

    visited[i][j] = false;

    return;
}

int main() {
    re(path);
    dfs(0, 0, 0);
    cout << answer;
}
{% endhighlight %}
