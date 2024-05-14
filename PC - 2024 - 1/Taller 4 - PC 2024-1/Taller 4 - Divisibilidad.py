#Taller 4 - Divisibilidad
x = int(input())
y = int(input())
res = 0
if y == 1:
    print("inf")
else:
    while x%y == 0:
        x = x//y
        res += 1
    print(res)