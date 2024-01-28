import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, visit):
    q = deque()
    q.append((x,y))
    visit[x][y] = True
    country = [(x,y)]
    peoples = people[x][y]
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                if L <= abs(people[r][c] - people[nr][nc]) <= R:
                    visit[nr][nc] = True
                    q.append((nr, nc))
                    country.append((nr, nc))
                    peoples += people[nr][nc]
    avg = peoples // len(country)
    for r, c in country:
        people[r][c] = avg
    return len(country) > 1

days = 0
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    flag = True
    if not flag: break
    days += 1
print(days)
