def solve(cards):
    # TODO: Compute and return answer here
    steps = cards[0]
    while cards[0] >= 0:
        for x in range (1,10):
            if cards[x] > 0:
                steps += 1
                cards[x] -= 1
        cards[0] -= 1
    return steps

cards = list(map(int,input().strip().split(" ")))
print("{}".format(solve(cards)))
