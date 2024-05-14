#Taller 8 - Mínimo palíndromo
def minPal(lis):
    dic = {}
    for key in lis:
        if key not in dic:
            dic[key] = 1
        else: dic[key] += 1
    items = dic.items()
    sortedList = sorted(list(items))
    odd = 0
    i = 0
    a = list('' for i in range(len((sortedList)*2)+1))
    while odd < 2:
        if sortedList[i][1]%2 != 0:
            a[len(a)//2] = sortedList[i][0]
            odd += 1
        a[i] = sortedList[i][0]*(sortedList[i][1]//2)
        a[-i-1] = sortedList[i][0]*(sortedList[i][1]//2)
        i += 1
        if i >= len(sortedList) or odd > 1: break
    if odd > 1: return '-1'
    else: return "".join(a)
def main():
    lis = input()
    print(minPal(lis))
main()