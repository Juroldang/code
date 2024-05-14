#Taller 6 - Eliminación de letras
S = input()
while True:
    breaker = True
    for i in range(len(S)-1):
        if len(S) > 1 and S[i] == S[i+1]:
            S = S[:i] + S [i+2:]
            breaker = True
            break
        else: breaker = False
    if len(S)== 0 or not breaker: break
print('"{}"'.format(S))