#Taller 6 - Máxima subcadena creciente
S = input()
Sf = ("", 0)
for i in range(len(S)-1):
    St = S[i]
    Val = ord(S[i])
    for j in range(len(S)-1-i):
        if ord(S[i+j]) < ord(S[j+i+1]):
            St += S[j+i+1]
            Val += ord(S[j+i+1])
        else: break
    if len(St) >= len(Sf[0]) and Val > Sf[1]:
        Sf = (St, Val)
print(Sf[0])