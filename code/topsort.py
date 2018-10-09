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
    n = len(adj)
    par = [0]*n
    for l in adj:
        for node in l:
            par[node] += 1
    count = 0
    sorting = [-1]*n
    queue = deque([])
    for i in range(n):
        if par[i] == 0:
            sorting[i] = count
            count += 1
            queue.append(i)

    is_unique_sorting = True
    while queue:
        if len(queue) > 1: is_unique_sorting = False
        cur = queue.popleft()
        for child in adj[cur]:
            par[child] -= 1
            if par[child] == 0:
                queue.append(child)
                sorting[child] = count
                count += 1

    if -1 in sorting: #Some element has not been given a number.
        return False
    if is_unique_sorting: 
        return sorting
    return 'not unique'
