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
