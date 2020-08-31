---
title: "USACO 2017 Dec Silver"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
---

# USACO 2017 Dec Silver

## Problem 1. My Cow Ate My Homework

[My Cow Ate My Homework](http://usaco.org/index.php?page=viewproblem2&cpid=762)

In your bovine history class, you have been given a rather long homework assignment with N questions (3≤N≤100,000), each graded with an integer score in the range 0...10,000. As is often customary, your teacher plans to assign a final grade by discarding a question on which you received the lowest score and then averaging the remaining scores together. Unfortunately, your pet cow Bessie has just eaten your answers to the first K questions! (K could be as small as 1 or as large as N−2).  
After copious explanation, your teacher finally believes your story, and agrees to grade the remaining non-eaten part of the assignment the same way as before -- by removing the lowest-scoring question (or one such question, in the event of a tie) and averaging the rest.  

Please output all values of K which would have earned you the maximum possible score according to this grading scheme, in sorted order.  

INPUT FORMAT (file homework.in):  
The first line of input contains N, and the next line contains the scores on the N homework questions.  
OUTPUT FORMAT (file homework.out):  
Please output, one value per line, all values of K which would have earned you the maximum possible score.  
SAMPLE INPUT:  
```
5
3 1 9 2 7
```
SAMPLE OUTPUT:
```
2
```
If Bessie eats the first two questions, then the remaining scores are 9, 2, and 7. Removing the minimum and averaging, we get a final grade of 8, which is the highest possible.  

Problem credits: Brian Dean  

{% highlight c++ linenos %}

ll N, M;

int main() {
    setIO("homework");

    cin >> N;

    vector<int> cows(N);

    F0R(i, N) cin >> cows[i];

    int currSum = 0;
    // value
    int smallest = 0;
    vector<int> ans;
    float ansVal = 0;

    for (int i = N - 2; i >= 0; i--){
        currSum += cows[i + 1];
        if (cows[i + 1] <= smallest || smallest == 0) {
            currSum = currSum + smallest - cows[i + 1];
            smallest = cows[i + 1];
        }

        float A = (float) currSum / (float) (N - i - 2);
        if (A > ansVal) {
            ans.clear();
            ans.pb(i + 1);
            ansVal = A;
        }
        else if (A == ansVal) {
            ans.pb(i + 1);
        }

    }


    for (int i = ans.size() - 1; i >= 0; i--) {
        cout << ans[i] << endl;
    }
}
{% endhighlight %}

## Problem 2. Milk Measurement

[Milk Measurement](http://usaco.org/index.php?page=viewproblem2&cpid=763)

Each of Farmer John's cows initially produces G gallons of milk per day (1≤G≤109). Since the milk output of a cow is known to potentially change over time, Farmer John decides to take periodic measurements of milk output and write these down in a log book. Entries in his log look like this:  
35 1234 -2  
14 2345 +3  
The first entry indicates that on day 35, cow #1234's milk output was 2 gallons lower than it was when last measured. The next entry indicates that on day 14, cow #2345's milk output increased by 3 gallons from when it was last measured. Farmer John has only enough time to make at most one measurement on any given day. Unfortunately, he is a bit disorganized, and doesn't necessarily write down his measurements in chronological order.  

To keep his cows motivated, Farmer John proudly displays on the wall of his barn the picture of whichever cow currently has the highest milk output (if several cows tie for the highest milk output, he displays all of their pictures).   Please determine the number of days on which Farmer John would have needed to change this display.  

Note that Farmer John has a very large herd of cows, so although some of them are noted in his log book as changing their milk production, there are always plenty of other cows around whose milk output level remains at G gallons.  

INPUT FORMAT (file measurement.in):  
The first line of input contains the number of measurements N that Farmer John makes (1≤N≤100,000), followed by G. Each of the next N lines contains one measurement, in the format above, specifying a day (an integer in the range 1…106), the integer ID of a cow (in the range 1…109), and the change in her milk output since it was last measured (a nonzero integer). Each cow's milk output will always be in the range 0…109.  
OUTPUT FORMAT (file measurement.out):  
Please output the number of days on which Farmer John needs to adjust his motivational display.  
SAMPLE INPUT:  
```
4 10
7 3 +3
4 2 -1
9 3 -1
1 1 +2
```
SAMPLE OUTPUT:
```
3
```
Problem credits: Brian Dean
{% highlight c++ linenos %}


ll N, M;

struct day {
    int da;
    int id;
    int val;
};

int main() {
    setIO("measurement");

    cin >> N >> M;

    vector<day> days(N);

    F0R(i, N) {
        cin >> days[i].da >> days[i].id;

        char v;
        int val;
        cin >> v >> val;
        if (v == '+') {
            days[i].val = val;
        }
        if (v == '-') {
            days[i].val = 0 - val;
        }
    }

    sort(all(days), [](day a, day b) {return a.da < b.da;});

    map<int, int, greater<int>> hist;
    hist[0] = N + 1;

    map<int, int> cows;

    int ans = 0;

    F0R(i, N) {
        // maxVal = old maxValue
        int maxVal = hist.begin()->f;

        // get rid of old value count in histogram
        hist[cows[days[i].id]]--;
        // check if it was the top cow
        bool isOldTop = cows[days[i].id] == hist.begin()->f;
        // check for other cows with same output
        int oldVal = cows[days[i].id];
        int oldCount = hist[oldVal];

        // if the milk output isn't relevant (it was the only cow with that amount), erase
        if (hist[cows[days[i].id]] == 0) {
            hist.erase(cows[days[i].id]);
        }

        // assign new value and update histogram
        cows[days[i].id] += days[i].val;
        hist[cows[days[i].id]]++;

        // was originally the old top
        if (isOldTop) {
            // fir/sec = new top
            int fir = hist.begin()->f, sec = hist.begin()->s;

            // not the new top anymore, other cows are top
            if ((cows[days[i].id] < fir)) {
                ans++;
            }
            // cow fell down (was only top), and now is on the same level as other cows (but still top)
            else if (oldVal < fir && oldCount >= 1) {
                ans++;
            }
            // was top (with other cows), raised up to be only cow
            else if (oldVal > fir && (sec > 1)) {
                ans++;
            }
            // fir = new top, assign maxVal
        }
        else {
            // was not originally top, now rose to top
            if (cows[days[i].id] >= maxVal) {
                ans++;
            }
        }
    }

    cout << ans;
}

{% endhighlight %}


## Problem 3. The Bovine Shuffle

[The Bovine Shuffle](http://usaco.org/index.php?page=viewproblem2&cpid=764)

Convinced that happy cows generate more milk, Farmer John has installed a giant disco ball in his barn and plans to teach his cows to dance!  
Looking up popular cow dances, Farmer John decides to teach his cows the "Bovine Shuffle". The Bovine Shuffle consists of his N cows (1≤N≤100,000) lining up in a row in some order, then performing successive "shuffles", each of which potentially re-orders the cows. To make it easier for his cows to locate themselves, Farmer John marks the locations for his line of cows with positions 1…N, so the first cow in the lineup will be in position 1, the next in position 2, and so on, up to position N.  

A shuffle is described with N numbers, a1…aN, where a cow in position i moves to position ai during the shuffle (and so, each ai is in the range 1…N). Every cow moves to its new location during the shuffle. Unfortunately, all the ai's are not necessarily distinct, so multiple cows might try to move to the same position during a shuffle, after which they will move together for all remaining shuffles.  

Farmer John notices that some positions in his lineup contain cows in them no matter how many shuffles take place. Please help him count the number of such positions.  

INPUT FORMAT (file shuffle.in):  
The first line of input contains N, the number of cows. The next line contains the N integers a1…aN.  
OUTPUT FORMAT (file shuffle.out):  
Please output the number of positions that will always contain cows, no matter how many shuffles take place.  
SAMPLE INPUT:  
```
4
3 2 1 3
```
SAMPLE OUTPUT:
```
3
```
Problem credits: Brian Dean

{% highlight c++ linenos %}
const int MaX = 100001;
int N, M;
vector<int> adj(MaX);



int main() {
    setIO("shuffle");

    cin >> N;

    vector<int> order(N + 1);



    F0R(i, N) {
        cin >> adj[i + 1];
        order[adj[i + 1]]++;
    }
    int ans = N;
    queue<int> myQ;
    FOR(i, 1, N + 1) {
        if (order[i] == 0) {
            myQ.push(i);
        }
    }
    while (myQ.size() > 0) {
        int curr = myQ.front();
        myQ.pop();
        ans--;
        order[adj[curr]]--;
        if (order[adj[curr]] == 0) {
            myQ.push(adj[curr]);
        }
    }
    cout << ans;
}
{% endhighlight %}
