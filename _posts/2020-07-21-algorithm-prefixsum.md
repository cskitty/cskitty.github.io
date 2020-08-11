---
title: "Prefix Sum"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - PrefixSum
---
# Prefix Sum

## Subarray Sums II

[Subarray Sums II](https://cses.fi/problemset/task/1661)

Given an array of n integers, your task is to count the number of subarrays having sum x.  

Input  

The first input line has two integers n and x: the size of the array and the target sum x.  

The next line has n integers a1,a2,…,an: the contents of the array.  

Output  

Print one integer: the required number of subarrays.  

Constraints  
1≤n≤2⋅105  
−109≤x,ai≤109  
Example  

Input:
```
5 7
2 -1 3 5 -2
```
Output:
```
2
```
{% highlight C++ linenos %}
int main() {
    ll N, X;
    cin >> N >> X;

    vector<ll> a(N);

    ll count = 0;
    map<ll, int> mp;
    mp[0]++;
    ll sum = 0;

    F0R(i, N) {
        cin >> a[i];
        sum += a[i];
        count += mp[sum - X];
        mp[sum]++;
    }

    cout << count;
}
{% endhighlight %}



## Prefix Sums

Given an array A and an index i, the prevfix sums array  P is accumulated sums calculated over [0] ... [i]

{% highlight java linenos %}
for (int i = 0; i < A.length; i++) {
    P[i + 1] = P[i] + A[i];
}
{% endhighlight %}


Prefix sums can be used to get sums of any arbitrary length subarray.

### Find Pivot Index

[Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)  

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.


{% highlight java linenos %}
class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        int half = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        for (int j = 0; j < nums.length; j++) {
            if (half + half + nums[j] == sum) {
                return j;
            }
            half += nums[j];
        }
        return -1;
    }
}
{% endhighlight %}



### Subarray Sums Divisible by K

[Leetcode  Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)  

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.  



Example 1:  

Input: A = [4,5,0,-2,-3,1], K = 5  
Output: 7  
Explanation: There are 7 subarrays with a sum divisible by K = 5:  
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]  


{% highlight java linenos %}
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] P = new int[A.length + 1];
        P[0] = 0;

        for (int i = 0; i < A.length; i++) {
            P[i + 1] = P[i] + A[i];
        }

        Map<Integer, Integer> remainders = new HashMap<Integer, Integer>();
        for (int i = 0; i < P.length; i++) {
            // if diff %k == 0, diff divisible
            int key = P[i] % K;
            if (key < 0) {
                key += K;
            }
            if (remainders.containsKey(key)) {
                remainders.put(key, remainders.get(key) + 1);
            }
            else {
                remainders.put(key, 1);
            }
        }

        int sum = 0;
        for (int i : remainders.values()) {
            sum += (i * (i - 1)) / 2 ;
        }
        return sum;
    }
}
{% endhighlight %}
