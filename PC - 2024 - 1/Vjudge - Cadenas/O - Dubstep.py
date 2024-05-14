#O - Dubstep
def main():
    S = input()
    print(original_song(S))
def original_song(S):
    song = (S.replace('WUB', " ")).strip()
    return song
main()