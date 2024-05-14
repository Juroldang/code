#Taller 2 - Problema del reloj
hh=int(input())
if hh==12:
    hora=12
    minuto=0
    segundos=0
else:
    pos=hh*3600
    avance=(300*hh)
    for i in range(5):
        porcentajeavance = avance/3600
        pos=pos+avance
        avance=(300*porcentajeavance)
    n=round(pos)
    hora=n//3600
    minuto=((n%3600)//60)
    segundos=(((n%3600)%60))
print("{:02d}:{:02d}:{:02d}".format(hora,minuto,segundos))