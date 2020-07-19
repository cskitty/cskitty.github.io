---
title: "Subsets"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - Backtracking
---

## Subsets

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
