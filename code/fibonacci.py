'''
Returns the x-th fibonnacci number modulo MOD,
f(0)=f(1)=1.
Time Complexity: O(log(x)*log(x))
Space Complexity: O(log(x)*log(x))
'''
DP = {}
def fib(x):
    if x < 2: return 1
    if x in DP: return DP[x]
    st = 1
    while x >= 2**(st+1): st += 1
    out = steps[st][0]*fib(x-2**st+1) + steps[st][1]*fib(x-2**st)
    out %= MOD
    DP[x] = out
    return out
MOD = 10**9
MAX_2pot = 64
steps = [(0,0),(1,1)]
for _ in range(2,MAX_2pot+1):
    a,b = steps[-1]
    a2 = (a*a+2*a*b)%MOD
    b2 = (a*a+b*b)%MOD
    steps.append((a2,b2))
