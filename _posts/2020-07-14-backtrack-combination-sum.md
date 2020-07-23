---
title: "Combination Sum"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - Backtracking
---

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
