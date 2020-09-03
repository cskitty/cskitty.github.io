---
title: "USACO 2018 Open Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2018 Open Silver

## Problem 1. Out of Sorts
[Out of Sorts](http://www.usaco.org/index.php?page=viewproblem2&cpid=831)  

Keeping an eye on long term career possibilities beyond the farm, Bessie the cow has started learning algorithms from various on-line coding websites.
Her favorite algorithm thus far is "bubble sort". Here is Bessie's implementation, in cow-code, for sorting an array A of length N.  
```
sorted = false
while (not sorted):
   sorted = true
   moo
   for i = 0 to N-2:
      if A[i+1] < A[i]:
         swap A[i], A[i+1]
         sorted = false
```
Apparently, the "moo" command in cow-code does nothing more than print out "moo". Strangely, Bessie seems to insist on including it at various points in her code.  

Given an input array, please predict how many times "moo" will be printed by Bessie's code.  

INPUT FORMAT (file sort.in):  
The first line of input contains N (1≤N≤100,000). The next N lines describe A[0]…A[N−1], each being an integer in the range 0…109. Input elements are not guaranteed to be distinct.  
OUTPUT FORMAT (file sort.out):  
Print the number of times "moo" is printed.  
SAMPLE INPUT:  
```
5
1
5
3
8
2
```
SAMPLE OUTPUT:
```
4
```
Problem credits: Brian Dean

{% highlight C++ linenos %}
int N;
int main() {
    setIO("sort");

    cin >> N;

    vector<pair<int, int>> arr(N);

    F0R(i, N) {
        cin >> arr[i].f;
        arr[i].s = i;
    }

    int ans = 0;

    sort(all(arr), [](pair<int, int> a, pair<int, int> b) {if (a.f == b.f) return a.s < b.s; else return a.f < b.f;});

    F0R(i, N) {
        ans = max(ans, arr[i].s - i);
    }

    cout << ans + 1;
}
{% endhighlight %}


## Problem 2. Lemonade Line
[Lemonade Line](http://usaco.org/index.php?page=viewproblem2&cpid=835)  

It's a hot summer day out on the farm, and Farmer John is serving lemonade to his N cows! All N cows (conveniently numbered 1…N) like lemonade, but some of them like it more than others. In particular, cow i is willing to wait in a line behind at most wi cows to get her lemonade. Right now all N cows are in the fields, but as soon as Farmer John rings his cowbell, the cows will immediately descend upon FJ's lemonade stand. They will all arrive before he starts serving lemonade, but no two cows will arrive at the same time. Furthermore, when cow i arrives, she will join the line if and only if there are at most wi cows already in line.  
Farmer John wants to prepare some amount of lemonade in advance, but he does not want to be wasteful. The number of cows who join the line might depend on the order in which they arrive. Help him find the minimum possible number of cows who join the line.  

INPUT FORMAT (file lemonade.in):  
The first line contains N, and the second line contains the N space-separated integers w1,w2,…,wN. It is guaranteed that 1≤N≤105, and that 0≤wi≤109 for each cow i.   
OUTPUT FORMAT (file lemonade.out):  
Print the minimum possible number of cows who might join the line, among all possible orders in which the cows might arrive.  
SAMPLE INPUT:
```  
5
7 1 400 2 2
```
SAMPLE OUTPUT:
```
3
```
In this setting, only three cows might end up in line (and this is the smallest possible). Suppose the cows with w=7 and w=400 arrive first and wait in line. Then the cow with w=1 arrives and turns away, since 2 cows are already in line. The cows with w=2 then arrive, one staying and one turning away.

Problem credits: Dhruv Rohatgi


{% highlight C++ linenos %}
int N;

int main() {
    setIO("lemonade");

    cin >> N;

    vector<int> cows(N);

    F0R(i, N) cin >> cows[i];

    sort(all(cows), greater<int>());

    int amt = 0;

    F0R(i, N) {
        if (cows[i] >= amt) {
            amt++;
        }
        else {
            break;
        }
    }

    cout << amt;
}
{% endhighlight %}



## Problem 3. Multiplayer Moo
[Multiplayer Moo](http://usaco.org/index.php?page=viewproblem2&cpid=836)  

The cows have come up with a creative new game, surprisingly giving it the least creative name possible: "Moo".
The game of Moo is played on an N×N grid of square cells, where a cow claims a grid cell by yelling "moo!" and writing her numeric ID number in the cell.  

At the end of the game, every cell contains a number. At this point, a cow wins the game if she has created a region of connected cells as least as large as any other region. A "region" is defined as a group of cells all with the same ID number, where every cell in the region is directly adjacent to some other cell in the same region either above, below, left, or to the right (diagonals don't count).  

Since it is a bit boring to play as individuals, the cows are also interested in pairing up to play as teams. A team of two cows can create a region as before, but now the cells in the region can belong to either of the two cows on the team.  

Given the final state of the game board, please help the cows compute the number of cells belonging to the largest region that any one cow owns, and the number of cells belonging to the largest region that can be claimed by a two-cow team. A region claimed by a two-cow team only counts if it contains the ID numbers of both cows on the team, not just one of the cows.  

INPUT FORMAT (file multimoo.in):  
The first line of input contains N (1≤N≤250). The next N lines each contain N integers (each in the range 0…106), describing the final state of the game board. At least two distinct ID numbers will be present in the board.  
OUTPUT FORMAT (file multimoo.out):  
The first line of output should describe the largest region size claimed by any single cow, and the second line of output should describe the largest region size claimed by any team of two cows.  
SAMPLE INPUT:  
```
4
2 3 9 3
4 9 9 1
9 9 1 7
2 1 1 9
```
SAMPLE OUTPUT:
``
5
10
```
In this example, the largest region for a single cow consists of five 9s. If cows with IDs 1 and 9 team up, they can form a region of size 10.

Problem credits: Brian Dean


{% highlight C++ linenos %}
int N;

const int MaX = 255;
map<int, int> regIDtoColor;
map<int, int> regIDtoSize;
int grid[MaX][MaX];
int maxColor = 0;

class MyGraph {

public:

   // construct a vector of vectors to represent an adjacency list
   map<int, set<int>> m_adj;
   set<int> m_nodes;
   map<int, int> m_regID;

   void addEdge(int a, int b) {
       m_nodes.insert(a);
       m_nodes.insert(b);

       m_adj[a].insert(b);
       m_adj[b].insert(a);
   }

   void setID(int a, int id) {
       m_regID[a] = id;
   }

   int regID(int a) {
       return m_regID[a];
   }

   int bfs(int nodeID, int regID) {
       // return size 0 if it is already visited
       if (m_regID[nodeID] > 0) {
           return 0;
       }

       queue<int> myQueue;
       myQueue.push(nodeID);
       int size = 0;

       while (myQueue.size() > 0) {
           int curr = myQueue.front();

           myQueue.pop();
           if (m_regID[curr] == 0) {
               size++;
           }
           else {
               continue;
           }

           m_regID[curr] = regID;


           for (auto j : m_adj[curr]) {
               if (m_regID[j] == 0) {
                   myQueue.push(j);
               }
           }
       }

       return size;
   }

   int bfs2(int nodeID, int regID) {

       queue<int> myQueue;
       myQueue.push(nodeID);
       int size = 0;

       while (myQueue.size() > 0) {
           int curr = myQueue.front();
           myQueue.pop();
           if (m_regID[curr] == 0) {
               size += regIDtoSize[curr];
           }
           else {
               continue;
           }


           m_regID[curr] = regID;
           for (auto j : m_adj[curr]) {
               if (m_regID[j] == 0) {
                   myQueue.push(j);
               }
           }
       }

       return size;
   }

};



int main() {
   setIO("multimoo");

   cin >> N;

   set<int> colors;

   F0R(i, N) {
       F0R(j, N) {
           cin >> grid[i][j];
           colors.insert(grid[i][j]);
       }
   }

   map<int, MyGraph> G1;


   // visit the matrix & create graphs for all colors
   F0R(i, N) {
       F0R(j, N) {
           int color = grid[i][j];
           int node = i * N + j;

           // check south neighbor for same color
           if (i + 1 < N && grid[i + 1][j] == color) {
               int southNeighbor = (i + 1) * N + j;
               G1[color].addEdge(node, southNeighbor);
           }
           // check right neighbor
           if (j + 1 < N && grid[i][j + 1] == color){
               int rightNeighbor = (i) * N + (j + 1);
               G1[color].addEdge(node, rightNeighbor);
           }
           // left and up already covered by prev node (2d rectangular grid)
       }
   }

   int regID = 1;
   int ans = 0;

   F0R(i, N) {
       F0R(j, N) {
           int color = grid[i][j];
           regIDtoColor[regID] = color;
           int regSize = G1[color].bfs(i*N + j, regID);
           if (regSize > 0) {
               regIDtoSize[regID] = regSize;
               ans = max(ans, regIDtoSize[regID]);
               regID++;
           }
       }
   }

   map<pair<int, int>, MyGraph> G2;

   F0R(i, N) {
       F0R(j, N) {
           int c1 = grid[i][j];

           if (i + 1 < N && grid[i + 1][j] != c1) {
               int c2 = grid[i + 1][j];

               int reg1 = G1[c1].regID(i * N + j);
               int reg2 = G1[c2].regID((i + 1) * N + j);

               if (c1 < c2) {
                   swap(c1, c2);
               }

               pair<int, int> c1c2 = mp(c1, c2);
               G2[c1c2].addEdge(reg1, reg2);
           }

           c1 = grid[i][j];
           // check right neighbor
           if (j + 1 < N && grid[i][j + 1] != c1) {
               int c2 = grid[i][j + 1];

               int reg1 = G1[c1].regID(i * N + j);
               int reg2 = G1[c2].regID(i * N + (j + 1));

               if (c1 < c2) {
                   swap(c1, c2);
               }

               G2[mp(c1, c2)].addEdge(reg1, reg2);

           }

       }
   }


   int ans1 = 0;

   int regID2 = 1;
   for (auto v : G2) {
       for (auto n : v.s.m_nodes) {
           int curr = v.s.bfs2(n, regID2);
           ans1 = max(ans1, curr);
           regID2++;
       }
   }

   cout << ans << endl;
   cout << ans1;
}

{% endhighlight %}
