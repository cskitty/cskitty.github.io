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
