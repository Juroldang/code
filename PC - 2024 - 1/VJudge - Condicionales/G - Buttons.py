#G - Buttons
n = int(input())
if n <= 3:
    print(1+(n-1)*n)
else:
    x=1+(n*2)
    f= n-3
    sumando = n
    for i in range(n-3):
        sumando = sumando + f
        x = x + sumando
        f=f-2
    print(x)