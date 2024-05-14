#F - Word
def main():
    S = input()
    print(constantly_words(S))
def constantly_words(S):
    up = 0
    low = 0
    for letter in S:
        if letter.islower(): low += 1
        else: up += 1
    if low >= up: return S.lower()
    else: return S.upper()
main()