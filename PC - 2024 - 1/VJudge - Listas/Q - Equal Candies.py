#Q - Equal Candies
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        print(candies_to_eat(n, s))
def candies_to_eat(n, s):
    s = sorted(s)
    candies = 0
    smallest_box = s[0]
    for i in range(1 ,n):
        candies += (s[i]-smallest_box)
    return candies
main()