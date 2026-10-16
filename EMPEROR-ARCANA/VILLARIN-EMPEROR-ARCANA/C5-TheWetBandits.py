def solve(n, k, vals):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        take = vals[i - 1]

        if i - k - 1 >= 1:
            take += dp[i - k - 1]

        dp[i] = max(dp[i - 1], take)

    return dp[n]


n, k = map(int, input().split())
vals = []

for i in range(n):
    vals.append(int(input()))

print(solve(n, k, vals))
