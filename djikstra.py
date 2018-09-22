from heapq import heappush, heappop

INF = 10**12
def djikstra(adj,s):
    d = [INF]*len(adj)
    vis = [False]*len(adj)
    d[s] = 0
    pq = []
    for i in range(len(adj)): 
        heappush(pq, (d[i],i))
    while pq:
        curD, curE = heappop(pq)
        if vis[curE]: continue
        vis[curE] = True
        for ne in adj[curE]:
            alt = curD + ne[1]
            if altD < d[ne[0]]:
                heappush(pq,(altD,ne[0]))
                d[ne[0]] = altD

    return d

                                                                                                                                            
