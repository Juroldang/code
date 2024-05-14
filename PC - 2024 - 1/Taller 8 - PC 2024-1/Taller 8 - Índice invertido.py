#Taller 8 - Índice invertido
def main():
    docs = eval(input())
    print(ind(docs))
def ind(docs):
    inds = {}
    for i in range(len(docs)):
        words = docs[i].split()
        for word in words:
            if word not in inds:
                inds[word] = [i]
            else: inds[word].append(i)
    inds = dict(sorted(inds.items()))
    return inds
main()