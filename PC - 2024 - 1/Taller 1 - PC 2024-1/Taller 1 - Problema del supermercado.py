#Taller 1 - Problema del supermercado
A = int(input())
B = int(input())
C = int(input())
Tomate = int((A+C-B)/2)
Cebolla = A - Tomate
Apio = C - Tomate
print(f"{Cebolla} {Tomate} {Apio}")