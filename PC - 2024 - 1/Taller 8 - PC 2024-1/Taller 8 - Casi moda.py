#Taller 8 - Casi moda
from operator import itemgetter, attrgetter
def quasimodal(lis):
    dic = {}
    for key in lis:
        if key not in dic:
            dic[key] = 1
        else: dic[key] += 1
    items = dic.items()
    sortedList = sorted(list(items), key=itemgetter(1), reverse=True)
    mod = sortedList[0][1]
    quasimod_val = 0
    for elem in sortedList[1:]:
        if elem[1] != mod and elem[1] > quasimod_val:
            quasimod = elem[0]
            quasimod_val = elem[1]
        elif elem[1] != mod and elem[1] == quasimod_val:
            return 'multiples soluciones'
    if quasimod_val == 0:
        return 'no existe'
    else: return str(quasimod)
def main():
    lis = input().split()
    print(quasimodal(lis))
main()