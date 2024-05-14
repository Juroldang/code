#Taller 7 - Contar en la lista
numbers = input().split()
dicNumbers = {}
for i in numbers:
    if i not in dicNumbers.keys():
        dicNumbers[i] = 1
    else: dicNumbers[i] = dicNumbers[i]+1
for i in range(int(input())):
    n = input()
    try: 
        print(dicNumbers[n])
    except: print('No existe')