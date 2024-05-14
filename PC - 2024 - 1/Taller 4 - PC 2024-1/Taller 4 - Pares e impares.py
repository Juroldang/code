#Taller 4 - Pares e impares
N = int(input())
X = 0
Y = 0
for i in range(N):
    a = int(input())
    if a%2 == 0:
        X += 1
    else:
        Y += 1
print("Hay un total de {} numeros pares".format(X))
print("Hay un total de {} numeros impares".format(Y))