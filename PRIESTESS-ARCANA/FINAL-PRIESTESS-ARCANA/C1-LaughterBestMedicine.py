def solve(n, k):
    if n == 0:
        return "H"
    if n == 1:
        return "A"

    length = [1, 1]

    for i in range(2, n + 1):
        length.append(min(10**18 + 1, length[i - 2] + length[i - 1]))

    while n > 1:
        if k < length[n - 2]:
            n -= 2
        else:
            k -= length[n - 2]
            n -= 1

    return "H" if n == 0 else "A"


n, k = list(map(int,input().rstrip().split(" ")))
print(solve(n,k))
