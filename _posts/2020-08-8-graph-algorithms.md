---
title: "Graph Algorithms"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Graph
---

# Graph Algorithms

##  Graph Basics
Graphs are made up of nodes and edges, where nodes are connected by edges. Graphs
can have either weighted edges, in which each edge has a certain length, or unweighted, in
which case all edges have the same length. Edges are either directed, which means they can
be traversed only in one direction, or undirected, which means that they can be traversed
in both directions.    

### Trees
A tree is a special type of graph satisfying two constraints: it is acyclic, meaning there
are no cycles, and the number of edges is one less than the number of nodes. Trees satisfy
the property that for any two nodes A and B, there is exactly one way to travel between A
and B.  

The root of a tree is the one vertex that is placed at the top, and is where we usually
start our tree traversals from. Usually, problems don’t tell us where the tree is rooted at, and
it usually doesn’t matter either; trees can be arbitrarily rooted (here, we’ll use the convention
of rooting at index 1).
Every node except the root node has a parent. The parent of a node s is defined as
follows: On the path from the root to s, the node that is one closer to the root than s is the
parent of s. Each non-root node has a unique parent.  

Child nodes are the opposite. They lie one farther away from the root than their parent
node. Unlike parent nodes, these are not unique. Each node can have arbitrarily many child
nodes, and nodes can also have zero children. If a node s is the parent of a node t, then t is
the child node of s.  

A leaf node is a node that has no children. Leaf nodes can be identified quite easily
because there is only one edge adjacent to them.


## Graph Representations

Graphs can be represented in three ways:  

* Adjacency List most frequently used when nodes are large
* Adjacency Matrix when nodes are small
* Edge List

### Adjacency List for Un-Weighted Graph

{% highlight c++ linenos %}

int MX = 1e5; // max num of nodes
vector<int> adj[MX]; // adjacency list where MX is max possible # of nodes
bool visited[MX]; // visited array of size MX as well  

void addEdge(int a, int b) {
  adj[a].push_back(b);

  // omit this line if the graph is directed
  adj[b].push_back(a);
}

int main(){
  cin >> n; // reads in number of nodes
  cin >> m; // reads in number of edges
  for(int i = 0; i < m; i++){ // reading in each of the m edges
    int a, b;
    cin >> a >> b;
    addEdge(a,b);
  }
  return 0;
}

{% endhighlight %}


### Adjacency List for Weighted Graph
We use c++ pair<int, int> to store the destination node ID and weight.

{% highlight c++ linenos %}

int MX = 1e5; // max num of nodes
vector<pair<int, int>> adj[MX];  
bool visited[MX]; // visited array of size MX as well  

void addEdge(int a, int b, int weight) {
  adj[a].push_back(make_pair(b, weight));
  adj[b].push_back(make_pair(a, weight));
}

int main(){
  cin >> n; // reads in number of nodes
  cin >> m; // reads in number of edges
  for(int i = 0; i < m; i++){ // reading in each of the m edges
    int a, b, w;
    cin >> a >> b >> w;
    addEdge(a,b, w);
  }
  return 0;
}

{% endhighlight %}


* Adjacency Matrix

When Graph nodes are small, we can use a 2D array to store the graph.

{% highlight c++ linenos %}
int MX = 1e5; // max num of nodes
int adj[MX][MX];

void addEdge(int a, int b, int weight = 1) {
  adj[a][b] = weight;
  adj[b][a] = weight;
}

int main(){
  int n, m; // number of nodes and edges
  cin >> n; // reads in number of nodes
  cin >> m; // reads in number of edges
  for(int i = 0; i < m; i++){ // reading in each of the m edges
    int a, b;
    cin >> a >> b;
    addEdge(a,b);
  }
  return 0;
}

{% endhighlight %}


## Graph Traversal Algorithms

Graph traversal is the process of visiting or checking each vertex in a graph. This is useful
when we want to determine which vertices can be visited, whether there exists a path from
one vertex to another, and so forth. There are two algorithms for graph traversal, namely
depth-first search (DFS) and breadth-first search (BFS).

###  Breadth-first search
Breadth-first search visits nodes in order of distance away from the starting node; it first
visits all nodes that are one edge away, then all nodes that are two edges away, and so on.


{% highlight c++ linenos %}
//Global variables

 // max num of nodes
int MX = 1e5;
int adj[MX][MX];
bool visited[MX];
int dist[MX];


void addEdge(int a, int b, int weight = 1) {
  adj[a][b] = weight;
  adj[b][a] = weight;
}

//recursive BFS
void bfs(int node){
  //step1: boundary processing
  cout << "visiting node " << node;

  //step2: check visited or not
  if (!visited[node]) {
    visited[node] = true;
  }

  //step3: loop through neighbors
  for(int next : adj[node]){
    if(!visited[next]){
      bfs(next);
    }
  }
}

//Queue based BFS

void BFS(int start){
  // fill distance array with -1's
  memset(dist, -1, sizeof(dist));

  queue<int> q;
  dist[start] = 0;

  q.push(start);
  while(!q.empty()){
    int node = q.front();
    q.pop();

    for(int next : adj[node]){
      if(dist[next] == -1){
        dist[next] = dist[node] + 1;
        q.push(next);
        }
      }
    }
}


int main(){
  int n, m; // number of nodes and edges
  cin >> n; // reads in number of nodes
  cin >> m; // reads in number of edges
  for(int i = 0; i < m; i++){ // reading in each of the m edges
    int a, b;
    cin >> a >> b;
    addEdge(a,b);
  }

  BFS(0);

  return 0;
}

{% endhighlight %}


### Depth-first search

Depth-first search continues down a single path as far as possible; once it has no more
vertices to visit along that path, it backtracks until it finds more vertices to visit. Depth-first
search will process all nodes that are reachable (connected by edges) to the starting node.
Let’s look at an example of how this works. Depth first-search can start at any node, but by
convention we’ll start the search at node 1. We’ll use the following color scheme: blue for
nodes we have already visited, red for nodes we are currently processing, and black for nodes
that have not been visited yet.


{% highlight c++ linenos %}
//Global variables

 // max num of nodes
int MX = 1e5;
int adj[MX][MX];
bool visited[MX];
int dist[MX];


void addEdge(int a, int b, int weight = 1) {
  adj[a][b] = weight;
  adj[b][a] = weight;
}

//recursive DFS
void dfs(int node){
  //step1: boundary processing
  cout << "visiting node " << node;
  
  //step2: check visited or not
  if (!visited[node]) {
    visited[node] = true;
  }

  //step3: loop through neighbors
  for(int next : adj[node]){
    if(!visited[next]){
      dfs(next);
    }
  }
}

//Stack based DFS
void DFS(int start){
  // fill distance array with -1's
  memset(dist, -1, sizeof(dist));

  stack<int> st;
  dist[start] = 0;

  st.push(start);
  while(!st.empty()){
    int node = st.top();
    st.pop();

    for(int next : adj[node]){
      if(dist[next] == -1){
        dist[next] = dist[node] + 1;
        st.push(next);
        }
      }
    }
}

int main(){
  int n, m; // number of nodes and edges
  cin >> n; // reads in number of nodes
  cin >> m; // reads in number of edges
  for(int i = 0; i < m; i++){ // reading in each of the m edges
    int a, b;
    cin >> a >> b;
    addEdge(a,b);
  }

  dfs(0);

  return 0;
}

{% endhighlight %}
