#W - Replacing Elements
def main():
    t = int(input())
    for _ in range(t):
        inp = input().split()
        d = int(inp[1])
        s = list(map(int, input().split()))
        print(replacing(d, s))
def replacing(d, s):
    s = sorted(s)
    if (s[len(s)-1] <= d) or (s[0]+s[1]<=d): return 'YES'
    else: return 'NO'
main()