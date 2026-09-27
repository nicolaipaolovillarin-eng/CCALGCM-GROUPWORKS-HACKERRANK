def solve(e, t):
    return pow(e, t, 10**7)


e, t = list(map(int,input().rstrip().split(" ")))

ans = solve(e, t)
print(ans)