"""
This function solves a test case.

Parameters:
n      : int        - number of duties available
t      : int        - time to do duties in minutes
duties : array-like - a 3-tuple of string values in the format (name, wait time,
                      completion time)

Returns:
A string containing the answer or "I need to find friends."             
"""
def solve(n,t,duties):
    left = t * 60
    count = 0
    for cost in sorted(w + c for _, w, c in duties):
        if cost > left:
            break
        left -= cost
        count += 1
    return str(count) if count else "I need to find friends."

n, t = list(map(int,input().split(" ")))
duties = []

for i in range(n):
    name = input()
    w,c = list(map(int,input().split(" ")))
    duties.append([name,w,c])


print(solve(n,t,duties))