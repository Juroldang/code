#Taller 1 - Problema de la máquina expendedora
I = int(input())
C = int(input())
D = I - C
m10 = D//10
D = D - m10*10
m5= 0
m1 = 0
if D > 0:
    m5 = D//5
    D = D - m5*5
m1 = D
print(f"{m1} {m5} {m10}")