import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cheese_count = sum([sum(row) for row in graph])

directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
time = 0
last_cheese_count = 0

while cheese_count:
    last_cheese_count = cheese_count
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in directs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    cheese_count -= 1
                else:
                    q.append((nx,ny))
    time += 1

print(time)
print(last_cheese_count)