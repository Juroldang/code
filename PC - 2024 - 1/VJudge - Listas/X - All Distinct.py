#X - All Distinct
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        print(array_distinct(n, s))
def array_distinct(n, s):
    temp = len(set(s))
    if n == temp: return n
    elif n%2 != 0 and temp%2 != 0: return temp
    elif n%2 != 0 or temp%2 != 0: return temp-1
    else: return temp
main()