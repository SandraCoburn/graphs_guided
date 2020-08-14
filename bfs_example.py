def bfs(s,lst):
    level = {s:0}
    parent = {s:None}
    i = 1
    frontier =[s]
    while frontier:
        next = []
        for u in frontier:
            for v in lst[u]:
                if v not in level:
                    level[v] =i
                    parent[v] = u
                    next.append(v)
    frontier = next  
    i += 1

adjlist = []
bfs(3,adjlist)
