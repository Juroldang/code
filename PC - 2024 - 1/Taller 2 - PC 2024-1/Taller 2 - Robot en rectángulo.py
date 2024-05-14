#Taller 2 - Robot en rectángulo
x = int(input())
y = int(input())
w = int(input())
h = int(input())
rec1x = w - x
rec1y = h - y
if rec1x >= rec1y:
    recf=rec1y
else:
    recf=rec1x
if (recf <= x) and (recf <= y):
    print(recf)
else:
    if x >= y:
        print(y)
    else:
        print(x)