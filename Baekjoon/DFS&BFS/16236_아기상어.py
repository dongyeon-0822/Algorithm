import sys
from collections import deque
input = sys.stdin.readline

answer = 0
N = int(input())
graph = []
x,y = 0,0
for i in range(N):
    row = list(map(int, input().split()))
    if 9 in row:
        x,y = i,row.index(9)
    graph.append(row)

shark_size = 2
fish_count = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

visited = [[False] * N for _ in range(N)]
q = deque()
q.append((0,[x,y]))
graph[x][y] = 0
visited[x][y] = True
while True:
    eatable = []
    while q:
        d, [x, y] = q.popleft()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if 0 <= graph[nx][ny] <= shark_size: # 이동 가능
                    q.append((d + 1, [nx, ny]))
                    visited[nx][ny] = True

                if 0 < graph[nx][ny] < shark_size:  # 먹을 수 있는 경우
                    eatable.append([d, nx,ny])
    if eatable:
        eatable.sort(key=lambda k:(k[0], k[1], k[2]))
        d, nx, ny = eatable[0]
        fish_count += 1
        if fish_count == shark_size:
            shark_size += 1
            fish_count = 0
        graph[nx][ny] = 0
        q = deque()  # 큐 초기화
        q.append((0, [nx, ny]))
        visited = [[False] * N for _ in range(N)]  # 방문 기록 초기화
        visited[nx][ny] = True
        answer += d + 1
    else: break

print(answer)
