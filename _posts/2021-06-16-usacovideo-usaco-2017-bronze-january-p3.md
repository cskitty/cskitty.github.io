---
title: USACO 2017 Bronze January P3. Cow Tipping
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2017 Bronze January P3. Cow Tipping](http://www.usaco.org/index.php?page=viewproblem2&cpid=689)

{% include video id="gttxR2ndcyg" provider="youtube" %}

{% highlight Java linenos %}
import java.io.*;
import java.util.*;

public class CowTip {
    public static void main(String[] args) throws IOException {
        CowTip.Kattio io = new CowTip.Kattio("cowtip");
        int N = io.nextInt();
        int[][] farm = new int[N][N];

        for (int i = 0; i < N; i++) {
            String a = io.next();
            for (int j = 0; j < N; j++) {
                farm[i][j] =  Character.getNumericValue(a.charAt(j));
            }
        }

        int totalflips = 0;
        for (int i = N-1; i >= 0; i--) {
            for (int j = N-1; j >= 0; j--) {
                // go from bottom right to top, check if it's a 1
                if (farm[i][j] == 1) {
                    totalflips++;

                    // cow flip rectangle
                    for (int a = 0; a <= i; a++) {
                        for (int b = 0; b <= j; b++) {
                            if (farm[a][b] == 0) {
                                farm[a][b] = 1;
                            }
                            else {
                                farm[a][b] = 0;
                            }
                        }
                    }
                    // end cow flip
                }
            }
        }

        io.println(totalflips);
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

int main() {
	freopen("cowtip.in", "r", stdin);
	freopen("cowtip.out", "w", stdout);

    // solution comes here
    int n;
    cin >> n;

    vector<vector<char> > farm(n, vector<char> (n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            char temp;
            cin >> temp;
            farm[i][j] = temp;
        }
    }

    int totalflips = 0;
    for (int i = n-1; i >= 0; i--) {
        for (int j = n-1; j >= 0; j--) {
            // go from bottom right to top, check if it's a 1
            if (farm[i][j] == '1') {
                totalflips++;

                // cow flip rectangle
                for (int a = 0; a <= i; a++) {
                    for (int b = 0; b <= j; b++) {
                        if (farm[a][b] == '0') {
                            farm[a][b] = '1';
                        }
                        else {
                            farm[a][b] = '0';
                        }
                    }
                }
                // end cow flip

            }
        }
    }

    cout << totalflips;

}
{% endhighlight %}  
