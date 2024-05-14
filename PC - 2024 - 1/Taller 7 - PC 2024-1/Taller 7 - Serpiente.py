#Taller 7 - Serpiente
N = int(input())
matrix = []
num = 0
for i in range(N):
  row = []
  for j in range(N):
    row.append(num)
    num += 1
  if i%2 != 0:
    row.reverse()
  matrix.append(row)
for row in matrix:
  print(" ".join(list(map(str,row))))
