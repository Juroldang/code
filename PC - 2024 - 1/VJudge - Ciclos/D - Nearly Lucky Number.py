#D - Nearly Lucky Number
n = input()
luckyNumbers = ["4","7"]
lucky=0
for i in n:
    if i in luckyNumbers:
        lucky += 1
if lucky==7 or lucky==4:
    print("YES")
else:
    print("NO")