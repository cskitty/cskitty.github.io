---
title: "Backtracking: Subset Sum Algorithm"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Backtracking
---

## Subset Sum Algorithm


Explanation
The subset sum algorithm is one of the simpler implementations of backtracking. The problem takes in a list and a value, and outputs different subsets from the list that sum up to the value. The implementation below is done in Java.


{% highlight java linenos %}
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SubsetSum {

    List<Integer> makeDeepCopyInteger(List<Integer> old){
        ArrayList<Integer> copy = new ArrayList<Integer>(old.size());
        for(Integer i : old){
            copy.add(new Integer(i));
        }
        return copy;
    }

    List<List<Integer>> subset_sum(Integer current, Integer currentIndex, Integer goal, List<Integer> currentPath, List<List<Integer>> ans, List<Integer> lst, List<Integer> lstused) {
        if (current == goal) {
            ans.add(makeDeepCopyInteger(currentPath));
            return ans;
        }
        else {
            for (int i = currentIndex + 1; i < lst.size(); i++) {
                if (current + lst.get(i) <= goal && lstused.get(i) == 0) {
                    lstused.set(i, 1);
                    currentPath.add(lst.get(i));

                    ans = subset_sum(current + lst.get(i), i, goal, currentPath, ans, lst, lstused);

                    currentPath.remove(currentPath.size() - 1);
                    lstused.set(i, 0);

                }
            }

            return ans;
        }
    }

    public static void main (String args[]) {
        SubsetSum subsetSum = new SubsetSum();

        List<Integer> lst = new ArrayList<Integer>(Arrays.asList(10, 7, 5, 18, 12, 20, 15));
        List<Integer> lst2 = new ArrayList<Integer>();

        for (int i = 0; i < lst.size(); i++) {
            lst2.add(0);
        }

        List<Integer> currentPath = new ArrayList<Integer>();

        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        subsetSum.subset_sum(0, -1, 35, currentPath, ans, lst, lst2);

        for (int i = 0; i < ans.size(); i++) {
            for (int j = 0; j < ans.get(i).size(); j++) {
                System.out.print(ans.get(i).get(j));
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}

{% endhighlight %}
