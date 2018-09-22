'''
Finds all distances in the graph given by edg (negative weights might occur)
edg is a list of (u,v,w) where is an edge from u to v with weight w.
'''
inf = 10**15
def fw(N,edg):
    dist = [[inf]*N for _ in range(N)]
    for e in edg:
        dist[e[0]][e[1]] = min(dist[e[0]][e[1]], e[2])
    for i in range(N):
        dist[i][i] = min(0,dist[i][i])
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] < inf and dist[k][j] < inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


