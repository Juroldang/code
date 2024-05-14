#J - Anton and Polyhedrons
def main():
    N = int(input())
    print(faces(N))
def faces(N):
    faces = 0
    for i in range(N):
        S = input()
        if S[0] == 'T': faces += 4
        elif S[0] == 'C': faces += 6
        elif S[0] == 'O': faces += 8
        elif S[0] == 'D': faces += 12
        else: faces += 20
    return faces
main()