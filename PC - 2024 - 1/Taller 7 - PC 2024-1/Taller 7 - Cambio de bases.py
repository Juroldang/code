#Taller 7 - Cambio de bases
base36 = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'a', 11 : 'b', 12 : 'c', 13 : 'd', 14 : 'e', 15 : 'f', 16 : 'g', 17 : 'h', 18 : 'i', 19 : 'j', 20 : 'k', 21 : 'l', 22 : 'm', 23 : 'n', 24 : 'o', 25 : 'p', 26 : 'q', 27 : 'r', 28 : 's', 29 : 't', 30 : 'u', 31 : 'v', 32 : 'w', 33 : 'x', 34 : 'y', 35 : 'z'}
n = int(input())
res = []
if n == 0:
    print(0)
else:
    while n >= 36:
        res.append(base36[n%36])
        n = n//36
    if n != 0:
        res.append(base36[n])
    for i in range(len(res)//2):
        res[i], res [-1-i] = res[-1-i], res[i]
    print("".join(res))