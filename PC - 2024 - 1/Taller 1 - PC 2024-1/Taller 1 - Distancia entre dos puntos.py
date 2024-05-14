#Taller 1 - Distancia entre dos puntos
X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
distancia = format((((X2-X1)**2)+((Y2-Y1)**2))**0.5, '.5f')
print(f"La distancia entre ({X1}, {Y1}) y ({X2}, {Y2}) es {distancia}")