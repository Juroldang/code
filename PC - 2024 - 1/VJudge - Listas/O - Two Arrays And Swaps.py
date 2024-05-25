#O - Two Arrays And Swaps
def main():
    t = int(input())
    for _ in range(t):
        inp = input().split()
        n, k = int(inp[0]), int(inp[1])
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(max_sum(n, k, a, b))
def max_sum(n, k, a, b):
    total = sum(a)
    for _ in range(k):
        a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
        temp = sum(a)
        if temp > total:
            total = temp
        else: return total
    return total
main()