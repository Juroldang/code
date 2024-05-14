#Taller 4 - Amigos
a = int(input())
b = int(input())
c = int(input())
def mcd(a, b):
    while b != 0:
        a, b = b, (a % b)
    return a
mcm1=(a*b/mcd(a,b))
mcmf=(mcm1*c/mcd(mcm1,c))
print(int(mcmf))