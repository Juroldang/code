#G - Drinks
def main():
    n = int(input())
    d = list(map(int, input().split()))
    print(drinks(n, d))
def drinks(n, d):
    s = sum(d)
    return round(s/n,10)
main()