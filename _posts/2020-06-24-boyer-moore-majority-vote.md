---
title: "Greedy: Boyer-Moore's Majority Vote"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Greedy
---

## Boyer-Moore's Majority Vote Algorithm

Explanation

The Boyer-Moore's Majority Vote algorithm finds whether or not a single element is present in more than half the list. It loops through the list twice and uses a counter with a greedy algorithm to find the element. (If no element is more than half, this program will return -1)

{% highlight java linenos %}
public class BoyerMooreMajorityVote {

    int majority_element(int[] lst) {
        int current = lst[0];
        int currentcount = 1;
        for (int i = 0; i < lst.length; i++) {
            if (lst[i] == current) {
                currentcount++;
            }
            else {
                currentcount--;
                if (currentcount == 0) {
                    current = lst[i];
                    currentcount++;
                }
            }
        }

        int counter = 0;
        for (int i = 0; i < lst.length; i++) {
            if (lst[i] == current) {
                counter++;
            }
        }
        if (counter > lst.length/2) {
            return current;
        }
        else {
            // no overwhelming majority
            return -1;
        }
    }

    public static void main(String args[]) {
        BoyerMooreMajorityVote boyerMooreMajorityVote = new BoyerMooreMajorityVote();

        int[] lst = {1, 3, 3, 2, 1, 1, 1};
        int[] lst2 = {1, 2, 3, 1, 2, 1, 3};

        System.out.println(boyerMooreMajorityVote.majority_element(lst));
        System.out.println(boyerMooreMajorityVote.majority_element(lst2));
    }
}

{% endhighlight %}
