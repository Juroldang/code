#I - New Year and Hurry
n, k = input().split()
time = int(k)
problems = 0
for i in range (int(n)):
    if (((i+1)*5)+time) > 240:
        break
    else:
        time = time + (i+1)*5
        problems += 1
print(problems)