from __future__ import division
'''
Contains the most common geometric operations on points, 
segments and lines. 
Points are represented as (x,y)
Segments are represented as (x1,y1,x2,y2)
Lines are represented as (a,b,c), where ax+by+c=0 is the 
equation of the line.

Contains the following operations:
    Getting a line from two points
    Getting intersection between pairs of lines or segments
    Getting the closest point on a line or segment to a point
    Getting distance from a point to a point, segment or line
    Finding out if a point is on a segment or not.

Time Complexity: O(1)
Space Complexity: O(1)
'''
#Returns a line from two points.
def two_points_to_line(x1,y1,x2,y2):
    return (y2-y1,x1-x2,x2*y1-y2*x1)

#Returns the intersection between the lines.
#Assumes the lines have either a or b different from 0.
def line_line_intersect(line1,line2):
    a1,b1,c1 = line1
    a2,b2,c2 = line2
    cp = a1*b2 - a2*b1
    if cp!=0:
        return ((b1*c2-b2*c1)/cp,(a2*c1-a1*c2)/cp)
    else:
        if a1*c2==a2*c1 and b1*c2==b2*c1:
            return line1
        return None

#Returns the intersection between two segments.
#Assumes the segments have length > 0.
#Return value is None, a point or a segment. 
def seg_seg_intersect(seg1,seg2):
    line1=two_points_to_line(*seg1)
    line2=two_points_to_line(*seg2)
    p=line_line_intersect(line1,line2)
    if p == None: return None
    if len(p)==2:
        if weak_point_on_seg(seg1,p) and weak_point_on_seg(seg2,p):
            return p
        return None
    pts = [(seg1[0],seg1[1],0), (seg1[2],seg1[3],0), 
            (seg2[0],seg2[1],1), (seg2[2],seg2[3],1)]
    pts.sort()
    if pts[1][0] == pts[2][0] and pts[1][1] == pts[2][1]\
            and pts[1][2] != pts[2][2]:
        return (pts[1][0],pts[1][1])
    if pts[0][2] != pts[1][2]:
        return (pts[1][0],pts[1][1],pts[2][0],pts[2][1])
    return None

#Returns the point on the segment closest to p.
def seg_point_project(seg, p):
    line = two_points_to_line(*seg)
    p2 = line_point_project(line,p)
    if weak_point_on_segment(seg,p2):
        return p2
    else:
        if dist(p,(seg[0],seg[1])) < dist(p,(seg[2],seg[3])):
            return (seg[0],seg[1])
        else:
            return (seg[2],seg[3])

#Returns the orthogonal projection of a point onto a line.
def line_point_project(line, p):
    a,b,c=line
    x,y=p
    return ((b*(b*x-a*y)-a*c)/(a**2+b**2),
            (a*(-b*x+a*y)-b*c)/(a**2+b**2))

#Returns the euclidean distance between two points.
def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

#Returns the distance from a point to a segment.
def seg_point_dist(seg,p):
    p2 = seg_point_project(seg,p)
    return dist(p,p2)

#Returns the distance from a point to a line.
def line_point_dist(line,p):
    p2 = line_point_project(line, p)
    return dist(p,p2)

#Returns if point p is on segment seg.
def point_on_seg(seg,p):
    x,y = p
    x1,y1,x2,y2 = seg 
    if (x-x1)*(y-y2) == (x-x2)*(y-y1):
        return (x-x1)*(x-x2) <= 0 and (y-y1)*(y-y2) <= 0
    return False

#Only checks that the order of the points is correct.
def weak_point_on_seg(seg,p):
    x,y = p
    x1,y1,x2,y2 = seg 
    return (x-x1)*(x-x2) <= 0 and (y-y1)*(y-y2) <= 0
