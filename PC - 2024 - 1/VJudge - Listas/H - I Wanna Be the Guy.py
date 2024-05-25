#H - I Wanna Be the Guy
def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(can_complete(n,x,y))
def can_complete(n, x, y):
    game = ['NO' for _ in range(n)]
    if x[0] == n or y[0] == n:
        return 'I become the guy.'
    for i in range(1, len(x)):
        game[x[i]-1] = 'YES'
    for i in range(1, len(y)):
        game[y[i]-1] = 'YES'
    if 'NO' in game: return 'Oh, my keyboard!'
    else: return 'I become the guy.'
main()