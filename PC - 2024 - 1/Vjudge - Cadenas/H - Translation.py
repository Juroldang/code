#H - Translation
def main():
    S = input()
    T = input()
    print(correct_translation(S, T))
def correct_translation(S, T):
    trans = []
    for i in range(len(S)-1, -1, -1):
        trans.append(S[i])
    trans_word = "".join(trans)
    if trans_word == T: return 'YES'
    else: return 'NO'
main()