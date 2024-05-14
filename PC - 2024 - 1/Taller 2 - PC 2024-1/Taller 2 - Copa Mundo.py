#Taller 2 - Copa Mundo
n = int(input())
if (n==1942) or (n==1946) or (n<1930) or (((n-1930)%4)!=0) or (n>2019):
    print(':(')
else :
    print(':)')