n = int(input())

movies = []

for i in range(n):
    r, c = list(map(int, input().rstrip().split(" ")))
    movies.append([r, c])

q = int(input())

for cc in range(q):
    s, e, a, k = list(map(int, input().rstrip().split(" ")))

    count = a // k

    arr = sorted(movies[s:e+1], key=lambda x: x[0] - x[1], reverse=True)

    if count == 0:
        print(-1)
    else:
        if count > len(arr):
            count = len(arr)

        r, c = arr[count - 1]
        print(r - c)
