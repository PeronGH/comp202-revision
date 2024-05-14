# Revision

## I. Course Overview

* The primary goal of the course was to develop students' ability to think algorithmically and analyze the correctness and running time of algorithms.
* The course focused mainly on the performance of algorithms in terms of running time, with a secondary emphasis on space complexity.
* Students were exposed to a variety of computational fields where algorithms play a crucial role and learned to apply abstract data types to solve classical algorithmic problems.
* The course covered various examples and problems, including:
    * Graph theory fundamentals and associated problems like maximum flows, shortest paths, and matchings. (Note: Minimum spanning trees are **not** included in the exam.)
    * NP-completeness, the theory of NP problems, and NP-completeness.
    * Cryptography basics, number theory principles, and the RSA algorithm. (Note: Proofs related to RSA components were skipped.)
* The course primarily focused on the mathematical design and analysis of algorithms, with an emphasis on theoretical analysis rather than experimental analysis.

## II. Key Concepts for the Final Exam

* **Running Time Analysis:**
    * The focus is on worst-case running time unless specified otherwise.
    * Input size is typically denoted by 'n,' and running time is expressed as a function of 'n' (e.g., f(n) or T(n)).
    * Big O notation is used to characterize running times. Students should be familiar with arranging functions (like n, log n, n², n log n) in ascending order of efficiency.
    * Understanding the difference between Big O, Big Omega, and Big Theta notation is crucial.
* **Proof Techniques:**
    * Common proof techniques used in the course include mathematical induction, proof by contradiction, proof by contrapositive argument, and disproof by counterexample. Students should be able to identify these techniques in the provided proofs.
* **Algorithmic Paradigms:**
    * The course covered three main algorithmic paradigms: Divide and Conquer, Greedy Algorithms, and Dynamic Programming. Students should be able to:
        * Recognize the importance and applicability of each paradigm.
        * Formulate recurrence relations for algorithms of a Divide and Conquer nature.
        * Solve recurrence relations using the Master method or the substitution method.
* **Data Structures and Sorting Algorithms:**
    * Students should be familiar with various data structures (arrays, lists, binary search trees, heaps) and the operations performed on them (searching, insertion, deletion).
    * Understanding traversal methods for binary search trees (pre-order, in-order, post-order) is important.
    * Several sorting algorithms were covered:
        * Merge sort and Quicksort (Divide and Conquer paradigm)
        * Heapsort
        * Counting sort and Radix sort (non-comparison based sorting)
    * Students should know the running times (worst-case and expected case, where applicable) and descriptions of all sorting algorithms.
* **Graph Algorithms:**
    * Familiarity with basic graph theory terminology (e.g., adjacency, incidence) and different notations for graphs is essential.
    * The course covered two shortest path algorithms: Bellman-Ford and All-Pairs Shortest Paths. Students should understand the running of these algorithms and be able to execute them for one step on a given instance.
* **Maximum Flow Problem:**
    * Students should understand how the Ford-Fulkerson algorithm works and be able to run it on a given graph or network.
    * Familiarity with the statement of the Max-Flow Min-Cut theorem is necessary, but the proof can be skipped. (Note: Finding maximum matchings in bipartite graphs, an application of Ford-Fulkerson, is **not** included in the syllabus.)
* **NP-Completeness:**
    * The theory of NP problems and NP-completeness was covered extensively.
    * Students should:
        * Be able to define formally the decision and optimization versions of NP-complete problems.
        * Argue whether a given problem belongs to NP.
    * While explicit reductions will **not** be asked on the exam, understanding the definition of a reduction is important.
* **Cryptography:**
    * Students should be able to explain how all elements of the RSA algorithm are defined and how it works.
    * The extended Euclidean algorithm is **not** included in the exam, but knowledge of the Euclidean algorithm and its application in RSA is expected.

## III. Exam Format and Preparation Guidance

* The final exam will consist of 50 multiple-choice questions, each with five options and only one correct answer.
* The first 40 questions will be directly based on the syllabus, including definitions, concepts, and basic problem-solving.
* The remaining questions will introduce a few new algorithmic problems that build up to constructing efficient algorithms for them.
* To prepare for the exam, students should:
    * Revise Big O, Big Omega, and Big Theta notation thoroughly, as these are fundamental to understanding algorithm analysis.
    * Review the details of all three algorithmic paradigms (Greedy, Divide and Conquer, Dynamic Programming) and practice examples to identify which method is applicable in various scenarios.
    * Practice formulating and solving recurrence relations for algorithms, especially those related to the Divide and Conquer paradigm.
    * Review all data structures covered, their complexities, and the running times of operations performed on them.
    * Study all sorting algorithms and their running times in detail, paying attention to both worst-case and expected case scenarios where applicable.
    * Be able to explain how the Ford-Fulkerson algorithm works and apply it to a given graph or network.
    * Understand the definitions of NP, NP-completeness, and reductions, and be able to apply this knowledge to determine whether a problem belongs to NP.
    * Understand the RSA method, including how its elements are defined, the Euclidean algorithm, and its steps.

## IV. Resources Available:

* Annotated lecture slides, recordings of lectures, exercises and solutions, past exam papers (without solutions but with a recorded solution for one of the harder problems), and tutorial exercises and solutions are available on Canvas.
* Students are encouraged to utilize these resources for review and practice.
