def solution(n):
    dp = [0] * 5001

    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = (dp[i-2] * 3 + (dp[i-2] - dp[i-4])) % 1000000007
    return dp[n]

print(solution(10))