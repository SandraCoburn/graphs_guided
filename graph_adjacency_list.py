class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    def __str__(self):
        return str(self.id)+ ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.verList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None
    def addEdge(self, f, t, cost=0):
        if f not in self.verList:
            nv = self.addVertex(f)
        if t not in self.verList:
            nv = self.addVertex(t)
        self.verList[f].addNeighbor(self.verList[t], cost)
    def getVertices(self):
        return self.verList.keys()
    def __iter__(self):
        return iter(self.verList.values())
    def __contains__(self, n):
        return n in self.verList
g = Graph()
for i in range(6):
    print(g.addVertex(i))
print(g.verList)
g.addEdge(0,1,2)
for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    