#A - Arrival of the General
def main():
    N = int(input())
    soldiers = list(map(int,input().split()))
    print(timeorganize(N, soldiers))
def timeorganize(N, S):
    seconds = 0
    max, min, max_i, min_i = 0, 101, len(S), -1
    for i in range(N):
        if S[i] > max: max, max_i = S[i], i
        if S[i] <= min: min, min_i = S[i], i
    if min_i < max_i: seconds -= 1
    seconds += abs(len(S)-1-min_i)+max_i
    return seconds
main()