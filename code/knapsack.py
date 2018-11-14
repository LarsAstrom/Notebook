def knapsack(w, v, W):
    n = len(w)
    DP = [[0]*(W+1) for _ in range(n+1)]
    for j in range(W+1): DP[0][j] = 0
    for i in range(1,n+1):
        for j in range(W+1):
            if w[i-1] > j: #If it is not possible to put i in the bag
                DP[i][j] = DP[i-1][j]
            else: #Otherwise we either put it or not. 
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-w[i-1]] + v[i-1])
    return DP
