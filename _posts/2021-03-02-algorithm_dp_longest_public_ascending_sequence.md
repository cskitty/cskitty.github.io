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

* f[i][j] represents the length of LCIS in a[1 ~ i] and b[1 ~ j] ending with b[j]

State calculation (corresponding to set division):

First, according to whether the common sub-sequence is included a[i], f[i][j]the represented set is divided into two mutually exclusive and complimentary sub-sets:

a) subsets of CIS not including a[i], the maximum value is f[i - 1][j];  
b) subsets of CIS including a[i], this can be further divided into mutually exclusive and complimentary sub-sets, depending on the second to last number of CIS:  
* CIS subset only contain one element in b[j], length is 1
* second to last number of CIS subset equals to b[1], the maximum length is f[i - 1][1] + 1;
* second to last number of CIS subset equals to b[j - 1]the subsequence is the set, and the maximum length is f[i - 1][j - 1] + 1;

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

Then we find that what we get for each iteration maxv is the maximum value a[i] > b[k] of f[i - 1][k] + 1 the prefix that is satisfied .

Therefore, you can directly maxv refer to the outside of the first layer of loops to reduce repeated calculations. At this time, only two loops are left.

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
            if (a[i] == b[j]) f[i][j] = max(f[i][j], maxv);
            if (a[i] > b[j]) maxv = max(maxv, f[i - 1][j] + 1);
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; ++ i) ans = max(f[n][i], ans);

    cout << ans << "\n";
    return 0;
}

{% endhighlight %}
