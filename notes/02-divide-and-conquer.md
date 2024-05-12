# Divide & Conquer

- Solve problem by dividing into subproblems, solving recursively, and combining solutions
- Steps: Divide, Recur, Conquer

## Merge Sort
- D&C sorting algorithm
- Divide array in half, recursively sort halves, merge sorted halves
- Running time: $\Theta(n \log n)$
- Recurrence: $T(n) = 2T(n/2) + cn$

## Binary Search 
- Recurrence: $T(n) = T(n/2) + c$

## Substitution Method
- Solve recurrences by substituting recursive terms
- Example: Merge Sort 
  $T(n) = 2T(n/2) + cn$
  $= 2(2T(n/4) + cn/2) + cn = 4T(n/4) + 2cn$
  $= 4(2T(n/8) + cn/4) + 2cn = 8T(n/8) + 3cn$
  $\ldots$
  $= 2^kT(n/2^k) + kcn$
  With $k = \log n$, $T(n) = \Theta(n\log n)$

## Maximum Subarray Problem
- Find contiguous subarray with largest sum
- D&C solution: Find max crossing mid, max in left half, max in right half
- Recurrence: $T(n) = 2T(n/2) + cn = \Theta(n \log n)$

## Matrix Multiplication
- Naive: $\Theta(n^3)$
- D&C: $T(n) = 8T(n/2) + bn^2 = \Theta(n^3)$ 

## Strassen's Algorithm
- D&C matrix multiplication 
- 7 recursive multiplications of $n/2 \times n/2$ matrices
- Recurrence: $T(n) = 7T(n/2) + bn^2 = \Theta(n^{\log_27}) = \Theta(n^{2.81})$

## Master Method 
For recurrences of form $T(n) = aT(n/b) + f(n)$:
1. If $f(n) = O(n^{\log_ba-\epsilon})$, then $T(n) = \Theta(n^{\log_ba})$
2. If $f(n) = \Theta(n^{\log_ba}\log^kn)$, then $T(n) = \Theta(n^{\log_ba}\log^{k+1}n)$  
3. If $f(n) = \Omega(n^{\log_ba+\epsilon})$ and $af(n/b) \leq \delta f(n)$, then $T(n) = \Theta(f(n))$

## Integer Multiplication
- Naive: $\Theta(n^2)$
- D&C: Split into high and low bits, 3 recursive $n/2$-bit multiplications
- Recurrence: $T(n) = 3T(n/2) + cn = \Theta(n^{\log_23}) = \Theta(n^{1.59})$
