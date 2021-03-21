---
title: "DP Finite Automata with Compression: Corn Yard"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Finite Automata
---

## DP Finite Automata with Compression: Corn Yard

Farmer John’s land is owned by M× N Composed of a small square, and now he wants to grow corn in the land.

Unfortunately, part of the land is sterile and cannot be planted.

Moreover, adjacent land cannot be planted with corn at the same time, which means that there is no common edge between all the squares where corn is planted.

Now given the size of the land, please find out how many planting methods there are.  

Planting nothing on the land is a method.  

Input format

First 1 Line contains two integers M with N.  

First 2.. M+ 1 Rows: each row contains N Integers 0 or 1, Used to describe the condition of the entire land,1 It means that the land is fertile,0 Indicates that the land is sterile.  

Output format
Output total planting methods in the modulo 10^8.

data range
1 ≤ M, N≤ 12

Sample Input:
```
2 3
1 1 1
0 1 0
```
Sample Output:
```
9
```

### Solution

We use an integer j to represent row i's corn plant. A k-th bit 1 in j represent a corn is planted in column k of row i.
dp[i][j]: The corn plating methods for up to i-th row and the status of the i-th row is j.  



{% highlight C++ linenos %}
#include<bits/stdc++.h>
#include <bits/stdc++.h>
using namespace std;
const int P=1e9;

int a[15][15],f[15],h[5010],dp[15][5010],ans;

int main(){
    int n,m;
    cin>>n>>m;

    //input
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++){
            cin>>a[i][j];
            f[i]=(f[i]<<1)+a[i][j];
        }

    dp[0][0]=1;

    //for each i, check if there's 2 consecutive bit 1 and set flag
    for(int i=0;i<(1<<m);i++)
      h[i]=((i&(i<<1))==0)&&((i&(i>>1))==0);

    //row
    for(int i=1;i<=n;i++)
        //all possible value of row[i]
        for(int j=0;j<(1<<m);j++)
            //h[j]: no two consecutive 1
            //f[i]&j == j means all bits in j have bit 1 in f[j] (ok to plant)
            if(h[j]&&((f[i]&j)==j))
                for(int k=0;k<(1<<m);k++)
                    if((j&k)==0)dp[i][j]=(dp[i][j]+dp[i-1][k])%P;

    for(int i=0;i<(1<<m);i++)
      ans=(ans+dp[n][i])%P;

    cout<<ans;
    return 0;
}
{% endhighlight %}
