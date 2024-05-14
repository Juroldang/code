#Taller 2 - Día de la semana
dia = input()
n = int(input())
semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
i = semana.index(dia)
indice = (n+i)%7
print(semana[indice]) 