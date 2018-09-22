def gcd(a,b):
    if a < b: return gcd(b,a)
    if b == 0: return a
    return gcd(b,a%b)

#Returns (u,v) such that au+bv = gcd(a,b)
def bezout(a,b):
    if a < b: 
        v,u = bezout(b,a)
        return (u,v)
    if b == 0: return (1,0)
    u1,v1 = bezout(b,a%b)
    return (v1,u1-a//b*v1)

#Solves x = a_i mod b_i for a_i in a, b_i in b.
def crt(a,b):
    if len(a) == 1: return (a[0],b[0])
    c1,c2,m1,m2 = (a[-2],a[-1],b[-2],b[-1])
    k = gcd(m1,m2)
    if c1%k != c2%k: return (False, False)
    r = c1%k
    u,v = bezout(m1/k,m2/k)
    x = ((((c1//k)*v*(m2//k) + (c2//k)*u*(m1//k))%(m1*m2/k/k))*k + r) % (m1*m2/k)
    return crt(a[:-2]+[x], b[:-2]+[m1*m2/k])
