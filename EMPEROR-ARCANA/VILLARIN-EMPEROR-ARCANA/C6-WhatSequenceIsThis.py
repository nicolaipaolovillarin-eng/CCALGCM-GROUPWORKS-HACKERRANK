def solve(n):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD

    return dp[n]


n = int(input().strip())
print(solve(n))
