#Taller 7 - Mayor que la derecha
numbers = list(map(int, input().split()))
max_val = max(numbers)
max_index = numbers.index(max_val)
for i in range(len(numbers)-1):
    if i > max_index:
        max_val = max(numbers[i:])
        max_index = numbers[i:].index(max_val) + i
    if numbers[i] >= max_val:
        print(numbers[i], end=" ")
print(numbers[-1], "")