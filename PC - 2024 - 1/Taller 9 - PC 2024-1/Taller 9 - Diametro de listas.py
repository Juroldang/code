#Taller 9 - Diametro de listas
import ast
import math
def main():
    l = ast.literal_eval(input())
    print(diametro(0, l))
def diametro(d, l):
    min = math.inf
    max = 0
    for val in l:
        if type(val) == list:
            d = diametro(d, val)
        else:
            if val < min: min = val
            if val > max: max = val
    if min != math.inf:
        if (max-min) > d: return max-min
        else: return d
    else: return d
main()