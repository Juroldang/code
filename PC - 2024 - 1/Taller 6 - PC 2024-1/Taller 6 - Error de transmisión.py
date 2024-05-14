# Taller 6 - Error de transmisión
trans = input()
recib = input()
errores = 0
for i in range(len(trans)):
    if trans[i] != recib[i]:
        errores += 1
print(errores)