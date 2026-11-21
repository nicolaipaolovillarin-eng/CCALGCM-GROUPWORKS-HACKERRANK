import sys


def solve(n, c, vals):
    vals.sort(key=lambda interval: interval[1])

    last_end = -1
    appearances = 0

    for start, end in vals:
        if start >= last_end:
            appearances += 1
            last_end = end

    return appearances * c


data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
c = data[1]

vals = [
    [data[i], data[i + 1]]
    for i in range(2, 2 + 2 * n, 2)
]

print(solve(n, c, vals))
