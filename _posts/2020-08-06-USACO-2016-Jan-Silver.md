---
title: "USACO 2016 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - Python
  - USACO
---

# USACO 2016 Jan Silver

## Problem 1. Angry Cows

[Angry Cows](http://www.usaco.org/index.php?page=viewproblem2&cpid=594)

Bessie the cow has designed what she thinks will be the next big hit video game: "Angry Cows". The premise, which she believes is completely original, is that the player shoots cows with a slingshot into a one-dimensional scene consisting of a set of hay bales located at various points on a number line. Each cow lands with sufficient force to detonate the hay bales in close proximity to her landing site. The goal is to use a set of cows to detonate all the hay bales.  

There are N hay bales located at distinct integer positions x1,x2,…,xN on the number line. If a cow is launched with power R landing at position x, this will causes a blast of "radius R", destroying all hay bales within the range x−R…x+R.  

A total of K cows are available to shoot, each with the same power R. Please determine the minimum integer value of R such that it is possible to use the K cows to detonate every single hay bale in the scene.  

INPUT FORMAT (file angry.in):  

The first line of input contains N (1≤N≤50,000) and K (1≤K≤10). The remaining N lines all contain integers x1…xN (each in the range 0…1,000,000,000).

OUTPUT FORMAT (file angry.out):  
Please output the minimum power R with which each cow must be launched in order to detonate all the hay bales.  
SAMPLE INPUT:  
```
7 2
20
25
18
8
10
3
1
```
SAMPLE OUTPUT:
```
5
```
Problem credits: Brian Dean

{% highlight c++ linenos %}

bool possible(ll R, vector<ll> cows, int amt) {
    ll value = R * 2;

    auto it = cows.begin();
    while(it != cows.end()) {
        it = upper_bound(it, cows.end(), value + *it);
        amt--;
    }

    if (amt < 0) {
        return false;
    }
    return true;
}

int angryCows(vector<ll> cities, ll amt) {
    int ans = 0;
    ll l = 0;
    ll r = cities.back() - cities.front();
    while (l <= r) {
        ll mid = (r + l)/2;
        if (possible(mid, cities, amt)) {
            dbg(mid, cities, amt);
            // greater
            ans = mid;
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }
    return ans;
}


int main() {
    ifstream cin ("angry.in");
    ofstream cout ("angry.out");

    ll N, K;
    cin >> N >> K;

    vector<ll> cows(N);

    F0R(i, N) {
        cin >> cows[i];
    }

    sort(cows.begin(), cows.end());

    dbg(cows);

    cout << angryCows(cows, K);

}
{% endhighlight %}

## Problem 2. Subsequences Summing to Sevens

Farmer John's N cows are standing in a row, as they have a tendency to do from time to time. Each cow is labeled with a distinct integer ID number so FJ can tell them apart. FJ would like to take a photo of a contiguous group of cows but, due to a traumatic childhood incident involving the numbers 1…6, he only wants to take a picture of a group of cows if their IDs add up to a multiple of 7.
Please help FJ determine the size of the largest group he can photograph.  

INPUT FORMAT (file div7.in):  
The first line of input contains N (1≤N≤50,000). The next N lines each contain the N integer IDs of the cows (all are in the range 0…1,000,000).  
OUTPUT FORMAT (file div7.out):  
Please output the number of cows in the largest consecutive group whose IDs sum to a multiple of 7. If no such group exists, output 0.  
You may want to note that the sum of the IDs of a large group of cows might be too large to fit into a standard 32-bit integer. If you are summing up large groups of IDs, you may therefore want to use a larger integer data type, like a 64-bit "long long" in C/C++.  

SAMPLE INPUT:  
```
7
3
5
1
6
2
14
10
```
SAMPLE OUTPUT:  
```
5  
```
In this example, 5+1+6+2+14 = 28.  

{% highlight c++ linenos %}
int main() {
    ifstream cin ("div7.in");
    ofstream cout ("div7.out");

    ll N;
    cin >> N;

    vector<ll> cows(N);
    vector<ll> prefix(N + 1);

    F0R(i, N) {
        cin >> cows[i];
        prefix[i + 1] = ( prefix[i] + cows[i]) % 7;
    }

    vector<int> myVec(7);
    F0R(i, 7) {
        myVec[i] = -1;
    }
    int maximum = 0;

    F0R(i, prefix.size()) {
        if (myVec[prefix[i]] == -1) {
            myVec[prefix[i]] = i;
        }
        else {
            maximum = max(i - myVec[prefix[i]], maximum);
        }
    }
    cout << maximum;


    // vector<pair<int, int>> dp(N + 1);

    // dp[i] = max up to then

    /*F0R(i, prefix.size()) {
        F0R(j, i) {
            int x = prefix[i] - prefix[j];
            if (x % 7 == 0) {
                maximum = max(maximum, i - j);
            }
        }
    }

    cout << maximum;*/
}
{% endhighlight %}

int N;
vector<vector<int>> G;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

void flood(int cor_x, int cor_y, int newColor) {

    queue<pair<int, int>> myQ;

    myQ.push(make_pair(cor_x, cor_y));

    while(! myQ.empty()) {
        pair<int, int> curr = myQ.front();
        myQ.pop();

        int x = curr.f;
        int y = curr.s;

        dbg(x, y);
        if (x < 0 || x > G.size() - 1 || y < 0 || y > G[0].size() - 1) {
            continue;
        }
        else {
            if (G[x][y] == 0) {
                G[x][y] = newColor;

                F0R(i, 4) {
                    myQ.push(make_pair(x + dx[i], y + dy[i]));
                }
            }
        }
    }
}

int gates() {
    int colors = 0;
    F0R(i, 2 * N + 1) {
        F0R(j, 2 * N + 1) {
            if (G[i][j] == 0) {
                colors++;
                flood(i, j, colors);
            }
        }
    }

    return colors;
}


int main() {
    ifstream cin ("gates.in");
    ofstream cout ("gates.out");

    cin >> N;
    G.resize(2*N + 1);
    F0R(i, 2*N + 1) {
        G[i].resize(2*N + 1);
    }

    string path;
    cin >> path;

    int x = N;
    int y = N;

    F0R(i, N) {
        if (path[i] == 'N') {
            y++;
            G[x][y] = -1;
            y++;
            G[x][y] = -1;
        }
        if (path[i] == 'S') {
            y--;
            G[x][y] = -1;
            y--;
            G[x][y] = -1;
        }
        if (path[i] == 'E') {
            x++;
            G[x][y] = -1;
            x++;
            G[x][y] = -1;
        }
        if (path[i] == 'W') {
            x--;
            G[x][y] = -1;
            x--;
            G[x][y] = -1;
        }
    }

    cout << gates() - 1;

}
