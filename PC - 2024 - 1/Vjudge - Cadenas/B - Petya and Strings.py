#B - Petya and Strings
S1 = input()
S2 = input()
for i in range(len(S1)):
    if S1[i].islower():
        S1 = S1[:i]+chr(ord(S1[i])-32)+S1[i+1:]
    if S2[i].islower():
        S2 = S2[:i]+chr(ord(S2[i])-32)+S2[i+1:]
if S1 == S2:
    print(0)
elif S1 > S2:
    print(1)
else: print(-1)