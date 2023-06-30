import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y, visit):
    if 0<=x<h and 0<=y<w and graph[x][y] == 1 and not visit[x][y]:
        visit[x][y] = True
        for direct in range(8):
            nx = x + dx[direct]
            ny = y + dy[direct]
            dfs(nx, ny, visit)
        return True
    else:
        return False

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, visited):
                answer += 1
    print(answer)
