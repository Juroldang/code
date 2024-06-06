#Taller 9 - Bosque más grande
def main():
    n = int(input())
    terrain = []
    for _ in range(n):
        terrain.append(list(input()))
    print(bg(n, 0, 0, terrain, True, 0))
def bg(n, y, x, t, new, F):
    current = F
    if x >= n or y >= n: return
    if not new:
        if t[x][y] != 'T':
            bg(n, y + 1, x, t, True, current)
            bg(n, y, x + 1, t, True, current)
        else:
            t[x][y] = 'O'
            current = 1 + bg(n, y + 1, x, t, False, current) + bg(n, y, x + 1, t, False, current)
    else:
        if t[x][y] != 'T':
            bg(n, y + 1, x, t, True, 0)
            bg(n, y, x + 1, t, True, 0)
