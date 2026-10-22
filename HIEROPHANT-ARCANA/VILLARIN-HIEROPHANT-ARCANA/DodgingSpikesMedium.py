n = int(input().rstrip())
s = input().rstrip()
MOD = int(1e9) + 7

ways = [0] * n
ways[0] = 1

for i in range(1, n):
    if s[i] == "0":
        ways[i] = ways[i - 1]
        
        if i>= 2:
            ways[i] += ways[i - 2]
        
        ways[i] %= MOD
        
print(ways[n - 1])
