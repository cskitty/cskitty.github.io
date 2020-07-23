---
title: "USACO 2017 Jan Silver"
categories:
  - USACO
tags:
  - Algorithms
  - Java
  - USACO
---

# USACO 2017 Jan Silver

## Problem 3: Secret Cow Code

[Secret Cow Code](http://www.usaco.org/index.php?page=viewproblem2&cpid=692)

The cows are experimenting with secret codes, and have devised a method for creating an infinite-length string to be used as part of one of their codes.
Given a string s, let F(s) be s followed by s "rotated" one character to the right (in a right rotation, the last character of s rotates around and becomes the new first character). Given an initial string s, the cows build their infinite-length code string by repeatedly applying F; each step therefore doubles the length of the current string.  

Given the initial string and an index N, please help the cows compute the character at the Nth position within the infinite code string.  

INPUT FORMAT (file cowcode.in):  
The input consists of a single line containing a string followed by N. The string consists of at most 30 uppercase characters, and N≤1018.  
Note that N may be too large to fit into a standard 32-bit integer, so you may want to use a 64-bit integer type (e.g., a "long long" in C/C++).  

OUTPUT FORMAT (file cowcode.out):  
Please output the Nth character of the infinite code built from the initial string. The first character is N=1.  
SAMPLE INPUT:  
COW 8  
SAMPLE OUTPUT:  
C  
In this example, the initial string COW expands as follows:  

COW -> COWWCO -> COWWCOOCOWWC  
                 12345678  

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
