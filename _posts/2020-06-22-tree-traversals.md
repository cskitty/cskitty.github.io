---
title: "Tree Traversal"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Tree
---

## Tree Traversal Algorithm

Overview

When looking at a tree, there are many ways to create and transform into a printed array. The three main ones include in order, pre order, and post order.


### inOrder

![](/assets/images/atreetraversal.gif)

Explanation


In Order Tree Traversal goes directly down all the way to the left, then prints the parent, then the right.


### Pre Order

![](/assets/images/apreorder.gif)

Explanation

Pre Order Tree Traversal prints the parent node, then the left, then the right.

### Post Order

![](/assets/images/apostorder.gif)

Post Order Tree Traversal prints the left, then the right, then finally the parent.


{% highlight java linenos %}import org.w3c.dom.Node;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.util.List.*;


class node {
    List<node> next;
    int value;
    node(int v, List<node> n) {
        value = v;
        next = n;
    }
}

public class TreeTraversal {

    void print_list(List<Integer> lst) {
        for (int i = 0; i < lst.size(); i++) {
            System.out.print(lst.get(i));
            System.out.print(" ");
        }
        System.out.println();
    }

    List<Integer> inOrder(node current, List<Integer> travelled) {
        if (current.next == null) {
            travelled.add(current.value);
            return travelled;
        }
        else {
            int half = (int) current.next.size()/2;
            // left
            for (int i = 0; i < half; i++) {
                inOrder(current.next.get(i), travelled);
            }
            travelled.add(current.value);
            // right
            for (int i = half; i < current.next.size(); i++) {
                inOrder(current.next.get(i), travelled);
            }
            return travelled;
        }
    }

    List<Integer> postOrder(node current, List<Integer> travelled) {
        if (current.next == null) {
            travelled.add(current.value);
            return travelled;
        }
        else {
            for (int i = 0; i < current.next.size(); i++) {
                postOrder(current.next.get(i), travelled);
            }
            travelled.add(current.value);
            return travelled;
        }
    }

    List<Integer> preOrder (node current, List<Integer> travelled) {
        if (current.next == null) {
            travelled.add(current.value);
            return travelled;
        }
        else {
            travelled.add(current.value);
            for (int i = 0; i < current.next.size(); i++) {
                preOrder(current.next.get(i), travelled);
            }
            return travelled;
        }
    }

    public static void main(String args[]) {
        TreeTraversal treeTraversal = new TreeTraversal();

        // creating tree
        node zero = new node(0, null);
        node two = new node(2, null);
        node seven = new node(7, null);
        node nine = new node(9, null);

        List<node> currentChildren = new ArrayList<node>(Arrays.asList(zero, two));
        node one = new node(1, currentChildren);

        currentChildren = new ArrayList<node>(Arrays.asList(seven));
        node six = new node(6, currentChildren);
        currentChildren = new ArrayList<node>(Arrays.asList(nine));
        node ten = new node(10, currentChildren);

        currentChildren = new ArrayList<node>(Arrays.asList(six, ten));
        node eight = new node(8, currentChildren);

        node four = new node(4, null);

        currentChildren = new ArrayList<node>(Arrays.asList(one, four));
        node three = new node(3, currentChildren);

        currentChildren = new ArrayList<node>(Arrays.asList(three, eight));
        node five = new node(5, currentChildren);

        // in order traversal
        List<Integer> inOrderTree = new ArrayList<Integer>();
        List<Integer> travelled = new ArrayList<Integer>();

        inOrderTree = treeTraversal.inOrder(five, travelled);

        treeTraversal.print_list(inOrderTree);

        // post order traversal
        List<Integer> postOrderTree = new ArrayList<Integer>();
        travelled = new ArrayList<>();

        postOrderTree = treeTraversal.postOrder(five, travelled);

        treeTraversal.print_list(postOrderTree);

        // pre order traversal

        List<Integer> preOrderTree = new ArrayList<Integer>();
        travelled = new ArrayList<>();

        preOrderTree = treeTraversal.preOrder(five, travelled);

        treeTraversal.print_list(preOrderTree);

    }
}

{% endhighlight %}
