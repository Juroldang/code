#F - Presents
def main():
    n = int(input())
    g = input().split()
    print(presents(n, g))
def presents(n, g):
    ans = ['' for _ in range(n)]
    for i in range(n):
        ans[int(g[i])-1] = str(i+1)
    return ' '.join(ans)
main()