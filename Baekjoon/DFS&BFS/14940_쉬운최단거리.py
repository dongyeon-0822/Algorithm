import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
directs = [[-1, 0], [1,0], [0,-1], [0,1]]
graph = []
start = []
for i in range(n):
    row = list(map(int, input().split()))
    for j, x in enumerate(row):
        if x == 2: start = [i,j]
    graph.append(row)

answer = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()

x,y = start
q.append((0, x, y))
visited[x][y] = True
while q:
    d, x, y = q.popleft()
    for dx, dy in directs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
            answer[nx][ny] = d+1
            visited[nx][ny] = True
            q.append((d+1, nx, ny))
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            answer[i][j] = -1
        print(answer[i][j], end=" ")
    print()
