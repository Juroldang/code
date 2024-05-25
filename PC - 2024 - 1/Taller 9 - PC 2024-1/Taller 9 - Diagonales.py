#Taller 9 - Diagonales
def main():
    n = int(input())
    print(diagonales(n))
def diagonales(n):
    if n < 4: return 0
    elif n == 4: return 2
    else: return int((n-2)+diagonales(n-1))
main()