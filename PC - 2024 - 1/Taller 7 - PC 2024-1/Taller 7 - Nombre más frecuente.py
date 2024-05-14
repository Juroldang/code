#Taller 7 - Nombre más frecuente
from operator import itemgetter, attrgetter
names = input().split()
namesDic = {}
for name in names:
    if name not in namesDic.keys():
        namesDic[name] = 1
    else:
        namesDic[name] = namesDic.get(name) + 1
listNames = []
items = namesDic.items()
for tupleItem in items:
    listNames.append(tupleItem)
sortedList = sorted(listNames, key=itemgetter(0))
ans = sorted(sortedList, key=itemgetter(1), reverse=True)[0]
print("{} {}".format(ans[0],ans[1]))