#Taller 4 - Máximo, mínimo y promedio
N = int(input())
sum = 0
numeros = []
for i in range(N):
    num = int(input())
    numeros.append(num)
    sum += num
print(max(numeros))
print(min(numeros))
print(sum//len(numeros))