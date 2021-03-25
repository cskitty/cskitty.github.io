---
title: "Interval DP: Scored Binary Tree"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Interval DP
---

## Interval DP: Bonus Binary Tree

Design an in-order traversal of a binary tree. Nodes are numbers (1 , 2 , 3 , … , n), where the number 1 , 2 , 3 , … , n is the node id.
Each node has a score (positive integer) and each subtree has a bonus.  The subtree bonus calculation is based on bonus of its subtrees and the score of the node itself:       
bonus for the left subtree * bonus for the right subtree + the score of the root of the subtree 

If a subtree is empty, then the bonus is 1,  all the leaf nodes' bonus is the score of the leaf node.

Try to find a tree that gives an in-order traversal as (1 , 2 , 3 , … , n) and the binary tree with the highest bonus.

Request output: 

(1) The highest points for tree 
(2) Preorder traversal of tree

Input format
First row: an integer n, Is the number of nodes. 
Second row: an integer separated by a space is the score of each node (0 <fraction< 100).  

Output format
First row:  an integer, which is the highest bonus point (the result will not exceed the intrange).     
Second row: an integer separated by a space which is the print out of pre-order traversal of the tree. If there are multiple schemes, the scheme with the smallest lexicographic order is output.

data range
n < 30

Sample Input:
```
5
5 7 1 2 10
```
Sample Output:
```
145
3 1 2 4 5
```

### Solution

{% highlight C++ linenos %}
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, int> PII;

const int N = 50;

int n;
int w[N];
unsigned dp[N][N];
int root[N][N];

//print out the in-order traversal of the binary tree
void dfs(int l, int r)
{
    if (l > r) return;

    int k = root[l][r];
    printf("%d ", k);
    dfs(l, k - 1);
    dfs(k + 1, r);
}

int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++ ) scanf("%d", &w[i]);

    //out loop: length of the binary tree range
    for (int len = 1; len <= n; len ++ )
        //inner loop: left index of the binary tree
        for (int l = 1; l + len - 1 <= n; l ++ )
        {
            //right index
            int r = l + len - 1;

            // try different possible root of the binary tree
            for (int k = l; k <= r; k ++ )
            {
                int left = k == l ? 1 : dp[l][k - 1];
                int right = k == r ? 1 : dp[k + 1][r];

                int score = left * right + w[k];

                if (l == r) score = w[k];

                if (dp[l][r] < score)
                {
                    dp[l][r] = score;
                    root[l][r] = k;
                }
            }
        }

    printf("%d\n", dp[1][n]);
    dfs(1, n);
    puts("");

    return 0;
}

{% endhighlight %}
