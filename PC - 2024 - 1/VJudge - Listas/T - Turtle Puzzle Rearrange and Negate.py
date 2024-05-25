#T - Turtle Puzzle Rearrange and Negate
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().split()
        ans = sum(list(map(operator, s)))
        print(ans)
def operator(x):
    temp = int(x)
    return abs(temp)
main()