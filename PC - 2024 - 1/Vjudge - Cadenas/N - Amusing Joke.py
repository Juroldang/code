#N - Amusing Joke
def main():
    G = input()
    H = input()
    S = input()
    amusing_joke(G,H,S)
def amusing_joke(G,H,S):
    actual_cards = {}
    shuffled_cards = {}
    S2 = G+H
    for letter in S2:
        if letter not in actual_cards: actual_cards[letter] = 1
        else: actual_cards[letter] += 1
    for letter in S:
        if letter not in shuffled_cards: shuffled_cards[letter] = 1
        else: shuffled_cards[letter] += 1
    if actual_cards == shuffled_cards: print('YES')
    else: print('NO')
main()