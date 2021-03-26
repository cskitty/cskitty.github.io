---
title: "Slicing Window Query: Min and Max of the Window"
categories:
  - Algorithm
tags:
  - C++
  - Algorithms
  - Monotonous Stack
  - Sliding Window
---

## Slicing Window Query: Min and Max of the Window

Given a size n ≤ 10^6 array.

Specify a size of k sliding window, it moves from the leftmost to the rightmost of the array.

You can only see in the sliding window k numbers.

Each time the sliding window moves one position to the right.

The following is an example:

The array is [1 3 -1 -3 5 3 6 7], k for 3.

Your task is to determine the maximum and minimum values ​​of the sliding window at each position.

Input format
The input contains two lines.

The first line contains two integers n and k representing the length of the array and the length of the sliding window.

The second line has n integer representing the specific value of the array.


Output format
The output contains two.

The first line of output, from left to right, is the minimum value in the sliding window at each position.

The second line of output, from left to right, is the maximum value in the sliding window at each position.

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
