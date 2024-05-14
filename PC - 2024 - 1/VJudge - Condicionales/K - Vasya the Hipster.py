#K - Vasya the Hipster
socks = input().split()
post = abs(int(socks[0])-int(socks[1]))//2
trend = min(list(map(int,socks)))
print(trend, post)