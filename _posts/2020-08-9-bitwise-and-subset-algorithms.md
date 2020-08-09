---
title: "Bitwise Operations and Subset Algorithms"
categories:
  - Programming
tags:
  - C++
  - Algorithms
  - Graph
---

# Bitwise Operations and Subset Algorithms

##  Combinations Using Bitwise

{% highlight c++ linenos %}
constexpr int pct(int x) { return __builtin_popcount(x); }
constexpr int bits(int x) { return 31-__builtin_clz(x); } // floor(log2(x))

int bitOneCount(int i) {
    int sum = 0;
    while (i) {
        sum += i & 1;
        i = i >> 1;
    }
    return sum;

    // entire function is same as 
    //return pct(i)
}


vector<vector<int>> combinations(int num, int needed) {
    vector<vector<int>> ans;

    F0R(i, pow(2, num)) {
        if (bitOneCount(i) == needed) {
            //dbg(bitset<12>(i));
            vector<int> x;
            int k = i;
            F0R(j, num) {
                if (k & 1) {
                    x.push_back(j);
                }
                k = k >> 1;
            }
            ans.push_back(x);
        }
    }
    dbg(ans.size());
    return ans;
}
{% endhighlight %}

## Complete Set Using Bitwise

{% highlight c++ linenos %}
vector<vector<int>> generateCompleteSet(int num, vector<int> arr) {
    vector<vector<int>> ans;

    F0R(i, pow(2, num)) {
        vector<int> x;
        int k = i;
        F0R(j, num) {
            if (k & 1) {
                x.push_back(arr[j]);
            }
            k = k >> 1;
        }
        ans.push_back(x);
    }

    return ans;
}


int main() {
    vector<int> x = {1, 2, 3, 4};

    vector<vector<int>> ans = generateCompleteSet(x.size(), x);

    for (auto x : ans) {
        dbg(x);
    }

    dbg(ans.size());
}
{% endhighlight %}
