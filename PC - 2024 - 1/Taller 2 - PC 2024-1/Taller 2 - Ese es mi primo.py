#Taller 2 - Ese es mi primo
n = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())
primos = [p1,p2,p3]
comprobador = 0
for i in range(3):
    if n%primos[i] != 0:
        print('Nunca he visto a este número')
        break
    n = n/primos[i]
    comprobador += 1
if comprobador == 3:
    print('Es uno de mis compuestos')