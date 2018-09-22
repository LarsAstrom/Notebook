'''
Returns gcd for two numbers, or for all numbers in a list.
Also returns Bezout's identity.
TODO: Do it iteratively.
'''
def gcd(a,b):
    if a < b: return gcd(b,a)
    if b == 0: return a
    return gcd(b,a%b)

def listgcd(l):
    if len(l) == 1: return l[0]
    else: return listgcd(l[:-2]+[gcd(l[-2],l[-1])])

#Returns (u,v) such that au+bv = gcd(a,b)
def bezout(a,b):
    if a < b: 
        v,u = bezout(b,a)
        return (u,v)
    if b == 0: return (1,0)
    u1,v1 = bezout(b,a%b)
    return (v1,u1-a//b*v1)
