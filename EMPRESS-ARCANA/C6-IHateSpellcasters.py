import math

def solve(a,T):
    if a == 0:
        return "Pat is the Best Tunnel Master!"

    low = 0
    high = T // a + 2

    while low <= high:
        mid = (low + high) // 2
        headache = a * (math.sin(mid) + mid)

        if headache <= T:
            low = mid + 1
        else:
            high = mid - 1

    return high

a, Q = list(map(int,input().strip().split(" ")))

for i in range(Q):
    T = int(input())
    print("{}".format(solve(a,T)))
