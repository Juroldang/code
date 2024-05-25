#D - Beautiful Matrix
def main():
    print(b_matrix())
def b_matrix():
    x = -1
    y = -1
    for i in range(5):
        matrix_row = input().split()
        if '1' in matrix_row:
            y = i
            x = matrix_row.index('1')
    ans = abs(x-2) + abs(y-2)
    return ans
main()