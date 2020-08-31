---
title: "USACO 2017 Open Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2017 Open Silver

## Problem 1. Paired Up

[Paired Up](http://usaco.org/index.php?page=viewproblem2&cpid=738)

Farmer John finds that his cows are each easier to milk when they have another cow nearby for moral support. He therefore wants to take his M cows (M≤1,000,000,000, M even) and partition them into M/2 pairs. Each pair of cows will then be ushered off to a separate stall in the barn for milking. The milking in each of these M/2 stalls will take place simultaneously.  
To make matters a bit complicated, each of Farmer John's cows has a different milk output. If cows of milk outputs A and B are paired up, then it takes a total of A+B units of time to milk them both.  

Please help Farmer John determine the minimum possible amount of time the entire milking process will take to complete, assuming he pairs the cows up in the best possible way.  

INPUT FORMAT (file pairup.in):  
The first line of input contains N (1≤N≤100,000). Each of the next N lines contains two integers x and y, indicating that FJ has x cows each with milk output y (1≤y≤1,000,000,000). The sum of the x's is M, the total number of cows.  
OUTPUT FORMAT (file pairup.out):  
Print out the minimum amount of time it takes FJ's cows to be milked, assuming they are optimally paired up.  
SAMPLE INPUT:  
```
3
1 8
2 5
1 2
```
SAMPLE OUTPUT:
```
10
```
Here, if the cows with outputs 8+2 are paired up, and those with outputs 5+5 are paired up, the both stalls take 10 units of time for milking. Since milking takes place simultaneously, the entire process would therefore complete after 10 units of time. Any other pairing would be sub-optimal, resulting in a stall taking more than 10 units of time to milk.

Problem credits: Brian Dean
{% highlight c++ linenos %}

ll N;

int main() {
    setIO("pairup");

    cin >> N;

    vector<pair<ll, ll>> cows(N);

    F0R(i, N) {
        int a, b;
        cin >> a >> b;
        cows[i] = {a, b};
    }

    int currL = 0;
    int countL = 0;
    int currR = N - 1;
    int countR = 0;
    ll ans = 0;

    sort(all(cows), [](pair<ll, ll> a, pair<ll, ll> b) {return a.s < b.s;});

    while (currL <= currR) {

        ans = max(ans, cows[currL].s + cows[currR].s);
        countL++, countR++;
        if (countL > cows[currL].f) {
            currL++;
            countL = 0;
        }
        if (countR > cows[currR].f) {
            currR--;
            countR = 0;
        }
    }

    cout << ans;

}

{% endhighlight %}

## Problem 2. Bovine Genomics

[Bovine Genomics](http://usaco.org/index.php?page=viewproblem2&cpid=739)

Farmer John owns N cows with spots and N cows without spots. Having just completed a course in bovine genetics, he is convinced that the spots on his cows are caused by mutations in the bovine genome.  
At great expense, Farmer John sequences the genomes of his cows. Each genome is a string of length M built from the four characters A, C, G, and T. When he lines up the genomes of his cows, he gets a table like the following, shown here for N=3:  

Positions:    1 2 3 4 5 6 7 ... M  

Spotty Cow 1: A A T C C C A ... T  
Spotty Cow 2: G A T T G C A ... A  
Spotty Cow 3: G G T C G C A ... A  

Plain Cow 1:  A C T C C C A ... G  
Plain Cow 2:  A G T T G C A ... T  
Plain Cow 3:  A G T T C C A ... T  
Looking carefully at this table, he surmises that positions 2 and 4 are sufficient to explain spottiness. That is, by looking at the characters in just these two positions, Farmer John can predict which of his cows are spotty and which are not (for example, if he sees G and C, the cow must be spotty).  

Farmer John is convinced that spottiness can be explained not by just one or two positions in the genome, but by looking at a set of three distinct positions. Please help him count the number of sets of three distinct positions that can each explain spottiness.  

INPUT FORMAT (file cownomics.in):  
The first line of input contains N (1≤N≤500) and M (3≤M≤50). The next N lines each contain a string of M characters; these describe the genomes of the spotty cows. The final N lines describe the genomes of the plain cows.
OUTPUT FORMAT (file cownomics.out):  
Please count the number of sets of three distinct positions that can explain spottiness. A set of three positions explains spottiness if the spottiness trait can be predicted with perfect accuracy among Farmer John's population of cows by looking at just those three locations in the genome.  
SAMPLE INPUT:  
```
3 8
AATCCCAT
GATTGCAA
GGTCGCAA
ACTCCCAG
ACTCGCAT
ACTTCCAT
```
SAMPLE OUTPUT:
```
22
```
Problem credits: Brian Dean

{% highlight c++ linenos %}

ll N, M;

int main() {
    setIO("cownomics");

    cin >> N >> M;

    vector<string> spotty(N);
    vector<string> plain(N);

    F0R(i, N) {
        cin >> spotty[i];
    }

    F0R(i, N) {
        cin >> plain[i];
    }

    map<char, int> dict = { {'A',0}, {'C', 1}, {'G', 2}, {'T', 3} };

    int ans = 0;
    vector<string> v(N+N);
    F0R(i, M - 2) {
        FOR(j, i + 1, M) {
            FOR(k, j + 1, M) {
                    vector<bool> spotVal(64);
                    F0R(l, N) {
                        spotVal[(dict[spotty[l][i]] * 16) + (dict[spotty[l][j]] * 4) + dict[spotty[l][k]]] = true;
                    }

                    ans++;
                    F0R(l, N) {
                        if (spotVal[(dict[plain[l][i]] * 16) + (dict[plain[l][j]] * 4) + dict[plain[l][k]]]) {
                            ans--;
                            break;
                        }
                    }
            }
        }
    }

    cout << ans;
}

{% endhighlight %}


## Problem 3. Where's Bessie?

[Where's Bessie?](http://usaco.org/index.php?page=viewproblem2&cpid=740)

Always known for being quite tech-savy, Farmer John is testing out his new automated drone-mounted cow locator camera, which supposedly can take a picture of his field and automatically figure out the location of cows. Unfortunately, the camera does not include a very good algorithm for finding cows, so FJ needs your help developing a better one.  
The overhead image of his farm taken by the camera is described by an N×N grid of characters, each in the range A…Z, representing one of 26 possible colors. Farmer John figures the best way to define a potential cow location (PCL) is as follows: A PCL is a rectangular sub-grid (possibly the entire image) with sides parallel to the image sides, not contained within any other PCL (so no smaller subset of a PCL is also a PCL). Furthermore, a PCL must satisfy the following property: focusing on just the contents of the rectangle and ignoring the rest of the image, exactly two colors must be present, one forming a contiguous region and one forming two or more contiguous regions.  

For example, a rectangle with contents  

AAAAA  
ABABA  
AAABB     
would constitute a PCL, since the A's form a single contiguous region and the B's form more than one contiguous region. The interpretation is a cow of color A with spots of color B.  

A region is "contiguous" if you can traverse the entire region by moving repeatedly from one cell in the region to another cell in the region taking steps up, down, left, or right.  

Given the image returned by FJ's camera, please count the number of PCLs.  

INPUT FORMAT (file where.in):  
The first line of input contains N, the size of the grid (1≤N≤20). The next N lines describe the image, each consisting of N characters.  
OUTPUT FORMAT (file where.out):  
Print a count of the number of PCLs in the image.  
SAMPLE INPUT:  
```
4
ABBC
BBBC
AABB
ABBC
```
SAMPLE OUTPUT:
```
2
```
In this example, the two PCLs are the rectangles with contents

ABB  
BBB  
AAB  
ABB  
and  

BC  
BC  
BB  
BC  

{% highlight c++ linenos %}
const int MaX = 20;
char grid[MaX][MaX];
int N;
bool visited[MaX][MaX];
int currentSize = 0;

void floodfill(int l, int r, int color, int x1, int x2, int y1, int y2) {
    if (r < x1 || r > x2|| l < y1 || l > y2|| visited[l][r] || grid[l][r] != (color - 'A')) {
        return;
    }

    visited[l][r] = true;

    floodfill(l + 1, r, color, x1, x2, y1, y2);
    floodfill(l - 1, r, color, x1, x2, y1, y2);
    floodfill(l, r + 1, color, x1, x2, y1, y2);
    floodfill(l, r - 1, color, x1, x2, y1, y2);
}

bool isPCL(int x1, int y1, int x2, int y2) {
    int colorNum = 0;
    int colorCount[26] = {0};

    FOR(i, x1, x2 + 1) {
        FOR(j, y1, y2 + 1) {
            visited[i][j] = false;
        }
    }

    FOR(i, x1, x2 + 1) {
        FOR(j, y1, y2 + 1) {
            if (! visited[i][j]) {
                int color
            }

            if (! newVisited[i][j]) {
                currentSize = 0;
                if (color == 1) {
                    aCount = 1;
                    a = grid[i][j];
                }
                else if (b == '1' && grid[i][j] != a) {
                    bCount = 1;
                    b = grid[i][j];
                }
                else {
                    if (grid[i][j] == a) {
                        aCount++;
                    }
                    else if (grid[i][j] == b) {
                        bCount++;
                    }
                    else return false;
                }
                floodfill(i, j, color, newVisited, newGrid, grid[i][j], x1, x2, y1, y2);

                color++;
                if (bCount > 1 && aCount > 1) {
                    return false;
                }
            }
        }
    }


    if ((aCount == 1 && bCount > 1) || (aCount > 1 && bCount == 1)) {
        return true;
    }
    return false;
}

bool contains(int x1, int x2, int x3, int x4, int y1, int y2, int y3, int y4) {
    // x1 contain x2
    return (x1 >= x2 && y1 >= y2 && x3 <= x4 && y3 <= y4);
}

int main() {
    setIO("where");

    cin >> N;
    F0R(i, N) {
        F0R(j, N) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> ans;
    F0R(x1, N) {
        F0R(y1, N) {

            FOR(x2, x1 + 1, N) {
                FOR(y2, y1 + 1, N) {

                    if (isPCL(x1,y1,x2,y2)) {
                        ans.push_back({x1, y1, x2, y2});
                    }

                }
            }
        }
    }

    int count = 0;
    F0R(i, ans.size()) {
        bool flag = false;
        F0R(j, ans.size()) {
            if (i != j && contains(ans[i][0], ans[j][0], ans[i][2], ans[j][2], ans[i][1], ans[j][1], ans[i][3], ans[i][3])) {
                flag = true;
                break;
            }
        }

        if (! flag) {
            count++;
        }
    }

    cout << count;
}
{% endhighlight %}
