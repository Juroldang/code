#Taller 8 - Estudiantes por programa
def main():
    students = eval(input())
    print(program_dict(students))
def program_dict(students):
    dicPro = {}
    for student in students:
        prog = student['programa']
        if prog not in dicPro:
            dicPro[prog] = [student['nombre']]
        else: dicPro[prog].append(student['nombre'])
    dicPro = dict(sorted(dicPro.items()))
    for prog in dicPro:
        dicPro[prog] = sorted(dicPro[prog])
    return dicPro
main()