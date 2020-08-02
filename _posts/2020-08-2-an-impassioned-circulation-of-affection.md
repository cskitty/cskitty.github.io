---
title: "An Impassioned Circulation of Affection"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Two Pointers
  - Dynamic Programming
---

# C. An Impassed Circulation of Affection

[An Impassed Circulation of Affection](https://codeforces.com/contest/814/problem/C)

Nadeko's birthday is approaching! As she decorated the room for the party, a long garland of Dianthus-shaped paper pieces was placed on a prominent part of the wall. Brother Koyomi will like it!  

Still unsatisfied with the garland, Nadeko decided to polish it again. The garland has n pieces numbered from 1 to n from left to right, and the i-th piece has a colour s i, denoted by a lowercase English letter. Nadeko will repaint at most m of the pieces to give each of them an arbitrary new colour (still denoted by a lowercase English letter). After this work, she finds out all subsegments of the garland containing pieces of only colour c — Brother Koyomi's favourite one, and takes the length of the longest among them to be the Koyomity of the garland.  

For instance, let's say the garland is represented by "kooomo", and Brother Koyomi's favourite colour is "o". Among all subsegments containing pieces of "o" only, "ooo" is the longest, with a length of 3. Thus the Koyomity of this garland equals 3.  

But problem arises as Nadeko is unsure about Brother Koyomi's favourite colour, and has swaying ideas on the amount of work to do. She has q plans on this, each of which can be expressed as a pair of an integer m i and a lowercase letter c i, meanings of which are explained above. You are to find out the maximum Koyomity achievable after repainting the garland according to each plan.  

Input  
The first line of input contains a positive integer n (1 ≤ n ≤ 1 500) — the length of the garland.  

The second line contains n lowercase English letters s 1 s 2... s n as a string — the initial colours of paper pieces on the garland.  

The third line contains a positive integer q (1 ≤ q ≤ 200 000) — the number of plans Nadeko has.  

The next q lines describe one plan each: the i-th among them contains an integer m i (1 ≤ m i ≤ n) — the maximum amount of pieces to repaint, followed by a space, then by a lowercase English letter c i — Koyomi's possible favourite colour.  

Output  
Output q lines: for each work plan, output one line containing an integer — the largest Koyomity achievable after repainting the garland according to it.  

Examples  
Input  
```
6
koyomi
3
1 o
4 o
4 m
```
Output  
```
3
6
5
```
Input  
```
15
yamatonadeshiko
10
1 a
2 a
3 a
4 a
5 a
1 b
2 b
3 b
4 b
5 b
```
Output  
```
3
4
5
7
8
1
2
3
4
5
```
Input  
```
10
aaaaaaaaaa
2
10 b
10 z
```
Output
```
10
10
```  

## Two Pointers

We can use two pointers to denote the start and the end of the largest Koyomity. Using the idea of a sliding window, we keep a "count" (denoted by changed, current amount allowed to move) and a maximum count (greatest). If the right pointer is not favorite char, or the right pointer value needs to be replaced, we subtract one from changed. However, when we are stuck (aka changed is < 0, or the right cannot move any longer) we need to move the left pointer. Thus, if the left side was replaced (or was not originally favoriteChar), we add one to change and increment the left pointer.

{% highlight c++ linenos %}

int main() {
    int x;
    re(x);
    vector<char> garland;
    F0R(i, x) {
        char c;
        re(c);
        garland.push_back(c);
    }

    int cases;
    re(cases);
    F0R(currentCase, cases) {
        int changed;
        char favoriteChar;
        re(changed, favoriteChar);

        // greatest poss. consec = amount changed
        int greatest = changed;

        // code
        int r = 0;
        int l = 0;
        while (r < garland.size()) {
            dbg(l, r, changed);
            if (changed >= 0) {
                if (garland[r] != favoriteChar) {
                    changed--;
                }
                r++;
            }
            if (changed < 0) {
                if (garland[l] != favoriteChar) {
                    changed++;
                }
                l++;
            }

            greatest = max(greatest, r-l);
        }

        cout << greatest << "\n";
    }
}

{% endhighlight %}

## Dynamic Programming

The dynamic programming method simply finds the maximum value for the garland, and has two parameters - the letter (or character) and the amount replaceable. For all test cases, we use the same DP array to find the max value.

{% highlight c++ linenos %}
 
int main() {
    int x;
    re(x);
    vector<char> garland;
    F0R(i, x) {
        char c;
        re(c);
        garland.push_back(c);
    }

    vector<vector<int>> dp(26, vector<int>(garland.size() + 1));

    F0R(letter, 26) {
        F0R(l, garland.size()) {
            int replaced = 0;
            FOR(r, l, garland.size()) {
                if (garland[r] != letter + 'a') {
                    replaced++;
                }
                assert(letter < 26);
                assert(replaced <= garland.size());
                dp[letter][replaced] = max(dp[letter][replaced], r - l + 1);
                dp[letter][replaced] = max(dp[letter][replaced], replaced);
            }
        }
        // max for letter
        FOR(k, 1, garland.size() + 1) {
            dp[letter][k] = max(dp[letter][k - 1], dp[letter][k]);
        }
    }

    int queries;
    re(queries);

    F0R(q, queries) {
        int changes;
        char letter;
        re(changes, letter);
        cout << dp[letter - 'a'][changes] << "\n";
    }

}
{% endhighlight %}
