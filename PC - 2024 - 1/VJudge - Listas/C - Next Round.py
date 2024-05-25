#C - Next Round
def main():
    inp = input().split()
    n, k = int(inp[0]), int(inp[1])
    c = list(map(int, input().split()))
    print(next_round(n, k ,c))
def next_round(n, k, c):
    last_c = -1
    c_pass = 0
    for i in range(n):
        if c[i]>0:
            c_pass += 1
            k -= 1
        if k == 0 and i < len(c)-1:
            last_c = c[i]
            for j in range(i+1, len(c)):
                if last_c == c[j]:
                    c_pass += 1
                else: break
        if c[i] == 0 or k == 0: break
    return c_pass
main()