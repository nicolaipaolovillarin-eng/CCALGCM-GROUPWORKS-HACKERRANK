"""
This function solves a test case.

Parameters:
l            : int        - # of length cutting points of quatrum cluster
w            : int        - # of width cutting points of quatrum cluster
d            : int        - # of depth cutting points of quatrum cluster
length_costs : array-like - list of length cutting point instability factors
width_costs  : array-like - list of width cutting point instability factors
depth_costs  : array-like - list of depth cutting point instability factors

Returns:
An integer indicating the smallest attainable instability after cutting the 
cluster down to 1 x 1 x 1 cubes
"""
def solve(l,w,d,length_costs,width_costs,depth_costs):
    MOD = int(1e9 + 7)
    cuts = sorted([(c, 0) for c in length_costs] + [(c, 1) for c in width_costs] + [(c, 2) for c in depth_costs], reverse=True)
    pieces = [1, 1, 1]
    total = 0
    for c, i in cuts:
        total = (total + c * pieces[0] * pieces[1] * pieces[2] // pieces[i]) % MOD
        pieces[i] += 1
    return total

l,w,d = list(map(int,input().split(" ")))
length_costs = [int(input()) for i in range(l)]
width_costs = [int(input()) for i in range(w)]
depth_costs = [int(input()) for i in range(d)]

print(solve(l,w,d,length_costs,width_costs,depth_costs))