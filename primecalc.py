from __future__ import division

maxNumber = 10000
primes = [2,3]
primeToPos = {2:0, 3:1}
posToPrime = {0:2, 1:3}

#Generate all primes
for pp in range(5,maxNumber + 1):
    pr = True
    for p in primes:
        if pp % p == 0:
            pr = False
            break
    if pr:
        primeToPos[pp] = len(primes)
        posToPrime[len(primes)] = pp
        primes.append(pp)

#Get all prime factorizations.
primefactors = [[],[],[2]]
for x in range(3,maxNumber + 1):
    foundD = False
    for prime in primes:
        if prime >= x: break
        if x % prime == 0:
            foundD = True
            primefactors.append(primefactors[x//prime]+[prime])
            break
    if not foundD: primefactors.append([x])
