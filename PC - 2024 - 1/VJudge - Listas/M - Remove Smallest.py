#M - Remove Smallest
def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        l = list(map(int, input().split()))
        print(one_element_list(n, l))
def one_element_list(n, l):
    l = sorted(l)
    for i in range(n-1):
        if abs(l[i]-l[i+1]) > 1:
            return 'NO'
    return 'YES'
main()