#V - Sasha and Array Coloring
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        print(max_color(n, s))
def max_color(n, s):
    steps = n//2
    s = sorted(s)
    cost = 0
    for i in range(steps):
        cost += abs(s[i]-s[-i-1])
    return cost
main()