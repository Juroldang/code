#Taller 4 - Último dígito
x = input()
y = input()
i = len(x)
res = 0
while i != 0:
    if x[i-1] == y:
        print(res)
        break
    else:
        res+=1
        i-=1
else:
    print("Imposible")