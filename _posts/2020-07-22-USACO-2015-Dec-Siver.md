---
title: "USACO 2015 Dec Silver"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - USACO
---

## USACO 2015 Dec Silver

# Problem 3: Breed Counting

[Breed Counting](http://www.usaco.org/index.php?page=viewproblem2&cpid=572)

Farmer John's N cows, conveniently numbered 1…N, are all standing in a row (they seem to do so often that it now takes very little prompting from Farmer John to line them up). Each cow has a breed ID: 1 for Holsteins, 2 for Guernseys, and 3 for Jerseys. Farmer John would like your help counting the number of cows of each breed that lie within certain intervals of the ordering.  

INPUT FORMAT (file bcount.in):  
The first line of input contains N and Q (1≤N≤100,000, 1≤Q≤100,000).  
The next N lines contain an integer that is either 1, 2, or 3, giving the breed ID of a single cow in the ordering.  

The next Q lines describe a query in the form of two integers a,b (a≤b).  

OUTPUT FORMAT (file bcount.out):  
For each of the Q queries (a,b), print a line containing three numbers: the number of cows numbered a…b that are Holsteins (breed 1), Guernseys (breed 2), and Jerseys (breed 3).  
SAMPLE INPUT:  
6 3  
2  
1  
1  
3  
2  
1  
1 6  
3 3  
2 4  
SAMPLE OUTPUT:  
3 2 1  
1 0 0  
2 0 1  
{% highlight python linenos %}

import java.io.*;
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
