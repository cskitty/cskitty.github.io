---
title: "USACO 2016 Feb Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Binary Search
---

# USACO 2016 Feb Silver

## Problem 1. Circular Barn

[Circular Barn](http://www.usaco.org/index.php?page=viewproblem2&cpid=618)  

Being a fan of contemporary architecture, Farmer John has built a new barn in the shape of a perfect circle. Inside, the barn consists of a ring of n rooms, numbered clockwise from 1…n around the perimeter of the barn (3≤n≤1000). Each room has doors to its two neighboring rooms, and also a door opening to the exterior of the barn.  
Farmer John owns n cows, and he wants exactly one cow to end up in each room in the barn. However, the cows, being slightly confused, line up at haphazard doors, with possibly multiple cows lining up at the same door. Precisely ci cows line up outside the door to room i, so ∑ci=n.  

To manage the process of herding the cows so that one cow ends up in each room, Farmer John wants to use the following approach: each cow enters at the door at which she initially lined up, then walks clockwise through the rooms until she reaches a suitable destination. Given that a cow walking through d doors consumes d2 energy, please determine the minimum amount of energy needed to distribute the cows so one ends up in each room.  

INPUT FORMAT (file cbarn.in):  
The first line of input contains n. Each of the remaining n lines contain c1…cn.  
OUTPUT FORMAT (file cbarn.out):  
Please write out the minimum amount of energy consumed by the cows.  
SAMPLE INPUT:  
```
10
1
0
0
2
0
0
1
2
2
2
```
SAMPLE OUTPUT:
```
33
```
Problem credits: Brian Dean  

{% highlight C++ linenos %}
int main() {
    setIO("cbarn");

    int N;
    cin >> N;

    vector<int> rooms(N);

    int sum = 0;
    F0R(i, N) {
        cin >> rooms[i];
        sum += rooms[i] - 1;
    }

    ll minAns = LONG_LONG_MAX;
    F0R(startIndex, N) {
        vector<int> cows = rooms;
        rotate(cows.begin(), cows.begin() + startIndex, cows.end());
        int K = 0;
        ll ans = 0;
        bool flag = true;
        for(int i = 0; i < N && flag; i++) {
            while (cows[K] == 0) {
                K++;
            }

            if (K > i) {
                flag = false;
                continue;
            }
            cows[K]--;
            ans += (i - K) * (i - K);
        }
        if (flag) {
            dbg(startIndex, ans);
            minAns = min(ans, minAns);
        }
    }

    cout << minAns;
}

{% endhighlight %}

## Problem 2. Load Balancing

[Load Balancing](http://www.usaco.org/index.php?page=viewproblem2&cpid=619)

Farmer John's N cows are each standing at distinct locations (x1,y1)…(xn,yn) on his two-dimensional farm (1≤N≤1000, and the xi's and yi's are positive odd integers of size at most 1,000,000). FJ wants to partition his field by building a long (effectively infinite-length) north-south fence with equation x=a (a will be an even integer, thus ensuring that he does not build the fence through the position of any cow). He also wants to build a long (effectively infinite-length) east-west fence with equation y=b, where b is an even integer. These two fences cross at the point (a,b), and together they partition his field into four regions.   
FJ wants to choose a and b so that the cows appearing in the four resulting regions are reasonably "balanced", with no region containing too many cows. Letting M be the maximum number of cows appearing in one of the four regions, FJ wants to make M as small as possible. Please help him determine this smallest possible value for M.  

INPUT FORMAT (file balancing.in):   
The first line of the input contains a single integer, N. The next N lines each contain the location of a single cow, specifying its x and y coordinates.   
OUTPUT FORMAT (file balancing.out):  
You should output the smallest possible value of M that FJ can achieve by positioning his fences optimally.   
SAMPLE INPUT:  
```
7
7 3
5 5
7 13
3 1
11 7
5 3
9 1
```
SAMPLE OUTPUT:
```
2  
```
{% highlight C++ linenos %}
int N;

map<int, int> compare;
vector<pair<int, int>> cows;

int main() {
    setIO("balancing");

    cin >> N;

    cows.resize(N);

    set<int> ySet;
    F0R(i, N) {
        cin >> cows[i].f >> cows[i].s;
        ySet.insert(cows[i].s);
    }

    sort(all(cows));

    int M = INT_MAX;
    F0R(i, N) {
      // y
      ll yPoint = cows[i].s + 1;

      vector<ll> upperY, lowerY;
      F0R(j, N) {
          if (cows[j].s < yPoint) {
              lowerY.push_back(j);
          }
          else {
              upperY.push_back(j);
          }
      }

      int p1 = 0, p2 = 0;
      while (p1 < lowerY.size() || p2 < upperY.size()) {
          int xLine = INT_MAX;
          if (p1 < lowerY.size()) {
              xLine = min(xLine, cows[lowerY[p1]].f);
          }
          if (p2 < upperY.size()) {
              xLine = min(xLine, cows[upperY[p2]].f);
          }

          while(p1 < lowerY.size() && cows[lowerY[p1]].f == xLine) {
              p1++;
          }
          while(p2 < upperY.size() && cows[upperY[p2]].f == xLine) {
              p2++;
          }
          // p1 = threshold

          int p3 = lowerY.size() - p1, p4 = upperY.size() - p2;
          M = min(M, max(p1, max(p2, max(p3, p4))));
      }


      /* Brute Force
        for (int yV : ySet) {
            l yLine = yV + 1;
            ll one = 0, two = 0, three = 0, four = 0;
            F0R(j, i) {
                if (cows[j].s < yLine) {
                    two++;
                }
            }
            three = i - two;
            FOR(j, i, N) {
                if (cows[j].s < yLine) {
                    one++;
                }
            }
            four = N - i - one;
            M = min(M, max(one, (max(two, max(three, four)))));
       }
      * /

    cout << M;
}

{% endhighlight %}


## Problem 3. Milk Pails

[Milk Pails](http://www.usaco.org/index.php?page=viewproblem2&cpid=620)  

Farmer John has received an order for exactly M units of milk (1≤M≤200) that he needs to fill right away. Unfortunately, his fancy milking machine has just become broken, and all he has are two milk pails of integer sizes X and Y (1≤X,Y≤100) with which he can measure milk. Both pails are initially empty. Using these two pails, he can perform up to K of the following types of operations (1≤K≤100):
- He can fill either pail completely to the top.   

- He can empty either pail.  

- He can pour the contents of one pail into the other, stopping when the former becomes empty or the latter becomes full (whichever of these happens first).  

Although FJ realizes he may not be able to end up with exactly M total units of milk in the two pails, please help him compute the minimum amount of error between M and the total amount of milk in the two pails. That is, please compute the minimum value of M−M′ such that FJ can construct M′ units of milk collectively between the two pails.  

INPUT FORMAT (file pails.in):  
The first, and only line of input, contains X, Y, K, and M.  
OUTPUT FORMAT (file pails.out):  
Output the smallest distance from M to an amount of milk FJ can produce.  
SAMPLE INPUT:  
```
14 50 2 32
```
SAMPLE OUTPUT:
```
18
```
In two steps FJ can be left with the following quanities in his pails  

(0, 0) = 0 units  
(14, 0) = 14 units  
(0, 50) = 50 units  
(0, 14) = 14 units  
(14, 36) = 50 units  
(14, 50) = 64 units  
The closest we can come to 32 units is 14 for a difference of 18. Note that it would require an extra step to pour out the first pail to end up with (0, 36).  

Problem credits: Brian Dean  
{% highlight C++ linenos %}
const int MaX = 1001;
int X, Y, K, M;
int closestValue = 0;
set<pair<pair<int, int>, int>> goneValues;

void simulate(int cX, int cY, int turn) {
    dbg(cX, cY, turn);
    if (goneValues.find(make_pair(make_pair(cX, cY), turn)) != goneValues.end()) {
        return;
    }
    goneValues.insert(make_pair(make_pair(cX, cY), turn));
    if (abs(M - (cX + cY)) < abs(M - closestValue)) {
        closestValue = cX + cY;
    }

    if (turn == K) {
        return;
    }

    if (cX == 0 && cY == 13 && turn == 1) {
        dbg("XXXXXXX");
    }

    // fill
    int oldX = cX, oldY = cY;
    if (cX != X) {
        cX = X;
        simulate(cX, cY, turn + 1);
        cX = oldX;
    }
    if (cY != Y) {
        cY = Y;
        simulate(cX, cY, turn + 1);
        cY = oldY;
    }
    // transfer
    int fill = min(cX, Y - cY);

    cX -= fill, cY += fill;
    simulate(cX, cY, turn + 1);
    cY = oldY, cX = oldX;

    fill = min(X - cX, cY);
    cX += fill, cY -= fill;
    simulate(cX, cY, turn + 1);
    cY = oldY, cX = oldX;

    // empty
    if (cX != 0) {
        cX = 0;
        simulate(cX, cY, turn + 1);
        cX = oldX;
    }

    if (cY != 0) {
        cY = 0;
        simulate(cX, cY, turn + 1);
        cY = oldY;
    }

}


int main() {
    setIO("pails");

    cin >> X >> Y >> K >> M;

    simulate(0, 0, 0);

    cout << abs(M - closestValue);
}
{% endhighlight %}
