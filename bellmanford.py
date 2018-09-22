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
        if dists[i] > INF/2 and dists[i] != '-Infinity': dists[i] = 'Impossible'
    return dists

INF = 10**20
n,m,q,s = map(int,raw_input().split())
while n != 0:
    edgs = []
    adj = [[] for _ in range(n)]
    dists = [INF]*n
    for _ in range(m):
        u,v,w = map(int,raw_input().split())
        edgs.append((u,v,w))
        adj[u].append(v)
    dists = bellmanford(edgs,s)
    for _ in range(q):
        print dists[int(raw_input())]
    print
    n,m,q,s = map(int,raw_input().split())
