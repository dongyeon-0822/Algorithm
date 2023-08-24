import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)] # (가로, 세로, 대각선)

dp[0][0] = [1,0,0]
for j in range(1, N):
    if not graph[0][j]:
        dp[0][j] = [dp[0][j - 1][0], 0, 0]

# 각 칸마다 가로, 세로, 대각선
for i in range(1, N):
    for j in range(2, N):
        if not graph[i][j]:
            w = dp[i][j-1][0] + dp[i][j-1][2]
            h = dp[i-1][j][1] + dp[i-1][j][2]
            d = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2] if graph[i-1][j] == graph[i][j-1] == 0 else 0
            dp[i][j] = [w, h, d]

print(sum(dp[N-1][N-1]))