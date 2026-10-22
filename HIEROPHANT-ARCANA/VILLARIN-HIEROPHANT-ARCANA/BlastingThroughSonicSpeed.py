def solve(n, a, b, c, k, slippery):
    slippery = set(slippery)
    energy = 0
    total_time = 0

    for square in range(1, n):
        if b < a and energy > 0 and square not in slippery:
            total_time += b
            energy -= 1
        else:
            total_time += a
            energy += 1

    return total_time


n, a, b, c, k = list(map(int, input().rstrip().split(" ")))

slippery = []
if k > 0:
    slippery = list(map(int, input().rstrip().split(" ")))

print(solve(n, a, b, c, k, slippery))
