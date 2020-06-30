---
title: "Greedy: Dijkstra's Shortest Path"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Greedy
---

## Dijkstra's Shortest Path

![](/assets/images/adijkstras.gif)

Explanation

Dijkstra's Shortest Path is an algorithm that finds the shortest (as in the best) path that involves the least amount of weight. The weight of a node is determined by the minimum weight on any path from the starting node (in this case, 0). In this case, we'll be finding the minimum possible distance from node 0 to 2.


{% highlight java linenos %}
import java.util.*;

class Node {
    int node;
    int weight;
    public Node(int n, int w) {
        node = n;
        weight = w;
    }
}

class NodeComparator implements Comparator<Node>{

    public int compare(Node s1, Node s2) {
        if (s1.weight < s2.weight) {
            return 1;
        }
        else if (s1.weight > s2.weight) {
            return -1;
        }
        return 0;
    }
}

public class DijkstraShortestPathA {



    Integer path_finder(PriorityQueue<Node> myQueue, List<Integer> values, Integer value, List<List<Integer>> graph) {
        for (int i = 0; i < graph.size(); i++) {
            Node currentNode = new Node(i, Integer.MAX_VALUE);
            myQueue.add(currentNode);
        }
        // Node prev = new Node(0, 0);
        while(myQueue.size() > 0) {
            Node n = myQueue.poll();

            for (int i = 0; i < graph.get(n.node).size(); i++) {
                // i is the node w/ the connection
                if (graph.get(n.node).get(i) != 0) {

                    int currentWeight = values.get(i) + graph.get(i).get(n.node);
                    if (values.get(n.node) > currentWeight) {
                        values.set(n.node, currentWeight);
                    }
                    myQueue.remove(n);

                }
            }
        }

        return values.get(value);
    }


    public static void main(String args[]) {
        DijkstraShortestPathA dijkstraShortestPathA = new DijkstraShortestPathA();

        List<List<Integer>> graph = new ArrayList<List<Integer>>();

        for (int i = 0; i < 5; i++) {
            List<Integer> templst = new ArrayList<Integer>();
            for (int j = 0; j < 5; j++) {
                templst.add(0);
            }
            graph.add(templst);
        }

        graph.get(0).set(1, 9);
        graph.get(0).set(2, 1);
        graph.get(0).set(3, 9);
        graph.get(0).set(4, 4);


        graph.get(1).set(0, 9);
        graph.get(1).set(2, 1);
        graph.get(1).set(3, 6);
        graph.get(1).set(4, 8);

        graph.get(2).set(1, 3);
        graph.get(2).set(0, 1);
        graph.get(2).set(4, 4);
        graph.get(2).set(3, 8);

        graph.get(3).set(2, 8);
        graph.get(3).set(1, 6);
        graph.get(3).set(0, 9);
        graph.get(3).set(4, 4);

        graph.get(4).set(3, 4);
        graph.get(4).set(2, 4);
        graph.get(4).set(1, 8);
        graph.get(4).set(0, 4);


        PriorityQueue<Node> myQueue = new PriorityQueue<Node>(5, new NodeComparator());


        List<Integer> values = new ArrayList<Integer>(5);
        for (int i = 0; i < 5; i++) {
            values.add(100000000);
        }
        values.set(0, 0);

        System.out.println(dijkstraShortestPathA.path_finder(myQueue, values, 2, graph));

    }
}

{% endhighlight %}
