n = int(input().rstrip())
s = input().rstrip()

position = 0
jumps = 0

while position < n - 1:
    if position + 2 < n and s[position + 2] == "0":
        position += 2
    elif position + 1 < n and s[position + 1] == "0":
        position += 1
    else:
        print(-1)
        break
        
    jumps += 1
else:
    print(jumps)
