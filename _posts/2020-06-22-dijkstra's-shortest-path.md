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

public class DijkstraShortestPath {

    Integer path_finder(Integer currentNode, List<Integer> values, List<Integer> visited, List<List<Integer>> connections, Integer wanted) {
        Queue<Integer> nodesNeeded = new ArrayDeque<Integer>();
        nodesNeeded.add(currentNode);

        while (nodesNeeded.size() > 0) {
            currentNode = nodesNeeded.peek();
            nodesNeeded.remove();
            for (int i = 0; i < connections.get(currentNode).size(); i++) {
                if (connections.get(currentNode).get(i) >= 1) {
                    int tempValue = values.get(currentNode) + connections.get(currentNode).get(i);
                    if (tempValue < values.get(i)) {
                        values.set(i,tempValue);
                    }
                    if (visited.get(i) == 0) {
                        nodesNeeded.add(i);
                        visited.set(i, 1);
                    }
                }
            }
        }

        return values.get(wanted);
    }

    public static void main(String args[]) {
        DijkstraShortestPath dijkstraShortestPath = new DijkstraShortestPath();

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

        List<Integer> values = new ArrayList<Integer>(5);
        for (int i = 0; i < 5; i++) {
            values.add(100000000);
        }
        values.set(0, 0);

        List<Integer> visited = new ArrayList<Integer>();
        for (int i = 0; i < 5; i++) {
            visited.add(0);
        }

        System.out.println(dijkstraShortestPath.path_finder(0, values, visited, graph, 2));

    }
}

{% endhighlight %}
