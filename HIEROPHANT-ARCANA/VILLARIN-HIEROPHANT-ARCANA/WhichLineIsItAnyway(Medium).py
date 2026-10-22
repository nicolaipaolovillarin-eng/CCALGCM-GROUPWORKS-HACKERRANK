def solve(n,m,k,times):
    dp = times[0][:]
    
    for level in range(1, n):
        next_dp = [0] * m
        
        for line in range(m):
            best_time = dp[line]
            
            if line > 0:
                best_time = min(best_time, dp[line - 1] + k)
            
            if line < m - 1:
                best_time = min(best_time, dp[line + 1] + k)
            
            next_dp[line] = times[level][line] + best_time
        
        dp = next_dp
        
    return min(dp)
    
n, m, k = list(map(int,input().rstrip().split(" ")))
times = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
print("{}".format(solve(n,m,k,times)))
