'''
Calculates the distance from a source to all other nodes.
Run this by putting edgs as a list of tuples (u,v,w) where 
the edge goes from u to v with weight w (w might be negative). 
Time Complexity: O(N*M), N #nodes, M #edges
Space Complexity: O(M)
'''
def bfs(cur):
    vis = [False]*n
    b = [cur]
    vis[cur] = True
    while b:
        c = b.pop()
        dists[c] = '-Infinity'
        for ne in adj[c]:
            if not vis[ne]:
                vis[ne] = True
                b.append(ne)

def bellmanford(edgs,s):
    dists[s] = 0
    for i in range(n-1):
        for edg in edgs:
            u,v,w = edg
            if dists[u] + w < dists[v]: dists[v] = dists[u] + w
    for edg in edgs:
        u,v,w = edg
        if dists[v] == '-Infinity': continue
        if dists[u] + w < dists[v] and dists[v] < INF/2: bfs(v)        
    for i in range(n):
        if dists[i] > INF/2 and dists[i] != '-Infinity': 
            dists[i] = 'Impossible'
    return dists
