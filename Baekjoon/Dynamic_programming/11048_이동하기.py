import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for r in range(N):
    for c in range(M):
        tmp = []
        for nr, nc in [(r-1, c), (r, c-1), (r-1, c-1)]:
            if 0 <= nr < N and 0 <= nc < M:
                tmp.append(dp[nr][nc])
        dp[r][c] = board[r][c] + (max(tmp) if tmp else 0)
print(dp[N-1][M-1])
