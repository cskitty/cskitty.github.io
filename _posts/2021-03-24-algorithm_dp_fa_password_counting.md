---
title: "DP Finite Automata with Compression: Password Counting"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Dynamic Programming
  - Finite Automata
---

## DP Finite Automata with Compression: Password Counting

You now need to design a password S,S Need to meet:

S The length is N；
S Only contain lowercase English letters;
S Does not contain substring T；
E.g: abc and abcde are abcde's substring while abde is not a substring of abcde.

How many different passwords meet the requirements?

Since the answer will be very large, please output the answer modulus 109 + 7 The remainder.

Input format  

Enter the integer N in the first line to indicate the length of the password.

Enter the string T on the second line. T contains only lowercase letters.

Output format

Output a positive integer , which means the total password number modulus109+ 7 After the result.

data range

Sample Input:
```
4
cbc
```
Sample Output:
```
456924
```

### Solution

Use T to generate a KMP state transition table. Looping from 0 to N and test every possible charater (a-z), the KMP state transition from j to newJ based on charater in position i+1. Add the numbers to that state.

dp[i][j]: the number of passwords so far from 0 to i-th Position

* i is the i-th position of the password(< N)   
* j is the j-th state of KMP state.  


{% highlight C++ linenos %}
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

const int N=55,mod=1e9+7;
int dp[N][N],kmp_table[N][26];

void buildKMPTable(string s) {
  int m = s.length();

  int x = 0;
  kmp_table[0][0] = 1;
  for (int i = 1; i < m; ++i) {
      for (char ch = 'a'; ch <= 'z'; ++ch) {
          if (ch == s[i]) {
              kmp_table[i][ch - 'a'] = i + 1;
          } else {
              kmp_table[i][ch - 'a'] = kmp_table[x][ch - 'a'];
          }
      }
          x = kmp_table[x][s[i] - 'a'];
  }
}

int main()
{
    int n;
    cin>>n;
    string T;
    cin>>T;
    int m= T.length();

    //create KMP state transition table based on T
    buildKMPTable(T);

    //inialize the empty password as count 1
    dp[0][0]=1;

    for(int i=0;i<n;i++)
     for(int j=0;j<m;j++)
      //iterate through all possible value of charater in position i + 1
      for(char k='a';k<='z';k++)
       {
           int u=kmp_table[j][k - 'a'];

           if(u<m)
              dp[i+1][u]=(dp[i+1][u]+dp[i][j])%mod;
       }

    int res=0;
    for(int i=0;i<m;i++)
      res=(res + dp[n][i])%mod;

    printf("%d",res);

    return 0;
}
{% endhighlight %}
