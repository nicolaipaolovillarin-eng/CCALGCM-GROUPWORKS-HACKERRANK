"""
Solves a test case

Parameters:
n    : int        - number of station levels
k    : int        - cost to transfer to the other line
vals : array-like - array of shape (n,2) containing the finishing times for each
                    station at each assembly line
"""
def solve(n, k, vals):
    line1 = vals[0][0]
    line2 = vals[0][1]

    for i in range(1, n):
        new_line1 = min(line1, line2 + k) + vals[i][0]
        new_line2 = min(line2, line1 + k) + vals[i][1]

        line1 = new_line1
        line2 = new_line2

    return min(line1, line2)


n, k = map(int, input().split())
vals = []

for i in range(n):
    vals.append(list(map(int, input().split())))

print(solve(n, k, vals))
