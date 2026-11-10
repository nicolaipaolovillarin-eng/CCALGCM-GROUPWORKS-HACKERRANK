n = int(input().rstrip())
s = input().rstrip()
MOD = int(1e9) + 7

prev2, prev1 = 0, 1
for i in range(1, n):
    cur = 0 if s[i] == '1' else (prev1 + prev2) % MOD
    prev2, prev1 = prev1, cur
print(prev1)