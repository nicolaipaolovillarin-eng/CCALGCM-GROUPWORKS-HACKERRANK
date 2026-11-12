def solve(n,k,cards):
    deck = sorted(cards, key=lambda c: (c[0] == "red", int(c[1])), reverse=True)[:k]
    r = 0
    tp = 0
    for color, power in deck:
        if color == "red":
            r += 1
        tp += int(power)
    return r, tp