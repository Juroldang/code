#K - I_love_username
def main():
    n = int(input())
    contests = list(map(int, input().split()))
    print(amazing_contests(n, contests))
def amazing_contests(n, c):
    amazing = 0
    best_contest = c[0]
    worst_contest = c[0]
    for i in range(1, n):
        if c[i] < worst_contest:
            amazing += 1
            worst_contest = c[i]
        elif c[i] > best_contest:
            amazing += 1
            best_contest = c[i]
    return amazing
main()