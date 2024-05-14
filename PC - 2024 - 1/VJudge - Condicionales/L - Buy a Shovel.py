#L - Buy a Shovel
k, r = list(map(int, input().split()))
shovels = 1
while True:
    if (shovels*k)%10 == 0 or ((shovels*k)-r)%10 == 0:
        break
    else:
        shovels += 1
print(shovels)