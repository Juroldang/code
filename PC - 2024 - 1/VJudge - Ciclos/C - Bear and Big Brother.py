#C - Bear and Big Brother
weights = list(map(int, input().split()))
a = weights[0]
b = weights[1]
years = 0
while b >= a:
    a = a*3
    b = b*2
    years += 1
print(years)