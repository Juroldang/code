#Taller 7 - Palabras comunes
set1 = set(input().split())
set2 = set(input().split())
res = sorted(list(set1.intersection(set2)))
print(" ".join(res))