---
title: "An Impassioned Circulation of Affection"
categories:
  - Programming
tags:
  - Algorithms
  - C++
  - Two Pointers
  - Binary Search
---

# C. An Impassed Circulation of Affection

[An Impassed Circulation of Affection](https://codeforces.com/contest/814/problem/C)

Nadeko's birthday is approaching! As she decorated the room for the party, a long garland of Dianthus-shaped paper pieces was placed on a prominent part of the wall. Brother Koyomi will like it!  

Still unsatisfied with the garland, Nadeko decided to polish it again. The garland has n pieces numbered from 1 to n from left to right, and the i-th piece has a colour s i, denoted by a lowercase English letter. Nadeko will repaint at most m of the pieces to give each of them an arbitrary new colour (still denoted by a lowercase English letter). After this work, she finds out all subsegments of the garland containing pieces of only colour c — Brother Koyomi's favourite one, and takes the length of the longest among them to be the Koyomity of the garland.  

For instance, let's say the garland is represented by "kooomo", and Brother Koyomi's favourite colour is "o". Among all subsegments containing pieces of "o" only, "ooo" is the longest, with a length of 3. Thus the Koyomity of this garland equals 3.  

But problem arises as Nadeko is unsure about Brother Koyomi's favourite colour, and has swaying ideas on the amount of work to do. She has q plans on this, each of which can be expressed as a pair of an integer m i and a lowercase letter c i, meanings of which are explained above. You are to find out the maximum Koyomity achievable after repainting the garland according to each plan.  

Input  
The first line of input contains a positive integer n (1 ≤ n ≤ 1 500) — the length of the garland.  

The second line contains n lowercase English letters s 1 s 2... s n as a string — the initial colours of paper pieces on the garland.  

The third line contains a positive integer q (1 ≤ q ≤ 200 000) — the number of plans Nadeko has.  

The next q lines describe one plan each: the i-th among them contains an integer m i (1 ≤ m i ≤ n) — the maximum amount of pieces to repaint, followed by a space, then by a lowercase English letter c i — Koyomi's possible favourite colour.  

Output  
Output q lines: for each work plan, output one line containing an integer — the largest Koyomity achievable after repainting the garland according to it.  

Examples  
Input  
```
6
koyomi
3
1 o
4 o
4 m
```
Output  
```
3
6
5
```
Input  
```
15
yamatonadeshiko
10
1 a
2 a
3 a
4 a
5 a
1 b
2 b
3 b
4 b
5 b
```
Output  
```
3
4
5
7
8
1
2
3
4
5
```
Input  
```
10
aaaaaaaaaa
2
10 b
10 z
```
Output
```
10
10
```  

## Two Pointers

We can use two pointers to denote the start and the end of the largest Koyomity. Using the idea of a sliding window, we keep a "count" (denoted by changed, current amount allowed to move) and a maximum count (greatest). If the right pointer is not favorite char, or the right pointer value needs to be replaced, we subtract one from changed. However, when we are stuck (aka changed is < 0, or the right cannot move any longer) we need to move the left pointer. Thus, if the left side was replaced (or was not originally favoriteChar), we add one to change and increment the left pointer.

{% highlight c++ linenos %}
#include <fstream>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <random>
#include <math.h>
#include <complex>
#include <set>
#include <string>
#include <bitset>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef double db;
typedef string str;

typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef pair<db,db> pd;

typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<db> vd;
typedef vector<str> vs;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<pd> vpd;

#define mp make_pair
#define f first
#define s second
#define sz(x) (int)(x).size()
#define all(x) begin(x), end(x)
#define rall(x) (x).rbegin(), (x).rend()
#define rsz resize
#define ins insert
#define ft front()
#define bk back()
#define pf push_front
#define pb push_back
#define eb emplace_back
#define lb lower_bound
#define ub upper_bound

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define trav(a,x) for (auto& a: x)

const int MOD = 1e9+7; // 998244353;
const int MX = 2e5+5;
const ll INF = 1e18;
const ld PI = acos((ld)-1);
const int xd[4] = {1,0,-1,0}, yd[4] = {0,1,0,-1};
//mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count());

template<class T> bool ckmin(T& a, const T& b) {
    return b < a ? a = b, 1 : 0; }
template<class T> bool ckmax(T& a, const T& b) {
    return a < b ? a = b, 1 : 0; }
constexpr int pct(int x) { return __builtin_popcount(x); }
constexpr int bits(int x) { return 31-__builtin_clz(x); } // floor(log2(x))
ll cdiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } // divide a by b rounded up
ll fdiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // divide a by b rounded down
ll half(ll x) { return fdiv(x,2); }

