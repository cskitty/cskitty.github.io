---
title: "Backtrack in Java"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - Backtracking
---

## Backtracking Applied to problems

We can apply the backtrack algorithm using Java to many problems. Let's look at two in particular.

### Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

[Leetcode 39] (https://leetcode.com/problems/combination-sum/)

{% highlight java linenos %}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class CombinationSum {

    public void backtrack(List<List<Integer>> answers, ArrayList<Integer> currentPath, int[] candidates, int target) {
        int sum = 0;
        for (int i = 0; i < currentPath.size(); i++){
            sum += currentPath.get(i);
        }
        if (target == sum) {
            ArrayList<Integer> temp = (ArrayList<Integer>) currentPath.clone();
            Collections.sort(temp);
            if (! answers.contains(temp)) {
                answers.add(temp);
            }
            return;
        }
        else {
            for (int i = 0; i < candidates.length; i++) {
                if (candidates[i] <= target - sum) {
                    currentPath.add(candidates[i]);
                    backtrack(answers, currentPath, candidates, target);
                    currentPath.remove(currentPath.size() - 1);
                }
            }
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        ArrayList<List<Integer>> ans = new ArrayList<List<Integer>>();
        ArrayList<Integer> currentPath = new ArrayList<Integer>();
        backtrack(ans, currentPath, candidates, target);
        return ans;
    }

    public static void main(String args[]) {
        int[] candidates = {2,3,5};
        int target = 8;
        CombinationSum comSun = new CombinationSum();
        System.out.println(comSun.combinationSum(candidates, target));
    }

}

{% endhighlight %}

We can solve this question by keeping track of a "current path". If we were to create a tree of all the different ways we can add up to the target, the current path will remember the nodes leading up the leaf, or last number. The only condition of this path is that sum of the path should equal the target. The list we return to the question contains all the different paths that satisfy this condition.

### Palindrome Partitioning

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
