'''
Calculates the area of the convex polygon given by the 
points in pts (that are given in the right order).

Time-Complexity: O(n), n = len(pts)
Space-Complexity: O(n)
'''
from __future__ import division

def area(pts):
    out = 0
    for i in range(-1,len(out)-1):
        out += pts[i][0]*pts[i+1][1]-pts[i][1]*pts[i+1][0]
    return abs(out/2)
