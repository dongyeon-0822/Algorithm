import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [input().strip() for _ in range(N)]

q = deque()
distance = [[[INF, INF] for _ in range(M)] for _ in range(N)]

q.append((False, 0, 0))
distance[0][0][0] = 1
while q:
    flag, x, y = q.popleft()
    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == '0':
                if flag and distance[nx][ny][1] > distance[x][y][1] + 1:
                    distance[nx][ny][1] = distance[x][y][1] + 1
                    q.append((flag, nx, ny))
                elif not flag and distance[nx][ny][0] > distance[x][y][0] + 1:
                    distance[nx][ny][0] = distance[x][y][0] + 1
                    q.append((flag, nx, ny))
            elif graph[nx][ny] == '1' and not flag and distance[nx][ny][1] > distance[x][y][0] + 1:
                distance[nx][ny][1] = distance[x][y][0] + 1
                q.append((True, nx, ny))

answer = min(distance[N-1][M-1])
if answer == INF:
    print(-1)
else:
    print(answer)
