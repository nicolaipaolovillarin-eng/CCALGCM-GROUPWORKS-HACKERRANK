import sys


def solve(p, n, towns):
    low = 1
    high = max(towns)

    while low < high:
        mid = (low + high) // 2

        required = sum((people + mid - 1) // mid for people in towns)

        if required <= p:
            high = mid
        else:
            low = mid + 1

    return low


data = list(map(int, sys.stdin.buffer.read().split()))

p = data[0]
n = data[1]
towns = data[2:2 + n]

print(solve(p, n, towns))
