#T - Two-gram
def main():
    N = int(input())
    S = input()
    print(twogram(S, N))
def twogram(S, N):
    twograms = {}
    for i in range(N-1):
        temp = S[i]+S[i+1]
        if temp not in twograms:
            twograms[temp] = 1
        else: twograms[temp] += 1
    ans = sorted(twograms, key=lambda x:twograms[x], reverse = True)
    return ans[0]
main()