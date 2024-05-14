#G - Anton and Danik
def main():
    N = int(input())
    S = input()
    print(winner(S))
def winner(S):
    A = 0
    D = 0
    for winner in S:
        if winner == "A": A += 1
        else: D += 1
    if A > D: return 'Anton'
    elif D > A: return 'Danik'
    else: return 'Friendship'
main()