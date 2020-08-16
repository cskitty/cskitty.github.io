---
title: "USACO 2017 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2017 Jan Silver

## Problem 1. Cow Dance Show

[Cow Dance Show](http://usaco.org/index.php?page=viewproblem2&cpid=690)

After several months of rehearsal, the cows are just about ready to put on their annual dance performance; this year they are performing the famous bovine ballet "Cowpelia".
The only aspect of the show that remains to be determined is the size of the stage. A stage of size K can support K cows dancing simultaneously. The N cows in the herd (1≤N≤10,000) are conveniently numbered 1…N in the order in which they must appear in the dance. Each cow i plans to dance for a specific duration of time d(i). Initially, cows 1…K appear on stage and start dancing. When the first of these cows completes her part, she leaves the stage and cow K+1 immediately starts dancing, and so on, so there are always K cows dancing (until the end of the show, when we start to run out of cows). The show ends when the last cow completes her dancing part, at time T.  

Clearly, the larger the value of K, the smaller the value of T. Since the show cannot last too long, you are given as input an upper bound Tmax specifying the largest possible value of T. Subject to this constraint, please determine the smallest possible value of K.  

INPUT FORMAT (file cowdance.in):  
The first line of input contains N and Tmax, where Tmax is an integer of value at most 1 million.  
The next N lines give the durations d(1)…d(N) of the dancing parts for cows 1…N. Each d(i) value is an integer in the range 1…100,000.  

It is guaranteed that if K=N, the show will finish in time.  

OUTPUT FORMAT (file cowdance.out):  
Print out the smallest possible value of K such that the dance performance will take no more than Tmax units of time.  
SAMPLE INPUT:  
```
5 8
4
7
8
6
4
```
SAMPLE OUTPUT:
```
4
```
Problem credits: Delphine and Brian Dean

{% highlight c++ linenos %}

int N;
ll M;

bool check(vector<ll> v, ll target) {
    dbg(target);
    if (target == 3) {
        dbg(v);
    }
     vector<ll> onStage;
     ll i = 0;
     ll time = 0;
     while (i < v.size()) {
         while (onStage.size() < target) {
             onStage.push_back(v[i]);
             i++;
         }

         auto sub = min_element(all(onStage));
         ll min = *sub;
         time += min;
         F0R(j, onStage.size()) {
             onStage[j] -= min;
             if (onStage[j] == 0) {
                 onStage[j] = v[i];
                 i++;
             }
         }
         if (time > M) {
             return false;
         }
     }
     time += *max_element(all(onStage));
     if (time > M) {
         return false;
     }
     return true;
}

ll binary_search(vector<ll> x) {

    ll max = x.end() - x.begin();
    ll p = max;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p - a) > 0 && check(x, p - a)) p -= a;
    }
    return p;
}

int main() {

    setIO("cowdance");

    cin >> N >> M;

    vector<ll> nums(N);

    F0R(i, N) cin >> nums[i];

    cout << binary_search(nums);

}

{% endhighlight %}
