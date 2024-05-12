# Fundamentals

- Algorithm analysis - time and space complexity, theoretical vs experimental analysis

- Big-O, Ω, Θ notation and asymptotic run time analysis

- Common functions - logarithmic, linear, quadratic, polynomial, exponential

- Proof techniques - induction, contradiction, contrapositive, counterexample

## Algorithms Analysis

Definition:

- **Algorithm**: Finite sequence of steps to solve a problem using data structures

Focus on:
- Time complexity (running time)
- Space complexity (memory usage)

Two types:
1. **Experimental**: Empirical, limited test cases, requires implementation
2. **Theoretical**: Considers all inputs, compares algorithms independently, uses high-level descriptions

### Theoretical requirements
1. Pseudo-code for algorithm description
2. RAM model assumes constant time primitives
3. Worst-case running time metric
4. Asymptotic notation for running time characterization

### Asymptotic Notation
Describes growth rate of functions w.r.t. input size $n$:
- $O$ (Big-O): Upper bound. $f(n) \leq c \cdot g(n)$ for large $n$.
- $\Omega$ (Omega): Lower bound. $f(n) \geq c \cdot g(n)$ for large $n$.
- $\Theta$ (Theta): Tight bound. $f(n) = \Theta(g(n))$ if both $O$ and $\Omega$.

#### Common growth rates
$1 < \log n < \sqrt{n} < n < n \log n < n^2 < 2^n$

## Proof techniques
- **Induction**: Base case + inductive step
- **Contradiction**: Assume false, derive contradiction
- **Contrapositive**: Prove equivalent statement
- **Counterexample**: Disprove by example

## Key takeaways
- Algorithms use data structures to solve problems
- Theoretical analysis is preferred, using asymptotic notation
- Various proof techniques are essential for correctness and efficiency
