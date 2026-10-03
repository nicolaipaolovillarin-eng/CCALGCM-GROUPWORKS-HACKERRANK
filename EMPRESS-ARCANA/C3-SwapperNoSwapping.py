import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))

    n = data[0]
    survivable_blasts = data[1]
    books = data[2:2 + n]

    # Coordinate compression
    ordered = sorted(books)
    rank = {value: i + 1 for i, value in enumerate(ordered)}

    bit = [0] * (n + 1)

    def add(index):
        while index <= n:
            bit[index] += 1
            index += index & -index

    def prefix_sum(index):
        total = 0
        while index:
            total += bit[index]
            index -= index & -index
        return total

    ascending_swaps = 0

    for i, book in enumerate(books):
        position = rank[book]

        numbers_not_greater = prefix_sum(position)
        ascending_swaps += i - numbers_not_greater

        add(position)

    total_pairs = n * (n - 1) // 2
    descending_swaps = total_pairs - ascending_swaps
    minimum_swaps = min(ascending_swaps, descending_swaps)

    if minimum_swaps == 0:
        print("Butz loses!")
    else:
        # He must receive more blasts than he can survive.
        print(survivable_blasts // minimum_swaps + 1)


if __name__ == "__main__":
    main()
