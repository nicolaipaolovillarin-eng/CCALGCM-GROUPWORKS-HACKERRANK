MOD = 1000000007

def solve(k,dp):
    # compute and return answer here
    return dp[k]    
    
q, n = list(map(int,input().rstrip().split(" ")))
a = [int(input().rstrip()) for i in range(n)]
outs = []

dp = [0] * (n)
total = 0
for x in range(0,n):
        dp[x] = (a[x] + total) % MOD  
        total += dp[x] % MOD
        
for i in range(q):
    k = int(input().rstrip())
    outs.append(solve(k,dp))
print("{}".format("\n".join(list(map(str,outs)))))
