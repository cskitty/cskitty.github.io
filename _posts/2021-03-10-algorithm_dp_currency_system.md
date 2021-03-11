---
title: "Dynamic Programming: Currency System"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Dynamic Programming: Currency System

There are n currencies of different denominations in the country of netizens. The denomination of the i-th currency is a[i]. You can assume that there are infinitely many currencies for each currency.

For convenience, we denote the currency system with n currency types and a denomination array a[1..n] as (n,a). 

In a perfect currency system, the amount x of each non-negative integer should be able to be expressed, that is, for each non-negative integer x, there are n non-negative integers t[i] satisfying a[i]× t The sum of [i] is x.

However, in the country of netizens, the currency system may be imperfect, that is, there may be an amount x that cannot be expressed by the currency system.

For example, in the currency system n=3, a=[2,5,9], the amount 1,3 cannot be expressed. 

The two currency systems (n,a) and (m,b) are equivalent, if and only if for any non-negative integer x, it can either be represented by the two currency systems or cannot be represented by any of them Out. 

Now netizens plan to simplify the currency system.

They hope to find a currency system (m,b), satisfying that (m,b) is equivalent to the original currency system (n,a), and m is as small as possible.

They want you to assist in this difficult task: find the smallest m.


Input format
The first line of the input file contains an integer T, which represents the number of groups of data.

Next, the T group data are given in the following format. 

The first row of each group of data contains a positive integer n.

The next line contains n positive integers a[i] separated by spaces.  

Output format
There are T lines in the output file. For each group of data, a positive integer is output on one line, which represents the smallest m in all currency systems (m, b) equivalent to (n, a).


Sample Input:
```
2
4
3 19 10 6
5
11 29 13 19 17
```
Sample Output:
```
2
5
```

## Solution  

After a little thought, you can find that if and only if the denomination of a currency can be represented by other currencies (linear combination) in the system,
the currency has no effect on this denomination that the system can represent.

In other words, there is no need for this currency to exist. , So removing this type of currency from the system will result in an equivalent minimum amount of currency system.

You can use dp to find the number of combinations that can represent the denomination. If the number of combinations for a currency is unique (that is, it can only be represented by yourself), the currency cannot be omitted, otherwise it can be omitted, and the final count is enough.


{% highlight C++ linenos %}
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int n,k,a[105],f[25005],ans,t;

int main()
{
    cin>>t;
    while(t--)
    {
        cin>>n;
        memset(a,0,sizeof(a));
        memset(f,0,sizeof(f));

        f[0]=1;
        k=0;
        for(int i=1;i<=n;i++)
        {
            cin>>a[i];
            k=max(k,a[i]);
        }

        for(int i=1;i<=n;i++)
        {
            for(int j=a[i];j<=k;j++)
            {
                f[j]=f[j-a[i]]+f[j];
            }
        }

        int ans=0;
        for(int i=1;i<=n;i++)
        {
            if(f[a[i]]==1)ans++;
        }
        cout<<ans<<endl;
    }
    return 0;
}

{% endhighlight %}
