---
title: "Tree Algorithms"
categories:
  - Programming
tags:
  - C++
  - Algorithms
  - BFS
  - DFS
  - Tree
---

# Tree Algorithms

##  Minimal Spamming Tree: Kruskal’s algorithm

In Kruskal’s algorithm, the initial spanning tree only contains the nodes of
the graph and does not contain any edges. Then the algorithm goes through the
edges ordered by their weights, and always adds an edge to the tree if it does not
create a cycle.   

The algorithm maintains the components of the tree. Initially, each node of
the graph belongs to a separate component. Always when an edge is added to the
tree, two components are joined. Finally, all nodes belong to the same component,
and a minimum spanning tree has been found.  

{% highlight c++ linenos %}
for (...) {
  if (!same(a,b)) unite(a,b);
}
{% endhighlight %}


###  Union-find structure

{% highlight c++ linenos %}

//parent of the node
for (int i = 1; i <= n; i++) link[i] = i;
//size of each set
for (int i = 1; i <= n; i++) size[i] = 1;

int find(int x) {
  while (x != link[x]) x = link[x];
  return x;
}

bool same(int a, int b) {
  return find(a) == find(b);
}

void unite(int a, int b) {
  a = find(a);
  b = find(b);
  if (size[a] < size[b]) swap(a,b);
  size[a] += size[b];
  link[b] = a;
}

{% endhighlight %}



### Trees
A tree is a special type of graph satisfying two constraints: it is acyclic, meaning there
are no cycles, and the number of edges is one less than the number of nodes. Trees satisfy
the property that for any two nodes A and B, there is exactly one way to travel between A
and B.  


###  Tree Diameter
[Tree Diameter] (https://cses.fi/problemset/task/1131)

* Pick any random node (let's call it X).
* Make a BFS traversal from this node.
* Pick the farthest node from X (let's call this node A).
* Run BFS again but from node A.
* Pick the farthest node from A (let's call this node B).
* Return A and B as the endpoints of the tree diameter.

{% highlight c++ linenos %}

const int MaX = 100001;
int N, M;
vector<int> adj[MX];
vector<int> height(MX);
vector<int> visited(MX);
int ans = 0;

void dfs(int st) {
    visited[st] = true;
    height[st] = 0;
    for (int u : adj[st]) {
        if (! visited[u]) {
            dfs(u);
            ans = max(height[st] + 1 + height[u], ans);
            height[st] = max(height[st], height[u] + 1);
            dbg(st, u, height[st], height[u], ans);
        }
    }
}

pair<int, int> bfs(int st) {

    queue<pair<int, int>> myQ;
    myQ.push(make_pair(st, 0));
    fill(visited.begin(), visited.begin() + N + 1, false);

    pair<int, int> curr;
    while (myQ.size() > 0) {
        curr = myQ.front();
        visited[curr.f] = true;
        myQ.pop();

        for(int i : adj[curr.f]) {
            if (! visited[i]) {
                myQ.push(make_pair(i, curr.s + 1));
            }
        }
    }

    return curr;
}

int main() {
    cin >> N;

    F0R(i, N - 1) {
        int A, B;
        cin >> A >> B;

        adj[A].push_back(B);
        adj[B].push_back(A);
    }

    // solution using DFS
    /*dfs(1);
    cout << ans;*/

    // solution using two BFS
    pair<int, int> x = bfs(1);
    pair<int, int> ans = bfs(x.f);

    cout << ans.s;
}

{% endhighlight %}


###  Tree Distances I
[Tree Distances I] (https://cses.fi/problemset/task/1132)

{% highlight c++ linenos %}
const int MaX = 100001;
int N, M;
vector<int> adj[MX];
vector<int> visited(MX);
vector<int> ansV(MX);


pair<int, int> bfs(int st) {

    queue<pair<int, int>> myQ;
    myQ.push(make_pair(st, 0));
    fill(visited.begin(), visited.begin() + N + 1, false);

    pair<int, int> curr;
    while (myQ.size() > 0) {
        curr = myQ.front();
        visited[curr.f] = true;
        myQ.pop();

        for(int i : adj[curr.f]) {
            if (! visited[i]) {
                myQ.push(make_pair(i, curr.s + 1));
            }
        }
    }

    return curr;
}

int dist(int st) {

    queue<pair<int, int>> myQ;
    myQ.push(make_pair(st, 0));
    fill(visited.begin(), visited.begin() + N + 1, false);

    pair<int, int> curr;
    while (myQ.size() > 0) {
        curr = myQ.front();
        myQ.pop();

        visited[curr.f] = true;
        ansV[curr.f] = max((ansV[curr.f]), curr.s);

        for(int i : adj[curr.f]) {
            if (! visited[i]) {
                myQ.push(make_pair(i, curr.s + 1));
            }
        }
    }

    return -1;
}

int main() {
    cin >> N;

    F0R(i, N - 1) {
        int A, B;
        cin >> A >> B;

        adj[A].push_back(B);
        adj[B].push_back(A);
    }

    pair<int, int> x = bfs(1);
    pair<int, int> y = bfs(x.f);

    dist(x.f);
    dist(y.f);

    FOR(i, 1, N + 1) {
        if (i != x.f && i != y.f) {
            cout << ansV[i] << " ";
        }
        else {
            cout << y.s << " ";
        }
    }
}
{% endhighlight %}
