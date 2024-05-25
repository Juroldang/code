#P - Honest Coach
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        print(min_difference(n, s))
def min_difference(n, s):
    s = sorted(s)
    dif = 1001
    for i in range(n-1):
        temp = abs(s[i]-s[i+1])
        if temp == 0: return 0
        if temp < dif : dif = temp
    return dif
main()