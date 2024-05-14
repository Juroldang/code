#Taller 8 - Unimodal, Bimodal o Multimodal
from operator import itemgetter, attrgetter
def modal(lis):
    dic = {}
    for key in lis:
        if key not in dic:
            dic[key] = 1
        else: dic[key] += 1
    lis = []
    items = dic.items()
    for tupleItem in items:
        lis.append(tupleItem)
    sortedList = sorted(lis, key=itemgetter(1), reverse=True)
    if len(sortedList) >= 3:
        if sortedList[0][1] == sortedList[1][1] and sortedList[0][1] == sortedList[2][1]:
            return 'multimodal'
    if len(sortedList) >= 2:
        if sortedList[0][1] == sortedList[1][1]:
            return 'bimodal'
        else: return 'unimodal'
    if len(sortedList) == 1:
        return 'unimodal'
def main():
    lis = input().split()
    print(modal(lis))
main()