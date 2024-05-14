#D - Calculating Function
n = int(input())
if n%2 == 0:
    print(int((((2+n)*n)/4)-((n*n)/4)))
else:
    print(int((((n+1)*(n-1))/4)-(((n+1)*(n+1)/4))))