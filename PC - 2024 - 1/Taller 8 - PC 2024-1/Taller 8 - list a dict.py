#Taller 8 - list a dict
country = input().split()
capital = input().split()
dict = {country[i]:capital[i] for i in range(len(country))}
print(dict)