from bisect import bisect_right

n, kx, ky = list(map(int,input().rstrip().split(" ")))
people = [list(map(int,input().rstrip().split(" "))) for i in range(n)]

dist = []

for x, y in people:
    dist.append(abs(kx - x) + abs(ky - y))

dist.sort()

q = int(input().rstrip())

for cc in range(q):
    e = int(input())
    
    ans = bisect_right(dist, e)
    
    print(ans)
