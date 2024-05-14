#Taller 7 - Espiral
def espiral(N):
    matrix = [[0]*N for _ in range(N)]
    direccion = 0
    num = 1
    fi = 0 #Fila Inicio
    ff = N - 1 #Fila Fin
    ci = 0 #Columna Inicio
    cf = N - 1 # Columna Fin
    while fi <= ff and ci <= cf:
        if direccion == 0:
            for i in range(ci, cf + 1):
                matrix[fi][i] = num
                num += 1
            fi += 1
        elif direccion == 1:
            for i in range(fi, ff + 1):
                matrix[i][cf] = num
                num += 1
            cf -= 1
        elif direccion == 2:
            for i in range(cf, ci - 1, -1):
                matrix[ff][i] = num
                num += 1
            ff -= 1
        elif direccion == 3:
            for i in range(ff, fi - 1, -1):
                matrix[i][ci] = num
                num += 1
            ci += 1
        
        direccion = (direccion + 1) % 4
    return matrix

N = int(input())
matrixFinal = espiral(N)
for fila in matrixFinal:
    print(" ".join(map(str, fila)))