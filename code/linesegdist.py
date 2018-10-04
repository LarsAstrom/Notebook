from __future__ import division
'''
line is defined by (a,b,c) such that ax+by+c=0 is the equation of 
the line. Segment is defined by (x1,y1,x2,y2), where the segment 
is from (x1,y1) to (x2,y2). Point is defined by (x,y).

if (a,b,c) is returned, then the solution is a line. If (x,y) is 
returned, the solution is a point, if False then no solution.

Time Complexity: O(1)
Space Complexity: O(1)
'''
def lineline(line1,line2):
    a1,b1,c1 = line1
    a2,b2,c2 = line2
    if a1 == a2 == 0:
        if b1*c2 == b2*c1: return (a1,b1,c1)
        else: return False
    elif a1 == 0:
        return ((-c2+b2*c1)/(a2*b1),-c1/b1) 
    elif a2 == 0:
        return ((-c1+c2*b1)/(b2*a1),-c2/b2)
    elif b1 == b2 == 0:
        if a1*c2 == a2*c1: return (a1,b1,c1)
        else: return False
    elif b1 == 0:
        return (-a2*c1/(b2*a1)-c2,c1/a1)
    elif b2 == 0:
        return (-a1*c2/(b1*a2)-c2,c2/a2)
    elif a1/b1 == a2/b2:
        if c1/b1 == c2/b2: return (a1,b1,c1)
        else: return False
    else:
        x = (c2/b2-c1/b1)/(a1/b1-a2/b2)
        y = -a1*x/b1-c1/b1
        return (x,y)

#If (x,y) is returned, this is the intersection point. 
#Otherwise False is returned.
def lineseg(line1,seg):
    line2 = twopointstoline(*seg)
    intersection = lineline(line1,line2)
    print line1
    print line2
    print 'Intersection in lineseg is: ',intersection
    if len(intersection) == 3:
        return (seg[0],seg[1])
    elif len(intersection) == 2:
        x,y = intersection
        if (x-seg[0])*(x-seg[2]) <= 0 and (y-seg[1])*(y-seg[3]) <= 0:
            return (x,y)
        return False
    else:
        return False

#The orthogonal projection is returned.
def linepoint(line,p):
    a,b,c = line
    x,y = p
    return ((b*(b*x-a*y)-a*c)/(a**2+b**2),
            (a*(-b*x+a*y)-b*c)/(a**2+b**2))

#Returns intersection point if it exists.
def segseg(seg1,seg2):
    line1 = twopointstoline(*seg1)
    line2 = twopointstoline(*seg2)
    if lineseg(line1,seg2) and lineseg(line2,seg1):
        return lineseg(line1,seg2)
    return False

#Returns the point closest to p on the segment seg.
def segpoint(seg,p):
    line = twopointstoline(*seg)
    p2 = linepoint(line,p)
    if p2 and (p2[0]-seg[0])*(p2[0]-seg[2]) <= 0 and \
            (p2[1]-seg[1])*(p2[1]-seg[3]) <= 0:
        return p2
    else:
        if dist(p,(seg[0],seg[1])) < dist(p,(seg[2],seg[3])):
            return (seg[0],seg[1])
        else: return (seg[2],seg[3])

#Returns the distance between p1 and p2.
def dist(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

#Returns the line as (a,b,c) from two points.
def twopointstoline(x1,y1,x2,y2):
    return (y2-y1,x1-x2,x2*y1-x1*y2)

seg1 = (0,0,2,3)
seg2 = (0,2,2,2)
o = segseg(seg1,seg2)
print o
#print 'Intersection is: ', segseg(seg1,seg2)
