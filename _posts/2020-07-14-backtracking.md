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

We can apply the backtrack algorithm using Java to many problems. Let's look at a few examples in particular.

## Backtrack Algorithm

Backtrack algorithms are used to solve a lot of brute force based DFS search problems. This is a standard python program for backtracking applied to Leetcode problem

[Leetcode 46 permutations](https://leetcode.com/problems/permutations/).

Explanation

Given a collection of distinct integers, return all possible permutations.

Example

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

{% highlight python linenos %}
import copy

def backtrack(answer,  track, nums):
    if len(track) == len(nums):
        # python only: use deepcopy to create a duplicate of track and push to answer
        answer.append( copy.deepcopy(track))
        return
    else:
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            else:
                #push
                track.append(nums[i])
                #explore
                backtrack(answer, track, nums)
                #pop
                track.pop(len(track) - 1)

answer = []
track = []
nums = [1, 2, 3]
backtrack(answer, track, nums)
print(answer)

{% endhighlight %}


### Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]  
Output:  
[  
  [3],  
  [1],  
  [2],  
  [1,2,3],  
  [1,3],  
  [2,3],  
  [1,2],  
  []  
]  

[Leetcode 78 Subsets] (https://leetcode.com/problems/subsets/)  

{% highlight java linenos %}
class Solution {
    Set<Set<Integer>> m_sum;

    Solution() {
        m_sum = new HashSet<Set<Integer>>();
    }


    Set<Integer> makeDeepCopyInteger(Set<Integer> old){
        Set<Integer> copy = new HashSet<Integer>(old.size());

        Iterator<Integer> it = old.iterator();
        while (it.hasNext()) {
            copy.add(it.next());
        }

        return copy;
    }


    void find_subset(Set<Integer> currentList, int[] nums) {
        // System.out.println(currentList);
        for (int i = 0; i < nums.length; i++) {

            if (! currentList.contains(nums[i])) {
                currentList.add(nums[i]);

                if (! m_sum.contains(currentList)) {
                    m_sum.add(makeDeepCopyInteger(currentList));
                    find_subset(currentList, nums);
                }
                currentList.remove(nums[i]);
            }

        }

    }

    public List<List<Integer>> subsets(int[] nums) {

        List<Integer> lst = new ArrayList<Integer>();

        Set<Integer> myLst = new HashSet<Integer>();

        m_sum.add(new HashSet<Integer>());

        find_subset(myLst, nums);

        List<List<Integer>> rLst = new ArrayList<List<Integer>>();

        Iterator<Set<Integer>> i = m_sum.iterator();
        while(i.hasNext()) {
            List<Integer> temp = new ArrayList<Integer>();
            Iterator<Integer> j = i.next().iterator();
            while(j.hasNext()) {
                temp.add(j.next());
            }
            rLst.add(temp);
        }

        return rLst;
    }
}

{% endhighlight %}

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
