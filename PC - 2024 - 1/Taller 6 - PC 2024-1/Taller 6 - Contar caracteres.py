#Taller 6 - Contar caracteres
from operator import itemgetter, attrgetter
text = input()
letters = {}
for letter in text:
    if letter not in letters.keys():
        letters[letter] = 1
    else:
        letters[letter] = letters.get(letter) + 1
list = []
items = letters.items()
for tupleItem in items:
    list.append(tupleItem)
sortedList = sorted(list, key=itemgetter(0))
ans = sorted(sortedList, key=itemgetter(1), reverse=True)[0]
print("{} {}".format(ans[0],ans[1]))