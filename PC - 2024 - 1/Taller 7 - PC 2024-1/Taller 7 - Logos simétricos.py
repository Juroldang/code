T = int(input())
for t in range(T):
    N = int(input())
    matrix = []
    for n in range(N):
        matrix.append(list(input()))
    sim = True
    mid = 0
    if N%2 != 0:
        mid = (N//2)+1
    else: mid = N//2
    for i in range(mid):
        if matrix[i] != matrix[-1-i]:
            sim = False
            break
        for j in range(mid):
            if matrix[i][j] != matrix[i][-1-j]:
                sim = False
                break
        if not sim: break
    if sim: print('YES')
    else: print('NO')
