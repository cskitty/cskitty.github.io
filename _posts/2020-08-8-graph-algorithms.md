---
title: "Graph Algorithms"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - BFS
  - Graph
  - BiPartite
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


## Graph Representations

Graphs can be represented in three ways:  

* Adjacency List most frequently used when nodes are large
* Adjacency Matrix when nodes are small
* Edge List

### Adjacency List for Un-Weighted Graph

{% highlight c++ linenos %}

int MX = 1e5; // max num of nodes
vector<int> adj[MX]; // adjacency list where MX is max possible # of nodes
bool visited[MX];    // visited array of size MX as well  
int group[MX];       // group that this node belongs to
bool bad = false;

void addEdge(int a, int b) {
  adj[a].push_back(b);

  // omit this line if the graph is directed
  adj[b].push_back(a);
}

void dfs(int n, int g)
{
    visited[n]=1;
    group[n]=g;
    for(int u:adj[n])
        if(visited[u])
        {
            // process groups, colors etc
            // or terminate the BFS by setting bad=1;
        }
        else
            dfs(u, g);
}

int main(){
  cin >> n; // reads in number of nodes
  cin >> m; // reads in number of edges
  for(int i = 0; i < m; i++){ // reading in each of the m edges
    int a, b;
    cin >> a >> b;
    addEdge(a,b);
  }

  int g = 0;
  for(int i=1;!bad && i<=N;++i)
        if(!vis[i])
            dfs(i, ++g);

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

###  Breadth-First Search
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


### Depth-First Search

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


## Finding Components (Undirected Graph)

### Counting Connected Components

{% highlight c++ linenos %}
int components = 0;
vector<bool> visited(N, false);

F0R(i, N) {
  if (!visited[i]) {
    components++;
    dfs(i, components);
  }
}

cout << "Total " << components << " components" << endl;  
{% endhighlight %}



### Graph Coloring using DFS or BFS

{% highlight c++ linenos %}

vector<int> adj[MX];
int coloring[MX];

string cowType;

bool flag(int current, int end) {
    if (current == end) {
        return true;
    }
    return false;
}

void DFS(int start, int color){
    // fill distance array with -1's

    vector<bool> visited(cowType.size(), false);
    stack<int> st;

    st.push(start);
    while(!st.empty()){
        int node = st.top();
        coloring[node] = color;
        visited[node] = true;
        st.pop();

        for(int next : adj[node]){
            if(! visited[next] && cowType[next] == cowType[node]){
                st.push(next);
            }
        }
    }
}

void DFSColoring(int N) {
    // read in N
    int color = 1;
    F0R(i, N) {
        if (coloring[i] == 0) {
            DFS(i, color);
            color++;
        }
    }
}

{% endhighlight %}
