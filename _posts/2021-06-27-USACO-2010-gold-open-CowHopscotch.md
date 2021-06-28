---
title: USACO 2010 Gold Cow Hopscotch
tags:
  - USACO Platinum
---

## Cow Hopscotch

The cows have reverted to their childhood and are playing a game similar
to human hopscotch. Their hopscotch game features a line of N (3 <=
N <= 250,000) squares conveniently labeled 1..N that are chalked onto
the grass.

Like any good game, this version of hopscotch has prizes!  Square i is
labeled with some integer monetary value V_i (-2,000,000,000 <=
V_i <= 2,000,000,000). The cows play the game to see who can earn the
most money.

The rules are fairly simple:

* A cow starts at square "0" (located just before square 1; it
      has no monetary value).

* She then executes a potentially empty sequence of jumps toward
square N. Each square she lands on can be a maximum of K (2
<= K <= N) squares from its predecessor square (i.e., from
square 1, she can jump outbound to squares 2 or 3 if K==2).

* Whenever she wishes, the cow turns around and jumps back
towards square 0, stopping when she arrives there. In addition
to the restrictions above (including the K limit), two
additional restrictions apply:

* She is not allowed to land on any square she touched on her
outbound trip (except square 0, of course).

* Except for square 0, the squares she lands on during the
return trip must directly precede squares she landed on
during the outbound trip (though she might make some larger
leaps that skip potential return squares altogether).

She earns an amount of money equal to the sum of the monetary values
of all the squares she jumped on. Find the largest amount of cash
a cow can earn.

By way of example, consider this six-box cow-hopscotch course where
K has the value 3:

```
Square Num:    0      1      2      3      4      5      6
             +---+  +---+  +---+  +---+  +---+  +---+  +---+
             |///|--|   |--|   |--|   |--|   |--|   |--|   |
             +---+  +---+  +---+  +---+  +---+  +---+  +---+
     Value:    -      0      1      2     -3      4      5
```

One (optimal) sequence Bessie could jump (shown with respective
bracketed monetary values) is: 1[0], 3[2], 6[5], 5[4], 2[1], 0[0]
would yield a monetary total of 0+2+5+4+1+0=12.

If Bessie jumped a sequence beginning with 0, 1, 2, 3, 4, ... then
she would be unable to return since she could not legally jump back
to an untouched square.

PROBLEM NAME: hop

INPUT FORMAT:

* Line 1: Two space separated integers: N and K

* Lines 2..N+1: Line i+1 contains a single integer: V_i

SAMPLE INPUT:
```
6 3
0
1
2
-3
4
5
```
OUTPUT FORMAT:

* Line 1: A single line with a single integer that is the maximum
        amount of money a cow can earn

SAMPLE OUTPUT:
```
12
```

# Solution

DP:  
dp[i] = dp[j] + V[i] + V[i-1] + PrefixSum[i-2] - PrefixSum[j], for all i-1-k <= j < i-1

Optimization to O(N):  
Using max queue and put all j related values (dp[j] - PrefixSum[j]) to the max queue.

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<long long> dp;
vector<long long> V;

struct maxqueue {
    deque<pair<long long, int>> dq;

    void insert_back(pair<long long, int> val) {
        while (! dq.empty() && dq.back().first <= val.first) {
            dq.pop_back();
        }
        dq.push_back(val);
    }
    void delete_front(int ind) {
        while (! dq.empty() && dq.front().second < ind) {
            dq.pop_front();
        }
    }
    long long get_max() {
        if (! dq.empty()) {
            return dq.front().first;
        }
        else {
            // change this
            return -1;
        }
    }
};

int main() {
    // sliding window of previous dp states
    // go from i to j?
    // ifstream cin("hop.in");

    cin >> N >> K;
    V.resize(N + 1);
    dp.resize(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> V[i];
    }

    vector<long long> nums(N + 1);
    for (int i = 1; i <= N; i++) {
        nums[i] = max(nums[i - 1], nums[i - 1] + V[i]);
    }

    // dp[j] = best solution for first j squares

    dp[1] = max(dp[0], V[1]);
    maxqueue maxQ;

    // go from i to j
    for (int i = 2; i <= N; i++) {
        // update dq
        maxQ.delete_front(i - K);
        // can only be i - 2, as i - 1 is used in dp[i]
        maxQ.insert_back({dp[i - 2] - nums[i - 2], i - 2});

        dp[i] = maxQ.get_max() + V[i] + V[i - 1] + nums[i - 2];
    }

    long long ans = 0;
    for (int i = 1; i <= N; i++) {
        ans = max(ans, dp[i] + nums[min(i - 1 + K, N)] - nums[i]);
    }
    cout << ans;
}

{% endhighlight %}  
