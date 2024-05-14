# Taller 4 - Problema de los huevos
a = int(input())
b = int(input())
c = int(input())
d = int(input())
breaker = 1
while True:
    if (breaker%2==a) and (breaker%3==b) and (breaker%5==c) and (breaker%7==d):
        break
    else:
        breaker+=1
print(breaker)