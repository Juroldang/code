# Taller 4 - Primos entre A y B
A = int(input())
B = int(input())
imposible = True
if A == 1:
    A = 2
while A <= B:
    DIV = 2
    while DIV < A:
        if (A%DIV == 0) and (A != 2):
            A+=1
            break
        else:
            DIV += 1
    else:
        imposible = False
        print(A)
        A += 1
if imposible:
    print("No hay primos en este intervalo.")