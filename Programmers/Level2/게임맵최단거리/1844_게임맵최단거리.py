from collections import deque

def solution(maps):
    answer = -1

    n,m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((1,0,0))
    while q:
        d, x, y = q.popleft()
        if x == n-1 and y == m-1:
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny]:
                maps[nx][ny] = 0
                q.append((d+1, nx, ny))

    return answer