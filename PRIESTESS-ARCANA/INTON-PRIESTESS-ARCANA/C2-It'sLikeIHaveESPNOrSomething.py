n, kx, ky = list(map(int,input().rstrip().split(" ")))
people = [list(map(int,input().rstrip().split(" "))) for i in range(n)]
q = int(input().rstrip())

arrayOfDistances = []
index = 0
while index < n:
    distance = abs((kx - people[index][0])) + abs((ky - people[index][1]))
    arrayOfDistances.append(distance)
    index += 1
arrayOfDistances.sort()
    
for cc in range(q):
    e = int(input())
    # solve for ans
    low = 0; high = n-1; ans = 0
    while (low <= high):
        mid = (low + high)//2
        if e >= arrayOfDistances[mid]:
            low = mid + 1; ans = low
        elif e < arrayOfDistances[mid]:
            high = mid - 1
            
    print(ans)