#E - In Search of an Easy Problem
n = int(input())
opinions = list(map(int,input().split()))
easy = True
for i in range(n):
    if opinions[i] == 1:
        easy = False
        break
if easy:
    print("EASY")
else:
    print("HARD")