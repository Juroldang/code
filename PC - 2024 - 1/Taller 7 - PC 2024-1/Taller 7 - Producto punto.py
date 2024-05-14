#Taller 7 - Producto punto
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
if len(v1) != len(v2): print('Error')
else:
    res = 0
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    print(res)