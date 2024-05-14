#Taller 2 - Dos alfiles
fila1 = int(input())
columna1 = int(input())
fila2 = int(input())
columna2= int(input())
if (abs(fila1-fila2)==abs(columna1-columna2)):
    print('Se están atacando')
else:
    print('No se están atacando')