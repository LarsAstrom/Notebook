from __future__ import division
'''
Solves Ax=b. A has size n*n, b has size n*1
Returns x if unique solution exists, otherwise
'multiple' or 'inconsistent'.

Time Complexity: O(n^3)
Space Complexity: O(n^2)
'''
def gaussianelimination(A,b):
    h = 0
    k = 0
    n = len(A)
    while h < n and k < n:
        imax = h
        for i in range(h+1,n):
            if abs(A[i][k]) > abs(A[imax][k]): imax = i
        if A[imax][k] == 0: k += 1
        else:
            temp = A[h]
            A[h] = A[imax]
            A[imax] = temp
            temp2 = b[h]
            b[h] = b[imax]
            b[imax] = temp2
            for i in range(h+1,n):
                f = A[i][k] / A[h][k]
                A[i][k] = 0
                for j in range(k+1,n):
                    A[i][j] -= A[h][j]*f
                b[i] -= b[h]*f
            h += 1
            k += 1
    x = [-1]*n
    if A[n-1][n-1] == 0 and b[n-1] == 0: return 'multiple'
    elif A[n-1][n-1] == 0 and b[n-1] != 0: return 'inconsistent'
    else: x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n): s += A[i][j]*x[j]
        x[i] = (b[i]-s)/A[i][i]
    return x
