#Taller 1 - 1+2+3+...+N
N = int(input())
sum = 0
for i in range(N):
    sum = sum + (i+1)
print(sum)