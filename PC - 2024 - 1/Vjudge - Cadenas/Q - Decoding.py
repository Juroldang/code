#Q - Decoding
def main():
    N = int(input())
    S = input()
    print(decode(S, N))
def decode(S, N):
    decoded_s = ["" for i in range(N)]
    for i in range(-1,-len(S)-1,-1):
        if i%2 != 0:
            decoded_s[len(S)+((i)//2)] = S[i]
        else:
            decoded_s[abs((i//2)+1)] = S[i]
    return "".join(decoded_s)
main()