'''
This is an algorithm for calculating max-flow. 
Timecomplexity is approximately O(log(c)*m^2) [Worst case]. 
Expected timecomplexity is much lower.
edg is an adjacency list, where e[i] is a list of all i's neighbors.
caps is a matrix where caps[i][j] is the current capacity from i to j.
inf is some sufficiently large number (larger than max capacity).
s and t are the source and sink, respectively.
n is the number of nodes.
'''
def dfs(vis,df,cmf,treshold):
    cur = df.pop()
    if vis[cur]: return 0
    vis[cur] = True
    if cur == t: return cmf
    for e in edg[cur]:
        if not vis[e] and caps[cur][e] > treshold:
            df.append(e)
            a = dfs(vis,df,min(caps[cur][e],cmf),treshold)
            if a:
                caps[cur][e] -= a
                caps[e][cur] += a
                return a
    return 0

def cap():
    c = 0
    for t in range(30,-1,-1):
        toAdd = dfs([False]*n,[s],inf,2**t-1)
        while toAdd: 
            c += toAdd
            toAdd = dfs([False]*n,[s],inf,2**t-1)
    return c

def delnegcyc():
    dist = [inf]*n
    prev = [-1]*n
    dist[s] = 0
    for v in range(n):
        for ne in edg[v]:
            if caps[v][ne] == 0: continue
            tempdist = dist[v] + costs[v][ne]
            if tempdist < dist[ne]:
                dist[ne] = tempdist
                prev[ne] = v
    for v in range(n):
        for ne in edg[v]:
            if caps[v][ne] == 0: continue
            if dist[v] + costs[v][ne] < dist[ne]:
                cur = prev[v]
                c = caps[cur][v]
                while cur != v:
                    c = min(caps[prev[cur]][cur],c)
                    cur = prev[cur]
                cur = prev[v]
                caps[cur][v] -= c
                caps[v][cur] += c
                while cur != v: 
                    caps[prev[cur]][cur] -= c
                    caps[cur][prev[cur]] += c
                    cur = prev[cur]
                return True
    return False

inf = 10**15
n,m,s,t = map(int, raw_input().split())
edg = [[] for _ in range(n)]
caps = [[0]*n for _ in range(n)]
origcaps = [[0]*n for _ in range(n)]
costs = [[0]*n for _ in range(n)]
for _ in range(m):
    u,v,c,w = map(int, raw_input().split())
    edg[u].append(v)
    edg[v].append(u)
    caps[u][v] += c
    origcaps[u][v] += c
    costs[u][v] = w
    costs[v][u] = -w
mf = cap()
while delnegcyc():
    pass
cst = 0
for node in range(n):
    for ne in edg[node]:
        if origcaps[node][ne]:
            cst += (origcaps[node][ne]-caps[node][ne])*costs[node][ne]
            
print mf,cst
