#Taller 2 - Error en servidor
h1 = input()
h2 = input()
h3 = input()
h4 = input()
horas = ['1:00am','1:30am','2:00am','2:30am']
respuestas = [h1,h2,h3,h4]
errores=0
for i in range(4):
    if (respuestas[i][0] in ['4','5']):
        print("Error "+horas[i])
        errores += 1
if errores == 0:
    print('OK')