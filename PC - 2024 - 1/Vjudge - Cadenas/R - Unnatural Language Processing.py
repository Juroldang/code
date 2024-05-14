#R - Unnatural Language Processing 
def main():
    N = int(input())
    splitsyl(N)
def splitsyl(N):
    v = {'a','e'}
    c = {'b','c','d'}
    for i in range(N):
        syllables = []
        n = int(input())
        S = input()
        if n < 4:
            print(S)
        else:
            j = 0
            while j < (n-3):
                if S[j] in c and S[j+3] in v:
                    syllables.append(S[j:j+2])
                    j += 2
                else:
                    syllables.append(S[j:j+3])
                    j += 3
            syllables.append(S[j:])
        print(".".join(syllables))
main()