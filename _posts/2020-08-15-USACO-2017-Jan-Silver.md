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

     vector<ll> onStage;
     ll i = 0;
     ll time = 0;
     while (i < v.size()) {
         while (onStage.size() < target) {
             onStage.push_back(v[i]);
             i++;
         }

         auto sub = min_element(all(onStage));
         ll min = * sub;
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
     time += * max_element(all(onStage));
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

## Problem 2. Hoof, Paper, Scissors

[Hoof, Paper, Scissors](http://usaco.org/index.php?page=viewproblem2&cpid=691)

You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".  
The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each-other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.  

Farmer John wants to play against his prize cow, Bessie, at N games of "Hoof, Paper, Scissors" (1≤N≤100,000). Bessie, being an expert at the game, can predict each of FJ's gestures before he makes it. Unfortunately, Bessie, being a cow, is also very lazy. As a result, she tends to play the same gesture multiple times in a row. In fact, she is only willing to switch gestures at most once over the entire set of games. For example, she might play "hoof" for the first x games, then switch to "paper" for the remaining N−x games.  

Given the sequence of gestures FJ will be playing, please determine the maximum number of games that Bessie can win.  

INPUT FORMAT (file hps.in):  
The first line of the input file contains N.  
The remaining N lines contains FJ's gestures, each either H, P, or S.  

OUTPUT FORMAT (file hps.out):  
Print the maximum number of games Bessie can win, given that she can only change gestures at most once.  
SAMPLE INPUT:  
```
5
P
P
H
P
S
```
SAMPLE OUTPUT:
```
4
```
Problem credits: Mark Chen and Brian Dean
{% highlight c++ linenos %}
int N;

struct hps {
    int pap;
    int hoof;
    int sci;
};

int main() {
    setIO("hps");

    cin >> N;

    vector<hps> prefix(N + 1);

    prefix[0] = {0, 0, 0};

    F0R(i, N) {
        prefix[i + 1] = prefix[i];
        char turn;
        cin >> turn;
        if (turn == 'P') {
            prefix[i + 1].pap++;
        }
        if (turn == 'H') {
            prefix[i + 1].hoof++;
        }
        if (turn == 'S') {
            prefix[i + 1].sci++;
        }
    }

    int ans = 0;

    F0R(i, N + 1) {
        // i is the cut point
        int currAns = max(prefix[i].pap, max(prefix[i].hoof, prefix[i].sci));
        currAns += max(prefix[N].pap - prefix[i].pap, max(prefix[N].hoof - prefix[i].hoof, prefix[N].sci - prefix[i].sci));
        ans = max(ans, currAns);
    }

    cout << ans;

}
{% endhighlight %}


## Problem 3. Secret Cow Code

[Hoof, Paper, Scissors](http://usaco.org/index.php?page=viewproblem2&cpid=691)

The cows are experimenting with secret codes, and have devised a method for creating an infinite-length string to be used as part of one of their codes.  
Given a string s, let F(s) be s followed by s "rotated" one character to the right (in a right rotation, the last character of s rotates around and becomes the new first character). Given an initial string s, the cows build their infinite-length code string by repeatedly applying F; each step therefore doubles the length of the current string.   

Given the initial string and an index N, please help the cows compute the character at the Nth position within the infinite code string.  

INPUT FORMAT (file cowcode.in):  
The input consists of a single line containing a string followed by N. The string consists of at most 30 uppercase characters, and N≤1018.  
Note that N may be too large to fit into a standard 32-bit integer, so you may want to use a 64-bit integer type (e.g., a "long long" in C/C++).  

OUTPUT FORMAT (file cowcode.out):  
Please output the Nth character of the infinite code built from the initial string. The first character is N=1.  
SAMPLE INPUT:  
```
COW 8
```  
SAMPLE OUTPUT:
```
C
```
In this example, the initial string COW expands as follows:

COW -> COWWCO -> COWWCOOCOWWC
                 12345678
Problem credits: Brian Dean
{% highlight c++ linenos %}
import java.io.* ;
import java.util.Scanner;

public class CowCode {

    char findChar(String original, long position, int k) {
        // base case
        // System.out.printf("%d %d\n", position, k);
        if (position <= original.length()) {
            return original.charAt((int) position - 1);
        }
        else {
            long half = (long) Math.pow(2, k) * original.length();
            if (half + 1 == position) {
                return (findChar(original, half, k - 1));
            }
            else {
                k = (int) (Math.log((position - 1 - half)/original.length())/Math.log(2));
                return (findChar(original, position - 1 - half, k));
            }
        }
    }

    public static void main(String[] args) {
        CowCode cowCode = new CowCode();

        try {
            // input
            BufferedReader br = new BufferedReader(new FileReader("cowcode.in"));
            Scanner scanner = new Scanner(br);

            String[] line = scanner.nextLine().split(" ");
            br.close();

            String original = line[0];
            long n = Long.parseLong(line[1]);

            int k = (int) (Math.log(n/original.length()) / Math.log(2));

            char ans = cowCode.findChar(original, n, k);

            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("cowcode.out"));
            bufferedWriter.write(ans);
            bufferedWriter.close();
            ///
        }


        catch (FileNotFoundException e) {
            System.out.println("File not exists or insufficient rights");
            e.printStackTrace();
        }
        catch (IOException e) {
            System.out.println("An exception occured while reading the file");
            e.printStackTrace();
        }
    }
}
{% endhighlight %}
