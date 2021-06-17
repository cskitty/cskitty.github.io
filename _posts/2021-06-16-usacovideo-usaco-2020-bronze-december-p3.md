---
title: USACO 2020 Bronze December P3. Stuck in a Rut
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2020 Bronze December P3. Stuck in a Rut](http://usaco.org/index.php?page=viewproblem2&cpid=1061)

{% include video id="kgweCjqzR9A" provider="youtube" %}

{% highlight Java linenos %}
import java.io.*;
import java.util.*;

public class StuckInARut {
    static final int myINF = 1000000007;

    public static void main(String[] args) throws IOException {
        StuckInARut.Kattio io = new StuckInARut.Kattio();
        Integer N = io.nextInteger();

        ArrayList<ArrayList<Integer>> east = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> north = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> pos = new ArrayList<ArrayList<Integer>>();

        for (Integer i = 0; i < N; i++) {
            String d = io.next();
            Integer x = io.nextInteger();
            Integer y = io.nextInteger();
            ArrayList<Integer> p = new ArrayList<Integer>();
            p.add(x);
            p.add(y);
            pos.add(p);
            p.add(i);
            if (d.compareTo("E") == 0) {
                east.add(p);
            }
            else {
                north.add(p);
            }
        }

        ArrayList<ArrayList<Integer>> meetTime = new ArrayList<ArrayList<Integer>>();
        for (ArrayList<Integer> nC : north) {
            for (ArrayList<Integer> eC : east) {
                Integer yT = eC.get(1) - nC.get(1);
                Integer xT = nC.get(0) - eC.get(0);

                if (xT == yT) {
                    continue;
                }

                if (yT > xT && xT > 0) {
                    meetTime.add(new ArrayList<Integer>(Arrays.asList(yT, nC.get(2), eC.get(2), 0)));
                }
                else if (yT < xT && yT > 0) {
                    meetTime.add(new ArrayList<Integer>(Arrays.asList(xT, eC.get(2), nC.get(2), 1)));
                }
            }
        }

        Collections.sort(meetTime, new Comparator<ArrayList<Integer>>(){
                    public int compare(ArrayList<Integer> s1, ArrayList<Integer> s2) {
                        return Integer.compare(s1.get(0) , s2.get(0));
                    }});

        ArrayList<Integer> ans = new ArrayList<Integer>(Collections.nCopies(N, myINF));

        for (ArrayList<Integer> mt : meetTime) {
            if (ans.get(mt.get(2)) == myINF && ans.get(mt.get(1)) == myINF) {
                // both not stopped
                ans.set(mt.get(1), mt.get(0));
                continue;
            }
            if (ans.get(mt.get(1)) == myINF) {
                // not yet assigned

                if (mt.get(3) == 1) {
                    Integer start = pos.get(mt.get(2)).get(1);
                    Integer end = start + ans.get(mt.get(2));

                    if (pos.get(mt.get(1)).get(1) >= start && pos.get(mt.get(1)).get(1) <= end) {
                        ans.set(mt.get(1), mt.get(0));
                    }
                }
                else {
                    Integer start = pos.get(mt.get(2)).get(0);
                    Integer end = start + ans.get(mt.get(2));

                    if (pos.get(mt.get(1)).get(0) >= start && pos.get(mt.get(1)).get(0) <= end) {
                        ans.set(mt.get(1), mt.get(0));
                    }
                }
            }
        }

        for (Integer v : ans) {
            if (v == myINF) {
                io.println("Infinity");
            }
            else {
                io.println(v);
            }
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

        public int nextInteger() { return Integer.parseInt(next()); }
        public double nextDouble() { return Double.parseDouble(next()); }
        public long nextLong() { return Long.parseLong(next()); }
    }
}
{% endhighlight %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
#include <bits/stdc++.h>
using namespace std;

vector<array<int, 3>> north;
vector<array<int, 3>> east;
int myINF = 1e9;

#define f first
#define s second

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> pos(N);
    for (int i = 0; i < N; i++) {
        char d;
        cin >> d;
        pair<int, int> p;
        cin >> p.first >> p.second;

        array<int, 3> varr = {p.f, p.s, i};
        if (d == 'E') {
            east.push_back(varr);
        }
        else {
            north.push_back(varr);
        }
        pos[i] = p;
    }

    vector<vector<int>> meetTime;

    for (auto nC : north) {
        for (auto eC : east) {
            int yT = eC[1] - nC[1];
            int xT = nC[0] - eC[0];

            if (xT == yT) {
                continue;
            }

            if (yT > xT && xT > 0) {
                meetTime.push_back({yT, nC[2], eC[2], 0});
            }
            else if (yT < xT && yT > 0) {
                meetTime.push_back({xT, eC[2], nC[2], 1});
            }
        }
    }

    sort(meetTime.begin(), meetTime.end());

    vector<int> ans(N, myINF);

    for (auto mt : meetTime) {
        if (ans[mt[2]] == myINF && ans[mt[1]] == myINF) {
            // both not stopped
            ans[mt[1]] = mt[0];
            continue;
        }
        if (ans[mt[1]] == myINF) {
            // not yet assigned

            if (mt[3]) {
                int start = pos[mt[2]].s;
                int end = start + ans[mt[2]];

                if (pos[mt[1]].s >= start && pos[mt[1]].s <= end) {
                    ans[mt[1]] = mt[0];
                }
            }
            else {
                int start = pos[mt[2]].f;
                int end = start + ans[mt[2]];

                if (pos[mt[1]].f >= start && pos[mt[1]].f <= end) {
                    ans[mt[1]] = mt[0];
                }
            }
        }
    }

    for (auto v : ans) {
        if (v == myINF) {
            cout << "Infinity" << endl;
        }
        else {
            cout << v << endl;
        }
    }
}
{% endhighlight %}  
