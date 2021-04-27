---
title: "USACO 2005 December Gold P1: Layout"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Graph
  - SPFA
---

# USACO 2005 December Gold P1: Layout

Description

Like everyone else, cows like to stand close to their friends when queuing for feed. FJ has N (2 <= N <= 1,000) cows numbered 1..N standing along a straight line waiting for feed. The cows are standing in the same order as they are numbered, and since they can be rather pushy, it is possible that two or more cows can line up at exactly the same location (that is, if we think of each cow as being located at some coordinate on a number line, then it is possible for two or more cows to share the same coordinate).

Some cows like each other and want to be within a certain distance of each other in line. Some really dislike each other and want to be separated by at least a certain distance. A list of ML (1 <= ML <= 10,000) constraints describes which cows like each other and the maximum distance by which they may be separated; a subsequent list of MD constraints (1 <= MD <= 10,000) tells which cows dislike each other and the minimum distance by which they must be separated.

Your job is to compute, if possible, the maximum possible distance between cow 1 and cow N that satisfies the distance constraints.

Input

Line 1: Three space-separated integers: N, ML, and MD.

Lines 2..ML+1: Each line contains three space-separated positive integers: A, B, and D, with 1 <= A < B <= N. Cows A and B must be at most D (1 <= D <= 1,000,000) apart.

Lines ML+2..ML+MD+1: Each line contains three space-separated positive integers: A, B, and D, with 1 <= A < B <= N. Cows A and B must be at least D (1 <= D <= 1,000,000) apart.
Output

Line 1: A single integer. If no line-up is possible, output -1. If cows 1 and N can be arbitrarily far apart, output -2. Otherwise output the greatest possible distance between cows 1 and N.


SAMPLE INPUT:
```
4 2 1
1 3 10
2 4 20
2 3 3
```
SAMPLE OUTPUT:  
```
27
```
Hint

Explanation of the sample:

There are 4 cows. Cows #1 and #3 must be no more than 10 units apart, cows #2 and #4 must be no more than 20 units apart, and cows #2 and #3 dislike each other and must be no fewer than 3 units apart.

The best layout, in terms of coordinates on a number line, is to put cow #1 at 0, cow #2 at 7, cow #3 at 10, and cow #4 at 27.

Solution:

1. Number arranged from 1-n, may be listed in d [i] <= d [i + 1], that is, d [i] -d [i + 1] <= 0, can be established i + 1 to i has a value of 0 to the edge, right  

2. ML given row A, B and N, the distances a and b can not exceed N, can be listed d [B] -d [A] <= D, that is d [B] -d [A] < = D, may be established with a value of a to B to D side, right  

3. given MD rows A, B and N, and b represents a distance of not less than N, can be listed d [B] -d [A]> = D, that is d [A] -d [B] <= -D, B to a may be established to have a value of the edge, right -D

Finally, to calculate the shortest path running side spfa from 1-n

Code: deposit with a star chart to finish before the chain overtime, but later found a small array of n plus side, plus pass by, pay attention to test cases to get rid of.


{% highlight python linenos %}
#include<vector>
#include<cstdio>
#include<iostream>
#include<cmath>
#include<queue>
#define numm ch-48
#define pd putchar(' ')
#define pn putchar('\n')
#define pb push_back
#define fi first
#define se second
#define fre1 freopen("1.txt","r",stdin)
#define fre2 freopen("2.txt","w",stdout)
using namespace std;
template <typename T>
void read(T &res) {
    bool flag=false;char ch;
    while(!isdigit(ch=getchar())) (ch=='-')&&(flag=true);
    for(res=numm;isdigit(ch=getchar());res=(res<<1)+(res<<3)+numm);
    flag&&(res=-res);
}

template <typename T>
void write(T x) {
    if(x<0) putchar('-'),x=-x;
    if(x>9) write(x/10);
    putchar(x%10+'0');
}

const int maxn=110;
const int N=1010;
const int M=10010;
const int inf=0x3f3f3f3f;
typedef long long ll;
struct edge {
    int to,w,net;
}edge[M+N];
int k,dis[N];
int sum[N],head[N],vis[N];
int que[M<<1];
void init(int n) {
    k=0;
    for(int i=1;i<=n;i++)
        head[i]=-1,vis[i]=false,sum[i]=0,dis[i]=inf;
}
void add(int u,int v,int w) {
    edge[++k].to=v;
    edge[k].w=w;
    edge[k].net=head[u];
    head[u]=k;
}


int spfa(int n) {
    ++sum[1],dis[1]=0;
    queue<int>que;
    que.push(1);
    while(!que.empty()) {
        int u=que.front();
        que.pop();
        vis[u]=false;
        for(int i=head[u];i!=-1;i=edge[i].net) {
            int v=edge[i].to;
            if(dis[v]>dis[u]+edge[i].w) {
                dis[v]=dis[u]+edge[i].w;
                if(!vis[v]) {
                    if(++sum[v]>n)
                        return -1;
                    vis[v]=true;
                    que.push(v);
                }
            }
        }
    }
    return dis[n]==inf ? -2 : dis[n];
}


int main()
{
    int n,ml,md;
    while(scanf("%d%d%d",&n,&ml,&md)!=EOF) {
        init(n);
        for(int i=1;i<=ml;i++) {    /// d[B]-d[A]<=D
            int a,b,d;
            read(a),read(b),read(d);
            add(a,b,d);
        }
        for(int i=1;i<=md;i++) {    /// d[A]-d[B]<=-D
            int a,b,d;
            read(a),read(b),read(d);
            add(b,a,-d);
        }
        for(int i=1;i<n;i++)    /// d[i]-d[i+1]<=0
            add(i+1,i,0);
        write(spfa(n));pn;
    }
    return 0;
}
{% endhighlight %}
