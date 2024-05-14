#Taller 6 - Alfanumérico
text = input()
if text.isdigit():
    print('Numérico')
elif text.isalpha():
    print('Alfabético')
else:
    print('Alfanumérico')