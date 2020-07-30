---
title: "Binary Search"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Binary Search
---

#Binary search

## B. Books

[Books](https://codeforces.com/problemset/problem/279/B)

When Valera has got some free time, he goes to the library to read some books. Today he's got t free minutes to read. That's why Valera took n books in the library and for each book he estimated the time he is going to need to read it. Let's number the books by integers from 1 to n. Valera needs a i minutes to read the i-th book.  

Valera decided to choose an arbitrary book with number i and read the books one by one, starting from this book. In other words, he will first read book number i, then book number i + 1, then book number i + 2 and so on. He continues the process until he either runs out of the free time or finishes reading the n-th book. Valera reads each book up to the end, that is, he doesn't start reading the book if he doesn't have enough free time to finish reading it.  

Print the maximum number of books Valera can read.  

Input  
The first line contains two integers n and t (1 ≤ n ≤ 105; 1 ≤ t ≤ 109) — the number of books and the number of free minutes Valera's got. The second line contains a sequence of n integers a 1, a 2, ..., a n (1 ≤ a i ≤ 104), where number a i shows the number of minutes that the boy needs to read the i-th book.  

Output  
Print a single integer — the maximum number of books Valera can read.  

Examples  
Input  
```
4 5
3 1 2 1
```
Output  
```
3
```
  
{% highlight c++ linenos %}
int binarySearch(int i, int l, int r, vector<int> arr, int maxTime) {
    while(l<r)
    {
        int mid=(l+r)>>1;
        mid++;
        dbg(l, r, mid);
        if(arr[mid] - arr[i] <= maxTime) {
            l = mid;
        }
        else r=mid-1;
    }
    return l;
}


int longestSequence(vector<int> prefixSum, int maxBooks, int maxTime) {
    int maxCount = 0;
    dbg(maxCount);
    for (int i = 0; i < maxBooks; i++) {
        int j = binarySearch(i, i, maxBooks, prefixSum, maxTime);
        if (j != -1) {
            maxCount = max(j - i, maxCount);
            //dbg(j, maxCount);
        }
        dbg(i, j, maxCount);
    }
    return maxCount;
}

int main() {
    int n, t;
    re(n, t);

    vector<int> minutes(n,0);
    vector<int> prefixSum(n + 1,0);

    F0R(i, n) {
        re(minutes[i]);
        prefixSum[i + 1] = prefixSum[i] + minutes[i];
    }
    dbg(prefixSum);
    int x = longestSequence(prefixSum, n, t);
    pr(x);
}
{% endhighlight %}


## C. Cellular Network

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

Input
```
3 2
-2 2 4
-3 0
```
Output
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
