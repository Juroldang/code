#A - Way Too Long Words
n = int(input())
for i in range(n):
    S = input()
    if len(S) > 10:
        print("{}{}{}".format(S[0],len(S)-2,S[len(S)-1]))
    else: print(S)