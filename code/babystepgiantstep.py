'''
Solves a^x=b mod P, where a is a primitive root of
prime P and b is an arbitrary number.

Time-complexity: O(sqrt(P))
Space-complexity: O(sqrt(P))
'''
def babystepgiantstep(a,b,P):
    m = int(P**0.5) + 1
    aminv = pow(pow(a,m,P),P-2,P)
    vals = {}
    for j in range(m):
        vals[pow(a,j,P)] = j
    for i in range(m):
        if b in vals:
            return i*m+vals[b]
        b *= aminv
        b %= P
