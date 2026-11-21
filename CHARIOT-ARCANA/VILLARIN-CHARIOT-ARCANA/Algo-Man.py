import sys

MOD = 1000000007


def solve(l, w, d, length_costs, width_costs, depth_costs):
    cuts = []

    for cost in length_costs:
        cuts.append((cost, 0))

    for cost in width_costs:
        cuts.append((cost, 1))

    for cost in depth_costs:
        cuts.append((cost, 2))

    cuts.sort(key=lambda item: item[0], reverse=True)

    length_done = 0
    width_done = 0
    depth_done = 0
    answer = 0

    for cost, direction in cuts:
        if direction == 0:
            sections = (width_done + 1) * (depth_done + 1)
            length_done += 1
        elif direction == 1:
            sections = (length_done + 1) * (depth_done + 1)
            width_done += 1
        else:
            sections = (length_done + 1) * (width_done + 1)
            depth_done += 1

        answer = (answer + cost * sections) % MOD

    return answer


data = list(map(int, sys.stdin.buffer.read().split()))

l, w, d = data[0:3]
pos = 3

length_costs = data[pos:pos + l]
pos += l

width_costs = data[pos:pos + w]
pos += w

depth_costs = data[pos:pos + d]

print(solve(l, w, d, length_costs, width_costs, depth_costs))
