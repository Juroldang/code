#Taller 4 - Descomposición en factores primos
n = int(input())
p = 2
while n != 1:
    DIV = 2
    while DIV < p:
        if (p%DIV == 0) and (p != 2):
            p+=1
            break
        else:
            DIV += 1
    else:
        while True:
            if n%p == 0:
                print("{}\t|\t{}".format(n,p))
                n = n//p
            else:
                p+=1
                break
print(1)