#B - Soldier and Bananas
knw = list(map(int,input().split()))
k, n, w = knw[0], knw[1], knw[2]
for i in range(w):
    n -=  k*(i+1)
if n > 0:
    print(0)
else:
    print(abs(n))