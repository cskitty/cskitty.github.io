---
title: "USACO 2007 March Gold P3: Face The Right Way"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Graph
  - SPFA
---

# USACO 2007 March Gold P3: Face The Right Way

Description

Farmer John has arranged his N (1 ≤ N ≤ 5,000) cows in a row and many of them are facing forward, like good cows. Some of them are facing backward, though, and he needs them all to face forward to make his life perfect.

Fortunately, FJ recently bought an automatic cow turning machine. Since he purchased the discount model, it must be irrevocably preset to turn K (1 ≤ K ≤ N) cows at once, and it can only turn cows that are all standing next to each other in line. Each time the machine is used, it reverses the facing direction of a contiguous group of K cows in the line (one cannot use it on fewer than K cows, e.g., at the either end of the line of cows). Each cow remains in the same *location* as before, but ends up facing the *opposite direction*. A cow that starts out facing forward will be turned backward by the machine and vice-versa.

Because FJ must pick a single, never-changing value of K, please help him determine the minimum value of K that minimizes the number of operations required by the machine to make all the cows face forward. Also determine M, the minimum number of machine operations required to get all the cows facing forward using that value of K.

Input

Line 1: A single integer: N
Lines 2..N+1: Line i+1 contains a single character, F or B, indicating whether cow i is facing forward or backward.

Output

Line 1: Two space-separated integers: K and M


SAMPLE INPUT:
```
7
B
B
F
B
F
B
B
```
SAMPLE OUTPUT:  
```
3 3
```
Hint

For K = 3, the machine must be operated three times: turn cows (1,2,3), (3,4,5), and finally (5,6,7)

Explanation of the sample:

There are 4 cows. Cows #1 and #3 must be no more than 10 units apart, cows #2 and #4 must be no more than 20 units apart, and cows #2 and #3 dislike each other and must be no fewer than 3 units apart.

The best layout, in terms of coordinates on a number line, is to put cow #1 at 0, cow #2 at 7, cow #3 at 10, and cow #4 at 27.

Solution:

* Brute force test K size.
* For each K, the i-th cow is will be forced to turn around by a backward facing cow from [i-k+1, i].
* Maintaining a sum of all the turns made previously with a K cow window. Odd value of the sum means the last cow is flipped. 
* Sweep through all the cows, for a new i-th cow, sum = sum + f[i] - f[i-K+1]


{% highlight C++ linenos %}
#include<cstdio>
#include<cstring>
#define maxn 5005
using namespace std;

int N,dir[maxn],f[maxn];
char ch;

int calc(int K)
{
   memset(f,0,sizeof(f));
   int res=0,sum=0;
   for(int i=0;i+K<=N;i++)
   {
       if((dir[i]+sum)%2!=0)
       {
           res++;
           f[i]=1;
       }
       sum+=f[i];
       if(i-K+1>=0)
       {
           sum-=f[i-K+1];
       }
   }

   for(int i=N-K+1;i<N;i++)
   {
       if((dir[i]+sum)%2!=0)
       {
           return -1;
       }
       if(i-K+1>=0)
       {
           sum-=f[i-K+1];
       }
   }
   return res;
}

void solve()
{
   int K=1,M=N;
   for(int k=1;k<=N;k++)
   {
       int m=calc(k);
       if(m>=0 && M>m)
       {
           M=m;
           K=k;
       }
   }
   printf("%d %d\n",K,M);
}

int main()
{
   scanf("%d",&N);
   for(int i=0;i<N;i++)
   {
       getchar();
       scanf("%c",&ch);
       if(ch=='F') dir[i]=0;
       if(ch=='B') dir[i]=1;
   }
   solve();
   return 0;
}

{% endhighlight %}
