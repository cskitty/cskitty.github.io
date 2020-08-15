---
title: "C. Maximum Median"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Binary Search
---
# C. Maximum Median

[C. Maximum Median](https://codeforces.com/contest/1201/problem/C)

You are given an array a of n integers, where n is odd. You can make the following operation with it:  

Choose one of the elements of the array (for example ai) and increase it by 1 (that is, replace it with ai+1).  
You want to make the median of the array the largest possible using at most k operations.  

The median of the odd-sized array is the middle element after the array is sorted in non-decreasing order. For example, the median of the array [1,5,2,3,5] is 3.  

Input  
The first line contains two integers n and k (1≤n≤2⋅105, n is odd, 1≤k≤109) — the number of elements in the array and the largest number of operations you can make  

The second line contains n integers a1,a2,…,an (1≤ai≤109).  

Output  
Print a single integer — the maximum possible median after the operations.  

{% highlight java linenos %}
long long k;
vector<long long> v;

// checks whether the number of given operations is sufficient
// to raise the median of the array to x
bool check(long long x){
    long long operationsNeeded = 0;
    for(int i = (n-1)/2; i < n; i++){
        operationsNeeded += max(0, x-v[i]);
    }
    if(operationsNeeded <= k) return true;
    else return false;
}

// binary searches for the correct answer
long long search(){
    long long pos = 0; long long max = 2E9;
    for(long long a = max; a >= 1; a /= 2){
        while(check(pos+a)) pos += a;
    }
    return pos;
}

int main() {
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        int t;
        cin >> t;
        v.push_back(t);
    }
    sort(v.begin(), v.end());

    cout << search() << '\n';
}

{% endhighlight %}
