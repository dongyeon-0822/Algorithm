import sys
input = sys.stdin.readline


# def dfs(visit, x, y):
#     if visit[x][y]: return False
#     visit[x][y] = True
#     for nx, ny in [(x+1, y), (x-1,y), (x, y+1), (x,y-1)]:
#         if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
#             dfs(visit, nx, ny)
#     return True
def dfs(visit, x,y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if not visit[x][y]:
        visit[x][y] = True
        dfs(visit,x - 1, y)
        dfs(visit,x, y - 1)
        dfs(visit,x + 1, y)
        dfs(visit,x, y + 1)
        return True
    return False

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
            if dfs(visited, i, j):
                answer += 1
    print(answer)


