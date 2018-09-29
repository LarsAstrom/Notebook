'''
Structure: all nodes in a list named uf. For each node its parent 
and height is stored as [parent,height]. 

Time Complexity: O(logN) for both find and union, where N is the 
                    number of objects in the structure
Space Complexity: O(N)
'''

#Finds root in the tree containing n.
def find(n):
    tochange = []
    cur = n
    while uf[cur][0] != cur:
        tochange.append(cur)
        cur = uf[cur][0]
    for tc in tochange: uf[tc][0] = cur
    return cur

#Unions the trees containing n and m. Returns true if the nodes 
#are in different trees, otherwise false.
def union(n,m):
    pn = find(n)
    pm = find(m)
    if pn == pm: return False
    if uf[pn][1] < uf[pm][1]:
        uf[pn][0] = pm
    elif uf[pm][1] < uf[pn][1]:
        uf[pm][0] = pn
    else:
        uf[pm][0] = pn
        uf[pn][1] += 1
    return True
