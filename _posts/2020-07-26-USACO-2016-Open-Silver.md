---
title: "USACO 2016 Open Silver"
categories:
  - USACO
tags:
  - Algorithms
  - C++
  - USACO
  - Two Pointers
  - Dynamic Programming
---

# USACO 2016 Open Silver

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
