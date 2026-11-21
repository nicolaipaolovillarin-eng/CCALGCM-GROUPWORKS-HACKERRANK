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

import bisect

def solve(n,t,duties):
    # TODO
    timeLimitInSeconds = t * 60
    answer = 0
    sumArray = sorted(duties[x][1] + duties[x][2] for x in range(n))
    
    for x in sumArray:
        timeLimitInSeconds -= x
        if timeLimitInSeconds < 0:
            break
        answer += 1
        
    if answer != 0:
        return answer
    else:
        return "I need to find friends."

n, t = list(map(int,input().split(" ")))
duties = []

for i in range(n):
    name = input()
    w,c = list(map(int,input().split(" ")))
    duties.append([name,w,c])


print(solve(n,t,duties))
