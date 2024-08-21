# https://www.acmicpc.net/problem/2073
import sys
input = sys.stdin.readline

D, P = map(int, input().split())

dp = [0] * (D+1)
dp[0] = int(1e9)
for i in range(P):
    l, c = map(int, input().split())
    for j in range(D, l-1, -1):
        dp[j] = max(dp[j], min(c, dp[j-l]))
print(dp[D])
