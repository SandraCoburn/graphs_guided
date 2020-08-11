# Graphs

# Graphs Terminology

- Nodes/Vertexes/Vertices -- the data components of the graph
- Edges -- the connections betweeen nodes

## Directed vs undirected

- Undirected, all edges are two-way
- Directed graphs have one way edges

## Cyclic and Acyclic graphs

- Cyclic graphs have edges pointing to nodes till it goes back at the start. It can form a circle. It goes back to itself. Two nodes graph undirected (going both ways) it's cyclic because you can always go back to the start.
- Acyclic graphs don't have edges pointing back to start. If you cannot form a circle and go back to start of graph, it's acyclic.

## Dense vs Sparse graphs

- Dense graphs - high ratio of edges to nodes, nodes are connected to many other nodes
- Sparse Graphs - The edges don't connect to many of the nodes.

## Weighted and non-weighted graphs

- Weighted edges. If there is a cost to travers between nodes there is a weight on them. The weight might be time, distance, traffic volume.
- Unweighted graphs: edges do not have different weight, are all the same weight

## Graph Representations

- Adjacency matrix: We are interested on which edges have connections with other edges.
  | A | B | C | E
  |---|---|---|---  
  A | F | T | T | T
  B | F | F | F | T
  C | F | F | C | F
  E | F | F | F | F

  | A   | B   | C   | E   |
  | --- | --- | --- | --- |
  | A   | 0   | 5   | 1   | 2 |
  | B   | 0   | 0   | 0   | 0 |
  | C   | 0   | 0   | 0   | 0 |
  | E   | 0   | 0   | 0   | 0 |

- Adjacency List:
  A: [B, C, E]
  B: [E]
  C: []
  E: []

## Breath-First Traversal:

- Init: add starting node to the queue
- Deque a node. If visited, ignore it. Else: add all node's neighbors to the queue. Mark node as visited.

## Depth-First Traversal

- Init: add starting node to Stack

## Breath-First Search:

- Init queue, queue the path: Queue front->[[C,B], [C,G], [C,B,C],[C,B,F], [C,B,E]]
- keep each path in a list
- Keep track of visited nodes with whole path: visited{C}
