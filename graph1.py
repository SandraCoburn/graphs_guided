class Graph:
    def __init_-(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices(vertex_id) = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) 
        else:
            raise IndexError("nonexisten vertex")
    def get_neighbors(self.vertex_id):
        return self.vertices[vertex_id]

g = Graph()
g.add_vertex(2)
g.add_edge(1,2)
g.add_edge(2,1) #undirected graph

self.vertices = {
    1: {2}
    2: set(1)
}