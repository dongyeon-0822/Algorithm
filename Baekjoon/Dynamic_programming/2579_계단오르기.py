import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

# sol 1
dp = [[] for _ in range(301)]
dp[0] = 0
dp[1] = stairs[1]
for i in range(2, n + 1):
    if i == 2:
        dp[i] = stairs[i-1] + stairs[i]
    else:
        dp[i] = max([dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i]])
print(dp[n])

# sol 2
dp = [[] for _ in range(301)]
dp[0] = [0, 0]
dp[1] = [stairs[1], stairs[1]]
for i in range(2, n + 1):
    if i == 2:
        dp[i] = [stairs[i], stairs[i-1] + stairs[i]]
    else:
        dp[i] = [max(dp[i-2]) + stairs[i], dp[i-1][0] + stairs[i]]
print(max(dp[n]))
