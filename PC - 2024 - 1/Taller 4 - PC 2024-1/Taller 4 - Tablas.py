#Taller 4 - Tablas
op = input()
n = int(input())
m = int(input())
if op == "+":
    for i in range(n+1):
        for j in range(m+1):
            if j == 0 and i == 0:
                print("",end="\t")
            elif j == 0:
                print("{}".format(i), end="\t")
            elif j == m:
                print("{}".format(j+i))
            else:
                print("{}".format(j+i),end="\t")
elif op == "*":
    for i in range(n+1):
        for j in range(m+1):
            if j == 0 and i == 0:
                print("",end="\t")
            if i == 0:
                i = 1
            elif j == 0:
                print("{}".format(i), end="\t")
            elif j == m:
                print("{}".format(j*i))
            else:
                print("{}".format(j*i),end="\t")
elif op == "^":
    for i in range(n+1):
        for j in range(m+1):
            if j == 0 and i == 0:
                print("", end="\t")
            elif i == 0 and j==m:
                print("{}".format(j))
            elif i == 0:
                print("{}".format(j), end="\t")
            elif i == 0:
                i = 1
            elif j == 0:
                print("{}".format(i), end="\t")
            elif j == m:
                print("{}".format(i**j))
            else:
                print("{}".format(i**j),end="\t")