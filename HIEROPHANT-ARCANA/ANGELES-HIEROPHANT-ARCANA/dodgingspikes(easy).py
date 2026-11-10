n = int(input().rstrip())
s = input().rstrip()

if "11" in s:
    print(-1)
else:
    pos = 0
    jumps = 0
    while pos < n - 1:
        if pos + 2 < n and s[pos + 2] == '0':
            pos += 2
        else:
            pos += 1
        jumps += 1
    print(jumps)