#I - Hulk
n = int(input())
for i in range(n):
    if (i+1) != n:
        if (i+1)%2 != 0:
            print("I hate that",end=" ")
        else:
            print("I love that",end=" ")
    else:
        if (i+1)%2 != 0:
            print("I hate it")
        else:
            print("I love it")