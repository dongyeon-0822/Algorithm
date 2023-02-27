import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append([0,0])
visited[0][0] = True
while q:
    x, y = q.popleft()
    for i in range(4):
       nx = x + dx[i]
       ny = y + dy[i]
       if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and not visited[nx][ny]:
           visited[nx][ny] = True
           q.append([nx,ny])
           graph[nx][ny] = graph[x][y] + 1

print(graph[N-1][M-1])