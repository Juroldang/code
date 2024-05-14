#Taller 7 - Inversiones
numbers = list(map(int, input().split()))
inv =  0
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j+i+1] < numbers[i]:
            inv += 1
        else: pass
print(inv)