# Greedy Algorithms
- Optimization problems: minimize or maximize objective function
- Makes locally optimal choice at each step
- Problems with greedy solution have "greedy choice property"
- Works for some problems, not always optimal

## Examples where Greedy Works
- Fractional Knapsack Problem
- Interval Scheduling 
- Task Scheduling
- Minimum Spanning Trees (Kruskal's, Prim's)
- Shortest Paths (Dijkstra's, Bellman-Ford)
- Change Making (for some coin sets)
- Maximum Spacing k-clustering

## Fractional Knapsack Problem (FKP)
- Items with weights $w_i$ and benefits $b_i$, max weight $W$
- Allowed to take fractional amounts $x_i$, $0 \leq x_i \leq w_i$
- Goal: Maximize total benefit $\sum_{i \in S} b_i \frac{x_i}{w_i}$
- Greedy algorithm:
  1. Compute value index $v_i = \frac{b_i}{w_i}$ for each item
  2. Sort by decreasing $v_i$ (e.g., with max heap)
  3. Take items until knapsack full
- Optimal: satisfies greedy choice property
- Time: $O(n \log n)$ to sort, $O(\log n)$ per choice
- Compare to {0, 1} Knapsack where greedy fails

## Interval Scheduling
- Tasks with start times $s_i$ and finish times $f_i$
- Two tasks compatible if $f_i \leq s_j$ or $f_j \leq s_i$
- Goal: Maximum subset of compatible tasks
- Greedy algorithm:
  1. Sort tasks by increasing $f_i$
  2. Take task that finishes first
  3. Remove conflicting tasks
  4. Repeat
- Optimal: Proof by contradiction with greedy choice 
- Time: $O(n \log n)$ to sort

## Key takeaways

- Greedy algorithms make locally optimal choices
- Work for some optimization problems, not always
- Fractional Knapsack (contrast with {0,1})
- Interval Scheduling (earliest finish time)
- Proofs of correctness exploit greedy choice property
