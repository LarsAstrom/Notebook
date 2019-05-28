from collections import deque

'''
Gets the topological sorting of the graph given by the adjacency
list adj, where adj[i] is a list of all nodes which are "after"
node i. Returns a sorting, which is given by sort[i] is the 
position of node i. The topological sorting is usually performed
on a DAG and is the DAG order. If an the solution is not unique, 
this is returned and if contradiction (cycle) is detected False is 
returned. These are easy to change to suit the problem.

Time-Complexity: O(m+n), n is the number of nodes.
Space-Complexity: O(m+n)
'''
def topsort(adj):
    N = len(adj)
    par = [0]*N
    for l in adj:
        for node in l:
            par[node] += 1
    sorting = []
    queue = deque([])
    for i in range(N):
        if par[i] == 0:
            sorting.append(i)
            queue.append(i)

    while queue:
        cur = queue.popleft()
        for child in adj[cur]:
            par[child] -= 1
            if par[child] == 0:
                queue.append(child)
                sorting.append(child)

    if len(sorting) < N: return None
    return sorting
