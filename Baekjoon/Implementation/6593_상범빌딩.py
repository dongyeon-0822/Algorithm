import sys
from collections import deque
input = sys.stdin.readline

while True:
    def dfs():
        q = deque()
        visited = [[[False] * C for _ in range(R)] for _ in range(L)]

        z, x, y = start
        q.append((0, z, x, y))
        visited[z][x][y] = True
        while q:
            d, z, x, y = q.popleft()
            for dz, dx, dy in directs:
                nz, nx, ny = z + dz, x + dx, y + dy
                if  0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny] and cube[nz][nx][ny] != '#':
                    if cube[nz][nx][ny] == 'E':
                        return d + 1
                    q.append((d + 1, nz, nx, ny))
                    visited[nz][nx][ny] = True
        return 0

    directs = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    L, R, C = map(int, input().split())
    if L == R == C == 0: break

    cube = []
    start, end = [], []
    for l in range(L):
        layer = []
        for r in range(R):
            row = input().rstrip()
            layer.append(row)
            for c, x in enumerate(row):
                if x == 'S':
                    start = [l, r, c]
                elif x == 'E':
                    end = [l, r, c]
        input()
        cube.append(layer)

    n = dfs()
    if n > 0:
        print("Escaped in " + str(n) + " minute(s).")
    else:
        print("Trapped!")