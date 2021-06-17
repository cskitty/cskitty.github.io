---
title: USACO 2020 Bronze December P2. Even More Odd Photos
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2020 Bronze December P2. Even More Odd Photos](http://usaco.org/index.php?page=viewproblem2&cpid=1084)

{% include video id="S0QqWFDiBGQ" provider="youtube" %}

{% highlight Java linenos %}
import java.io.*;
import java.util.*;

public class EvenMoreOddPhotos {
    public static  int group(int O, int E) {
        int diff = O - E;
        if (diff == 0) {
            return O + E;
        }
        else if (diff ==1) {
            return O + E - 2;
        }
        else if (diff ==2) {
            return E + O - 1;
        }
        else {
            O -= 2;
            E += 1;
        }

        return group(O, E);
    }

    public static void main(String[] args) throws IOException {
        EvenMoreOddPhotos.Kattio io = new EvenMoreOddPhotos.Kattio();
        int N = io.nextInt();
        int oddC = 0, evenC = 0;
        for (int i = 0; i < N; i++) {
            int cow = io.nextInt();
            if (cow % 2 == 0){
                evenC += 1;
            }
            else {
                oddC += 1;
            }
        }

        if (evenC > oddC) {
            io.println(2 * oddC + 1);
        }
        else {
            io.println(group(oddC, evenC));
        }

        io.close();
    }

    // https://usaco.guide/general/io?lang=java#io-template
    static class Kattio extends PrintWriter {
        private BufferedReader r;
        private StringTokenizer st;

        // standard input
        public Kattio() { this(System.in, System.out); }
        public Kattio(InputStream i, OutputStream o) {
            super(o);
            r = new BufferedReader(new InputStreamReader(i));
        }
        // USACO-style file input
        public Kattio(String problemName) throws IOException {
            super(new FileWriter(problemName + ".out"));
            r = new BufferedReader(new FileReader(problemName + ".in"));
        }

        // returns null if no more input
        public String next() {
            try {
                while (st == null || !st.hasMoreTokens())
                    st = new StringTokenizer(r.readLine());
                return st.nextToken();
            } catch (Exception e) {}
            return null;
        }

        public int nextInt() { return Integer.parseInt(next()); }
        public double nextDouble() { return Double.parseDouble(next()); }
        public long nextLong() { return Long.parseLong(next()); }
    }
}
{% endhighlight %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int group(int O, int E) {
    int diff = O - E;
    if (diff == 0) {
        return O + E;
    }
    else if (diff ==1) {
        return O + E - 2;
    }
    else if (diff ==2) {
        return E + O - 1;
    }
    else {
        O -= 2;
        E += 1;
    }

    return group(O, E);
}

int main() {
    int N;
    cin >> N;

    int oddC = 0, evenC = 0;
    for (int i = 0; i < N; i++) {
        int cow;
        cin >> cow;
        if (cow % 2 == 0){
            evenC += 1;
        }
        else {
            oddC += 1;
        }
    }

    if (evenC > oddC) {
        cout << 2 * oddC + 1;
    }
    else {
        cout << group(oddC, evenC);
    }
    return 0;
}
{% endhighlight %}  
