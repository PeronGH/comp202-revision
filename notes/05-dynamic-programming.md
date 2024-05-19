# Dynamic Programming
- Optimization problems: maximize or minimize some function
- Similar to Divide and Conquer (D&C), but avoids repetitive recursive calls
- Stores computed values in a table
- Requires certain problem structure:
  1. Simple subproblems with similar structure
  2. Optimal solution composed of optimal subsolutions
  3. Subproblem overlap
- Approach: Find recursive solution, then compute bottom-up to avoid recomputation

## {0, 1} Knapsack Problem
- $n$ Items with weights $w_i$ and benefits $b_i$, max total weight $W$ (capacity)
- Goal: Subset with maximum total benefit, total weight $\leq W$  
- Naïve: Try all $2^n$ subsets, $O(2^n)$ time
- DP Solution:
  - $B[k, w]$ = max benefit with subset of first $k$ items, weight $\leq w$
  - If $k$-th item not used: $B[k, w] = B[k-1, w]$
  - If $k$-th item used: $B[k, w] = b_k + B[k-1, w-w_k]$
  - Desired solution: $B[n, W]$
  - Compute bottom-up: $B[1, w]$, then $B[2, w]$, etc.
  - Algorithm: $O(nW)$ time

## Fibonacci Numbers  
- $F(1) = F(2) = 1$, $F(n) = F(n-1) + F(n-2)$ for $n \geq 3$
- Naïve algorithm: $T(n) = T(n-1) + T(n-2)$, exponential time
- Memoization: Store computed values, $O(n)$ time
- Matrix multiplication: 
  $\begin{bmatrix} F(i+2) \\ F(i+1) \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} F(i+1) \\ F(i) \end{bmatrix}$
  Repeated squaring: $O(\log n)$ time
- Closed form: $F(n) = \frac{1}{\sqrt{5}}(\phi^n - \hat{\phi}^n)$ where $\phi = \frac{1+\sqrt{5}}{2}, \hat{\phi} = \frac{1-\sqrt{5}}{2}$
  Derived using generating functions

## Key takeaways

- DP used for optimization problems 
- Requires decomposability into subproblems with optimal substructure and overlap
- Compute solutions bottom-up to avoid recomputation
- Examples: {0,1} Knapsack and Fibonacci numbers
- Matrix exponentiation and generating functions as additional DP techniques
