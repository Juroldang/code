#Taller 9 - Bosque más grande
def main():
    n = int(input())
    terrain = []
    for _ in range(n):
        terrain.append(list(input()))
    print(biggest_forest(terrain, n))


def counting_trees(terrain, n, j, i, forests, forest):
    if i < 0 or i >= n or j >= n or j < 0 or j >= n or terrain[i][j] != 'T': return
    else:
        forests[forest] += 1
        terrain[i][j] = 'V'
        counting_trees(terrain, n, j, i + 1, forests, forest)
        counting_trees(terrain, n, j + 1, i, forests, forest)
        counting_trees(terrain, n, j, i - 1, forests, forest)
        counting_trees(terrain, n, j - 1, i, forests, forest)


def biggest_forest(terrain, n):
    forests = {}
    for i in range(n):
        for j in range(n):
            if terrain[i][j] == 'T':
                forest = len(forests) + 1
                forests[forest] = 0
                counting_trees(terrain, n, j, i, forests, forest)
    return max(forests.values())


main()
