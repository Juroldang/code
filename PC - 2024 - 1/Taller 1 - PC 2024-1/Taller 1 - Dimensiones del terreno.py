#Taller 1 - Dimensiones del terreno
A = int(input())
P = int(input())
L1 = int(((-A+((P**2)/16))**0.5)+(P/4))
L2 = int((P/2)-L1)
if L1 <= L2:
    largo = L1
    ancho = L2
else:
    largo = L2
    ancho = L1
print(largo)
print(ancho)