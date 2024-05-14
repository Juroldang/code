#M - Codeforces Checking
def main():
    N = int(input())
    checkcode(N)
def checkcode(N):
    codeforces = {'f', 'r', 's', 'o', 'd', 'e', 'c'}
    for i in range(N):
        c = input()
        if c in codeforces:
            print('YES')
        else: print('NO')
main()