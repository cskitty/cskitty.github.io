---
title: "DP Finite Automata with Compression: DNA Repairing"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Finite Automata
---

## DP Finite Automata with Compression: DNA Repairing

Biologists finally invented DNA repair technology, which can repair DNA fragments containing various genetic diseases.

For the sake of simplicity, DNA is regarded as a string consisting of'A','G','C', and'T'.

The repair technique is to eliminate the disease-causing fragments contained in the string by changing some characters in the string.

For example, we can change the DNA fragment "AAGCAG" to "AGGCAC" by changing two characters, so that the DNA fragment no longer contains the disease-causing fragments "AAG", "AGC", "CAG" in order to repair the DNA The purpose of the fragment.

Note that the repaired DNA fragment can still only contain the characters'A','G','C', and'T'.

Please help biologists repair a given DNA fragment, and the number of characters changed during the repair process should be as few as possible.

Input format
The input contains multiple sets of test data.

The first row of each group of data contains an integer N, which represents the number of disease-causing DNA fragments.

In the next N lines, each line contains a non-empty string with a length of no more than 20. The string only contains the characters'A','G','C', and'T', which are used to represent the disease-causing DNA fragments.

Another line contains a non-empty string of no more than 1000 in length. The string only contains the characters'A','G','C', and'T' to indicate the DNA fragment to be repaired.

The last set of test data is followed by a line, which contains a 0, indicating the end of the input.

Output format
Each group of data outputs a result, and each result occupies one line.

The input form is "Case x: y", where x is the test data number (starting from 1), and y is the minimum number of characters that need to be changed during the repair process. If the given DNA fragment cannot be repaired, then y is "- 1".

data range
1 ≤ N≤ 50

Sample Input:
```
2
AAA
AAG
AAAG    
2
A
TG
TGAATG
4
A
G
C
T
AGT
0
```
Sample Output:
```
Case 1: 1
Case 2: 4
Case 3: -1
```

### Solution

We can first build a dictionary tree (trie) and mark the end of each word to indicate that the point is a disease-causing segment that is unreachable.

Next, build the [AC automata](https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/). The purpose of the construction is to follow the definition of the next array. If the suffix of a word is a disease-causing segment, then the node should also be marked, so that all illegal nodes are marked.

The minimum modification required for the original question does not include the disease-causing segment, that is, starting from the root of the tree, you can choose 'ATCG' any one of them at each step .

If the character selected in step k is the same as that of the DNA fragment, it means that this step has not been modified, and the cost is 0, otherwise it is 1.

Go m=len(DNA) steps, the premise is that you cannot go to the marked node, so that the minimum cost of all moves.

DP can be adopted, the state transition side process is as follows:
```
if (!st[trie[u][i]])
    res = min(res, dp(trie[u][i], len + 1) + (id[s[len]] == i ? 0 : 1));
```
Indicates that the next step must select the unmarked point transfer, and the cost is 0 or 1 depending on the character selected in this step.

dp[u][v] means the minimum cost of all moves to the end node, which starts from node u, currently in the v step.   

The meaning of the end point is taking m steps without passing through the marked point.


{% highlight C++ linenos %}
#include <iostream>
#include <cstring>
#include <queue>

using namespace std;
const int N = 1005, INF = 1e9;
int n, m, id[N], trie[N][4], st[N], tot = 0, ne[N];
int f[N][N];
char s[N];
queue<int> q;

void insert() {
    int p = 0;
    for (int i = 1; i <= m; i++) {
        int ch = id[s[i]];
        if (!trie[p][ch]) trie[p][ch] = ++tot;
        p = trie[p][ch];
    }
    st[p] = 1;
}

void build() {
    for (int i = 0; i < 4; i++)
        if (trie[0][i]) q.push(trie[0][i]);
    while (!q.empty()) {
        int t = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            if (trie[t][i]) {
                ne[trie[t][i]] = trie[ne[t]][i];
                if (st[ne[trie[t][i]]]) st[trie[t][i]] = 1;
                q.push(trie[t][i]);
            } else trie[t][i] = trie[ne[t]][i];
        }
    }
}

int dp(int u, int len) {
    if (len == m + 1) return f[u][len] = 0;
    if (f[u][len] != -1) return f[u][len];
    int res = INF;
    for (int i = 0; i < 4; i++)
        if (!st[trie[u][i]])
            res = min(res, dp(trie[u][i], len + 1) + (id[s[len]] == i ? 0 : 1));
    return f[u][len] = res;
}

int main() {
    id['T'] = 1, id['C'] = 2, id['G'] = 3;
    int cnt = 0;
    while (scanf("%d", &n), n) {
        tot = 0;
        memset(ne, 0, sizeof ne);
        memset(st, 0, sizeof st);
        memset(trie, 0, sizeof trie);
        memset(f, -1, sizeof f);
        for (int i = 1; i <= n; i++) {
            scanf("%s", s + 1);
            m = strlen(s + 1);
            insert();
        }
        build();
        scanf("%s", s + 1);
        m = strlen(s + 1);
        int res = dp(0, 1);
        printf("Case %d: %d\n", ++cnt, res == INF ? -1 : res);
    }
    return 0;
}
{% endhighlight %}
