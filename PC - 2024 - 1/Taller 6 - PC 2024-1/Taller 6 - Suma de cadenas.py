#Taller 6 - Suma de cadenas
S1 = input()
S2 = input()
S = ""
for i in range(len(S1)):
    S+=chr(((ord(S1[i])-97)+(ord(S2[i])-97))%26+97)
print(S)