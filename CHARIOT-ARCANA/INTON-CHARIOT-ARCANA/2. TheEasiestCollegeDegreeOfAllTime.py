"""
Solve a single test case.

Parameters:
n : int - number of courses to consider
k : int - maximum number of courses that can be taken in one term
vals : array-like - list of difficulty ratings of each of the n courses

Returns:
An integer indicating the smallest total difficulty rating across all terms.
"""

def solve(n,k,vals):
    # TODO

    return sum(x for x in sorted(vals)[n::-k])

n,k = list(map(int,input().strip().split(" ")))
vals = sorted([int(input()) for i in range(n)])

print(f"{solve(n,k,vals)}\n")