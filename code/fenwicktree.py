'''
Constructs a fenwicktree of an array. Can update a bit and get the
sum up to and including i in the array.

Time Complexity: O(NlogN) for construction, O(logN) for update and query.
SpaceComplexity: O(N)
'''
def fenwicktree(arr):
    fwtree = [0]*(len(arr)+1)
    for i in range(len(arr)):
        updatebit(fwtree,i,arr[i])
    return fwtree

def updatebit(fwtree,i,val):
    i += 1
    while i < len(fwtree):
        fwtree[i] += val
        i += i&(-i)

# get sum of [0,i] inclusive
def getsum(fwtree,i):
    s = 0
    i += 1
    while i > 0:
        s += fwtree[i]
        i -= i&(-i)
    return s
