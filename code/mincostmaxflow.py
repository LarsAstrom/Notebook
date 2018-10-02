'''
Solves the min-cost-max-flow problem. This is finding a flow
of maximal capacity (or of capacity at most maxf) with a 
minimal cost. Each edge has a capacity and a cost.

Time Complexity: O(min(N^2*M^2, N*M*F))
Space Complexity: O(N^2)

This solution is about 2 times slower than java.
'''

#edge = [to, cap, cost, rev, f]
INF = 10**15

def createGraph(n):
    return [[] for _ in range(n)]

def addEdge(graph, fr, to, cap, cost):
    graph[fr].append([to,cap,cost,len(graph[to]),0])
    graph[to].append([fr,0,-cost,len(graph[fr])-1,0])

#edge = [to, cap, cost, rev, f]
def bellmanFord(s):
    n = len(graph)
    for i in range(n): dist[i] = INF
    dist[s] = 0
    inqueue = [False]*n
    curflow[s] = INF
    q = [0]*n
    qt = 0
    q[qt] = s
    qt += 1
    qh = 0
    while (qh-qt)%n != 0:
        u = q[qh%n]
        inqueue[u] = False
        for i in range(len(graph[u])):
            e = graph[u][i]
            if(e[4] >= e[1]): continue
            v = e[0]
            ndist = dist[u] + e[2]
            if dist[v] > ndist:
                dist[v] = ndist
                prevnode[v] = u
                prevedge[v] = i
                curflow[v] = min(curflow[u], e[1]-e[4])
                if not inqueue[v]:
                    inqueue[v] = True
                    q[qt%n] = v
                    qt += 1
        qh += 1

#edge = [to, cap, cost, rev, f]
def minCostFlow(s, t, maxf):
    n = len(graph)

    flow = 0
    flowCost = 0
    while flow < maxf:
        bellmanFord(s)
        if dist[t] == INF: break
        df = min(curflow[t], maxf - flow)
        flow += df
        v = t
        while v != s:
            e = graph[prevnode[v]][prevedge[v]]
            graph[prevnode[v]][prevedge[v]][4] += df
            graph[v][e[3]][4] -= df
            flowCost += df*e[2]
            v = prevnode[v]
    return (flow, flowCost)

#Example of useage. MUST USE THE SAME NAMES!
N,M,S,T = map(int, raw_input().split())
graph = createGraph(N)
for i in range(M):
    U,V,C,W = map(int, raw_input().split())
    addEdge(graph, U, V, C, W)

dist = [INF]*N
curflow = [0]*N
prevedge = [0]*N
prevnode = [0]*N
flow, flowCost = minCostFlow(S, T, INF)
print flow, flowCost









