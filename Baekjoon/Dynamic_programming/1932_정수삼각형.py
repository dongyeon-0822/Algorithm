import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [row[:] for row in triangle]

for i in range(n-1):
    for j in range(i+1):
        if dp[i + 1][j] < dp[i][j] + triangle[i + 1][j]:
            dp[i + 1][j] = dp[i][j] + triangle[i + 1][j]
        if dp[i + 1][j + 1] < dp[i][j] + triangle[i + 1][j + 1]:
            dp[i + 1][j + 1] = dp[i][j] + triangle[i + 1][j + 1]
print(max(dp[n-1]))