template<class T, class U> T fstTrue(T lo, T hi, U f) {
    hi ++; assert(lo <= hi); // assuming f is increasing
    while (lo < hi) { // find first index such that f is true
        T mid = half(lo+hi);
        f(mid) ? hi = mid : lo = mid+1;
    }
    return lo;
}
template<class T, class U> T lstTrue(T lo, T hi, U f) {
    lo --; assert(lo <= hi); // assuming f is decreasing
    while (lo < hi) { // find first index such that f is true
        T mid = half(lo+hi+1);
        f(mid) ? lo = mid : hi = mid-1;
    }
    return lo;
}
template<class T> void remDup(vector<T>& v) {
    sort(all(v)); v.erase(unique(all(v)),end(v)); }

// INPUT
template<class A> void re(complex<A>& c);
template<class A, class B> void re(pair<A,B>& p);
template<class A> void re(vector<A>& v);
template<class A, size_t SZ> void re(array<A,SZ>& a);

template<class T> void re(T& x) { cin >> x; }
void re(db& d) { str t; re(t); d = stod(t); }
void re(ld& d) { str t; re(t); d = stold(t); }
template<class H, class... T> void re(H& h, T&... t) { re(h); re(t...); }

template<class A> void re(complex<A>& c) { A a,b; re(a,b); c = {a,b}; }
template<class A, class B> void re(pair<A,B>& p) { re(p.f,p.s); }
template<class A> void re(vector<A>& x) { trav(a,x) re(a); }
template<class A, size_t SZ> void re(array<A,SZ>& x) { trav(a,x) re(a); }

// TO_STRING
#define ts to_string
str ts(char c) { return str(1,c); }
str ts(const char* s) { return (str)s; }
str ts(str s) { return s; }
str ts(bool b) {
#ifdef LOCAL
    return b ? "true" : "false";
#else
    return ts((int)b);
#endif
}
template<class A> str ts(complex<A> c) {
    stringstream ss; ss << c; return ss.str(); }
str ts(vector<bool> v) {
    str res = "{"; F0R(i,sz(v)) res += char('0'+v[i]);
    res += "}"; return res; }
template<size_t SZ> str ts(bitset<SZ> b) {
    str res = ""; F0R(i,SZ) res += char('0'+b[i]);
    return res; }
template<class A, class B> str ts(pair<A,B> p);
template<class T> str ts(T v) { // containers with begin(), end()
#ifdef LOCAL
    bool fst = 1; str res = "{";
		for (const auto& x: v) {
			if (!fst) res += ", ";
			fst = 0; res += ts(x);
		}
		res += "}"; return res;
#else
    bool fst = 1; str res = "";
    for (const auto& x: v) {
        if (!fst) res += " ";
        fst = 0; res += ts(x);
    }
    return res;

#endif
}
template<class A, class B> str ts(pair<A,B> p) {
#ifdef LOCAL
    return "("+ts(p.f)+", "+ts(p.s)+")";
#else
    return ts(p.f)+" "+ts(p.s);
#endif
}

// OUTPUT
template<class A> void pr(A x) { cout << ts(x); }
template<class H, class... T> void pr(const H& h, const T&... t) {
    pr(h); pr(t...); }
void ps() { pr("\n"); } // print w/ spaces
template<class H, class... T> void ps(const H& h, const T&... t) {
    pr(h); if (sizeof...(t)) pr(" "); ps(t...); }

// DEBUG
void DBG() { cerr << "]" << endl; }
template<class H, class... T> void DBG(H h, T... t) {
    cerr << ts(h); if (sizeof...(t)) cerr << ", ";
    DBG(t...); }


//   #define LOCAL

#ifdef LOCAL // compile with -DLOCAL
#define dbg(...) cerr << "LINE(" << __LINE__ << ") -> [" << #__VA_ARGS__ << "]: [", DBG(__VA_ARGS__)
#else
#define dbg(...) 0
#endif

