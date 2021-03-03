---
title: "Dynmamic Programming: LCIS (Longest Common Increasing Sequence)"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Dynmamic Programming: LCIS (Longest Common Increasing Sequence)

For two sequences A and B, find length of the longest common increasing subsequence.

The length of sequence A and B does not exceed 3000.

Input format
The first line contains an integer N, which represents the length of the sequence A and B.

The second row contains N integers, representing the sequence A.

The third row contains N integers, representing the sequence B.

Output format
Output an integer that represents the length of the longest common increasing sequence.

data range
1 ≤ N≤ 3000, None of the numbers in the sequence exceed231− 1
Input sample:

```
4
2 2 1 3
2 1 2 3
```
Sample output:
```
2
```


State representation:

* f[i][j] is the length of LCIS in a[1 ~ i] and b[1 ~ j] ending with b[j]

State calculation:

We can first loop through i and j to get a matching pair of a[i] and b[j].
Once we have found them, we then need to find the LCIS ending with the value b[j]. We can do this by looping through all previous DP values of numbers with an array b index less than j, denoted as "k". If the value at b[k] is less than the value of b[j], we can assume b[j] can be added to the end of the sequence and creating a new LCIS of length f[i - 1][k] + 1 (the longest possible length ending with b[k] and adding 1 for b[j]).  

If implemented directly according to the above ideas, a three-fold loop is required:

```
for (int i = 1; i <= n; i ++ )
{
    for (int j = 1; j <= n; j ++ )
    {
        f[i][j] = f[i - 1][j];
        if (a[i] == b[j])
        {
            int maxv = 1;
            for (int k = 1; k < j; k ++ )
                if (a[i] > b[k])
                    maxv = max(maxv, f[i - 1][k] + 1);
            f[i][j] = max(f[i][j], maxv);
        }
    }
}
```

Optimization:   

We can change our program from three for loops (O(N^3)) to two (O(N^2)) by realizing that we don't need to visit all of the previous values "k" to get the maxv. Because the implementation involved is DP, for every new value of j we can reuse the previously calculated maxv value instead of looping through all previous values again in k.

The final answer enumeration subsequence ends with the maximum value.


{% highlight C++ linenos %}
#include <bits/stdc++.h>

using namespace std;

const int N = 3005;

int n;
int a[N], b[N];
int f[N][N];
int g[N][N];  

int main() {
    cin >> n;
    for (int i = 1; i <= n; ++ i) cin >> a[i];
    for (int j = 1; j <= n; ++ j) cin >> b[j];


    for (int i = 1; i <= n; ++ i) {
        int maxv = 1;

        for (int j = 1; j <= n; ++ j) {  
            f[i][j] = f[i - 1][j];
            if (a[i] == b[j])
              f[i][j] = max(f[i][j], maxv);

            if (a[i] > b[j])
              maxv = max(maxv, f[i - 1][j] + 1);
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++ i) ans = max(f[n][i], ans);

    cout << ans << "\n";
    return 0;
}

{% endhighlight %}
