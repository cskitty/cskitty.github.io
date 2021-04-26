---
title: "Course Selection"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - DP on a Tree
---

## Course Selection

Description

The school implements a credit system.

Each compulsory course has a fixed number of credits, and the corresponding elective course credits must be obtained at the same time.

The school has N elective courses total. Each student can take M courses. Students that take the

Students that take the M courses can get the corresponding credits for each course if they pass the class and assessment.

Among the elective courses, some courses can be taken directly, and some courses require certain basic knowledge, which can only be obtained through other courses. For example, "Windows Programming" must be selected after "Windows Operating Basics". We call "Basics of Windows Operation" a prerequisite for "Windows Programming".

There is at most one direct prerequisite for each course.

Two courses may have the same prerequisites.

Your task is to determine a course selection plan for yourself so that you can get the most credits. You must meet the prerequisites of each course before taking it.

It is assumed that there is no time conflict between courses.

Input format  
The first line of the input file contains two integers N, M (Separated by a space in the middle) where 1 ≤ N≤ 300 , 1 ≤ M≤ N

The next N rows represents a course, where the course numbers are in order 1 , 2 , … , N. Each line has two numbers (separated by a space). The first number is the course number of the prerequisite course of this course (if there is no prerequisite course, this item is 0), and  the second number is the credits for this course. Credits are positive integers not exceeding 10.

Output format  
Output an integer, indicating the maximum number of credits you can earn.

### Solution  

State: dp[root][t] represents the maximum credits received where t courses are selected from the subtree of root
State Transition: Suppose the root has p children. c1 classes are taken from child 1, c2 classes are taken from child 2, c3 from child 3, etc. The state transition becomes
* dp[root][t] = dp[child1][c1] + dp[child2][c2] + ... + dp[childp][cp];
* c1 + c2 + c3 + ... + cp = t - 1 because we select the root class as one of the t classes taken

This becomes a classical 0/1 Knapsack question with t - 1 as the "weight" and p as the number of objects, where we want the maximum value (credits) from a specific combination of classes.

```
for(int t=m; t >= 0; t--)
    for(int j=t; j >= 0; j--)
       if (t - j >= 0)
          dp[root][t] = max(dp[root][t], dp[root][t - j] + dp[children[i]][j]);
```

{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

const int N = 310, M = N * 2;

vector<int> children[N];
int w[N];
int dp[N][N];
int n, m;

void add(int a, int i, int b) {
    children[a].push_back(i);
    w[i] = b;
}

void rundp(int root) {
    dp[root][0] = 0;

    // loop through children and get dp[root][t]
    for (int i = 0; i < children[root].size(); i++) {
        rundp(children[root][i]);
        for(int t=m; t >= 0; t--)
            for(int j=t; j >= 0; j--)
                if (t - j >= 0)
                    dp[root][t] = max(dp[root][t], dp[root][t - j] + dp[children[root][i]][j]);
    }

    if (root != 0) {
        for (int t = m; t > 0; t--) {
            dp[root][t] = dp[root][t - 1] + w[root];
        }
    }
}

int main() {
    cin >> n >> m;

    for(int i = 1; i <= n; i++) {
        int a, b;
        cin >> a >> b;
        add(a, i, b);
    }
    rundp(0);

    cout << dp[0][m];
}
{% endhighlight %}
