'''
Constructs a fenwicktree of an array. Can update a bit and get the 
sum up to and including i in the array.
'''
def fenwicktree(arr):
    fwtree = [0]*(len(arr)+1)
    for i in range(len(arr)):
        updatebit(fwtree,len(arr),i,arr[i])
    return fwtree

def updatebit(fwtree,n,i,val):
    i += 1
    while i <= n:
        fwtree[i] += val
        i += i&(-i)

def getsum(fwtree,i):
    s = 0
    i += 1
    while i > 0:
        s += fwtree[i]
        i -= i&(-i)
    return s
