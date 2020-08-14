'''
Edge classification:
- Tree edge: (parent pointer) visit new vertex via edge
- Forward Edge: node to descendent in tree
- backward edge: node to ancestor in tree
- cross edgees: from one subtree to another subtree (not ancestor related)
'''
parent = {s:None}
def dfs_visit(adj, s):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(adj,v)
def dfs(v, adj): #this will check the not strongly connected nodes
    parent ={}
    for s in v:
        if s not in parent:
            parent[s] =None
            dfs_visit(adj, s)

