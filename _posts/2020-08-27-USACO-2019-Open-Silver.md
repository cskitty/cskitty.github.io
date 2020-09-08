---
title: "USACO 2019 Open Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Binary Search
---

# USACO 2019 Open Silver


## Problem 1. Left Out

[Fence Planning](http://www.usaco.org/index.php?page=viewproblem2&cpid=942)  

Farmer John is attempting to take a photograph of his herd of cows. From past experience, he knows this particular endeavor never usually ends well.
This time, Farmer John has purchased an expensive drone in order to take an aerial photo. To make the photo look as good as possible, he wants his cows all to be facing the same direction when the photo is taken. The cows are currently arranged in an N×N grid (2≤N≤1000) inside a fenced-in square pasture, for example:  

 ```
RLR  
RRL  
LLR
```

Here, an 'R' means a cow facing right, and an 'L' means a cow facing left. Since the cows are packed together, Farmer John cannot walk up to an individual cow to make it turn around. All he can do is shout at any row or column of cows to turn around, causing L's to change to R's and R's to L's within the row or column in question. Farmer John can yell at as many rows or columns as he wants, even at the same row or column more than once.  

As expected, Farmer John observes that he is unable to make his cows all face one common direction. The best he can do is get all but one of the cows to face the same direction. Please determine the identity of such a cow.  

INPUT FORMAT (file leftout.in):  
The first line contains N. The next N lines describe rows 1…N in the grid of cows, each containing a string of length N.  
OUTPUT FORMAT (file leftout.out):  
Print the row and column index of a cow such that if that cow were flipped, Farmer John could make all his cows face the same direction. If no such cow exists, print -1. If multiple such cows exist, print the one with the smallest row index, or if multiple such cows have the same smallest row index, print the one with the smallest column index.  
SAMPLE INPUT:   
```
3
RLR
RRL
LLR
```
SAMPLE OUTPUT:
```
1 1
```
In the example above, the cow in row 1, column 1 (the upper-left corner) is the offending cow, since Farmer John can shout at row 2 and column 3 to make all other cows face left, with just this cow facing right.

Problem credits: Brian Dean

## Problem 2. Cow Steeplechase II

[Fence Planning](http://www.usaco.org/index.php?page=viewproblem2&cpid=943)  

In the past, Farmer John had contemplated a number of innovative ideas for new cow sports, among them Cow Steeplechase, where herds of cows would race around a course and jump over hurdles. His past efforts to build interest in this sport have met with mixed results, so he is hoping to build an even larger Cow Steeplechase course on his farm to try and create more publicity for the sport.
Farmer John's new course is carefully planned around N hurdles, conveniently numbered 1…N (2≤N≤105), each one described as a line segment on the 2D map of the course. These line segments should not intersect each-other in any way, even their at endpoints.  

Unfortunately, Farmer John wasn't paying attention when crafting the course map and notices that there are intersections between segments. However, he also notices that if he takes away just one segment, the map is restored to its intended state of having no intersecting segments (not even at endpoints).  

Please determine a line segment Farmer John can remove from his plan to restore the property that no segments intersect. If multiple segments are possible to remove in this way, please output the index of the earliest one in the input.  

INPUT FORMAT (file cowjump.in):  
The first line of input contains N. Each of the N remaining lines describe one line segment with four integers x1 y1 x2 y2, all nonnegative integers at most 109. The line segment has (x1,y1) and (x2,y2) as its endpoints. All endpoints are distinct from each-other.  
OUTPUT FORMAT (file cowjump.out):  
Output the earliest index within the input of a segment such that removing that segment causes the remaining segments not to intersect.  
SAMPLE INPUT:
```
4
2 1 6 1
4 0 1 5
5 6 5 5
2 7 1 3
```
SAMPLE OUTPUT:
```
2
```
Note: You may want to be careful of integer overflow in this problem, due to the size of the integers provided as coordinates of segment endpoints.

Problem credits: Brian Dean




{% highlight C++ linenos %}  


ll N;
ll x;

struct Point {
    ll x, y;
    int segindex;
    bool start;
};

bool operator< (Point p1, Point p2) { return p1.x==p2.x ? p1.y<p2.y : p1.x<p2.x; }

struct Segment {
    Point p, q;
    int index;
};

// What is the y coordinate of segment s when evaluated at x?
double eval(Segment s) {
    if (s.p.x == s.q.x) return s.p.y;
    return s.p.y + (s.q.y-s.p.y) * (x-s.p.x) / (s.q.x-s.p.x);
}

bool operator< (Segment s1, Segment s2) { return s1.index != s2.index && eval(s1)<eval(s2); }
bool operator== (Segment s1, Segment s2) { return s1.index == s2.index; }


// Intersection testing (here, using a standard "cross product" trick)
int sign(ll x) { if (x==0) return 0; else return x<0 ? -1 : +1; }
int operator* (Point p1, Point p2) { return sign(p1.x * p2.y - p1.y * p2.x); }
Point operator- (Point p1, Point p2) { Point p = {p1.x-p2.x, p1.y-p2.y}; return p; }
bool isect(Segment &s1, Segment &s2)
{
    Point &p1 = s1.p, &q1 = s1.q, &p2 = s2.p, &q2 = s2.q;
    return ((q2-p1)*(q1-p1)) * ((q1-p1)*(p2-p1)) >= 0 && ((q1-p2)*(q2-p2)) * ((q2-p2)*(p1-p2)) >= 0;
}



int main() {
    setIO("cowjump");

    cin >> N;

    vector<Point> points;
    vector<Segment> hurdles(N);

    /*Shamos-Hoey Algorithm*/
    F0R(i, N) {
        cin >> hurdles[i].p.x >> hurdles[i].p.y >> hurdles[i].q.x >> hurdles[i].q.y;

        hurdles[i].p.segindex = i, hurdles[i].q.segindex = i;

        if (hurdles[i].p.x < hurdles[i].q.x) {
            hurdles[i].p.start = true;
            hurdles[i].q.start = false;
        }
        else if (hurdles[i].p.x == hurdles[i].q.x) {
            if (hurdles[i].p.y > hurdles[i].q.y) {
                hurdles[i].p.start = false;
                hurdles[i].q.start = true;
            }
            else {
                hurdles[i].p.start = true;
                hurdles[i].q.start = false;
            }
        }
        else {
            hurdles[i].p.start = false;
            hurdles[i].q.start = true;
        }
        hurdles[i].index = i;
        points.pb(hurdles[i].p);
        points.pb(hurdles[i].q);
    }

    sort(all(points), [](Point a, Point b) {if (a.x == b.x) return a.y < b.y; else {return a.x < b.x;}});

    int line1, line2;
    set<Segment> active;

    bool flag = true;
    for (int i = 0; i < points.size() && flag; i++) {
        x = points[i].x;

        if (points[i].start) {

            set<Segment>::iterator next = lower_bound(all(active), hurdles[points[i].segindex]);
            if (next != active.end() && isect(hurdles[next->index], hurdles[points[i].segindex])) {
                line1 = points[i].segindex;
                line2 = next->index;
                flag = false;
                break;
            }

            set<Segment>::iterator prev = next;
            if (prev != active.begin()) {
                prev--;
                if (isect(hurdles[prev->index], hurdles[points[i].segindex])) {
                    line1 = points[i].segindex;
                    line2 = prev->index;
                    flag = false;
                    break;
                }
            }
            active.insert(hurdles[points[i].segindex]);
        }
        else {
            //set<Segment>::iterator prev = active.begin(), curr = active.begin();
            auto it = active.find(hurdles[points[i].segindex]);
            if (it != active.end()) {
                auto after = it, before = it;
                after++;
                if (before != active.begin() && after != active.end()) {
                    before--;
                    if (isect(hurdles[before->index], hurdles[after->index])) {
                        line1 = before->index;
                        line2 = after->index;
                        flag = false;
                        break;
                    }
                }
                active.erase(hurdles[points[i].segindex]);
            }
        }
    }

    if (line1 < line2) {
        swap(line1, line2);
    }
    int val = 0;
    F0R(i, N) {
        if (i != line1) {
            if (isect(hurdles[i], hurdles[line1])) {
                val++;
            }
        }
    }

    if (val > 1) {
        cout << line1 + 1;
    }
    else {
        cout << line2 + 1;
    }
}
{% endhighlight %}

## Problem 3. Fence Planning

[Fence Planning](http://www.usaco.org/index.php?page=viewproblem2&cpid=944)  

Farmer John's N cows, conveniently numbered 1…N (2≤N≤105), have a complex social structure revolving around "moo networks" --- smaller groups of cows that communicate within their group but not with other groups.  
Each cow is situated at a distinct (x,y) location on the 2D map of the farm, and we know that M pairs of cows (1≤M<105) moo at each-other. Two cows that moo at each-other belong to the same moo network.  

In an effort to update his farm, Farmer John wants to build a rectangular fence, with its edges parallel to the x and y axes. Farmer John wants to make sure that at least one moo network is completely enclosed by the fence (cows on the boundary of the rectangle count as being enclosed). Please help Farmer John determine the smallest possible perimeter of a fence that satisfies this requirement. It is possible for this fence to have zero width or zero height.  

INPUT FORMAT (file fenceplan.in):  
The first line of input contains N and M. The next N lines each contain the x and y coordinates of a cow (nonnegative integers of size at most 108). The next M lines each contain two integers a and b describing a moo connection between cows a and b. Every cow has at least one moo connection, and no connection is repeated in the input.  
OUTPUT FORMAT (file fenceplan.out):  
Please print the smallest perimeter of a fence satisfying Farmer John's requirements.  
SAMPLE INPUT:  
```
7 5
0 5
10 5
5 0
5 10
6 7
8 6
8 4
1 2
2 3
3 4
5 6
7 6
```
SAMPLE OUTPUT:
```
10
```
Problem credits: Brian Dean



{% highlight C++ linenos %}  
int N, M;
int ans;
int rep[MX];
vector<int> adj_list[MX];
vector<vector<int>> cows(MX);
int lx, ly, rx, ry;
int mlx, mly, mrx, mry;
int minPeri = INT_MAX;
int currCount;

bool visited[MX];

void dfs(int node) {
    visited[node] = true;
    currCount++;

    lx = min(lx, cows[node][0]);
    rx = max(rx, cows[node][0]);
    ly = min(ly, cows[node][1]);
    ry = max(ry, cows[node][1]);

    for (int i : adj_list[node]) {
        if (! visited[i]) {
            dfs(i);
        }
    }
}

int countComponents() {
    int mCount = 0;
    F0R(i, N) {
        if (! visited[i]) {
            lx = cows[i][0], rx = cows[i][0], ly = cows[i][1], ry = cows[i][1];
            dfs(i);

            int peri = (rx - lx) + (ry - ly) + (rx - lx) + (ry - ly);
            if (peri < minPeri) {
                minPeri = peri;
                mlx = lx, mrx = rx, mly = ly, mry = ry;
            }

        }
    }
    return minPeri;
}

int main() {
    setIO("fenceplan");
    cin >> N >> M;

    F0R(i, N) {
        int A, B;
        cin >> A >> B;
        cows[i] = {A, B};
    }

    F0R(i, M) {
        int O, T;
        cin >> O >> T;

        adj_list[O - 1].push_back(T - 1);
        adj_list[T - 1].push_back(O - 1);
    }

    ans = countComponents();

    cout << ans << endl;
}
{% endhighlight %}
