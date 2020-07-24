---
title: "Maximum Subarray Sum"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - PrefixSum
  - Dynamic Programming
---

## Maximum Subarray Sum

[Maximum Subarray Sum](/https://cses.fi/problemset/task/1643/)

Given an array of n integers, your task is to find the maximum sum of values in a contiguous, nonempty subarray.

Explanation

Using prefix sum, we can create an array with all the prefix (or partial) sums. Using this array, we can then find that all the sums formed can be found with one of the prefix sums subtracting another. Thus, we use dp (dynamic programming) to find the minimum prefix sum, while iterating with prefixSum[i] being the maximum (current) prefix sum, and subtracting the two to find the overall maximum subarray sum.


{% highlight java linenos %}
import java.util.List;
import java.util.Scanner;

public class SubarraySum {

    long maxSubArray(long[] myLst) {
        long[] prefixSum = new long[myLst.length + 1];

        long smallest = Long.MAX_VALUE;
        long smallestIndex = 0;
        for (int i = 0; i < myLst.length; i++) {
            prefixSum[i + 1] = prefixSum[i] + myLst[i];
            if (prefixSum[i + 1] < smallest) {
                smallest = prefixSum[i + 1];
            }
        }

        long min = Long.MAX_VALUE;

        long currentAnswer = Long.MIN_VALUE;
        for (int i = 0; i < prefixSum.length; i++) {
            if (prefixSum[i] - min > currentAnswer) {
                currentAnswer = prefixSum[i] - min;
            }

            if (prefixSum[i] < min) {
                min = prefixSum[i];
            }

        }

        return currentAnswer;

    }

    public static void main(String args[]) {

        Scanner myObj = new Scanner(System.in);
        int x = Integer.parseInt(myObj.nextLine());

        long[] myLst = new long[x];
        String[] line = myObj.nextLine().split(" ");
        for (int i = 0; i < x; i++) {
            myLst[i] = Long.parseLong(line[i]);
        }

        SubarraySum subarraySum = new SubarraySum();
        System.out.println(subarraySum.maxSubArray(myLst));

    }
}

{% endhighlight %}
