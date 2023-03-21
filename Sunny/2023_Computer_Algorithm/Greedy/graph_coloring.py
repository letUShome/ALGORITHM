def colorGraph(graph, n):
    result = {}
    # assign a color to vertex one by one
    for u in range(n):
    # save colors of adjacent vertices
        adj_colors = set([result.get(i) for i in graph.adj[u] if i in result])
    # check for the first available color
        color = 1
        for c in adj_colors :
            if color != c: break
            color = color + 1
    # assign vertex `u` the first available color
        result[u] = color
    for v in range(n):
        print('Color of vertex {} is {}').format(v, adj_colors[result[v]])

class Graph:
    def __init__(self, edges, n):
        self.adj = [[] for _ in range(n)]
        for (start, end) in edges:
            self.adj[start].append(end)
            self.adj[end].append(start)