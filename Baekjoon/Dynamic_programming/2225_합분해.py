import sys
input = sys.stdin.readline

# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
N, K = map(int, input().split())

# dp[N][K] = K개의 0~N의 숫자를 더해 N을 만들 수 있는 경우의 수
# dp[N][K] = dp[0][K-1] + dp[1][K-1] + ... + dp[N][K-1]
# dp[N][K] = dp[N-1][K] + dp[N][K-1]
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
for n in range(N+1):
    for k in range(1, K+1):
        dp[n][k] = dp[n-1][k] + dp[n][k-1]
print(dp[N][K] % 1000000000)