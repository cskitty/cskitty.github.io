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

Given an array A and an index i, the prevfix sums array  P is accumulated sums calculated over [0] ... [i]

{% highlight java linenos %}
for (int i = 0; i < A.length; i++) {
    P[i + 1] = P[i] + A[i];
}
{% endhighlight %}


Prefix sums can be used to get sums of any arbitrary length subarray.


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

## Subarray Divisibility

[Subarray Divisibility](https://cses.fi/problemset/task/1661)

Given an array of n integers, your task is to count the number of subarrays where the sum of values is divisible by n  

Input  

The first input line has an integer n: the size of the array.  

The next line has n integers a1,a2,…,an: the contents of the array.  

Output  

Print one integer: the required number of subarrays.  

Constraints  
1≤n≤2⋅105  
−109≤ai≤109  
Example  

Input:
```
5
3 1 2 7 4
```
Output:
```
1
```

{% highlight C++ linenos %}
int main() {
    ll N;
    cin >> N;

    vector<ll> prefix(N + 1);
    vector<ll> a(N);
    map<ll, ll> myMap;

    ll count = 0;
    myMap[0]++;

    F0R(i, N) {
        cin >> a[i];

        // add a[i]%N+ N to get positive mod result 0...N-1 for negative a[i]
        prefix[i + 1] = (prefix[i] + a[i]%N+ N) % N;

        count += myMap[prefix[i + 1]];
        myMap[prefix[i + 1]]++;

    }
    cout << count;
}
{% endhighlight %}


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



### Forest Queries (2D PrefixSum)

[Forest Queries](https://cses.fi/problemset/task/1652)  

You are given an n×n grid representing the map of a forest. Each square is either empty or contains a tree. The upper-left square has coordinates (1,1), and the lower-right square has coordinates (n,n).  

Your task is to process q queries of the form: how many trees are inside a given rectangle in the forest?  

Input  

The first input line has two integers n and q: the size of the forest and the number of queries.  

Then, there are n lines describing the forest. Each line has n characters: . is an empty square and * is a tree.  

Finally, there are q lines describing the queries. Each line has four integers y1, x1, y2, x2 corresponding to the corners of a rectangle.  

Output  

Print the number of trees inside each rectangle.  

Constraints  
1≤n≤1000  
1≤q≤2⋅105  
1≤y1≤y2≤n  
1≤x1≤x2≤n  
Example  

Input:
```
4 3
.*..
*.**
**..
****
2 2 3 4
3 1 3 1
1 1 2 2
```
Output:
```
3
1
2
``
{% highlight C++ linenos %}
int main() {
    int N, Q;
    cin >> N >> Q;
    vector<vector<int>> prefix(N + 1, vector<int> (N + 1));

    F0R(i, N) {
        F0R(j, N) {
            char x;
            cin >> x;
            if (x == '*') {
                prefix[i + 1][j + 1]++;
            }
        }
        // by row!
        F0R(j, N) {
            prefix[i + 1][j + 1] += prefix[i + 1][j];
        }
    }
    // prefix
    F0R(i, N) {
        FOR(j, 1, N + 1) {
            prefix[i + 1][j] += prefix[i][j];
        }
    }

    F0R(i, Q) {
        int x1, x2, y1, y2;
        cin >> y1 >> x1 >> y2 >> x2;
        // actually y2 + 1, x2 + 1
        cout << prefix[y2][x2] - prefix[y1 - 1][x2] - prefix[y2][x1 - 1] + prefix[y1 - 1][x1 - 1] << endl;
    }
}
{% endhighlight %}
