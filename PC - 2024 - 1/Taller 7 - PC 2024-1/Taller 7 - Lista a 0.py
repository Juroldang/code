#Taller 7 - Lista a 0
numbers = list(map(int, input().split()))
res = numbers[0]
possible = False
for i in range(len(numbers)-1):
    if (numbers[i+1] - res) < 0:
        break
    else:
        res = numbers[i+1] - res
if res == 0: possible = True
if possible: print('SI')
else: print('NO')