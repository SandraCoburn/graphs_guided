# Depht First Search, Topological Sort

## Cycle Detection:

- Graph has a cycle:
  - dfs has a back edge
  - Proof:
    - Start at zero and go left

## Job Scheduling

- given directed acyclic graph - DAG
- order the vertices so that all edges point from lower to higher order
  This is a topological sort algorithm. Run DFS. Reverse of finishing times of vertices.
  Every time we finish a vertix we can add it to the list. We take that order and we reverse it and that would be a topological order.

### Correctness: For any eges point from an early number to a later number. e=(u,v) We want the second number v to finish before the first number u.

- Case 1. U starts before V
- Case 2. V starts before U
