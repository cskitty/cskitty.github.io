---
title: USACO 2018 Bronze December P1. Mixing Milk
categories:
  - video
tags:
  - USACO Bronze
  - VIDEO
---

## [USACO 2018 December Contest, Bronze](http://usaco.org/index.php?page=viewproblem2&cpid=855)

{% include video id="Sntu-XaCNy8" provider="youtube" %}

{% highlight Java linenos %}
import java.io.*;
import java.util.StringTokenizer;

public class mixmilk {
    static int[] c = new int[3];
    static int[] m = new int[3];

    static void pour(int from, int to) {
        int amt = Math.min(m[from], c[to] - m[to]);
        m[from] -= amt;
        m[to] += amt;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader("mixmilk.in"));
        PrintWriter fout = new PrintWriter("mixmilk.out");
        for (int i = 0; i < 3; i++) {
            StringTokenizer line = new StringTokenizer(fin.readLine());
            c[i] = Integer.parseInt(line.nextToken());
            m[i] = Integer.parseInt(line.nextToken());
        }

        for(int i = 0; i < 100; i++) {
            pour(i % 3, (i + 1) % 3);
        }
        for(int i = 0; i < 3; i++) {
            fout.println(m[i]);
        }
        fout.close();

    }
}
{% endhighlight %}


{% highlight C++ linenos %}
#include <bits/stdc++.h>
using namespace std;

int c[3], m[3];

void pour(int from, int to) {
    int amt = min(m[from], c[to] - m[to]);
    m[from] -= amt;
    m[to] += amt;
}

int main() {
    ifstream fin("mixmilk.in");
    ofstream fout("mixmilk.out");

    for(int i = 0; i < 3; i++) {
        fin >> c[i] >> m[i];
    }

    for(int i = 0; i < 100; i++) {
        pour(i % 3, (i + 1) % 3);
    }

    for(int i = 0; i < 3; i++) {
        fout << m[i] << endl;
    }
}
{% endhighlight %}  
