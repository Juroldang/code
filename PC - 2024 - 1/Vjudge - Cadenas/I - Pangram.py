#I - Pangram
def main():
    N = int(input())
    S = input()
    print(pangram(S))
def pangram(S):
    letters = {'u', 'd', 'h', 'n', 'q', 'g', 'o', 'b', 'p', 'v', 'w', 'r', 'c', 'm', 'i', 'o', 'e', 'a', 's', 'y', 't', 'k', 'j', 'l', 'f', 'z', 'x'}
    S = S.lower()
    for letter in S:
        if letter in letters:
            letters.remove(letter)
        else: continue
    if len(letters) == 0:
        return 'YES'
    else: return 'NO'
main()