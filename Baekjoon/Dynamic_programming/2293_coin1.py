import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1
for value in values:
    for x in range(value, k+1):
        dp[x] += dp[x-value]
print(dp[k])
