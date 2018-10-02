'''
Solves the problem of counting out. Given n people and 
counting out every k-th person, josephus(n,k) gives the
last person standing. 

Time Complexity: O(n)
Space Complexity: O(n)
'''
def josephus(n,k):
    DP = [-1]*(n+1)
    DP[1] = 0
    for i in range(2,n+1):
        DP[i] = (DP[i-1]+k)%i
    return DP[n]
