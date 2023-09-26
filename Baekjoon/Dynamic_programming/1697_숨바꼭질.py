import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [int(1e9)] * (2 * K + 1)

if N >= K:
    print(N - K)
else:
    dp[N] = 0
    for i in range(1, N+1):
        dp[N-i] = i
    for i in range(N, 2 * K + 1):
        dp[i] = i - N
    # print(dp[:K * 2 + 1])
    for i in range(N, 2 * K + 1):
        if i % 2 == 0 and i // 2 >= 0 and i + 1 < 2 * K + 1:
            dp[i] = min(dp[i - 1] + 1 , dp[i], dp[i // 2] + 1)
        elif i + 1 < 2 * K + 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    # print(dp[:K * 2 + 1])
    print(dp[K])