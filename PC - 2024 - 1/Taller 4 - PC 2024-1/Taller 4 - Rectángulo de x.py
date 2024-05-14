#Taller 4 - Rectángulo de x
X = int(input())
Y = int(input())
if Y == 1:
    print("x"*X)
else:
    print("x"*X)
    Y -= 1
    while Y != 1:
        if X == 1:
            print("x")
    else:
        print("x"+"o"*(X-2)+"x")
    Y -= 1
    print("x"*X)