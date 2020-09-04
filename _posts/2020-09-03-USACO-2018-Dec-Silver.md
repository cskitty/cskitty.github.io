---
title: "USACO 2018 Dec Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2018 Dec Silver

## Problem 1. Convention
[Convention](http://www.usaco.org/index.php?page=viewproblem2&cpid=858)

Farmer John is hosting a new bovine grass-eating convention at his farm!  
Cows from all over the world are arriving at the local airport to attend the convention and eat grass. Specifically, there are N cows arriving at the airport (1≤N≤105) and cow i arrives at time ti (0≤ti≤109). Farmer John has arranged M (1≤M≤105) buses to transport the cows from the airport. Each bus can hold up to C cows in it (1≤C≤N). Farmer John is waiting with the buses at the airport and would like to assign the arriving cows to the buses. A bus can leave at the time when the last cow on it arrives. Farmer John wants to be a good host and so does not want to keep the arriving cows waiting at the airport too long. What is the smallest possible value of the maximum waiting time of any one arriving cow if Farmer John coordinates his buses optimally? A cow’s waiting time is the difference between her arrival time and the departure of her assigned bus.  

It is guaranteed that MC≥N.  

INPUT FORMAT (file convention.in):  
The first line contains three space separated integers N, M, and C. The next line contains N space separated integers representing the arrival time of each cow.  
OUTPUT FORMAT (file convention.out):  
Please write one line containing the optimal minimum maximum waiting time for any one arriving cow.  
SAMPLE INPUT:  
```
6 3 2
1 1 10 14 4 3
```
SAMPLE OUTPUT:
```
4
```
If the two cows arriving at time 1 go in one bus, cows arriving at times 3 and 4 in the second, and cows arriving at times 10 and 14 in the third, the longest time a cow has to wait is 4 time units (the cow arriving at time 10 waits from time 10 to time 14).

Problem credits: Grace Cai

{% highlight C++ linenos %}

int N;
ll M, C;
ll ans = -1;

bool check(vector<ll> v, ll target) {
    ll currMax = 0;
    dbg(target);

    if (target == 1) {
        dbg('x');
    }

    ll i = 0;
    ll buses = 1;
    ll inBus = 0;

    F0R(j, v.size()) {
        if (inBus >= C || v[j] - v[i] > target) {
            buses++;
            i = j;
            inBus = 1;
        }
        else {
            currMax = max(currMax, v[j] - v[i]);
            inBus++;
        }

        if (buses > M) {
            dbg("out");
            return false;
        }
    }

    if (currMax > target) {
        dbg("out");
        return false;
    }
    ans = currMax;
    dbg("in");
    return true;
}

ll binary_search(vector<ll> x) {
    //ll max = x.end() - x.begin();
    ll max = x[x.size() - 1] - x[0];
    ll p = max;
    for (ll a = max; a >= 1; a /= 2) {
        while ((p - a) >= 0 && check(x, p - a)) p -= a;
    }
    return p;
}

int main() {

    setIO("convention");

    cin >> N >> M >> C;

    vector<ll> nums(N);

    F0R(i, N) cin >> nums[i];

    sort(all(nums));

    ll a = binary_search(nums);

    if (ans == -1 ) {
        cout << a;
    }
    else {
        cout << ans;
    }
}
{% endhighlight %}

## Problem 2. Convention II
[Convention II](http://www.usaco.org/index.php?page=viewproblem2&cpid=859)

Despite long delays in airport pickups, Farmer John's convention for cows interested in eating grass has been going well so far. It has attracted cows from all over the world.  
The main event of the conference, however, is looking like it might cause Farmer John some further scheduling woes. A very small pasture on his farm features a rare form of grass that is supposed to be the tastiest in the world, according to discerning cows. As a result, all of the N cows at the conference (1≤N≤105) want to sample this grass. This will likely cause long lines to form, since the pasture is so small it can only accommodate one cow at a time.  

Farmer John knows the time ai that each cow i plans to arrive at the special pasture, as well as the amount of time ti she plans to spend sampling the special grass, once it becomes her turn. Once cow i starts eating the grass, she spends her full time of ti before leaving, during which other arriving cows need to wait. If multiple cows are waiting when the pasture becomes available again, the cow with the highest seniority is the next to be allowed to sample the grass. For this purpose, a cow who arrives right as another cow is finishing is considered "waiting". Similarly, if a number of cows all arrive at exactly the same time while no cow is currently eating, then the one with highest seniority is the next to eat.  

Please help FJ compute the maximum amount of time any cow might possibly have to wait in line (between time ai and the time the cow begins eating).  

INPUT FORMAT (file convention2.in):  
The first line of input contains N. Each of the next N lines specify the details of the N cows in order of seniority (the most senior cow being first). Each line contains ai and ti for one cow. The ti's are positive integers each at most 104, and the ai's are positive integers at most 109.  
OUTPUT FORMAT (file convention2.out):  
Please print the longest potential waiting time over all the cows.  
SAMPLE INPUT:  
```
5
25 3
105 30
20 50
10 17
100 10
```
SAMPLE OUTPUT:
```
10
```
In this example, we have 5 cows (numbered 1..5 according to their order in the input). Cow 4 is the first to arrive (at time 10), and before she can finish eating (at time 27) cows 1 and 3 both arrive. Since cow 1 has higher seniority, she gets to eat next, having waited 2 units of time beyond her arrival time. She finishes at time 30, and then cow 3 starts eating, having waited for 10 units of time beyond her starting time. After a gap where no cow eats, cow 5 arrives and then while she is eating cow 2 arrives, eating 5 units of time later. The cow who is delayed the most relative to her arrival time is cow 3.  

Problem credits: Brian Dean  

{% highlight C++ linenos %}
int N;

struct cow {
    int arrive;
    int eat;
    int senior;
};

int main() {
    setIO("convention2");

    cin >> N;

    vector<cow> cows(N);

    F0R(i, N) {
        cin >> cows[i].arrive >> cows[i].eat;
        cows[i].senior = i;
    }

    // sort by 1. arrival time and then 2. seniority
    sort(all(cows), [](cow a, cow b) {if (a.arrive == b.arrive) return a.senior < b.senior; else return a.arrive < b.arrive;});

    // set the next UNUSED cow as 1 (first used cow = 0)
    int nextCow = 1;
    // priority queue based off seniority
    // Note: RHS is closer to top of queue (PRIORITY QUEUE RETURNS FALSE)
    auto comp = [](cow a, cow b) { return a.senior > b.senior; };
    priority_queue<cow, vector<cow>,  decltype(comp)> waiting(comp);

    // global time starts at cow 0 time
    int T = cows[0].arrive;
    int mxWait = 0;

    waiting.push(cows[0]);

    while (nextCow < N) {
         // eat cow; current cow
         cow eatCow = waiting.top();
         waiting.pop();

         // update wait time, mxWait w/ old time, update T
         mxWait = max(mxWait, T - eatCow.arrive);
         T += eatCow.eat;

        // add cows to queue (cows that are waiting by the time the current T arrives)
        while (nextCow < N && cows[nextCow].arrive <= T) {
            waiting.push(cows[nextCow]);
            nextCow++;
        }

        // if empty, no cows are waiting, so update world time to next cow's arrival
        if (waiting.empty()) {
            T = cows[nextCow].arrive;
            // push all cows with the arrival time, so when the loop continues, they're sorted by seniority
            while (nextCow < N && cows[nextCow].arrive <= T) {
                waiting.push(cows[nextCow]);
                nextCow++;
            }
        }

    }

    cout << mxWait;
}
{% endhighlight %}

## Problem 3. Mooyo Mooyo

[Mooyo Mooyo](http://www.usaco.org/index.php?page=viewproblem2&cpid=860)         

With plenty of free time on their hands (or rather, hooves), the cows on Farmer John's farm often pass the time by playing video games. One of their favorites is based on a popular human video game called Puyo Puyo; the cow version is of course called Mooyo Mooyo.  
The game of Mooyo Mooyo is played on a tall narrow grid N cells tall (1≤N≤100) and 10 cells wide. Here is an example with N=6:  
```
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
```
Each cell is either empty (indicated by a 0), or a haybale in one of nine different colors (indicated by characters 1..9). Gravity causes haybales to fall downward, so there is never a 0 cell below a haybale.   

Two cells belong to the same connected region if they are directly adjacent either horizontally or vertically, and they have the same nonzero color. Any time a connected region exists with at least K cells, its haybales all disappear, turning into zeros. If multiple such connected regions exist at the same time, they all disappear simultaneously. Afterwards, gravity might cause haybales to fall downward to fill some of the resulting cells that became zeros. In the resulting configuration, there may again be connected regions of size at least K cells. If so, they also disappear (simultaneously, if there are multiple such regions), then gravity pulls the remaining cells downward, and the process repeats until no connected regions of size at least K exist.   

Given the state of a Mooyo Mooyo board, please output a final picture of the board after these operations have occurred.  

INPUT FORMAT (file mooyomooyo.in):  
The first line of input contains N and K (1≤K≤10N). The remaining N lines specify the initial state of the board.
OUTPUT FORMAT (file mooyomooyo.out):  
Please output N lines, describing a picture of the final board state.  
SAMPLE INPUT:  
```
6 3
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
```
SAMPLE OUTPUT:
```
0000000000
0000000000
0000000000
0000000000
1054000000
2254500000
```
In the example above, if K=3, then there is a connected region of size at least K with color 1 and also one with color 2. Once these are simultaneously removed, the board temporarily looks like this:
```
0000000000
0000000300
0054000300
1054500030
2200000000
0000000003
```
Then, gravity takes effect and the haybales drop to this configuration:
```
0000000000
0000000000
0000000000
0000000000
1054000300
2254500333
```
Again, there is a region of size at least K (with color 3). Removing it yields the final board configuration:
```
0000000000
0000000000
0000000000
0000000000
1054000000
2254500000
```
Problem credits: Brian Dean


{% highlight C++ linenos %}

const int MaX = 101;
const int rowM = 10;
int N, M;
vector<vector<int>> board(MaX, vector<int>(rowM));
int currSize = 0;
vector<vector<int>> visited(MaX, vector<int> (rowM));

bool fall() {

    bool flag = false;
    for (int i = N - 2; i >= 0; i--) {
        // col
        for (int j = 0; j < 10; j++) {
            int r = i;
            while (r + 1 < N && board[r + 1][j] == 0 && board[r][j] != 0) {
                flag = true;
                board[r + 1][j] = board[r][j];
                board[r][j] = 0;
                r++;
            }
        }
    }
    return flag;
}
vector<pair<int, int>> addVec;

void ff(int r, int c, int color) {
    if (r > N || r < 0 || c > 10 || c < 0 || visited[r][c] || board[r][c] != color) {
        return;
    }

    addVec.push_back({r, c});
    currSize++;
    visited[r][c] = 1;

    ff(r + 1, c, color);
    ff(r - 1, c, color);
    ff(r, c + 1, color);
    ff(r, c - 1, color);

}


bool update() {
    bool flag = false;
    F0R(i, N) {
        fill(visited[i].begin(), visited[i].end(), 0);
    }
    F0R(i, N) {
        F0R(j, 10) {
            if (! visited[i][j] && board[i][j] != 0) {
                currSize = 0;
                addVec.clear();

                ff(i, j, board[i][j]);
                if (currSize >= M) {
                    flag = true;
                    F0R(k, addVec.size()) {
                        board[addVec[k].f][addVec[k].s] = 0;
                    }
                }

            }
        }
    }

    return flag;
}

int main() {
    setIO("mooyomooyo");

    cin >> N >> M;

    F0R(i, N) {
        F0R(j, 10) {
            char V;
            cin >> V;
            board[i][j] = (int) V - '0';
        }
    }

    bool flag = true;
    while (flag) {
        flag = update();
        fall();
    }

    F0R(i, N) {
        F0R(j, 10) {
            cout << board[i][j];
        }
        cout << endl;
    }

}

{% endhighlight %}
