# Taller 4 - Diamante
n = int(input())
esp = n-1
ast = 1
for i in range((2*n)-1):
    print(" "*esp+"*"*ast+" "*esp)
    if (i+1) < n:
        esp -= 1
        ast += 2
    else:
        esp += 1
        ast -= 2