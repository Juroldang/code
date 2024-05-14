#H - Plus or Minus
n = int(input())
for i in range(n):
    a, b, c = input().split()
    if(int(a)+int(b))==int(c):
        print('+')
    else:
        print('-')