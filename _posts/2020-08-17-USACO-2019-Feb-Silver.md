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

[The Great Revegetation](http://usaco.org/index.php?page=viewproblem2&cpid=918)

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


int N;

int main() {
    setIO("herding");

    cin >> N;

    int val = 0;
    vector<int> left(N);
    vector<int> cows(N);
    F0R(i, N) {
        cin >> cows[i];
    }

    sort(all(cows));

    int maxL = 0;
    int minL = INT_MAX;

    FOR(i, 1, N) {
        int count = 0;
        int j = i - 1;
        while (j >= 0 && cows[i] - cows[j] < N) {
            count++;
            j--;
        }
        maxL = max(maxL, count);
        minL = min(minL, count);
        left[i] = count;
    }


        cout << N - 1 - maxL << endl;



    cout << N - 1 - minL;

    // cout << 1 << endl << 2;
}

{% endhighlight %}


## Problem 3. The Great Revegetation

[The Great Revegetation](http://usaco.org/index.php?page=viewproblem2&cpid=920)

{% highlight c++ linenos %}

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
