#Taller 4 - Serpiente
N = int(input())
X = int(input())
Y = int(input())
for i in range(N-1):
    print("x"*X)
    for i in range(Y):
        print(" "*(X-1)+"x")
    print("x"*X)
    for i in range(Y):
        print("x")
print("x"*X)
for i in range(Y):
    print(" "*(X-1)+"x")
print("x"*X)
for i in range(Y-1):
    print("x")
print("o")