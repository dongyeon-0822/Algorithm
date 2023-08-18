import sys
input = sys.stdin.readline

def rotate(sx, sy, rx, ry):
    a, b = rx - sx, ry - sy
    return sx + b, sy - a

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
grid = [[False] * 101 for _ in range(101)]
direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
answer = 0

for y, x, d, g in info:
    curves = []
    nx, ny = x + direct[d][0], y + direct[d][1]
    curves.extend([(x,y), (nx, ny)])
    for _ in range(g):
        sx, sy = curves[-1]
        new_curves = []
        for rx, ry in curves[-2::-1]:
            new_curves.append(rotate(sx, sy, rx, ry))
        curves.extend(new_curves)
    for r, c in curves:
        grid[r][c] = True

for i in range(100):
    for j in range(100):
        if all([grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]):
            answer += 1

print(answer)