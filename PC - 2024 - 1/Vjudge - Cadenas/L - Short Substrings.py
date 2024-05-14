#L - Short Substrings
def main():
    N = int(input())
    sstrings(N)
def sstrings(N):
    for i in range(N):
        S = input()
        message = []
        for i in range((len(S)//2)-1):
            message.append(S[i*2])
        message.append(S[len(S)-2:])
        print("".join(message))
main()