#Taller 7 - Espiral
def main():
    N = int(input())
    matrix = [[-1 for i in range(N)] for i in range(N)]
    print(matrix)
    matrix = espiral(matrix, 'Right', 1, 0, 0)
    for row in matrix:
        print(" ".join(list(map(str,row))))
def espiral(matrix, direct, num, ix, iy):
    print(matrix)
    print(len(matrix))
    print(ix, iy)
    if direct == 'Right':
        matrix[iy][ix] = num
        num += 1
        if ix+1 >= len(matrix):
            return espiral(matrix, 'Down', num, ix, (iy+1) )
        elif matrix[iy][ix+1] != -1:
            if matrix[iy+1][ix] != -1:
                return matrix
            else: return espiral(matrix, 'Down', num, ix, (iy+1) )
        else: return espiral(matrix, 'Right', num, (ix+1), iy )
    elif direct == 'Down':
        matrix[iy][ix] = num
        num += 1
        if iy+1 >= len(matrix):
            return espiral(matrix, 'Left', num, (ix-1), iy )
        elif matrix[iy+1][ix] != -1:
            if matrix[iy][ix-1] != -1:
                return matrix
            else: return espiral(matrix, 'Left', num, (ix-1), iy )
        else: return espiral(matrix, 'Down', num, ix, (iy+1) )
    elif direct == 'Left':
        matrix[iy][ix] = num
        num += 1
        if ix-1 < 0:
            return espiral(matrix, 'Up', num, ix, (iy-1) )
        elif matrix[iy][ix-1] != -1:
            if matrix[iy-1][ix] != -1:
                return matrix
            else: return espiral(matrix, 'Up', num, ix, (iy-1) )
        else: return espiral(matrix, 'Left', num, (ix-1), iy )
    elif direct == 'Up':
        matrix[iy][ix] = num
        num += 1
        if matrix[iy-1][ix] != -1:
            if matrix[iy][ix+1] != -1:
                return matrix
            else: return espiral(matrix, 'Right', num, (ix+1), iy )
        else: return espiral(matrix, 'Up', num, ix, (iy-1) )
main()