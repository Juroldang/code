#R - Increasing
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        print(isincreasing(n, s))
def isincreasing(n, s):
    compare = set(s)
    if len(compare) != len(s):return 'NO'
    else: return 'YES'
main()