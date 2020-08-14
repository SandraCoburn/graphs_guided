# Connected Components

- A set of nodes that is connected to one another in some way.
- Graphs can have multiple sets of connected nodes that are disjoint.
- A set of connected nodes is called a "connected component".

## Counting connected components:

### Algorithm 1:

- While there are unvisited nodes:
  - Chose an unvisited node
  - Traverse from that node, marking each as visited
  - Increment connected components counter

### Algorithm 2:

- For each node in the graph:
  - If it's unvisited:
  - Traverse from that node, marking each as visited
  - Increment connected component counter