// FILE I/O
void setIn(str s) { freopen(s.c_str(),"r",stdin); }
void setOut(str s) { freopen(s.c_str(),"w",stdout); }
void unsyncIO() { ios_base::sync_with_stdio(0); cin.tie(0); }
void setIO(str s = "") {
    unsyncIO();
    // cin.exceptions(cin.failbit);
    // throws exception when do smth illegal
    // ex. try to read letter into int
    if (sz(s)) { setIn(s+".in"), setOut(s+".out"); } // for USACO
}

int main() {
    int x;
    re(x);
    vector<char> garland;
    F0R(i, x) {
        char c;
        re(c);
        garland.push_back(c);
    }

    int cases;
    re(cases);
    F0R(currentCase, cases) {
        int changed;
        char favoriteChar;
        re(changed, favoriteChar);

        // greatest poss. consec = amount changed
        int greatest = changed;

        // code
        int r = 0;
        int l = 0;
        while (r < garland.size()) {
            dbg(l, r, changed);
            if (changed >= 0) {
                if (garland[r] != favoriteChar) {
                    changed--;
                }
                r++;
            }
            if (changed < 0) {
                if (garland[l] != favoriteChar) {
                    changed++;
                }
                l++;
            }

            greatest = max(greatest, r-l);
        }

        cout << greatest << "\n";
    }
}

{% endhighlight %}

## Dynamic Programming

The dynamic programming method simply finds the maximum value for the garland, and has two parameters - the letter (or character) and the amount replaceable. For all test cases, we use the same DP array to find the max value.

{% highlight c++ linenos %}
#include <fstream>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <random>
#include <math.h>
#include <complex>
#include <set>
#include <string>
#include <bitset>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef double db;
typedef string str;

typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef pair<db,db> pd;

typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<db> vd;
typedef vector<str> vs;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<pd> vpd;

#define mp make_pair
#define f first
#define s second
#define sz(x) (int)(x).size()
#define all(x) begin(x), end(x)
#define rall(x) (x).rbegin(), (x).rend()
#define rsz resize
#define ins insert
#define ft front()
#define bk back()
#define pf push_front
#define pb push_back
#define eb emplace_back
#define lb lower_bound
#define ub upper_bound

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define trav(a,x) for (auto& a: x)

const int MOD = 1e9+7; // 998244353;
const int MX = 2e5+5;
const ll INF = 1e18;
const ld PI = acos((ld)-1);
const int xd[4] = {1,0,-1,0}, yd[4] = {0,1,0,-1};
//mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count());

template<class T> bool ckmin(T& a, const T& b) {
    return b < a ? a = b, 1 : 0; }
template<class T> bool ckmax(T& a, const T& b) {
    return a < b ? a = b, 1 : 0; }
constexpr int pct(int x) { return __builtin_popcount(x); }
constexpr int bits(int x) { return 31-__builtin_clz(x); } // floor(log2(x))
ll cdiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } // divide a by b rounded up
ll fdiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // divide a by b rounded down
ll half(ll x) { return fdiv(x,2); }

template<class T, class U> T fstTrue(T lo, T hi, U f) {
    hi ++; assert(lo <= hi); // assuming f is increasing
    while (lo < hi) { // find first index such that f is true
        T mid = half(lo+hi);
        f(mid) ? hi = mid : lo = mid+1;
    }
    return lo;
}
template<class T, class U> T lstTrue(T lo, T hi, U f) {
    lo --; assert(lo <= hi); // assuming f is decreasing
    while (lo < hi) { // find first index such that f is true
        T mid = half(lo+hi+1);
        f(mid) ? lo = mid : hi = mid-1;
    }
    return lo;
}
template<class T> void remDup(vector<T>& v) {
    sort(all(v)); v.erase(unique(all(v)),end(v)); }

// INPUT
template<class A> void re(complex<A>& c);
template<class A, class B> void re(pair<A,B>& p);
template<class A> void re(vector<A>& v);
template<class A, size_t SZ> void re(array<A,SZ>& a);

template<class T> void re(T& x) { cin >> x; }
void re(db& d) { str t; re(t); d = stod(t); }
void re(ld& d) { str t; re(t); d = stold(t); }
template<class H, class... T> void re(H& h, T&... t) { re(h); re(t...); }

