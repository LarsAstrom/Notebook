def primefactors(n):
    out = set()
    for i in range(2,int(n**0.5)+3):
        if n % i == 0:
            out2 = primefactors(n/i)
            out.add(i)
            for o in out2: out.add(o)
            return out
    out.add(n)
    return out

def primroot(p):
    ps = primefactors(p-1)
    for i in range(2,p-2):
        suc = True
        for pp in ps:
            if pow(i,(p-1)/pp,p) == 1:
                suc = False
                break
        if suc: return i
    return False
