'''
Returns the solution to the knapsack problem with weights w, values v
and total capacity W. DP[i][j] is the total value when taking a the i
first objects with a total weight of at most j. The solution is found in
DP[len(w)], where the specific problem will have different places to
find the solution. NOTE THAT SOMETIMES, IT IS MORE EFFICIENT TO STORE
MAPS AT EACH LEVEL IN THE DP.

Time Complexity: O(n*W)
Space Complexity: O(n*W)
'''
def knapsack(w, v, W):
    n = len(w)
    DP = [[0]*(W+1) for _ in range(n+1)]
    for j in range(W+1): DP[0][j] = 0
    for i in range(1,n+1):
        for j in range(W+1):
            if w[i-1] > j: #If it is not possible to put i in the bag
                DP[i][j] = DP[i-1][j]
            else: #Otherwise we either 
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-w[i-1]] + v[i-1])
    return DP
