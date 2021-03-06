 
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()

        # Add starting vertex ID
        q.enqueue(starting_vertex_id)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while q.size() > 0:

            # Dequeue a vert
            v = q.dequeue()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def bfs(self, starting_vertex_id, target_vertex_id):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex_id])
        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty..
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_node = path[-1]
            # If that vertex has not been visited...
            if last_node not in visited:
                # CHECK IF IT'S THE TARGET
                if last_node == target_vertex_id:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_node)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_nbr in self.get_neighbors(last_node):
                    new_path = list(path)
                    # COPY THE PATH
                    new_path.append(next_nbr)
                    print("new path:", new_path)
                    # APPEND THE NEIGHOR TO THE BACK
                    q.enqueue(new_path)

    def dft_recursive(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex_id)
        print("dft recursive", starting_vertex_id)
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
    def dfs_recursive(self, vertex, ending_ver, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(vertex)
        path = path + [vertex] #subtly makes a copy of the path
        '''
        line above is equivalent to:
        path = list(path) #make a copy
        path.append(vertex)
        '''
        if vertex == ending_ver:
            return path
        for neighbor in self.get_neighbors(vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, ending_ver, visited, path)
                if new_path is not None:
                    print("recursive dfs:", new_path)
                    return new_path
        return None


g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(6, 5)
g.add_edge(5, 4)

print(g.vertices)

g.bft(3)
g.dft_recursive(1)
g.dfs_recursive(1,6)
# self.vertices = {
#     1: {2}
#     2: set(1)
# }