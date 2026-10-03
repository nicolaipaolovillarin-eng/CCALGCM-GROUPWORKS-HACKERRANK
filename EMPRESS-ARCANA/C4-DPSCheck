import sys
from bisect import bisect_right


def solve(k, h, knights, hillichurls):
    hillichurls.sort()

    ranking = []

    for name, stats in knights:
        atk = stats[0]
        best_scaling = max(stats[1:])

        # Scaling is a percentage, and damage is rounded down.
        damage = atk * best_scaling // 100

        defeated = bisect_right(hillichurls, damage)

        # Negative count gives descending order.
        ranking.append((-defeated, name))

    ranking.sort()

    for negative_count, name in ranking:
        print(name, -negative_count)


def main():
    read = sys.stdin.buffer.readline

    k, h = map(int, read().split())

    knights = []

    for _ in range(k):
        name = read().decode().strip()
        stats = list(map(int, read().split()))
        knights.append((name, stats))

    hillichurls = [
        int(read())
        for _ in range(h)
    ]

    solve(k, h, knights, hillichurls)


if __name__ == "__main__":
    main()
