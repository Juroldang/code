#D - Word Capitalization
def main():
    S = input()
    print(capitalizator(S))
def capitalizator(S):
    if S[0].islower():
        return S[0].capitalize()+S[1:]
    else: return S
main()