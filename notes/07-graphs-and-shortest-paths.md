# Graphs and Shortest Paths

## Graph Terminology
- Graph $G = (V, E)$: vertices $V$, edges $E$ (directed or undirected)
- Adjacent vertices, incident edges, degree of vertex
- In digraphs: in-degree, out-degree
- Walk, path, circuit, cycle
- Simple graph: at most one edge between any pair of vertices
- Subgraph, spanning subgraph, connected graph, components
- Forest, tree, rooted tree, spanning tree

### Graph Representation
- Adjacency list: linked lists of neighbors for each vertex
- Adjacency matrix: $\{0,1\}$ matrix, 1 if edge exists

### Graph Search
- Depth-First Search (DFS): explore as far as possible, backtrack
- Breadth-First Search (BFS): explore all neighbors first
- Running time: $O(|V| + |E|)$
- Applications: connectivity, cycles, shortest paths, etc.

## Shortest Paths
- Weighted graph: edges have weights (lengths)
- Single-source shortest paths (SSSP): shortest paths from source $s$ to all vertices
- Dijkstra's algorithm: greedy BFS, doesn't work with negative weights
- Bellman-Ford: works with negative weights, detects negative cycles
  - $|V|$ passes, relax all edges in each pass
  - Running time: $O(|V| \cdot |E|)$

### All-Pairs Shortest Paths (APSP)
- Shortest paths between all pairs of vertices
- Bellman-Ford from each vertex: $O(|V|^2 \cdot |E|)$, up to $O(|V|^4)$
- Dynamic programming: $\ell_{ij}^{(m)}$ = min weight path $i \to j$ with $\leq m$ edges
  $\ell_{ij}^{(m)} = \min\{\ell_{ij}^{(m-1)}, \min_{1 \leq k \leq n} \{\ell_{ik}^{(m-1)} + w_{kj}\}\}$
- Define $(\min, +)$-matrix product $\odot$, compute $L^{(1)}, \ldots, L^{(n-1)}$
- Repeated squaring: $O(|V|^3 \log |V|)$ time
- Floyd-Warshall algorithm: $O(|V|^3)$
- Open problem to find $O(|V|^{3-\epsilon})$ APSP algorithm

## Summary

The key ideas are representing graphs, basic search algorithms, and shortest path algorithms for SSSP (Dijkstra, Bellman-Ford) and APSP (repeated squaring, difficulty of subcubic algorithms). Graph algorithms utilize greedy and dynamic programming approaches.

