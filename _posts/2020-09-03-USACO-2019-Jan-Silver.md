---
title: "USACO 2019 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2019 Jan Silver

Problem 1. Grass Planting
[Convention](http://usaco.org/index.php?page=viewproblem2&cpid=894)

It's the time of year for Farmer John to plant grass in all of his fields. The entire farm consists of N fields (1≤N≤105), conveniently numbered 1…N and conveniently connected by N−1 bidirectional pathways in such a way that every field can reach every other field via some collection of pathways.  
Farmer John can potentially plant a different type of grass in each field, but he wants to minimize the number of grass types he uses in total, since the more types of grass he uses, the more expense he incurs.  

Unfortunately, his cows have grown rather snobbish about their selection of grass on the farm. If the same grass type is planted in two adjacent fields (directly connected by a pathway) or even two nearly-adjacent fields (both directly connected to a common field with pathways), then the cows will complain about lack of variety in their dining   options. The last thing Farmer John needs is complaining cows, given how much mischief they have been known to create when dissatisfied.  

Please help Farmer John determine the minimum number of types of grass he needs for his entire farm.  

INPUT FORMAT (file planting.in):  
The first line of input contains N. Each of the remaining N−1 lines describes a pathway in terms of the two fields it connects.  
OUTPUT FORMAT (file planting.out):  
Print the minimum number of types of grass that Farmer John needs to use.  
SAMPLE INPUT:
```
4
1 2
4 3
2 3
```
SAMPLE OUTPUT:
```
3
```
In this simple example, there are 4 fields all connected in a linear fashion. A minimum of three grass types are needed. For example, Farmer John could plant the fields with grass types A, B, and C as A - B - C - A.

Problem credits: Dhruv Rohatgi

{% highlight C++ linenos %}
int main() {
    setIO("planting");

    ll ans = 0;
    vector<ll> degree;

    cin >> N;
    degree.resize(N+1);

    F0R(i, N-1) {
        int x, y;
        cin >> x >> y;

        ++degree[x];
        ++degree[y];
    }

    ans = * max_element(all(degree));
    cout << ans + 1 << endl;
}

{% endhighlight %}


Problem 2. Icy Perimeter
[Icy Perimeter](http://usaco.org/index.php?page=viewproblem2&cpid=895)

Farmer John is going into the ice cream business! He has built a machine that produces blobs of ice cream but unfortunately in somewhat irregular shapes, and he is hoping to optimize the machine to make the shapes produced as output more reasonable.  
The configuration of ice cream output by the machine can be described using an N×N grid (1≤N≤1000) as follows:  


##....  
....#.  
.#..#.  
.#####  
...###  
....##  
Each '.' character represents empty space and each '#' character represents a 1×1 square cell of ice cream.  

Unfortunately, the machine isn't working very well at the moment and might produce multiple disconnected blobs of ice cream (the figure above has two). A blob of ice cream is connected if you can reach any ice cream cell from every other ice cream cell in the blob by repeatedly stepping to adjacent ice cream cells in the north, south, east, and west directions.  

Farmer John would like to find the area and perimeter of the blob of ice cream having the largest area. The area of a blob is just the number of '#' characters that are part of the blob. If multiple blobs tie for the largest area, he wants to know the smallest perimeter among them. In the figure above, the smaller blob has area 2 and perimeter 6, and the larger blob has area 13 and perimeter 22.   

Note that a blob could have a "hole" in the middle of it (empty space surrounded by ice cream). If so, the boundary with the hole also counts towards the perimeter of the blob. Blobs can also appear nested within other blobs, in which case they are treated as separate blobs. For example, this case has a blob of area 1 nested within a blob of area 16:  

#####  
#...#  
#.#.#  
#...#  
#####  
Knowing both the area and perimeter of a blob of ice cream is important, since Farmer John ultimately wants to minimize the ratio of perimeter to area, a quantity he calls the icyperimetric measure of his ice cream. When this ratio is small, the ice cream melts slower, since it has less surface area relative to its mass.  

INPUT FORMAT (file perimeter.in):  
The first line of input contains N, and the next N lines describe the output of the machine. At least one '#' character will be present.  
OUTPUT FORMAT (file perimeter.out):  
Please output one line containing two space-separated integers, the first being the area of the largest blob, and the second being its perimeter. If multiple blobs are tied for largest area, print the information for whichever of these has the smallest perimeter.  
SAMPLE INPUT:  
```
6
##....
....#.
.#..#.
.#####
...###
....##
```
SAMPLE OUTPUT:
```
13 22
```
Problem credits: Brian Dean

{% highlight C++ linenos %}

const int MaX = 1001;
const int MaaX = MaX*MaX;
int grid[MaX][MaX];
int N, M;
bool visited[MaX][MaX];
int area[MaaX];
int perimeter[MaaX];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};


void floodfill(int r, int c, int color){
    if (r < 0 || r >= N || c < 0 || c >= N || grid[r][c] == -1) {
        return; // if outside grid
    }
    // if(grid[r][c] != color) return; // wrong color
    if(visited[r][c]) return; // already visited this square
    visited[r][c] = true; // mark current square as visited
    area[color]++;
    dbg(r, c, area[color]);
    grid[r][c] = color;


    floodfill(r, c+1, color);
    floodfill(r, c-1, color);
    floodfill(r-1, c, color);
    floodfill(r+1, c, color);
}



void findPerimeter() {
    F0R(i, N) {
        F0R(j, N) {
            if (grid[i][j] != -1) {

                F0R(k, 4) {
                    int newX = i + dx[k];
                    int newY = j + dy[k];
                    if ((newX >= N || newX < 0 || newY >= N || newY < 0)
                    || grid[newX][newY] == -1) {
                        perimeter[grid[i][j]]++;
                    }
                }
            }
        }
    }
}



int main() {
    setIO("perimeter");

    cin >> N;
    F0R(i, N) {
        F0R(j, N) {
            char currI;
            cin >> currI;
            if (currI == '.') {
                grid[i][j] = -1;
            }
            else {
                grid[i][j] = 0;
            }
        }
    }

    int color = 1;
    F0R(i, N) {
        F0R(j, N) {
            if (! visited[i][j] && grid[i][j] == 0) {
                dbg(i, j, grid[i][j]);
                floodfill(i, j, color);
                color++;

            }
        }
    }


    findPerimeter();
    int ans = 1;

    FOR(i, 1, color + 1) {
        if (area[i] > area[ans]) {
            ans = i;
        }
        else if (area[i] == area[ans] && perimeter[i] < perimeter[ans]) {
            ans = i;
        }
    }

    cout << area[ans] << " " << perimeter[ans];
}

{% endhighlight %}

Problem 3. Mountain View
[Mountain View](http://usaco.org/index.php?page=viewproblem2&cpid=896)

From her pasture on the farm, Bessie the cow has a wonderful view of a mountain range on the horizon. There are N mountains in the range (1≤N≤105). If we think of Bessie's field of vision as the xy plane, then each mountain is a triangle whose base rests on the x axis. The two sides of the mountain are both at 45 degrees to the base, so the peak of the mountain forms a right angle. Mountain i is therefore precisely described by the location (xi,yi) of its peak. No two mountains have exactly the same peak location.  
Bessie is trying to count all of the mountains, but since they all have roughly the same color, she cannot see a mountain if its peak lies on or within the triangular shape of any other mountain.  

Please determine the number of distinct peaks, and therefore mountains, that Bessie can see.  

INPUT FORMAT (file mountains.in):  
The first line of input contains N. Each of the remaining N lines contains xi (0≤xi≤109) and yi (1≤yi≤109) describing the location of one mountain's peak.  
OUTPUT FORMAT (file mountains.out):  
Please print the number of mountains that Bessie can distinguish.  
SAMPLE INPUT:  
```
3
4 6
7 2
2 5
```
SAMPLE OUTPUT:
```
2
```
In this example, Bessie can see the first and last mountain. The second mountain is obscured by the first.

Problem credits: Brian Dean

{% highlight C++ linenos %}

int main() {
    setIO("mountains");

    ll N;
    cin >> N;

    vector<pair<ll, ll>> mt(N);
    F0R(i, N) {
        ll X, Y;
        cin >> X >> Y;
        mt[i].f = X - Y;
        mt[i].s = X + Y;
    }

    ll ans = 0;
    ll currMaxY = INT_MIN;

    sort(all(mt), [](pair<ll, ll> a, pair<ll, ll> b){if (a.f == b.f) return a.s > b.s; else {return a.f < b.f;}});
    F0R(i, N) {
        dbg(mt[i].f, mt[i].s);
    }

    F0R(i, N) {
        if (mt[i].s > currMaxY) {
            currMaxY = mt[i].s;
            ans++;
            dbg(currMaxY, ans);
        }
    }

    cout << ans;
}

{% endhighlight %}
