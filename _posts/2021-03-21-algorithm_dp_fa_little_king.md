---
title: "DP Finite Automata with Compression: Little King"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Finite Automata
---

## DP Finite Automata with Compression: Little King

In a n × n board, there are k Kings, kings can attack 8 surrounding neighbors, find the total number of solutions that make them unable to attack each other.

Input format

A line containing two integers n and k.

Output format

A total of one line, indicating the total number of solutions, if it cannot be placed, output 0.

data range

1 ≤ n ≤ 10
0 ≤ k ≤ n^2

Sample Input:
```
3 2
```
Sample Output:
```
16
```

### Solution

dp[i][j][k]:  i: current row, j: number of kings placed so far k:the placement of kings in row i
We use an integer k to represent row i's king's placement in row i.
A k-th bit 1 in k represent a king is planted in column k of row i.

If we know i-th row is a, i-1 row is b, then the valid placement of kings are  (a & b)==0 && check(a | b).

* a&b == 0 means there's no two kings on the same column in the two rows.
* check(a|b) means there's no two diagnal kings in the two rows

dp[i][j][a] += dp[i-1][j-c][compatible_list[a][b]]

{% highlight C++ linenos %}
#include<bits/stdc++.h>
using namespace std;

typedef long long  ll;
const int N=12,M=1<<10,K=120;  
int n,m;     

//valid state of row i, with no two kings next to each other
vector<int>state;    

//precalculated king's numbers for each row's number
int count_one[M];    

//a map: giving i-th row value as key, return a list of possible arrangements for i-1 row values
vector<int>compatible_list[M];

//i: current row, j: number of kings placed so far k:the placement of kings in row i
ll dp[N][K][M];   

/*check if there are two consecutive 1
bool check(int state)    
{
    for(int i=0;i<n;i++)
    {
        if((state>>i & 1) && (state>>i+1 & 1))    
        return false;
    }
    return true;
}*/

// an O(1) algorithm to check if there are two consecutive 1
inline bool check(int x)
{
    return !(x&x>>1);
}

//count number of bit 1 in state
int count(int state)
{
    int res=0;
    for(int i=0;i<n;i++)
    {
        if(state>>i & 1) res++;
    }
    return res;
}

int main()
{
    cin>>n>>m;

    //optimization step: pre-calculate state list and count_one
    //iterate all possible king arrangements (0 ... 1<<n)
    //add all valid placement to state list
    //count number of kings for each possible state and store in count_one
    for(int i=0;i<1<<n;i++)
    {
        if(check(i))
          state.push_back(i);

        count_one[i]=count(i);
    }

    //optimization step: pre-calculate all possible compatible pairs of row i and row i-1
    for(int i=0;i<state.size();i++)
    {
        for(int j=0;j<state.size();j++)
        {
            int a=state[i],b=state[j];

            if(check(a | b) && (a & b)==0)
              compatible_list[a].push_back(b);     
        }
    }

    dp[0][0][0]=1;
    for(int i=1;i<=n+1;i++)
    {
        for(int j=0;j<=m;j++)
        {
            for(int k=0; k<state.size(); k++)
            {
                int p=state[k];
                for(int z=0; z<compatible_list[p].size(); z++)   
                {
                     int h=compatible_list[p][z];
                     if(j>=count_one[p])
                     {
                        dp[i][j][p] += dp[i-1][j-count_one[p]][h];
                     }
                }
            }
        }
    }

    //the answer means placing no king in n+1 row, total placed king is m
    cout<< dp[n+1][m][0] << endl;
}
{% endhighlight %}
