---
title: "USACO 2016 Dec Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2016 Dec Silver

## Problem 1.  Counting Haybales

[Counting Haybales](http://www.usaco.org/index.php?page=viewproblem2&cpid=666)

Farmer John has just arranged his N haybales (1≤N≤100,000) at various points along the one-dimensional road running across his farm. To make sure they are spaced out appropriately, please help him answer Q queries (1≤Q≤100,000), each asking for the number of haybales within a specific interval along the road.
INPUT FORMAT (file haybales.in):
The first line contains N and Q.
The next line contains N distinct integers, each in the range 0…1,000,000,000, indicating that there is a haybale at each of those locations.

Each of the next Q lines contains two integers A and B (0≤A≤B≤1,000,000,000) giving a query for the number of haybales between A and B, inclusive.

OUTPUT FORMAT (file haybales.out):
You should write Q lines of output. For each query, output the number of haybales in its respective interval.
SAMPLE INPUT:
```
4 6
3 2 7 5
2 3
2 4
2 5
2 7
4 6
8 10
```
SAMPLE OUTPUT:
```
2
2
3
4
1
0
```
Problem credits: Nick Wu

{% highlight c++ linenos %}

// USACO Input & Output
void setIO(string name) {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen((name+".in").c_str(),"r",stdin);
    freopen((name+".out").c_str(),"w",stdout);
}

int myLowerBound(int l, int r, vector<int> arr, int needed) {
    while(l<r)
    {
        int mid=(l+r)>>1;
        mid++;
        //dbg(l, r, mid);
        // switch to < if upper bound
        if(arr[mid] < needed) {
            l = mid;
        }
        else r=mid-1;
    }
    return l + 1;
}

int main() {
    setIO("haybales");

    int N, Q;
    cin >> N >> Q;

    vector<int> bales(N);

    F0R(i, N) {
        int x;
        cin >> bales[i];
    }

    sort(bales.begin(), bales.end());

    F0R(i, Q) {
        int S, E;
        cin >> S >> E;


        //dbg( lower_bound(bales.begin(), bales.end(), E) - bales.begin());
        //dbg( myLowerBound(0, N - 1, bales, E) );
        cout << upper_bound(bales.begin(), bales.end(), E) - bales.begin() - myLowerBound(0, N - 1, bales, S) << endl;
    }

}
{% endhighlight %}

## Problem 2. Cities and States

To keep his cows intellectually stimulated, Farmer John has placed a large map of the USA on the wall of his barn. Since the cows spend many hours in the barn staring at this map, they start to notice several curious patterns. For example, the cities of Flint, MI and Miami, FL share a very special relationship: the first two letters of "Flint" give the state code ("FL") for Miami, and the first two letters of "Miami" give the state code ("MI") for Flint.  
Let us say that two cities are a "special pair" if they satisfy this property and come from different states. The cows are wondering how many special pairs of cities exist. Please help them solve this amusing geographical puzzle  

INPUT FORMAT (file citystate.in  
The first line of input contains N (1≤N≤200,000), the number of cities on the map  
The next N lines each contain two strings: the name of a city (a string of at least 2 and at most 10 uppercase letters), and its two-letter state code (a string of 2 uppercase letters). Note that the state code may be something like ZQ, which is not an actual USA state. Multiple cities with the same name can exist, but they will be in different states.  

OUTPUT FORMAT (file citystate.out):  
Please output the number of special pairs of cities.  
SAMPLE INPUT  
```
6
MIAMI FL
DALLAS TX
FLINT MI
CLEMSON SC
BOSTON MA
ORLANDO FL
```
SAMPLE OUTPUT:  
```
1
```
Problem credits: Brian Dean  

## Problem 3. Moocast

[Moocast](http://www.usaco.org/index.php?page=viewproblem2&cpid=668)

Farmer John's N cows (1≤N≤200) want to organize an emergency "moo-cast" system for broadcasting important messages among themselves.
Instead of mooing at each-other over long distances, the cows decide to equip themselves with walkie-talkies, one for each cow. These walkie-talkies each have a limited transmission radius -- a walkie-talkie of power P can only transmit to other cows up to a distance of P away (note that cow A might be able to transmit to cow B even if cow B cannot transmit back, due to cow A's power being larger than that of cow B). Fortunately, cows can relay messages to one-another along a path consisting of several hops, so it is not necessary for every cow to be able to transmit directly to every other cow.

Due to the asymmetrical nature of the walkie-talkie transmission, broadcasts from some cows may be more effective than from other cows in their ability to reach large numbers of recipients (taking relaying into account). Please help the cows determine the maximum number of cows that can be reached by a broadcast originating from a single cow.

INPUT FORMAT (file moocast.in):
The first line of input contains N.
The next N lines each contain the x and y coordinates of a single cow ( integers in the range 0…25,000) followed by p, the power of the walkie-talkie held by this cow.

OUTPUT FORMAT (file moocast.out):
Write a single line of output containing the maximum number of cows a broadcast from a single cow can reach. The originating cow is included in this number.
SAMPLE INPUT:
'''
4
1 3 5
5 4 3
7 2 1
6 1 1
'''
SAMPLE OUTPUT:
'''
3
'''

In the example above, a broadcast from cow 1 can reach 3 total cows, including cow 1.

Problem credits: Brian Dean

{% highlight c++ linenos %}

int N;
int ans;
int rep[MX];
vector<int> adj_list[MX];
vector<vector<int>> cows(MX);
int currCount;

bool visited[MX];

void dfs(int node) {
    visited[node] = true;
    currCount++;

    for(int i : adj_list[node]) {
        if (! visited[i]) {
            dfs(i);
        }
    }
}

int countComponents() {
    int mCount = 0;
    int count = 0;
    F0R(i, N) {
        F0R(i, N) {
            visited[i] = false;
        }
            // count++;
        currCount = 0;
        dfs(i);
        rep[count] = currCount;
        count++;
        mCount = max(currCount, mCount);
        dbg(currCount, rep[count], count, i, mCount);
    }
    return mCount;
}

int main() {
    setIO("moocast");
    cin >> N;

    F0R(i, N) {
        int A, B, C;
        cin >> A >> B >> C;
        cows[i] = {A, B, C};
    }

    F0R(i, N) {
        F0R(j, N) {
            int diff = (abs(cows[i][0] - cows[j][0]) * abs(cows[i][0] - cows[j][0])) + (abs(cows[i][1] - cows[j][1]) * abs(cows[i][1] - cows[j][1]));
            if (diff <= (cows[i][2] * cows[i][2])) {
                adj_list[i].push_back(j);
            }
            if (diff <= (cows[j][2] * cows[j][2])) {
                adj_list[j].push_back(i);
            }

        }
    }

    ans = countComponents();

    cout << ans << endl;
}

{% endhighlight %}
