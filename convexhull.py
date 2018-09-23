def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

#Returns hull in counter-clockwise order.
#pts is a list of tuples, each tuple is (x,y).
def hull(pts):
    n = len(pts)
    pts.sort()
    U = []
    L = []
    for i in range(n):
        while len(L)>1 and ccw(L[-2],L[-1],pts[i]) <= 0: L.pop()
        L.append(pts[i])
    for i in range(n-1,-1,-1):
        while len(U)>1 and ccw(U[-2],U[-1],pts[i]) <= 0: U.pop()
        U.append(pts[i])
    L.pop()
    U.pop()
    if len(L) == len(U) == 1 and L[0] == U[0]: return L
    return L+U
