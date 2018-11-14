'''
All roots stored in roots, depth of each tree stored in depth.
Both roots and depth can be either a list or a dict.

Time Complexity: O(logN) for both find and union, where N is the 
                    number of objects in the structure
Space Complexity: O(N)
'''

#Finds root in the tree containing n.
def find(n):
    if roots[n] != n: roots[n] = find(roots[n])
    return roots[n]

#Unions the trees containing n and m. Returns true if the nodes 
#are in different trees, otherwise false.
def union(n,m):
    pn = find(n)
    pm = find(m)
    if pn == pm: return False
    if depth[pn] < depth[pm]: roots[pn] = pm
    elif depth[pm] < depth[pn]: roots[pm] = pn
    else:
        roots[pn] = pm
        depth[pm] += 1
    return True
