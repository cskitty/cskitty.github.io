---
title: "Dynamic Programming: Chrous "
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Dynamic Programming: Chrous

N students stand in a row, and the music teacher will invite (NK) students out of them to make the remaining K students line up in a chorus formation.     

The chorus formation refers to the formation: Suppose the K students are numbered 1, 2..., K from left to right, and their heights are respectively T1,T2, … ,TK, Then their height satisfies T1< … < Ti > Ti + 1 > … > TK( 1 ≤ i ≤ K).     

Your task is to know the heights of all N classmates, and calculate at least a few classmates to get out of the queue, so that the remaining classmates can be formed into a chorus formation.

Input format
The first line of input is an integer N, which represents the total number of students.

There are n integers in the second line, separated by spaces, and the i-th integer Ti is the height (cm) of the i-th student.

Output format
The output consists of one line, this line only contains an integer, that is, at least a few students are required to be listed.

data range
2 ≤ N ≤ 100,
130 ≤ Ti ≤ 230

Sample Input:
```
8
186 186 150 200 160 130 197 220
```
Sample Output:
```
4
```

## Solution  

Assume that the center of the optimal solution is the first ii Individual, then T1,T2, … ,Ti must be based on Ti the longest ascending subsequence at the end.

Similarly,TK, TK− 1, … ,Ti Must also be Ti the longest ascending subsequence at the end.

So you can preprocess it first O(N^2):

The length of the longest ascending subsequence from front to back ending with each point f[i];
The length of the longest ascending subsequence ending at each point from back to front g[i];

Then use a for loop O(N) to find the best Ti location.

{% highlight C++ linenos %}
#include <bits/std++.h>
using namespace std;

const int N = 110;

int n;
int h[N];
int f[N], g[N];

int main()
{
    cin >> n;
    for (int i = 1; i <= n; i ++ )
      cin >> h[i];

    for (int i = 1; i <= n; i ++ ){
        f[i] = 1;
        for (int j = 1; j < i; j ++ )
            if (h[j] < h[i])
                f[i] = max(f[i], f[j] + 1);
    }

    for (int i = n; i; i -- ) {
        g[i] = 1;
        for (int j = n; j > i; j -- )
            if (h[j] < h[i])
                g[i] = max(g[i], g[j] + 1);
    }

    int res = 0;
    for (int i = 1; i <= n; i ++ )
       res = max(res, f[i] + g[i] - 1);

    cout << n - res;
    return 0;
}

{% endhighlight %}
