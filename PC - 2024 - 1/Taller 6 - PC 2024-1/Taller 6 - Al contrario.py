#Taller 6 - Al contrario
S = input()
Sf = ""
for i in range(-1, -len(S)-1, -2):
    Sf += S[i]
print(Sf)