template<class A> void re(complex<A>& c) { A a,b; re(a,b); c = {a,b}; }
template<class A, class B> void re(pair<A,B>& p) { re(p.f,p.s); }
template<class A> void re(vector<A>& x) { trav(a,x) re(a); }
template<class A, size_t SZ> void re(array<A,SZ>& x) { trav(a,x) re(a); }

// TO_STRING
#define ts to_string
str ts(char c) { return str(1,c); }
str ts(const char* s) { return (str)s; }
str ts(str s) { return s; }
str ts(bool b) {
#ifdef LOCAL
    return b ? "true" : "false";
#else
    return ts((int)b);
#endif
}
template<class A> str ts(complex<A> c) {
    stringstream ss; ss << c; return ss.str(); }
str ts(vector<bool> v) {
    str res = "{"; F0R(i,sz(v)) res += char('0'+v[i]);
    res += "}"; return res; }
template<size_t SZ> str ts(bitset<SZ> b) {
    str res = ""; F0R(i,SZ) res += char('0'+b[i]);
    return res; }
template<class A, class B> str ts(pair<A,B> p);
template<class T> str ts(T v) { // containers with begin(), end()
#ifdef LOCAL
    bool fst = 1; str res = "{";
		for (const auto& x: v) {
			if (!fst) res += ", ";
			fst = 0; res += ts(x);
		}
		res += "}"; return res;
#else
    bool fst = 1; str res = "";
    for (const auto& x: v) {
        if (!fst) res += " ";
        fst = 0; res += ts(x);
    }
    return res;

#endif
}
template<class A, class B> str ts(pair<A,B> p) {
#ifdef LOCAL
    return "("+ts(p.f)+", "+ts(p.s)+")";
#else
    return ts(p.f)+" "+ts(p.s);
#endif
}

// OUTPUT
template<class A> void pr(A x) { cout << ts(x); }
template<class H, class... T> void pr(const H& h, const T&... t) {
    pr(h); pr(t...); }
void ps() { pr("\n"); } // print w/ spaces
template<class H, class... T> void ps(const H& h, const T&... t) {
    pr(h); if (sizeof...(t)) pr(" "); ps(t...); }

// DEBUG
void DBG() { cerr << "]" << endl; }
template<class H, class... T> void DBG(H h, T... t) {
    cerr << ts(h); if (sizeof...(t)) cerr << ", ";
    DBG(t...); }

//    #define LOCAL

#ifdef LOCAL // compile with -DLOCAL
#define dbg(...) cerr << "LINE(" << __LINE__ << ") -> [" << #__VA_ARGS__ << "]: [", DBG(__VA_ARGS__)
#else
#define dbg(...) 0
#define assert(...) 0
#endif

// FILE I/O
void setIn(str s) { freopen(s.c_str(),"r",stdin); }
void setOut(str s) { freopen(s.c_str(),"w",stdout); }
void unsyncIO() { ios_base::sync_with_stdio(0); cin.tie(0); }
void setIO(str s = "") {
    unsyncIO();
    // cin.exceptions(cin.failbit);
    // throws exception when do smth illegal
    // ex. try to read letter into int
    if (sz(s)) { setIn(s+".in"), setOut(s+".out"); } // for USACO
}

int main() {
    int x;
    re(x);
    vector<char> garland;
    F0R(i, x) {
        char c;
        re(c);
        garland.push_back(c);
    }

    vector<vector<int>> dp(26, vector<int>(garland.size() + 1));

    F0R(letter, 26) {
        F0R(l, garland.size()) {
            int replaced = 0;
            FOR(r, l, garland.size()) {
                if (garland[r] != letter + 'a') {
                    replaced++;
                }
                assert(letter < 26);
                assert(replaced <= garland.size());
                dp[letter][replaced] = max(dp[letter][replaced], r - l + 1);
                dp[letter][replaced] = max(dp[letter][replaced], replaced);
            }
        }
        // max for letter
        FOR(k, 1, garland.size() + 1) {
            dp[letter][k] = max(dp[letter][k - 1], dp[letter][k]);
        }
    }

    int queries;
    re(queries);

    F0R(q, queries) {
        int changes;
        char letter;
        re(changes, letter);
        cout << dp[letter - 'a'][changes] << "\n";
    }

}
{% endhighlight %}
