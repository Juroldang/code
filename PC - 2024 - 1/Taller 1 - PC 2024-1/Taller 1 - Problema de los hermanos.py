#Taller 1 - Problema de los hermanos
T = int(input())
P = int(input())
segundo = int(((2*T)/9)-P)
primero = int(segundo + 2*P)
cuarto = int(((T-primero-segundo)*4)/5)
tercero = int(cuarto/4)
print(f"{primero} {segundo} {tercero} {cuarto}")