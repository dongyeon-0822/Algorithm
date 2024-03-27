import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(visit, x, y):
    visit[x][y] = True
    for nx, ny in [(x+1, y), (x-1,y), (x, y+1), (x,y-1)]:
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and board[nx][ny]:
            dfs(visit, nx, ny)
    return True

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1

    visited = [[False] * M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] and dfs(visited, i, j):
                answer += 1
    print(answer)


