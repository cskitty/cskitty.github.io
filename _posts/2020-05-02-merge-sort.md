---
title: "Merge Sort"
date: 2020-04-13T15:34:30-04:00
categories:
  - Programming
tags:
  - Java
  - Algorithms
# ![](/assets/images/girlprogrammer1.jpg)
---

## Merge Sort



Explanation

Merge Sort is a divide and conquer method of sorting. The idea of it is to constantly break down the size of the list, dividing it into two. We can continuously split the list in two until we get the individual items. Next, we can reconstruct the list by comparing the smaller list. We can "stitch" these lists together, and sort the two smaller sorted lists by using two pointers in each one (p1, p2).

### Visual Steps

[3, 6, 2, 9, 1] <-- our main list

[3, 6, 2] [9, 1] <-- split in half

[3, 6] [2] [9] [1] <-- again

[3] [6] [2] [9] [1] <-- back to individual

[3, 6] [2, 9] [1] <-- compare the elements and reorder them

[2, 3, 6, 9] [1] <-- again

[1, 2, 3, 6, 9] <-- We’re done!


{% highlight java linenos %}
public class MergeSort {

    int[] mergesorter(int[] currentlist) {
        if (currentlist.length <= 1) {
            if (currentlist.length == 1) {
                return currentlist;
            }
            else {
                return null;
            }
        }
        else {
            int[] currentlistfront = new int[currentlist.length/2];
            int[] currentlistback = new int[currentlist.length - currentlist.length/2];
            for (int i = 0; i < currentlist.length; i++) {
                if (i >= currentlist.length/2) {
                    currentlistback[i-currentlist.length/2] = currentlist[i];
                }
                else {
                    currentlistfront[i] = currentlist[i];
                }
            }

            currentlistfront = mergesorter(currentlistfront);
            currentlistback = mergesorter(currentlistback);

            int[] returnlist = new int[currentlist.length];
            int p1 = 0, p2 = 0, currentindex = 0;

            while (p1 < currentlistfront.length && p2 < currentlistback.length) {
                if (currentlistfront[p1] < currentlistback[p2]) {
                    returnlist[currentindex] = currentlistfront[p1];
                    p1++;
                }
                else {
                    returnlist[currentindex] = currentlistback[p2];
                    p2++;
                }
                currentindex++;
            }

            while (p1 < currentlistfront.length){
                returnlist[currentindex] = currentlistfront[p1];
                p1++;
                currentindex++;
            }
            while(p2 < currentlistback.length) {
                returnlist[currentindex] = currentlistback[p2];
                p2++;
                currentindex++;
            }

            return returnlist;
        }
    }

    public static void main(String args[]) {
        MergeSort mergeSort = new MergeSort();

        int[] lst = {2, 24, 45, 66, 75, 90, 170, 802};

        int[] returnlst = mergeSort.mergesorter(lst);

        for (int i = 0; i < returnlst.length; i++) {
            System.out.print(returnlst[i] + " ");
        }
    }
}

{% endhighlight %}
