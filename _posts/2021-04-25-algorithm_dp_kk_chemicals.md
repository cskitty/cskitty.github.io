---
title: "KK's Chemicals"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Combinatorics
---

## KK's Chemicals

Description

Our lovely KK has a difficult chemistry problem: There are N (1≤N≤100) bottles of chemicals in the laboratory, numbered from 0 to N-1. KK finds that for every bottle, there is a uniquely different bottle that will cause an explosion if the two are put together. KK needs to put the N bottles into K different boxes so that no explosions will happen. KK wants to know how many ways (modulo 1e9+7) he can do this.

Input
a number T in the first line (1≤T≤200), which indicates the number of testcases.
Each group of data has two rows. The first row has two integers N (1≤N≤100) and K (1≤K≤1000), indicating the number of chemicals and the number of boxes that need to be placed.
Next, in the second row, N integers c[i] (0≤c[i]≤N−1) where on row i the bottle that makes bottle i explode is bottle c[i].

Output
outputs an integer for each piece of data, which represents the result of the number of schemes modulo 1e9+7.

Sample Input  
```
3
3 3
1 2 0
4 3
1 2 0 0
3 2
1 2 0
```

Sample Output
```
6
12
0
```

Solution

According to the given relationship, build a graph. The problem is transformed into coloring this graph with k different colors, where the colors of adjacent points cannot be the same. Considering that the i-th bottle will explode if and only if it is put together with the c[i]th bottle, it can be seen that this graph is composed of several connected blocks, where the number of points in each connected block is equal to the number of edges. Each connected block has only one ring, and other nodes branching off some vertexes of the ring. Therefore, we only need to dfs to find the connected block and the ring in the connected block.

* For the nodes not in the ring, each point only needs to have a different color from its adjacent points, so there are k-1 coloring schemes for each one. We can calculate the number of nodes not in the ring and do (k-1)^(the number of nodes).

* For the coloring on a ring, consider a ring with i points, and choose a point j. If the points at both ends of j have different colors, then j itself has k-2 coloring schemes, and we can calculate the answer as (k-2) times (the number of ways to color in the ring with i-1 points). If the colors of the points at both ends of j are the same, then j itself has k-1 coloring schemes. We can calculate the answer then as (k-1) times (the coloring of the ring of i-2 points) because the points with the same color at both ends of j are regarded as one point (as once we get the color of one of them, the other has to be the same). dp[i] represents the number of coloring schemes of the ring with i points.

* The transition can be obtained from the above analysis: dp[i]= ((k-2) * dp[i-1]) +((k-1) * dp[i-2])


### Solution  

{% highlight C++ linenos %}
#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
#define mod 1000000007ll
#define maxn 111
ll dp1[maxn],dp2[maxn];
int T,n,k,vis[maxn],cnt,res;
vector<int>v[maxn];

void init()
{
    memset(vis,0,sizeof(vis));
    for(int i=0;i<n;i++)v[i].clear();
    dp1[1]=k,dp1[2]=k*(k-1),dp1[3]=k*(k-1)*(k-2);
    for(int i=4;i<=n;i++)dp1[i]=((k-2)*dp1[i-1]%mod+(k-1)*dp1[i-2]%mod)%mod;
    dp2[0]=1;
    for(int i=1;i<=n;i++)dp2[i]=(k-1)*dp2[i-1]%mod;
}

void dfs(int u,int fa,int deep)
{
    vis[u]=deep,cnt++;
    for(int i=0;i<v[u].size();i++)
        if(v[u][i]!=fa)
        {
            if(vis[v[u][i]]&&vis[v[u][i]]<deep)
                res=deep-vis[v[u][i]]+1;
            if(!vis[v[u][i]])dfs(v[u][i],u,deep+1);
        }
}

int main()
{
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&k);
        if(k==1)
        {
            printf("%d\n",n-1?0:1);
            continue;
        }
        init();
        for(int i=0;i<n;i++)
        {
            int c;
            scanf("%d",&c);
            v[i].push_back(c),v[c].push_back(i);
        }
        ll ans=1ll;
        for(int i=0;i<n;i++)
            if(!vis[i])
            {
                cnt=res=0;
                dfs(i,-1,1);
                if(!res)res=2;
                ans=ans*dp1[res]%mod*dp2[cnt-res]%mod;
            }
        printf("%I64d\n",ans);
    }
    return 0;
}

{% endhighlight %}
