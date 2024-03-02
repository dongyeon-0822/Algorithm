import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j][0] = dp[i-1][j][0] + board[i][j]
        dp[i][j][1] = dp[i][j-1][1] + board[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    for y in range(y1, y2+1):
        answer += dp[x2][y][0] - dp[x1-1][y][0]
    print(answer)