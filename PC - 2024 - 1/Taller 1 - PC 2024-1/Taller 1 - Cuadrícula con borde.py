#Taller 1 - Cuadrícula con borde
altura = int(input())
ancho = int(input())
cuadricula = "*"*(ancho+2)
estructura = "*"+("+"*ancho)+"*"
print(cuadricula)
for i in range(altura):
    print(estructura, end='\n')
print(cuadricula)