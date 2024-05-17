# Data Structures

## Linked Lists
- Nodes store element and next/prev pointers
- Doubly-linked list: nodes have next and prev pointers
- List ADT supports referring, update (insert/delete), search

### List Update Methods
- `replaceElement(p, e)`, `swapElements(p, q)`
- `insertFirst(e)`, `insertLast(e)`, `insertBefore(p, e)`, `insertAfter(p, e)`
- `remove(p)`

### Complexity
- Known position $p$: $O(1)$ for insertion, removal
- Only head known: $O(p)$ to traverse to $p$

## Binary Search
- Recursive search on sorted array
- `BINARYSEARCH(S, k, low, high)`: 
  - If `low > high`, key not found
  - Else, compare `k` to `mid = ⌊(low+high)/2⌋`
  - Recurse on left half if `k < key(mid)`, else right half
- Running time: $T(n) = T(n/2) + b = O(\log n)$

## Rooted Trees
- Nodes in parent-child relationship
- Root: special node with no parent
- Leaf: node with no children
- Depth of node $v$: number of ancestors excluding $v$
- Height of tree: max depth of an external node

### Tree Traversals
1. **Preorder**: Root, left subtree, right subtree
2. **Postorder**: Left subtree, right subtree, root  
3. **Inorder**: Left subtree, root, right subtree

### Binary Search Tree (BST)
- Each node stores an element
- Left subtree elements $\leq$ node's element
- Right subtree elements $\geq$ node's element
- Inorder traversal visits nodes in non-decreasing order

#### BST Operations
- Search: `TREESEARCH(k, v)` recursively searches for key $k$
  - If `isExternal(v)`, return $v$
  - If `k = key(v)`, return $v$  
  - If `k < key(v)`, recurse left child, else recurse right child
  - Time: $\Theta(h)$ for tree of height $h$​
- Insertion: search to find where new key belongs, insert there, time $\Theta(h)$
- Deletion: several cases, time $\Theta(h)$ at middle, $\Omega(1)$ at leaf or only 1 child without traversing the tree.

General BSTs may be unbalanced with $h = n$, losing $\Theta(\log n)$ search time.

## Priority Queues
- Elements with associated keys determining priority 
- Methods:
  - `insertItem(k, e)`: insert element $e$ with key $k$
  - `removeMax()`: remove max element
  - `maxElement()`: return max element
  - `maxKey()`: return key of max element
- Can sort using PQ: $n$ inserts then $n$ `removeMax` ops

## Heaps
- Implementation of a PQ 
- Almost complete binary tree, heap-order property
- Can be implemented in arrays:
  - Root: index `0`
  - For node at `i`:
    - Left child: `2i+1`
    - Right child: `2i+2`
- Insertions/deletions in $O(\log n)$ time
- Heap-sort:
  - Build heap in $O(n)$ (Bottom-up/heapify) or $O(n \log n)$ (Insertion-based)
  - Then extract $n$ elements in $O(n\log n)$
