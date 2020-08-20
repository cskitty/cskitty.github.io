---
title: "USACO 2018 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2018 Jan Silver

## Problem 1: Lifeguards

[Lifeguards](http://www.usaco.org/index.php?page=viewproblem2&cpid=786)

Farmer John has opened a swimming pool for his cows, figuring it will help them relax and produce more milk.  

To ensure safety, he hires N cows as lifeguards, each of which has a shift that covers some contiguous interval of time during the day. For simplicity, the pool is open from time t=0 until time t=1,000,000,000 on a daily basis, so each shift can be described by two integers, giving the time at which a cow starts and ends her shift. For example, a lifeguard starting at time t=4 and ending at time t=7 covers three units of time (note that the endpoints are "points" in time).  

Unfortunately, Farmer John hired 1 more lifeguard than he has the funds to support. Given that he must fire exactly one lifeguard, what is the maximum amount of time that can still be covered by the shifts of the remaining lifeguards? An interval of time is covered if at least one lifeguard is present.  

INPUT FORMAT (file lifeguards.in):  

The first line of input contains N (1≤N≤100,000). Each of the next N lines describes a lifeguard in terms of two integers in the range 0…1,000,000,000, giving the starting and ending point of a lifeguard's shift. All such endpoints are distinct. Shifts of different lifeguards might overlap.  

OUTPUT FORMAT (file lifeguards.out):  
Please write a single number, giving the maximum amount of time that can still be covered if Farmer John fires 1 lifeguard.  
SAMPLE INPUT:  
```
3
5 9
1 4
3 7
```
SAMPLE OUTPUT:
```
7
```
Problem credits: Brian Dean

{% highlight C++ linenos %}
struct Shift {
    ll time;
    int type;
    ll ID;
};

ll N;
vector<Shift> guards;

ll nonOverlap() {

    vector<ll> minT(N, 0);
    ll currT = 0;
    ll timeCovered = 0;
    set<ll> onDuty;

    F0R(i, guards.size()) {
        Shift guard = guards[i];

        currT = guard.time;
        if (onDuty.size() > 0) {
            ll diffT = currT - guards[i - 1].time;
            timeCovered += diffT;
        }
        if (guard.type == 0) {
            // add guard
            onDuty.insert(guard.ID);
        }
        else {
            onDuty.erase(guard.ID);
        }

        if (onDuty.size() == 1) {
            auto index = onDuty.begin();
            minT[*index] += guards[i + 1].time - currT;
        }
    }

    ll minA = *min_element(all(minT));

    F0R(i, minT.size()) {
        minA = min(minA, minT[i]);
    }

    return timeCovered - minA;
}

int main() {
    setIO("lifeguards");
    cin >> N;

    F0R(i, N) {
        ll X, Y;
        cin >> X >> Y;
        guards.push_back({X, 0, i});
        guards.push_back({Y, 1, i});
    }

    sort(guards.begin(), guards.end(), [](Shift a, Shift b){return a.time < b.time;});
    cout << nonOverlap();
}

{% endhighlight %}

## Problem 2:  Rental Service

[Rental Service](http://www.usaco.org/index.php?page=viewproblem2&cpid=787)

Farmer John realizes that the income he receives from milk production is insufficient to fund the growth of his farm, so to earn some extra money, he launches a cow-rental service, which he calls "USACOW" (pronounced "Use-a-cow").
Farmer John has N cows (1≤N≤100,000), each capable of producing some amount of milk every day. The M stores near FJ's farm (1≤M≤100,000) each offer to buy a certain amount of milk at a certain price. Moreover, Farmer John's R (1≤R≤100,000) neighboring farmers are each interested in renting a cow at a certain price.   

Farmer John has to choose whether each cow should be milked or rented to a nearby farmer. Help him find the maximum amount of money he can make per day.   

INPUT FORMAT (file rental.in):  
The first line in the input contains N, M, and R. The next N lines each contain an integer ci (1≤ci≤1,000,000), indicating that Farmer John's ith cow can produce ci gallons of milk every day. The next M lines each contain two integers qi and pi (1≤qi,pi≤1,000,000), indicating that the ith store is willing to buy up to qi gallons of milk for pi cents per gallon. Keep in mind that Farmer John can sell any amount of milk between zero and qi gallons to a given store. The next R lines each contain an integer ri (1≤ri≤1,000,000), indicating that one of Farmer John's neighbors wants to rent a cow for ri cents per day.  
OUTPUT FORMAT (file rental.out):  
The output should consist of one line containing the maximum profit Farmer John can make per day by milking or renting out each of his cows. Note that the output might be too large to fit into a standard 32-bit integer, so you may need to use a larger integer type like a "long long" in C/C++.  
SAMPLE INPUT:  
```
5 3 4
6
2
4
7
1
10 25
2 10
15 15
250
80
100
40
```
SAMPLE OUTPUT:
```
725
```
Farmer John should milk cows #1 and #4, to produce 13 gallons of milk. He should completely fill the order for 10 gallons, earning 250 cents, and sell the remaining three gallons at 15 cents each, for a total of 295 cents of milk profits.  

Then, he should rent out the other three cows for 250, 80, and 100 cents, to earn 430 more cents. (He should leave the request for a 40-cent rental unfilled.) This is a total of 725 cents of daily profit.   

Problem credits: Jay Leeds  

{% highlight C++ linenos %}
int main() {
    setIO("rental");

    ll N, M, R;
    cin >> N >> M >> R;

    vector<ll> cows(N);

    F0R(i, N) cin >> cows[i];

    vector<pair<ll, ll>> stores(M);
    vector<ll> milkPrice(M + 1);
    vector<ll> milkAmount(M + 1);

    F0R(i, M) {
        cin >> stores[i].f >> stores[i].s;
    }

    vector<ll> rent(R);
    F0R(i, R) cin >> rent[i];


    ll ans = 0;

    sort(all(cows), [](ll a, ll b) {return a > b;});
    sort(all(stores), [](pair<ll, ll> a, pair<ll, ll> b) { return a.s > b.s;});
    sort(all(rent), [] (ll a, ll b) {return a > b;});

    F0R(i, M) {
        milkPrice[i + 1] = milkPrice[i] + stores[i].f * stores[i].s;
        milkAmount[i + 1] = milkAmount[i] + stores[i].f;
    }

    vector<ll> rentSort(R + 1);
    F0R(i, R) {
        rentSort[i + 1] = rentSort[i] + rent[i];
    }

    ll currentMilk = 0;
    F0R(i, N) {
        ll currentPrice = 0;

        currentMilk += cows[i];

        int index = upper_bound(all(milkAmount), currentMilk) - milkAmount.begin() - 1;

        currentPrice += milkPrice[index];
        if (currentMilk < milkAmount[M]) {
            currentPrice += (currentMilk - milkAmount[index]) * stores[index].s;
        }


        if (N - i > R) {
            currentPrice += rentSort[R];
        }
        else {
            currentPrice += rentSort[N - 1 - i];
        }

        ans = max(ans, currentPrice);
        // brute force
        /*ll tempMilk = currentMilk;
        for (int j = 0; j < M; j++) {
            if (tempMilk >= stores[j].f) {
                currentPrice += stores[j].f * stores[j].s;
                tempMilk -= stores[j].f;
            }
            else {
                currentPrice += tempMilk * stores[j].s;
                break;
            }
            dbg(currentPrice, j);
        }
        for(int j = i; j < N - 1 && j - i < R; j++) {
            currentPrice += rent[j - i];
        }*/

    }

    cout << ans;
}
{% endhighlight %}
