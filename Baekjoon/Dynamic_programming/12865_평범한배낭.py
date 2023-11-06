import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        if stuff[n][0] > k:
            dp[n][k] = dp[n-1][k]
        else:
            dp[n][k] = max(stuff[n][1] + dp[n-1][k-stuff[n][0]], dp[n-1][k])
print(dp[N][K])