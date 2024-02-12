import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for n in range(1, N+1):
    dp[n] = P[n]
    for i in range(1, n // 2 + 1):
        dp[n] = max(dp[n], dp[n-i] + dp[i])
print(dp[N])