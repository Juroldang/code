#L - Choosing Teams
def main():
    inp = input().split()
    n, k = int(inp[0]), int(inp[1])
    c = list(map(int, input().split()))
    print(teams(n, k, c))
def teams(n, k, c):
    c = sorted(c)
    limit = n-(n%3)
    t = 0
    for i in range(0, limit, 3):
        if max(c[i:i+3])+k > 5:
            break
        else: t += 1  
    return t
main()