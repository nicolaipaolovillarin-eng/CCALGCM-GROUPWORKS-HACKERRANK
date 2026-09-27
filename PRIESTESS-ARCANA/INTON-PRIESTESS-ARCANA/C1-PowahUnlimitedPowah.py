def solve(e,t):
  # solve for answer
    return pow(e, t, 10 ** 7)

e, t = list(map(int,input().rstrip().split(" ")))
print(solve(e, t))