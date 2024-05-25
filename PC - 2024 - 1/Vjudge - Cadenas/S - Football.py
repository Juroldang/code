#S - Football
def main():
    S = input()
    print(danger(S))
def danger(S):
    prev_player = ''
    players = 0
    for player in S:
        if prev_player == player:
            players += 1
        else : players = 1
        prev_player = player
        if players > 6:
            return 'YES'
    return 'NO'
main()