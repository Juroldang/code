#S - Ten Words of Wisdom
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(winner(n))
def winner(n):
    winner = 0
    points = 0
    for i in range(1,n+1):
        temp = list(map(int, input().split()))
        if temp[0] <= 10 and temp[1] > points: 
            points = temp[1]
            winner = i
    return winner
main()