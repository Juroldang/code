#J - The New Year: Meeting Friends
xs = input().split()
coordenates = list(map(int,xs))
coordenates_sorted = sorted(coordenates)
print((coordenates_sorted[2]-coordenates_sorted[1])+(coordenates_sorted[1]-coordenates_sorted[0]))