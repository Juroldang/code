#Taller 9 - Nivel de anidamiento
import ast
def main():
    l = ast.literal_eval(input())
    print(anidamiento(l, 0, []))
def anidamiento(l, level, levels):
    levels.append(level)
    for element in l:
        if type(element) == list:
            anidamiento(element, level+1, levels)
        else: pass
    return max(levels)
main()