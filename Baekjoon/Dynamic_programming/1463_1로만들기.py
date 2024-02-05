import sys
input = sys.stdin.readline

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

N = int(input())
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 0
for i in range(2, N+1):
    tmp = [dp[i-1]]
    if i % 3 == 0:
        tmp.append(dp[i // 3])
    if i % 2 == 0:
        tmp.append(dp[i // 2])
    dp[i] = min(tmp) + 1

print(dp[N])