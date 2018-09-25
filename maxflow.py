'''
This is an algorithm for calculating max-flow. 
edg is an adjacency list, where e[i] is a list of all i's neighbors.
caps is a matrix where caps[i][j] is the current capacity from i to j.
inf is some sufficiently large number (larger than max capacity).
s and t are the source and sink, respectively.
n is the number of nodes.

Time Complexity: O(C*N)
Space Complexity: O(N^2)
'''
def dfs(vis,df,cmf):
    cur = df.pop()
    vis[cur] = True
    if cur == t: return cmf
    for e in edg[cur]:
        if not vis[e] and caps[cur][e] > 0:
            df.append(e)
            a = dfs(vis,df,min(caps[cur][e],cmf))
            if a:
                caps[cur][e] -= a
                caps[e][cur] += a
                return a
    return 0

def cap():
    c = 0
    toAdd = dfs([False]*n,[s],inf)
    while toAdd: 
        c += toAdd
        toAdd = dfs([False]*n,[s],inf)
    return c

#Example of useage.
inf = 10**15
n,m,s,t = map(int, raw_input().split())
edg = [[] for _ in range(n)]
caps = [[0]*n for _ in range(n)]
origcaps = [[0]*n for _ in range(n)]
for _ in range(m):
    u,v,c = map(int, raw_input().split())
    edg[u].append(v)
    edg[v].append(u)
    caps[u][v] = c
    origcaps[u][v] = c
mf = cap()
out = []
for node in range(n):
    for ne in edg[node]:
        if origcaps[node][ne] and (origcaps[node][ne]-caps[node][ne]):
            out.append([node,ne,origcaps[node][ne]-caps[node][ne]])
            
print n, mf, len(out)
for o in out:
    print ' '.join(map(str,o))
