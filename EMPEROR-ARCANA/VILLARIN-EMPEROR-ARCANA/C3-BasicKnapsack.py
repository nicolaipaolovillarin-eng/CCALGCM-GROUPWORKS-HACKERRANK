MOD = 1000000007

def solve(n, c, ws):
    dp = [0] * (c + 1)
    dp[0] = 1

    for w in ws:
        for capacity in range(c, w - 1, -1):
            dp[capacity] = (dp[capacity] + dp[capacity - w]) % MOD

    return sum(dp) % MOD


n, c = map(int, input().split())
ws = [int(input()) for _ in range(n)]

print(solve(n, c, ws))
