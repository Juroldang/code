#N - Team Olympiad
def main():
    n = int(input())
    students = list(map(int, input().split()))
    teams(n, students)
def teams(n, s):
    students = {}
    for i in range(n):
        if s[i] not in students:
            students[s[i]] = [i+1]
        else: students[s[i]].append(i+1)
    if len(students) < 3: print(0)
    else:
        t = min(len(students[1]), len(students[2]), len(students[3]))
        print(t)
        for i in range(t):
            print(students[1].pop(), students[2].pop(), students[3].pop())
main()