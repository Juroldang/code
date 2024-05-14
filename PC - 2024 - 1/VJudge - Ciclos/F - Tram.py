#F - Tram
n = int(input())
passengers = 0
max = 0
for i in range(n):
    tram = list(map(int, input().split()))
    passengers += tram[1]
    passengers -= tram[0]
    if passengers > max:
        max = passengers
print(max)