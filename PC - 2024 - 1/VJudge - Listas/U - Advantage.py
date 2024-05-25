#U - Advantage
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print(dif_strenght(n, p))
def dif_strenght(n, p):
    temp = sorted(p, reverse=True)
    dif = []
    max_s, second_max_s = temp[0], temp[1]
    for i in range(n):
        if p[i] == max_s: dif.append(p[i]-second_max_s)
        else: dif.append(p[i]-max_s)
    return " ".join(list(map(str, dif)))
main()