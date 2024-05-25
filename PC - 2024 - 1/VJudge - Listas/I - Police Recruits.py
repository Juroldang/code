#I - Police Recruits
def main():
    n = int(input())
    events = list(map(int, input().split()))
    print(untreated_crimes(n, events))
def untreated_crimes(n, e):
    polices = 0
    u_crimes = 0
    for i in range(n):
        if e[i] == -1:
            if polices == 0:
                u_crimes += 1
            else: polices -= 1
        else: polices += e[i]
    return u_crimes
main()