---
title: "Palindrome Partitioning"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - Backtracking
---

## Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

[Leetcode 131](https://leetcode.com/problems/palindrome-partitioning/)

{% highlight java linenos %}
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PalindromePartitioning {

    public boolean isPalindrome(String s) {
        int half = s.length()/2;
        for (int i = 0; i < half; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public void backtrack(List<List<String>> ans, ArrayList<String> pastChars, String s, int currentPos) {
        //System.out.println(currentPos);
        //System.out.print(pastChars);
        if (currentPos == s.length()) {
            ArrayList<String> temp = (ArrayList<String>) pastChars.clone();
            ans.add(temp);
            return;
        }
        else {
            for (int i = 1; i <= s.length() - currentPos; i++) {
                String temp = s.substring(currentPos, currentPos+i);
                if (isPalindrome(temp)) {
                    pastChars.add(temp);
                    backtrack(ans, pastChars, s, currentPos + i);
                    pastChars.remove(pastChars.size() - 1);
                }
            }
        }
    }

    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<List<String>>();
        ArrayList<String> pastChars = new ArrayList<String>();

        backtrack(ans, pastChars, s, 0);
        return (ans);
    }

    public static void main (String args[]) {
        String s = "aab";

        PalindromePartitioning palindromePartitioning = new PalindromePartitioning();

        System.out.print(palindromePartitioning.partition(s));
    }
}

{% endhighlight %}

We can solve this question by keeping note of our current position in the tree (as mentioned in the problem above). This is denoted with "currentPos". Every time we add a segment onto our "pastChars" path, we use the helper function "isPalindrome" to check if it is a valid palindrome. At the end, we can return a list of all the paths that have values that satisfy the condition of isPalindrome.
