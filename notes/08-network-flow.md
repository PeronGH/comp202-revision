# Network Flow

## Maximum Flow Problem
- Flow network $G = (V, E)$: directed graph with capacities $c(u,v) \geq 0$ on edges
- Source $s$, sink $t$
- Flow $f(u,v)$ on each edge, subject to:
  - Capacity constraint: $0 \leq f(u,v) \leq c(u,v)$
  - Flow conservation: $\sum_{v} f(v,u) = \sum_{v} f(u,v)$ for all $u \neq s,t$
- Value of flow: $|f| = \sum_{v} f(s,v) - \sum_{v} f(v,s)$
- Maximum flow problem: find flow of maximum value

### Ford-Fulkerson Algorithm
- Start with $f(u,v) = 0$ for all $(u,v)$
- At each iteration:
  - Find augmenting path $P$ in residual network $G_f$
  - Send maximum possible flow $\Delta_f(P)$ along $P$
  - Update flow $f$ and residual network $G_f$
- Terminates when no augmenting path exists

#### Residual Network  
- Edges that can admit more flow
- For each edge $(u,v)$ in $G$:
  - If $f(u,v) < c(u,v)$, include forward edge $(u,v)$ with residual capacity $\Delta_f(u,v) = c(u,v) - f(u,v)$
  - If $f(u,v) > 0$, include backward edge $(v,u)$ with residual capacity $\Delta_f(v,u) = f(u,v)$

#### Augmenting Path
- Path $s \leadsto t$ in residual network $G_f$ 
- Update flow: $f'(u,v) = f(u,v) + \Delta_f(P)$ for forward edge, $f'(v,u) = f(v,u) - \Delta_f(P)$ for backward edge

### Max-Flow Min-Cut Theorem
- Cut $(S,T)$: partition of $V$ with $s \in S$, $t \in T$
- Capacity of cut: $c(S,T) = \sum_{u \in S, v \in T} c(u,v)$   
- **Theorem**: Max flow value equals min cut capacity

### Running Time
- $O(|f^*| m)$ augmentations, $O(m)$ per augmentation
- Bad if $|f^*|$ large
- Edmonds-Karp: pick shortest augmenting path, $O(nm^2)$ time

## Bipartite Matching
- Bipartite graph: vertices partitioned into $X$ and $Y$, all edges $X \to Y$
- Matching: subset of edges, each vertex in at most one edge
- Maximum matching: matching with max number of edges

### Reduction to Max Flow
- Add source $s$, sink $t$
- Edges $s \to X$, $X \to Y$, $Y \to t$, all with capacity 1
- Max flow = max matching
- Find max matching via Ford-Fulkerson: $O(nm)$ time

## Summary

The key ideas are the max flow problem setup, the Ford-Fulkerson algorithm using augmenting paths and residual networks, the Max-Flow Min-Cut Theorem, and the reduction of bipartite matching to max flow.
