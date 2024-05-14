# Taller 4 - Pirámide
X = int(input())
esp = 1
print(" "*((2*X)-1)+"_")
for i in range(X-1):
    print(" "*((2*X)-(2*(i+1)+1))+"_"+"|"+" "*esp+"|_")
    esp += 4
print("|"+" "*esp+"|")