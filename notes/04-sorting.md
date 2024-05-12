# Sorting

## Sorting Problem
- Arrange elements of a collection $C$ into non-decreasing order
- Fundamental algorithmic problem, crucial for performance

## Comparison-based Sorting
- Lower bound: $\Omega(n \log n)$ comparisons
- Proof: Decision tree must have $\geq n!$ leaves, so depth $\geq \log(n!) = \Omega(n \log n)$

## Counting Inversions
- Inversion: pair $(i,j)$ with $i < j$ but $a_i > a_j$ in permutation $a_1, \ldots, a_n$
- Measure of "out-of-orderness" 
- Naively $\Theta(n^2)$ to count
- D&C algorithm in $O(n \log n)$:
  1. Divide list in half
  2. Recursively count inversions in each half
  3. Merge sorted halves and count inversions across halves
- Similar to modified Merge Sort

## Quick Sort
- D&C algorithm: 
  - Choose pivot $x$
  - Divide into $L$ (< $x$), $E$ (= $x$), $G$ (> $x$)
  - Recursively sort $L$ and $G$
  - Concatenate $L$, $E$, $G$
- Worst case: $O(n^2)$ if bad pivots chosen

### Randomised Quick Sort  
- Choose pivots randomly to avoid worst case
- Good pivot: neither $L$ nor $G$ has size > $\frac{3}{4}|S|$
- Probability of good pivot = $\frac{1}{2}$, expect 2 attempts
- With good pivots, expected path length $2\log_{4/3}n$  
- Overall expected time: $O(n \log n)$

## Linear-time Sorting
- Counting Sort: 
  - Assumes input in $\{0,\ldots,k\}$ 
  - Count occurrences of each value
  - Compute positions and place elements
  - Stable, $O(n+k)$ time
- Radix Sort:
  - Sort by least significant digit, then next least, etc. using stable sort
  - Correctness by induction, requires stability
  - $O(dn)$ time for $n$ elements with $d$ digits

## Summary

The key ideas are the $\Omega(n \log n)$ lower bound for comparison-based sorting, the D&C approach of Quick Sort and analysing its expected time with randomisation, and using non-comparative sorting like Counting Sort and Radix Sort to achieve linear time.
