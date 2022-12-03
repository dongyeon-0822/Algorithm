import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    # 초기화
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * col for _ in range(row)]

    queue = deque()
    queue.append([x, y, 0])
    visited[x][y] = True

    cnt = 0
    while queue:
        x, y, d= queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0<= nx <row and 0<= ny <col and not visited[nx][ny] and arr[nx][ny] == 'L':
                visited[nx][ny] = True
                queue.append([nx,ny,d+1])
        cnt = d+1
    return cnt-1

row, col = map(int,input().split())
arr = [input().rstrip() for _ in range(row)]

q = deque()
distance = 0
for i in range(row):
    for j in range(col):
        if arr[i][j] == 'L': # 모든 지점의 최단거리 구하기
            distance = max(distance, bfs(i,j))
print(distance)

