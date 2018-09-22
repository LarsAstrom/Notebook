#z[i] = Length of the longest common prefix of s and s[i:], i > 0.
def zfun(s):
    n = len(s)
    z = [0]*n
    l,r = (0,0)
    for i in range(1,n):
        if i < r:
            z[i] = min(z[i-l], r-i+1)
        while z[i] + i < n and s[i+z[i]] == s[z[i]]:
            z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
    return z

#b[i] = Length of longest suffix of s[:i] that is a prefix of s.
def boarders(s):
    n = len(s)
    b = [0]*n
    for i in range(1,n):
        k = b[i-1]
        while k > 0 and s[k] != s[i]: k = b[k-1]
        if s[k] == s[i]: b[i] = k + 1
    return b
