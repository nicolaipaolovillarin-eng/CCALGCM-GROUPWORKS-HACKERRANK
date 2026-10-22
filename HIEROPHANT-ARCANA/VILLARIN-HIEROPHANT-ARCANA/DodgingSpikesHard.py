MOD = 1000000007
n,k = list(map(int,input().rstrip().split(" ")))
s = input().rstrip()
jumps = []
for i in range(k):
	jumps.append(int(input().rstrip()))

INF = float("inf")

min_jumps = [INF] * n

ways = [0] * n

min_jumps[0] = 0
ways[0] = 1

for current in range(1, n):
    if s[current] == "1":
        continue
    
    for jump in jumps:
        previous = current - jump
        
        if previous < 0:
            continue
            
        ways[current] = (ways[current] + ways[previous]) % MOD
        
        if min_jumps[previous] != INF:
            candidate = min_jumps[previous] + 1
            
            if candidate < min_jumps[current]:
                min_jumps[current] = candidate

if min_jumps[n - 1] == INF:
    print(-1, ways[n - 1])
else:
    print(min_jumps[n - 1], ways[n - 1])        
        
        
        
