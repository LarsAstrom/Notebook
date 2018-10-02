'''
Returns the longest increasing of list X.

Time Complexity: O(N), N = len(X)
Space Complexity: O(N)
'''

def lis(X):
    L = 0
    N = len(X)
    P = [-1]*N
    M = [-1]*(N+1)
    
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo+hi+1)/2
            if X[M[mid]] < X[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo
        P[i] = M[newL-1]
        M[newL] = i
        if newL > L:
            L = newL

    S = [-1]*L
    k = M[L]
    for i in range(L-1,-1,-1):
        S[i] = X[k]
        k = P[k]

    return S
