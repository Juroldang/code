'''Punto 1. Taller Modulos, Presentado por:
Nicolas Fuentes Ramos
Santiago Cardenas Rodriguez
Juan Jose Roldan'''
#Declaracion de variables

DIAS_ENERO=31
DIAS_FEBRERO=28
DIAS_MARZO=31
DIAS_ABRIL=30
DIAS_MAYO=31
DIAS_JUNIO=30
DIAS_JULIO=31
DIAS_AGOSTO=31
DIAS_SEPTIEMBRE=30
DIAS_OCTUBRE=31
DIAS_NOVIEMBRE=30
DIAS_DICIMEBRE=31
DIAS_FEBRERO_BISIESTO=29
meses={'1':DIAS_ENERO,
       '2':DIAS_FEBRERO,
       '3':DIAS_MARZO,
       '4':DIAS_ABRIL,
       '5':DIAS_MAYO,
       '6':DIAS_JUNIO,
       '7':DIAS_JULIO,
       '8':DIAS_AGOSTO,
       '9':DIAS_SEPTIEMBRE,
       '10':DIAS_OCTUBRE,
       '11':DIAS_NOVIEMBRE,
       '12':DIAS_DICIMEBRE,
       '2.1':DIAS_FEBRERO_BISIESTO}
DIA_ANHO_NUEVO=1 
MES_ANHO_NUEVO=1
DIA_DIA_TRABAJO=1
MES_DIA_TRABJO=5
DIA_NAVIDAD=24
MES_NAVIDAD=12
DIA_FIN_ANHO=31
MES_FIN_ANHO=12

#Declaracion de funciones

def es_bisiesto(a):
    if a%4==0:
        if a%100==0:
            if a%400==0:
                tot=True
            else: 
                tot=False
        else:
            tot=True
    else:
        tot=False
    return(tot)
  
def dias_mes(m,a):
  if es_bisiesto(a) and m==2: return(meses['2.1'])
  else: return(meses[f'{m}'])
  
def fecha_valida(d,m,a):
    try:
      x=dias_mes(m,a)
      if d<=x and d>0:
          tot=True
      else:
          return(False)
      if a<0:
        return(False)
    except:
        tot=False
    return(tot)

def es_anterior(d1,m1,a1,d2,m2,a2):
    if a1>a2:
        return False
    elif a1 == a2:
      if m1>m2:
          return False
      else:
        if m1==m2:
          if d1>=d2:
            return False
          else:
            return True
        else:
          return True
    else:
      return True

def es_posterior(d1,m1,a1,d2,m2,a2):
  if a1<a2:
    return False
  elif a1 == a2:
    if m1<m2:
        return False
    else:
      if m1==m2:
        if d1<=d2:
          return False
        else:
          return True
      else:
        return True
  else:
    return True

def es_igual(d1,m1,a1,d2,m2,a2):
    if a1==a2 and m1==m2 and d1==d2:
        return True
    else:
        return False

def dias_transcurridos(d,m,a):
    tot=0
    for i in range (1,m):
        tot=tot+meses[f'{i}']
    if es_bisiesto(a)==True and m>2:
        tot=tot+1
    tot=tot+d
    return(tot)

def siglo(a):
      siglo=a//100+1
      return(siglo)

def siglo_numeral_romano(a):
  ar = siglo(a)
  m = ["", "M", "MM", "MMM"]
  c = ["", "C", "CC", "CCC", "CD", "D",
       "DC", "DCC", "DCCC", "CM "]
  x = ["", "X", "XX", "XXX", "XL", "L",
       "LX", "LXX", "LXXX", "XC"]
  i = ["", "I", "II", "III", "IV", "V",
       "VI", "VII", "VIII", "IX"]
  thousands = m[ar // 1000]
  hundreds = c[(ar % 1000) // 100]
  tens = x[(ar % 100) // 10]
  ones = i[ar % 10]
  ans = (thousands + hundreds +
         tens + ones)
  return ans