#Taller 2 - Calculadora
operador = input()
n1 = int(input())
if operador == 'sqrt':
    print(int(n1**0.5))
else:
    n2 = int(input())
    if operador == '+':
        print(n1+n2)
    elif operador == '-':
        print(n1-n2)
    elif operador == '/':
        print(n1//n2)
    elif operador == '*':
        print(n1*n2)
    elif operador == 'pow':
        print(n1**n2)