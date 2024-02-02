import sys
input = sys.stdin.readline

# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 7
# 5 -> 11 # 11111, 11112, 122, 23 -> 1 + 5 + 3 + 2
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])
