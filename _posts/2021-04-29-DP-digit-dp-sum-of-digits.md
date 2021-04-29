---
title: "Sum of Digits"
categories:
  - USACO
tags:
  - Algorithms
  - DP on digits
---

# Sum of digits

Description

Given X and Y, output the sum of digits for all numbers from X to Y inclusive.


Solution

Using DP on digits, from MSB to LSB.


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

long long dp[22];

// use dp to calculate sum of digit all size i numbers : 00...00 - 99..99
void init() {
    dp[0] = 0;

    for (int i = 1; i < 21; i++) {
        dp[i] = 10 * dp[i - 1] + 45 * pow(10, i-1);
    }
}

int rundp(int n) {
    if (!n) return 0;

    vector<int> nums;
    while (n) {
        nums.push_back(n % 10);
        n /= 10;
    }

    long long res = 0, last = 0;
    // handling i-th position, from MSB to LSB
    for (int i = nums.size() - 1; i >= 0; i--) {
        int digit = nums[i];
        if (digit) {
            // j is current digit executing
            for (int j = 0; j < digit; j++) {
                // left branch
                // for each value of j, we have last.j.00..0 - last.j.99..9
                // the sum of digit for last.j.00..00 == (last + j) * pow(10,i)
                res += (last + j) * pow(10, i)  + dp[i];
            }
        }
        last += digit;
    }

    // adding the last digit
    res += last + nums[0];
    return res;
}

int main() {
    long long a = 5675, b = 9864;

    init();

    int acount = rundp(a - 1);
    int bcount = rundp(b);

    cout << bcount - acount;
}
{% endhighlight %}
