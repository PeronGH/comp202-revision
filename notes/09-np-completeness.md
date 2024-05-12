# NP-Completeness

## Hard Computational Problems
- Some problems seem hard to solve efficiently
- Open question: Does P = NP? 
- Important in theoretical CS, $1 million Millennium Prize

### Examples 
- {0,1} Knapsack problem
- Hamiltonian Cycle problem

## Optimisation vs Decision Problems
- Decision problem: Output is yes/no
- Optimization: Maximize/minimize some function
- Decision version adds parameter $k$, asks if optimal value $\leq k$ or $\geq k$
- If decision version is hard, optimization version is also hard
- Solving decision problem efficiently allows binary search for optimal value

## Complexity Classes
### Class P
- Decision problems solvable in polynomial time
- Examples: MST, fractional knapsack, shortest paths (non-negative weights), max flow, Euler tours, interval scheduling

### Efficient Certification and Class NP 
- NP: Problems with efficient certifiers
- Efficient certifier $B$: 
  - Takes input $s$ and certificate $t$
  - $s$ is a yes-instance iff there exists $t$, $|t| \leq \text{poly}(|s|)$, with $B(s,t) = $ yes
  - $B$ runs in polynomial time
- Equivalent definition: Problems solvable by non-deterministic polynomial time algorithms
- Examples in NP:
  - {0,1} Knapsack: certificate is subset, check weight and value 
  - Hamiltonian Cycle: certificate is a cycle, check visits each vertex once
  - Circuit-SAT: certificate is satisfying input assignment
- P $\subseteq$ NP, unknown if P = NP

### Class co-NP
- Problems with efficient disqualifiers 
- Example: Primality - certificate for no is factorization
- NP = co-NP also unknown

## Reductions and Hardness
- Reduction: Transform instance of one problem to another
- $L \leq_p M$ ($L$ poly-time reduces to $M$) if $\exists$ poly-time function $f$ mapping instances $s$ of $L$ to instances $f(s)$ of $M$ s.t. $s$ is yes-instance iff $f(s)$ is yes-instance
- $M$ is NP-hard if $\forall L \in NP$, $L \leq_p M$ 
- $M$ is NP-complete if it is NP-hard and in NP
- Cook-Levin Theorem: Circuit-SAT is NP-complete

### Proving NP-completeness
To show $X$ is NP-complete:
1. $X \in NP$
2. $\exists$ known NP-complete problem $Y$ with $Y \leq_p X$

### Some NP-complete Problems
- Circuit-SAT
- {0,1} Knapsack 
- Hamiltonian Cycle
- 3-SAT and CNF-SAT 
- {0,1} Integer Programming 
- Subset Sum
- 3-Coloring (and $k$-coloring for fixed $k \geq 3$)

## Summary

The key ideas are the definitions of P, NP, NP-hard, and NP-complete, the importance of the P vs NP question, polynomial-time reductions, the Cook-Levin theorem, and a variety of canonical NP-complete problems.
