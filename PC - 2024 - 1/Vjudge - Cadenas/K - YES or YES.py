#K - YES or YES
def main():
    N = int(input())
    yes(N)
def yes(N):
    for i in range(N):
        S = input()
        if S.lower() == 'yes': print('YES')
        else: print('NO')
main()