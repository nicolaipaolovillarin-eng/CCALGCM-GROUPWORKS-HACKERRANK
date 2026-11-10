"""
State: 
k - number of vampires to stake left
t - total vampire evil

Transition:
stake or not stake
Greedy:
lowest power first
"""
n, f, k = list(map(int,input().rstrip().split(" ")))
vamps = [int(input()) for x in range(n)]
ans = ""
# solve answer here
vamps = sorted(vamps)
total = 0
for i in range(k):
    total += vamps[i]

if total > f:
    ans = "NO"
else:
    ans = "YES"

print(ans)
