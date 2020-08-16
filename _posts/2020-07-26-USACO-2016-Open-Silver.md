---
title: "USACO 2016 Open Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Two Pointers
  - Dynamic Programming
---

# USACO 2016 Open Silver


## Problem 1. Field Reduction

[Field Reduction](http://www.usaco.org/index.php?page=viewproblem2&cpid=642)

Farmer John's N cows (5≤N≤50,000) are all located at distinct positions in his two-dimensional field. FJ wants to enclose all of the cows with a rectangular fence whose sides are parallel to the x and y axes, and he wants this fence to be as small as possible so that it contains every cow (cows on the boundary are allowed).  
FJ is unfortunately on a tight budget due to low milk production last quarter. He would therefore like to build an even smaller fenced enclosure if possible, and he is willing to sell up to three cows from his herd to make this possible.  

Please help FJ compute the smallest possible area he can enclose with his fence after removing up to three cows from his herd (and thereafter building the tightest enclosing fence for the remaining cows).  

For this problem, please treat cows as points and the fence as a collection of four line segments (i.e., don't think of the cows as "unit squares"). Note that the answer can be zero, for example if all remaining cows end up standing in a common vertical or horizontal line.  

INPUT FORMAT (file reduce.in):  
The first line of input contains N. The next N lines each contain two integers specifying the location of a cow. Cow locations are positive integers in the range 1…40,000.  
OUTPUT FORMAT (file reduce.out):  
Write a single integer specifying the minimum area FJ can enclose with his fence after removing up to three carefully-chosen cows from his herd.  
SAMPLE INPUT:  
```
6
1 1
7 8
10 9
8 12
4 100
50 7
```
SAMPLE OUTPUT:  
```
12
```
Problem credits: Brian Dean

{% highlight c++ linenos %}

int N;

struct Point {
    int x;
    int y;
    bool disable;
};

vector<Point> cows;
// vector<Point> chosen;

int find(int one, int two, int three) {

    int minX = INT_MAX, maxX = INT_MIN;
    int minY = INT_MAX, maxY = INT_MIN;


    F0R(i, N) {
        if (i != one && i != two && i != three) {
            minX = min(minX, cows[i].x);
            maxX = max(maxX, cows[i].x);
            minY = min(minY, cows[i].y);
            maxY = max(maxY, cows[i].y);
        }
    }

    return (maxX - minX) * (maxY - minY);
}


bool valid(int i) {
    int sum = 0;
    while (i) {
        sum += i & 1;
        i = i >> 1;
    }
    return sum == 3;
}

vector<vector<int>> combinations(int num) {
    vector<vector<int>> ans;

    F0R(i, pow(2, num)) {
        if (valid(i)) {
            //dbg(bitset<12>(i));
            vector<int> x;
            int k = i;
            F0R(j, num) {
                if (k & 1) {
                    x.push_back(j);
                }
                k = k >> 1;
            }
            ans.push_back(x);
        }
    }
    dbg(ans.size());
    return ans;
}


int main() {
    ifstream cin("reduce.in");
    ofstream cout("reduce.out");

    cin >> N;

    cows.resize(N);

    F0R(i, N) {
        cin >> cows[i].x >> cows[i].y;
    }

    sort(cows.begin(), cows.end(), [](Point a, Point b) {return a.x < b.x;});

    cows[0].disable = true;
    cows[1].disable = true;
    cows[2].disable = true;

    cows[N - 1].disable = true;
    cows[N - 2].disable = true;
    cows[N - 3].disable = true;


    sort(cows.begin(), cows.end(), [](Point a, Point b) {return a.y < b.y;});

    cows[0].disable = true;
    cows[1].disable = true;
    cows[2].disable = true;

    cows[N - 1].disable = true;
    cows[N - 2].disable = true;
    cows[N - 3].disable = true;

    vector<int> chosen;

    F0R(i, cows.size()) {
        if (cows[i].disable) {
            chosen.push_back(i);
        }
    }


    dbg(chosen);

    vector<vector<int>> myVec = combinations(chosen.size());

    int ans = INT_MAX;


    for(auto choice : myVec) {
        int area = find(chosen[choice[0]], chosen[choice[1]], chosen[choice[2]]);
        dbg(choice, chosen[choice[0]], chosen[choice[1]], chosen[choice[2]], area);
        ans = min(ans, area);
    }

    cout << ans;
}
{% endhighlight %}

## Problem 2: Diamond Collector

[Diamond Collector](http://www.usaco.org/index.php?page=viewproblem2&cpid=643)  

Bessie the cow, always a fan of shiny objects, has taken up a hobby of mining diamonds in her spare time! She has collected N diamonds (N≤50,000) of varying sizes, and she wants to arrange some of them in a pair of display cases in the barn.  
Since Bessie wants the diamonds in each of the two cases to be relatively similar in size, she decides that she will not include two diamonds in the same case if their sizes differ by more than K (two diamonds can be displayed together in the same case if their sizes differ by exactly K). Given K, please help Bessie determine the maximum number of diamonds she can display in both cases together.  

INPUT FORMAT (file diamond.in):  
The first line of the input file contains N and K (0≤K≤1,000,000,000). The next N lines each contain an integer giving the size of one of the diamonds. All sizes will be positive and will not exceed 1,000,000,000.  
OUTPUT FORMAT (file diamond.out):  
Output a single positive integer, telling the maximum number of diamonds that Bessie can showcase in total in both the cases.  
SAMPLE INPUT:  
```
7 3
10
5
1
12
9
5
14
```
SAMPLE OUTPUT:  
```
5
```
Problem credits: Nick Wu and Brian Dean  

{% highlight c++ linenos %}
#include <fstream>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int diamondCollection(vector<int> diamonds, int n, int k) {

    sort(diamonds.begin(), diamonds.end());

    //int lst = new int[diamonds.size()];
    vector<int> front(diamonds.size(), 0);
    vector<int> back(diamonds.size(), 0);

    int currentIndex = 0;
    for (int i = 0; i < diamonds.size(); i++) {
        while (currentIndex < i && diamonds[i] - diamonds[currentIndex] > k) {
            currentIndex++;
        }
        front[i] = i - currentIndex + 1;
    }

    currentIndex = n - 1;
    for (int i = n - 1; i > 0; i--) {
        while (currentIndex > i && diamonds[currentIndex] - diamonds[i] > k) {
            currentIndex--;
        }
        back[i] = currentIndex - i + 1;
    }


    int maximum = 0;

    vector<int> frontMax(diamonds.size(), 0);
    vector<int> backMax(diamonds.size(), 0);
    frontMax[0] = front[0];
    backMax[diamonds.size() - 1] = back[diamonds.size() - 1];
    for (int i = 1; i < diamonds.size(); i++) {
        // i = partition
        frontMax[i] = max(frontMax[i - 1], front[i]);
        backMax[diamonds.size() - i] = max(backMax[diamonds.size() - 1 + 1], back[diamonds.size() - i]);
    }
    for (int i = 0; i < diamonds.size() - 1; i++) {
        if (frontMax[i] + backMax[i + 1] > maximum) {
            maximum = frontMax[i] + backMax[i + 1];
        }
    }
    return maximum;

}

int main() {
    ifstream fIn("diamond.in");
    ofstream fOut("diamond.out");

    // solution comes here
    int n, k;
    fIn >> n >> k;

    vector<int> diamonds;
    for (int i = 0; i < n; i++) {
        int diamond;
        fIn >> diamond;
        diamonds.push_back(diamond);
    }

    fOut << diamondCollection(diamonds, n, k);

    fIn.close();
    fOut.close();
}

{% endhighlight %}


## Closing the Farm

Farmer John and his cows are planning to leave town for a long vacation, and so FJ wants to temporarily close down his farm to save money in the meantime.
The farm consists of N barns connected with M bidirectional paths between some pairs of barns (1≤N,M≤3000). To shut the farm down, FJ plans to close one barn at a time. When a barn closes, all paths adjacent to that barn also close, and can no longer be used.  

FJ is interested in knowing at each point in time (initially, and after each closing) whether his farm is "fully connected" -- meaning that it is possible to travel from any open barn to any other open barn along an appropriate series of paths. Since FJ's farm is initially in somewhat in a state of disrepair, it may not even start out fully connected.  

INPUT FORMAT (file closing.in):  
The first line of input contains N and M. The next M lines each describe a path in terms of the pair of barns it connects (barns are conveniently numbered 1…N). The final N lines give a permutation of 1…N describing the order in which the barns will be closed.  
OUTPUT FORMAT (file closing.out):  
The output consists of N lines, each containing "YES" or "NO". The first line indicates whether the initial farm is fully connected, and line i+1 indicates whether the farm is fully connected after the ith closing.  
SAMPLE INPUT:  
```
4 3
1 2
2 3
3 4
3
4
1
2
```
SAMPLE OUTPUT:
```
YES
NO
YES
YES
```
Problem credits: Yang Liu  
{% highlight c++ linenos %}

vector<int> adj[MX];
vector<int> closed;
int dist[MX];
int N;

void addEdge(int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}


string cowType;


bool DFS(int start){
    // fill distance array with -1's
    memset(dist, -1, sizeof(dist));

    stack<int> st;
    dist[start] = 0;

    st.push(start);
    while(!st.empty()){
        int node = st.top();
        st.pop();

        for(int next : adj[node]){
            if(dist[next] == -1 && (! closed[next])) {
                dist[next] = dist[node] + 1;
                st.push(next);
            }
        }
    }

    FOR(i, 1, N) {
        if (dist[i] == -1 && (! closed[i])) {
            return false;
        }
    }
    return true;
}


int main() {
    ifstream cin ("closing.in");
    ofstream cout ("closing.out");

    int M;
    cin >> N >> M;
    N++;

    F0R(i, M) {
        int x, y;
        cin >> x >> y;
        addEdge(x, y);
    }

    closed.resize(N);

    if (DFS(1)) {
        cout << "YES" << endl;
    }


    F0R(i, N - 2) {
            int closedB;
            cin >> closedB;
            closed[closedB] = true;

            int start = 1;
            FOR(j, 1, N - 1) {
                if (! closed[j]) {
                    start = j;
                    break;
                }
            }

            if (DFS(start)) {
                cout << "YES" << endl;
            }
            else {
                cout << "NO" << endl;
            }
    }

}

{% endhighlight %}
