# A - Vanya and Fence
nh = list(map(int,input().split()))
n, h = nh[0], nh[1]
heights = list(map(int, input().split()))
width = 0
for i in range(n):
    if heights[i] > h:
        width += 2
    else:
        width += 1
print(width)