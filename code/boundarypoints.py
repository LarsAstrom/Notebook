'''
Calculates the number of lattice boundary points of the
polygon given by pts (including the points in pts). pts has 
to be sorted either in clockwise or counter clockwise order.

Time Complexity: O(nlogn), where n = len(pts).
Space Complexity: O(n)
'''
def gcd(a,b):
    if a < b: return gcd(a,b)
    if b == 0: return a
    return gcd(b,a%b)

def boundarypoints(pts):
    n = len(pts)
    out = 0
    for i in range(-1,n-1):
        dx = abs(pts[i][0]-pts[i+1][0])
        dy = abs(pts[i][1]-pts[i+1][1])
        out += gcd(dx,dy)
    return out
