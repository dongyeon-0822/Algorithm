import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * 11 for _ in range(N+1)]
for i in range(1, 11):
    dp[1][i] = 1

for n in range(2, N+1):
    for i in range(1, 11):
        dp[n][i] = dp[n][i-1] + dp[n-1][i]

print(sum(dp[N]) % 10007)
