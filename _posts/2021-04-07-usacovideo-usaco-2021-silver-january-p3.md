---
title: USACO 2021 Silver January P3. Spaced Out
categories:
  - video
tags:
  - USACO Silver
  - VIDEO
---

## USACO 2021 Silver January P3: Spaced Out  

{% include video id="7eMHxpDQJEw" provider="youtube" %}


{% highlight java linenos %}
import java.io.*;
import java.util.*;
public class SpaceOutP2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int arr[][] = new int[N][N];

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int rowSum = 0, colSum = 0;

        for(int i = 0; i < N; ++i) {
            int a = 0, b = 0;
            for(int j = 0; j < N; ++j) {
                if(j % 2 == 0) {
                    a+=arr[i][j];
                }
                else {
                    b+=arr[i][j];
                }
            }
            rowSum += Math.max(a, b);
        }

        for(int i = 0; i < N; ++i) {
            int a = 0, b = 0;
            for(int j = 0; j < N; ++j) {
                if(j%2==0) {
                    a+=arr[j][i];
                }
                else {
                    b+=arr[j][i];
                }
            }
            colSum += Math.max(a, b);
        }

        System.out.println(Math.max(rowSum, colSum));
    }

}  
{% endhighlight %}  
