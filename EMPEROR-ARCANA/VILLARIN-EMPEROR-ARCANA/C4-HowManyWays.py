MOD = 1000000007

def solve(n, r):
    if r < 0 or r > n:
        return 0

    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD


q = int(input().strip())
queries = []

max_n = 0

for _ in range(q):
    n, r = map(int, input().split())
    queries.append((n, r))
    max_n = max(max_n, n)

fact = [1] * (max_n + 1)
inv_fact = [1] * (max_n + 1)

for i in range(1, max_n + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)

for i in range(max_n, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

for n, r in queries:
    print(solve(n, r))
