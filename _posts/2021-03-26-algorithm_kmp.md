---
title: "KMP Algorithm Explained"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Monotonous Stack
  - Sliding Window
---

## KMP Algorithm Explained

KMP is called Knuth Morris Pratt algorithm. The three words are the names of the three authors. KMP is an efficient string matching algorithm that is used to find the position of the pattern string in the main string (for example , to find the position of the "world" pattern string in the "hello, world" main string ).

For string pattern search, let's start the BF (Brute Force) algorithm. Its idea is to intercept substrings of length m in the interval [0, n-m] of the main string to see if the substring is the same as the pattern string (n is the length of the main string, and m is the length of the substring). The code is like this:

{% highlight C++ linenos %}
string main, pattern;

int n = main.size();
int m = pattern.size();

for (i := 0; i <= n-m; i++) {
    string substr = main.substr(i, m)
    //another for loop of m is used here
    if substr == pattern {
        return i;
    }
}

return -1;
{% endhighlight %}

The time complexity of BF is O(N*M) , and there is a lot of room for optimization. Let's take a concrete example to see what can be optimized. For example, the main pattern string is "ababaeaba" and the pattern string is "ababacd".  Suppose we match up to "ababa", the 5-th charater in the pattern string,  which means the current state is 5. However, the next character in the pattern string 'c' doesn't match the next character in the main 'e'.

main:    "ababaeaba"  
pattern: "ababacd"    

The idea of ​​the KMP algorithm is: in the process of matching the pattern string and the main string, when encountering unmatched characters, for the same prefix string in the main string and the pattern string, find the same prefix string with the longest length. Thus, the pattern string is slid multiple positions at a time, and some comparison processes are omitted. In the previous example, the KMP algorithm is processed as follows:

main:    "ababaeaba" // main[2:4] ("aba") is same as
pattern: "ababacd"   // pattern[0:2] ("aba"), so we can slide so we can slide j = j - k positions  
                     // j is index of 'c' and k is length of "aba"

            "ababaeaba"      // 比较过程中，main[5] is "e" doesn't match with pattern[5] which is "c". but both main[1:5] and
            "ababacd"            // 串中都有相同的"aba"前缀,所以可以滑动j-k位
                    |           
                    ∨
            "ababaeaba"   
                "ababacd"
                    |               // 滑动j-k位后发现main[5]和patterb[3]不相同，需要再次滑动
                    ∨
            "ababaeaba"   
                    "ababacd" // 滑动过程和上次类似。

From this example, it can be seen that the number of digits of each sliding is jk, and the number of sliding digits has nothing to do with the main string. It can be obtained only by the pattern string. In the KMP algorithm, the next array is used to store the number of bits that the pattern string should move when two characters are not equal.

How to use the next array of KMP algorithm
Again, clarify the meaning of the next array : the next array is used to store the subscript of the longest prefix in the pattern string that can match the end character of the prefix substring. next[i] = j means that the subscript starts with ij, the suffix with i as the end point and the subscript with 0 as the start point, and the prefix with j as the end point are equal, and the length of this string is the longest. The symbol is expressed as p[0~j] == p[ij~i] . Taking the "ababacd" pattern string as an example, the next array of this string is given below.

 We create an automata with m + 1 states, representing matched pattern length of 1, 2, 3...m and an additional initial non-matching state. If a new charater in the main string matches with the next pattern charater, then we advance to the next state (state + 1). However if the next character in the pattern string cannot be matched, we need to go back to previous states.

Sample Input:
```
8 3
1 3 -1 -3 5 3 6 7
```
Sample Output:
```
-1 -3 -3 -3 3 3
3 3 5 5 6 7
```

### Solution

Brute force: maintain the current window in a list and query min max of the list. Complexity is O(n^2).
Optimization: maintain a monotonous queue. We store indexes of the array in the monotonous queue instead of array value so that we can delete element in the queue if it is out of the sliding window.

When we move window from left to right, compare the new number against the tail element of the queue. If it is smaller than tail, then delete the tail and replace with the new element.  

{% highlight C++ linenos %}
#include<bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;
int n, k, a[N];

deque<int> dq;

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin>>n>>k;

    for(int i = 0; i <n; i ++)
      cin>>a[i];

    //find the minimal number in the sliding window
    for(int i = 0; i < n; i ++)
    {
        //keep the front of the deque always inside sliding window of size k
        if( !dq.empty() && k < i - dq.front() + 1)
            dq.pop_front();

        //maintain monotonous queue
        //if the queue is not empty and the tail element is not smaller than a[i]
        //pop all the bigger elements until it is smaller than a[i]
        while( !dq.empty() && a[dq.back()] >= a[i])
            dq.pop_back();

        dq.push_back(i);

        if(i + 1 >= k)
            cout << a[dq.front()] << " ";
    }

    cout << endl;

    dq.clear();

    //find the maximimal number in the sliding window
    for(int i = 0; i < n; i ++)
    {
        //keep the front of the deque always inside sliding window of size k
        if( !dq.empty() && k < i - dq.front() + 1)
            dq.pop_front();

        //maintain monotonous queue
        //if the queue is not empty and the tail element is not larger than a[i]
        //pop all the bigger elements until it is smaller than a[i]
        while( !dq.empty() && a[dq.back()] <= a[i])
            dq.pop_back();

        dq.push_back(i);

        if(i + 1 >= k)
            cout << a[dq.front()] << " ";
    }

    return 0;
}
{% endhighlight %}
