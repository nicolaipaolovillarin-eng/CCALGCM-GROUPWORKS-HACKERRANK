"""
This function solves a test case.

Parameters:
k : int - number of transmission frequencies
n : int - number of participants
fs : array-like - sorted transmission frequencies
ms : array-like - participant frequencies

Returns a list of answers.
"""

from bisect import bisect_right


def solve(k, n, fs, ms):
    return [
        bisect_right(fs, participant)
        for participant in ms
    ]


def main():
    k, n = map(int, input().split())

    fs = sorted(
        int(input())
        for _ in range(k)
    )

    ms = [
        int(input())
        for _ in range(n)
    ]

    answers = solve(k, n, fs, ms)

    print("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
