---
title: "Group Knapsack Problem"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Knapsack
---

## Group Knapsack Problem

Have N Group items and a capacity are V Backpack.

There are several items in each group, and only one item in the same group can be selected.
The volume of each item isvi j, The value is wi j,among them i Is the group number,j Is the number in the group.

Solve which items are loaded into the backpack, so that the total volume of the items does not exceed the capacity of the backpack, and the total value is the largest.

Output the maximum value.

Input format
There are two integers in the first line N, V, Separated by spaces, respectively indicate the number of item groups and the capacity of the backpack.

Next there is N Group data:

There is an integer in the first row of each group of data Si, Said the first i The number of items in each item group;  
Next to each set of data Si Rows, each row has two integers vi j,wi j, Separated by spaces, indicating the first i Item group j The volume and value of each item;  

Output format
Output an integer that represents the maximum value.

data range
0 < N, V≤ 100
0 <Si≤ 100
0 <vi j,wi j≤ 100

Sample Input:
```
3 5
2
1 2
2 4
1
3 4
1
4 5
```
Sample Output:
```
8
```

### Solution




{% highlight C++ linenos %}
#include<bits/stdc++.h>
using namespace std;

const int N=110;

//dp[i][j]: select from first i groups, volume equal or smaller than j   
int dp[N][N];  

int v[N][N],w[N][N];

//item number for group i
int s[N];    

int n,m,k;

int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>s[i];
        for(int j=0;j<s[i];j++){
            cin>>v[i][j]>>w[i][j];   
        }
    }

    for(int i=1;i<=n;i++){
        for(int j=0;j<=m;j++){
            //do not pick any item from group i
            dp[i][j]=dp[i-1][j];   

            //pick the k-th item from group i
            for(int k=0;k<s[i]; k++){
                if(j>=v[i][k])     
                  dp[i][j]=max(f[i][j],dp[i-1][j-v[i][k]]+w[i][k]);  
            }
        }
    }
    cout<<dp[n][m]<<endl;
}
{% endhighlight %}
