#Taller 2 - Tres números y divisibilidad
a = int(input())
b = int(input())
c = int(input())
comprobador = 0
if ((b*c)%a==0):
    print('El número {} es divisor de {}'.format(a,(b*c)))
    comprobador += 1
if ((a*c)%b==0):
    print('El número {} es divisor de {}'.format(b,(a*c)))
    comprobador += 1
if ((a*b)%c==0):
    print('El número {} es divisor de {}'.format(c,(b*a)))
    comprobador += 1
if comprobador == 0:
    print('Ninguna de las tres condiciones se cumple')