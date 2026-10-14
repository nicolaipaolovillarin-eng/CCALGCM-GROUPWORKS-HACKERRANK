ways = []


def solve(d, denoms, v):
    return ways[v]


d, q = list(map(int, input().rstrip().split(" ")))
denoms = sorted(list(map(int, input().rstrip().split(" "))))

# Read queries first so we know the largest value to preprocess
ans_list = []

for i in range(q):
    v = int(input().rstrip())
    ans_list.append(v)

# preprocess here
max_value = max(ans_list, default=0)

ways = [0] * (max_value + 1)
ways[0] = 1

for coin in denoms:
    if coin <= 0 or coin > max_value:
        continue

    for amount in range(coin, max_value + 1):
        ways[amount] += ways[amount - coin]

# build answer to avoid TLE
for i in range(q):
    v = ans_list[i]
    ans_list[i] = solve(d, denoms, v)

print("{}".format("\n".join(list(map(str, ans_list)))))
