---
title: "Dynamic Programming: Longest Common Subsequence"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Longest Common Subsequence

[Leetcode 1143](https://leetcode.com/problems/longest-common-subsequence/)


LCS Problem Statement: Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.


If there is no common subsequence, return 0.  

Input sample:
```
text1 = "abcde", text2 = "ace"
```
Sample output:
```
3
```

## Solution:

State representation:

* dp[i][j] is the length of LCS of text1[0 ~ i-1] and text2[0 ~ j-1]

State calculation:

* text1[i - 1] == text2[j - 1] : add the value of text1[i - 1] to the end of the LCS, as both strings have this value with dp[i - 1][j - 1] + 1
* text1[i - 1] != text2[j - 1] : don't include it in the LCS, look at dp[i - 1][j] and dp[i][j - 1]

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string text1, string text2) {

    vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1));

    // dp[i][j] = length of LCS of text1[0 ~ i-1] and text2[0 ~ j-1]
    for (int i = 1; i < text1.size() + 1; i++) {
        for (int j = 1; j < text2.size() + 1; j++) {
            int n = 0;

            if (text1[i - 1] == text2[j - 1]) {
                n = max(n, dp[i - 1][j - 1] + 1);
            }
            else {
                n = max(n, dp[i - 1][j]);
                n = max(n, dp[i][j - 1]);
            }

            dp[i][j] = n;
        }
    }

    return dp[text1.size()][text2.size()];
}

int main() {
    cout << longestCommonSubsequence("abc", "abc");

}
{% endhighlight %}
