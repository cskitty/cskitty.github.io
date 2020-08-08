---
title: "USACO 2015 Dec Silver"
categories:
  - USACO
tags:
  - Algorithms
  - Java
  - USACO
---

# USACO 2015 Dec Silver

## Problem 1: Switching on the Lights
[Switching on the Lights](http://www.usaco.org/index.php?page=viewproblem2&cpid=570)

Farmer John has recently built an enormous barn consisting of an N×N grid of rooms (2≤N≤100), numbered from (1,1) up to (N,N). Being somewhat afraid of the dark, Bessie the cow wants to turn on the lights in as many rooms as possible.  
Bessie starts in room (1,1), the only room that is initially lit. In some rooms, she will find light switches that she can use to toggle the lights in other rooms; for example there might be a switch in room (1,1) that toggles the lights in room (1,2). Bessie can only travel through lit rooms, and she can only move from a room (x,y) to its four adjacent neighbors (x−1,y), (x+1,y), (x,y−1) and (x,y+1) (or possibly fewer neighbors if this room is on the boundary of the grid).  

Please determine the maximum number of rooms Bessie can illuminate.  

INPUT FORMAT (file lightson.in):  
The first line of input contains integers N and M (1≤M≤20,000).  
The next M lines each describe a single light switch with four integers x, y, a, b, that a switch in room (x,y) can be used to toggle the lights in room (a,b). Multiple switches may exist in any room, and multiple switches may toggle the lights of any room.  

OUTPUT FORMAT (file lightson.out):  
A single line giving the maximum number of rooms Bessie can illuminate.  
SAMPLE INPUT:  
 ```
3 6
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1
```
SAMPLE OUTPUT:   
```
5
```
Here, Bessie can use the switch in (1,1) to turn on lights in (1,2) and (1,3). She can then walk to (1,3) and turn on the lights in (2,1), from which she can turn on the lights in (2,2). The switch in (2,3) is inaccessible to her, being in an unlit room. She can therefore illuminate at most 5 rooms.  

{% highlight c++ linenos %}
int N;
map<pair<int, int>, vector<pair<int, int>>> rooms;
vector<vector<bool>> lights;
vector<vector<bool>> visited;
vector<pair<int, int>> targets;

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

bool valid(int x, int y) {
    return (x >= 0 && y >= 0 && x < N && y < N);
}

bool findNeighbors(int x, int y) {
    F0R(i, 4) {
        int newX = x + dx[i];
        int newY = y + dy[i];
        if (valid(newX, newY) && visited[newX][newY] && lights[newX][newY]) {
            return true;
        }
    }
    return false;
}

void floodfill(int x, int y) {
    visited[x][y] = true;

    pair<int, int> curr = make_pair(x, y);
n
    F0R(i, rooms[curr].size()) {
        int newX = rooms[curr][i].f;
        int newY = rooms[curr][i].s;
        if (! lights[newX][newY]) {
            lights[newX][newY] = true;

            if (findNeighbors(newX, newY)) {
                floodfill(newX, newY);
            }
        }
    }

    F0R(i, 4) {
        int newX = x + dx[i];
        int newY = y + dy[i];
        if (valid(newX, newY) && lights[newX][newY] && ! visited[newX][newY]) {
            floodfill(newX, newY);
        }
    }

}

int main() {
    ifstream cin ("lightson.in");
    ofstream cout ("lightson.out");

    int Q;
    cin >> N >> Q;

    visited.resize(N);
    lights.resize(N);


    F0R(i, N) {
        visited[i].resize(N);
        lights[i].resize(N);
        F0R(j, N) {
            visited[i][j] = false;
            lights[i][j] = false;
        }
    }

    F0R(i, Q) {
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        rooms[make_pair(x1- 1, y1 - 1)].push_back(make_pair(x2 - 1, y2 - 1));
    }

    lights[0][0] = true;
    floodfill(0, 0);
    int count = 0;
    F0R(i, N) {
        F0R(j, N) {
            if (lights[i][j]) {
                count++;
            }
        }
    }

    cout << count;
}
{% endhighlight %}


## Problem 2: High Card Wins
[High Card Wins](http://www.usaco.org/index.php?page=viewproblem2&cpid=571)  

Bessie the cow is a huge fan of card games, which is quite surprising, given her lack of opposable thumbs. Unfortunately, none of the other cows in the herd are good opponents. They are so bad, in fact, that they always play in a completely predictable fashion! Nonetheless, it can still be a challenge for Bessie to figure out how to win.
Bessie and her friend Elsie are currently playing a simple card game where they take a deck of 2N cards, conveniently numbered 1…2N, and divide them into N cards for Bessie and N cards for Elsie. The two then play N rounds, where in each round Bessie and Elsie both play a single card, and the player with the highest card earns a point.  

Given that Bessie can predict the order in which Elsie will play her cards, please determine the maximum number of points Bessie can win.  

INPUT FORMAT (file highcard.in):  
The first line of input contains the value of N (1≤N≤50,000).  
The next N lines contain the cards that Elsie will play in each of the successive rounds of the game. Note that it is easy to determine Bessie's cards from this information.  

OUTPUT FORMAT (file highcard.out):  
Output a single line giving the maximum number of points Bessie can score.  
SAMPLE INPUT:  
```
3
1
6
4
```
SAMPLE OUTPUT:  
```
2
```
Here, Bessie must have cards 2, 3, and 5 in her hand, and she can use these to win at most 2 points by saving the 5 until the end to beat Elsie's 4.  

{% highlight c++ linenos %}
int main() {
    ifstream cin("highcard.in");
    ofstream cout("highcard.out");

    int N;
    cin >> N;

    vector<int> elsie(N);
    F0R(i, N) {
        cin >> elsie[i];
    }
    sort(elsie.begin(), elsie.end());

    vector<int> bessie;

    vector<int> N2(2 * N);
    F0R(i, N * 2) {
        N2[i] = i + 1;
    }

    set_difference(N2.begin(), N2.end(), elsie.begin(), elsie.end(), inserter(bessie, bessie.begin()));

    /*
    int n = 1;
    int i = 0;
    int j = 0;
    dbg(elsie);

    while (n <= 2*N) {// i < N) {
        if (elsie[i] == n) {
            i++;
            n++;
        }
        else {
            bessie[j] = n;
            j++;
            n++;
        }
    }
    */

    int count = 0;
    int i = 0;
    int j = 0;

    while (i < N && j < N) {
        if (elsie[i] < bessie[j]) {
            count++;
            i++;
            j++;
        }
        else {
            j++;
        }
    }

    cout << count;
}
{% endhighlight %}

## Problem 3: Breed Counting

[Breed Counting](http://www.usaco.org/index.php?page=viewproblem2&cpid=572)

Farmer John's N cows, conveniently numbered 1…N, are all standing in a row (they seem to do so often that it now takes very little prompting from Farmer John to line them up). Each cow has a breed ID: 1 for Holsteins, 2 for Guernseys, and 3 for Jerseys. Farmer John would like your help counting the number of cows of each breed that lie within certain intervals of the ordering.  

INPUT FORMAT (file bcount.in):  
The first line of input contains N and Q (1≤N≤100,000, 1≤Q≤100,000).  
The next N lines contain an integer that is either 1, 2, or 3, giving the breed ID of a single cow in the ordering.  

The next Q lines describe a query in the form of two integers a,b (a≤b).  

OUTPUT FORMAT (file bcount.out):  
For each of the Q queries (a,b), print a line containing three numbers: the number of cows numbered a…b that are Holsteins (breed 1), Guernseys (breed 2), and Jerseys (breed 3).    

SAMPLE INPUT:  
```
6 3  
2  
1  
1  
3  
2  
1  
1 6  
3 3  
2 4
```  
SAMPLE OUTPUT:
```  
3 2 1  
1 0 0  
2 0 1  
```
{% highlight c++ linenos %}
int main() {
    ifstream cin ("bcount.in");
    ofstream cout ("bcount.out");

    int N, Q;
    cin >> N >> Q;

    vector<int> one(N + 1);
    vector<int> two(N + 1);
    vector<int> three(N + 1);

    FOR(cow, 1, N + 1) {
        int val;
        cin >> val;
        one[cow] = one[cow - 1];
        two[cow] = two[cow - 1];
        three[cow] = three[cow - 1];

        if (val == 1) {
            one[cow]++;
        }
        if (val == 2) {
            two[cow]++;
        }
        if (val == 3) {
            three[cow]++;
        }
    }

    F0R(query, Q) {
        int start, end;
        cin >> start >> end;

        cout << one[end] - one[start - 1] << " " << two[end] - two[start - 1] << " " << three[end] - three[start - 1] << endl;

    }

}
{% endhighlight %}
