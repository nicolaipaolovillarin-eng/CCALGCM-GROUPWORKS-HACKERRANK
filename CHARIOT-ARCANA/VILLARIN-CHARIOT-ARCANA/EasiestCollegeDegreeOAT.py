def solve(n, k, vals):
    vals.sort(reverse=True)
    return sum(vals[::k])


n, k = map(int, input().split())
vals = [int(input()) for _ in range(n)]

print(solve(n, k, vals))
