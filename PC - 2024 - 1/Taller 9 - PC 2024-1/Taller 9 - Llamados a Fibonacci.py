#Taller 9 - Llamados a Fibonacci
def main():
    n = int(input())
    print(llamados(0, 0, 0, n))
def llamados(n1, n2, iter, n):
    if n <= 1: return 1
    if n == 2: return 3
    if n == 3: return 5
    if n >= 4 and n1 == 0 and n2 == 0:
        n1, n2 = 3, 5
    else:
        n1, n2 = n2, n2+n1+1
    if iter > n-4: return n2
    else: return llamados(n1, n2, iter+1, n)
main()