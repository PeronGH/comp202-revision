# Graphs and Shortest Paths

## Graph Terminology
- Graph $G = (V, E)$: vertices $V$, edges $E$ (directed or undirected)
- Adjacent vertices, incident edges, degree of vertex
- In digraphs: in-degree, out-degree
- Walk (vertex to vertex), path (distinct walk), circuit (closed walk), cycle (distinct closed walk)
- Simple graph: at most one edge between any pair of vertices
- Subgraph, spanning subgraph, connected graph, components
- Forest (no cycles), tree (connected forest), rooted tree, spanning tree

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
  - Running time: $O(|E|+|V| \log |V|)$ with priority queue, or $O(|V|^2)$ with array

- Bellman-Ford: works with negative weights, detects negative cycles
  - $|V|$​ passes, relax all edges in each pass
    - Relax: for edge $(u, v)$, if path to $v$ through $u$ is shorter than current, update.
  - Running time: $O(|V| \cdot |E|)$

### All-Pairs Shortest Paths (APSP)
- Shortest paths between all pairs of vertices
- Bellman-Ford from each vertex: $O(|V|^2 \cdot |E|)$, up to $O(|V|^4)$
- Floyd-Warshall algorithm: $O(|V|^3)$​
  - Init DP Table: $|V| \cdot |V|$ with $0$ if is self, $weight$ if adjacent, or $\infty$​ if not adjacent
  - `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])` (`k` is intermediate vertex)
  - If any `dist[i][i] < 0`, the negative cycle detected

- Open problem to find $O(|V|^{3-\epsilon})$ APSP algorithm

## Summary

The key ideas are representing graphs, basic search algorithms, and shortest path algorithms for SSSP (Dijkstra, Bellman-Ford) and APSP (repeated squaring, difficulty of subcubic algorithms). Graph algorithms utilize greedy and dynamic programming approaches.

