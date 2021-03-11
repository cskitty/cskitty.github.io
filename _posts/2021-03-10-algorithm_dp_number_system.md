---
title: "Dynamic Programming: Number Combination"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Dynamic Programming: Number Combination

Given N Positive integer A1,A2, … ,AN, Select a subset of numbers from them so that their sum is M, How many options are there?

Input format
The first line contains two integers N with M.

The second line contains N Integers, representing A1,A2, … ,AN.

Output format
Contains an integer, indicating the number of options.

data range
1 ≤ N≤ 100,
1 ≤ M≤ 10000,
1 ≤Ai≤ 1000

Sample Input:
```
4 4
1 1 2 2
```
Sample Output:
```
3
```

## Solution  

{% highlight C++ linenos %}
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std ;

const int N = 100010 ;

// number of ways to get N
int dp[N] ;
int n,m ;

int main(){
    cin >> n >> m ;

    // nothing is chosen, there's 1 way
    dp[0] = 1 ;

    for(int i=1;i<=n;i++){
        int a ;
        cin >> a ;

        /* solution using 2D dp
        for(int j=m;j>=0;j--){
          if (j>a)
            dp[i][j] = dp[i-1][j] + dp[i-1][j-a] ;
          else
            dp[i][j] = dp[i-1][j];        
        }
        */

        for(int j=m;j>=a;j--){
            dp[j] = dp[j] + dp[j-a] ;
        }
    }

    cout << f[m] << endl ;

    return 0 ;
}
{% endhighlight %}
