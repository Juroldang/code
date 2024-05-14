#G - Divisibility Problem
n = int(input())
for i in range(n):
    numbers = list(map(int, input().split()))
    a, b = numbers[0], numbers[1]
    count = 0
    if a%b == 0:
        print(0)
    elif a//b == 0:
        print(b-a)
    else:
        fact = (a//b)+1
        print((b*fact)-a)