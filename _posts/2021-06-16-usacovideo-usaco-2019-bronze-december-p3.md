---
title: USACO 2019 Bronze December P3. Livestock Lineup
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2019 Bronze December P3. Livestock Lineup](http://www.usaco.org/index.php?page=viewproblem2&cpid=965)

{% include video id="kgweCjqzR9A" provider="youtube" %}

{% highlight Java linenos %}
import java.io.*;
import java.util.*;

public class Lineup {
    static ArrayList<String> restrictionsA;
    static ArrayList<String> restrictionsB;

    private static ArrayList<String> permutations(ArrayList<String> s ) {
        // 1. finds the largest k, that c[k] < c[k+1]
        int first = s.size() - 2;
        for ( ; first >= 0; first-- ) {
            if (s.get(first).compareTo(s.get(first + 1)) < 0)
                break;
        }

        if (first == -1)
            return null;

        // 2. find last index toSwap, that c[k] < c[toSwap]
        int toSwap = s.size() - 1;
        for ( ; toSwap >= 0; toSwap-- ) {
            if (s.get(first).compareTo(s.get(toSwap)) < 0)
                break;
        }

        // 3. swap elements with indexes first and last
        Collections.swap(s, first++, toSwap);

        // 4. reverse sequence from k+1 to n (inclusive)
        toSwap = s.size() - 1;
        while ( first < toSwap )
            Collections.swap( s, first++, toSwap-- );

        return s;
    }

    private static int findIndex(ArrayList<String> perm, String cow) {
        for (int i = 0; i < perm.size(); i++) {
            if (cow.equals(perm.get(i))) {
                return i;
            }
        }
        return -1;
    }

    private static boolean check(ArrayList<String> perm) {
        boolean passed = true;
        for (int i = 0; i < restrictionsA.size() ; i++) {
            String cow1 = restrictionsA.get(i);
            String cow2 = restrictionsB.get(i);
            int a = findIndex(perm, cow1);
            int b = findIndex(perm, cow2);
            if (Math.abs(a - b) != 1) {
                passed = false;
                break;
            }
        }

        if (passed) {
            return true;
        }
        else {
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        Lineup.Kattio io = new Lineup.Kattio("lineup");
        int N = io.nextInt();

        ArrayList<String> cows = new ArrayList<String>(
                Arrays.asList("Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"));

        restrictionsA = new ArrayList<String>();
        restrictionsB = new ArrayList<String>();

        for (int i = 0; i < N; i++) {
            String a = io.next();
            io.next();
            io.next();
            io.next();
            io.next();
            String b = io.next();
            restrictionsA.add(a);
            restrictionsB.add(b);
        }

        Collections.sort(cows);
        while (cows != null) {
            if (check(cows)) {
                for(String c : cows) {
                    io.println(c);
                }
                break;
            }
            cows = permutations(cows);
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
