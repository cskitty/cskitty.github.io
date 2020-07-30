---
title: "Cellular Network"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Binary Search
---

#Binary search

## Cellular Network

[Cellular Network](https://codeforces.com/problemset/problem/702/C)  

You are given n points on the straight line — the positions ( x-coordinates) of the cities and m points on the same line — the positions ( x-coordinates) of the cellular towers. All towers work in the same way — they provide cellular network for all cities, which are located at the distance which is no more than r from this tower.  

Your task is to find minimal r that each city has been provided by cellular network, i.e. for each city there is at least one cellular tower at the distance which is no more than r.  

If r = 0 then a tower provides cellular network only for the point where it is located. One tower can provide cellular network for any number of cities, but all these cities must be at the distance which is no more than r from this tower.  

Input  
The first line contains two positive integers n and m (1 ≤ n, m ≤ 105) — the number of cities and the number of cellular towers.  

The second line contains a sequence of n integers a 1, a 2, ..., a n ( - 109 ≤ a i ≤ 109) — the coordinates of cities. It is allowed that there are any number of cities in the same point. All coordinates a i are given in non-decreasing order.  

The third line contains a sequence of m integers b 1, b 2, ..., b m ( - 109 ≤ b j ≤ 109) — the coordinates of cellular towers. It is allowed that there are any number of towers in the same point. All coordinates b j are given in non-decreasing order.  

Output
Print minimal r so that each city will be covered by cellular network.  

inputCopy
```
3 2
-2 2 4
-3 0
```
outputCopy
```
4
```


Explanation  

A search algorithm that splits the decision in half every time. If larger, "l" becomes the mid + 1, and if smaller, "r" becomes mid -1, changing the range to the smaller/larger halves.


{% highlight c++ linenos %}


bool possible(ll r, vector<ll> cities, vector<ll> towers) {
    int i = 0, j = 0;
    while (i < cities.size() && j < towers.size()) {
        dbg(i, cities[i]);
        dbg(j, towers[j]);
        if (abs(cities[i] - towers[j]) > r) {
            j++;
            // too small
            while (j < towers.size() && abs(cities[i] - towers[j]) > r) {
                j++;
            }
            if (j == towers.size()) {
                return false;
            }
        }
        i++;
    }
    return true;
}

int cellularNetwork(vector<ll> cities, vector<ll> towers) {
    int ans = 0;
    ll l = 0;
    ll r = max(cities.back(), towers.back()) - min(cities[0], towers[0]);
    while (l <= r) {
        ll mid = (r + l)/2;
        if (possible(mid, cities, towers)) {
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
    int n, m;
    re(n, m);
    vector<ll> cities(n);
    F0R(i, n) {
        re(cities[i]);
    }
    vector<ll> towers(m);
    F0R(i, m) {
        re(towers[i]);
    }

    pr(cellularNetwork(cities, towers));

}

{% endhighlight %}
