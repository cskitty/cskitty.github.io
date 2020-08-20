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

# USACO 2019 Jan Silver

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
