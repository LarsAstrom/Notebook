'''
Implementation of dijkstras algorithm. Finds the shortest path from a 
source, to all other nodes (non-negative weights).
adj is a list of adjacency lists and s the source node.

Time Complexity: O(M + NlogN), where N is the number of nodes, M edges.
Space Complexity: O(M + N)
'''
from heapq import heappush, heappop

INF = 10**12
def dijkstra(adj,S):
    N = len(adj)
    d = [INF]*N
    vis = [False]*N
    d[S] = 0
    pq = [] 
    heappush(pq, (d[S],S))
    while pq:
        curD, curN = heappop(pq)
        if vis[curN]: continue
        vis[curN] = True
        for ne,w in adj[curN]:
            altD = curD + w
            if altD < d[ne]:
                heappush(pq,(altD,ne))
                d[ne] = altD
    return d                                                                                                                                
