#H - George and Accommodation
n = int(input())
disp = 0
for i in range(n):
    pyq = list(map(int,input().split()))
    p, q = pyq[0], pyq[1]
    if (q - p) >= 2:
        disp += 1
print(disp)