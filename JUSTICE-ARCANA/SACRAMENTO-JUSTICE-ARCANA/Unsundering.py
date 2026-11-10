"""
Solves a test case.

Parameters:
n : int - number of cards available
k : int - number of cards to include in Jason's deck
cards : array-like - string list of shape (n,2). Each element has two elements: 
the first is a string containing the color (either "red" or "blue"). The second 
is a string containing the power of the card.

Returns:
r  : int - number of red cards added
tp : int - total power of cards in your deck
"""
def solve(n,k,cards):
    red = 0
    power = 0
    cards = sorted([(color, int(value)) for color, value in cards])[::-1]
    
    for x in range(k):
        if cards[x][0] == 'red':
            red += 1
        power += cards[x][1]
    return red, power

n,k = list(map(int,input().strip().split(' ')))
cards = [list(input().strip().split(' ')) for i in range(n)]

red, tp = solve(n,k,cards)

print(f"{red} {tp}")