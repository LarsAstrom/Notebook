'''
Solves a^x=b mod P, where a is a number, P is a prime
and b is an arbitrary number. Here a is usually a 
primitive root with respect to the prime P.

Time-complexity: O(sqrt(P))
Space-complexity: O(sqrt(P))
'''
def babystepgiantstep(a,b,P):
    m = int(P**0.5) + 1
    aminv = pow(pow(a,m,P),P-2,P)
    vals = {}
    for j in range(m):
        val = pow(a,j,P)
        if val not in vals: vals[val] = j
    for i in range(m):
        if b in vals:
            return i*m+vals[b]
        b *= aminv
        b %= P
    return -1
