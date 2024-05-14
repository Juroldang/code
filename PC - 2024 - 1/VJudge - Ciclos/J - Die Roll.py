#J - Die Roll
YW = list(map(int,input().split()))
if YW[0] > YW[1]:
    p = YW[0]
else:
    p = YW[1]
results = {1: '1/1', 2: '5/6', 3: '2/3', 4: '1/2', 5: '1/3', 6: '1/6'}
print(results[p])