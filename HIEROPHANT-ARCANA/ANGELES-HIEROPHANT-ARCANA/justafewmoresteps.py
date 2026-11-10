def solve(n):
    MOD = 1000000007
    if n % 2:
        return 0
    c = 1
    for k in range(n // 2):
        c = c * 2 * (2 * k + 1) % MOD * pow(k + 2, MOD - 2, MOD) % MOD
    return c


n = int(input().rstrip())
print(solve(n))