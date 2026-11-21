import sys


def solve(L, n, coverage):
    coverage.sort()

    position = 1
    used = 0
    i = 0

    while position <= L:
        farthest = position - 1

        while i < n and coverage[i][0] <= position:
            farthest = max(farthest, coverage[i][1])
            i += 1

        if farthest < position:
            return "'Salem's Lot is doomed."

        position = farthest + 1
        used += 1

    return n - used


data = list(map(int, sys.stdin.buffer.read().split()))

L, n = data[0], data[1]
coverage = [
    [data[i], data[i + 1]]
    for i in range(2, 2 + 2 * n, 2)
]

print(solve(L, n, coverage))
