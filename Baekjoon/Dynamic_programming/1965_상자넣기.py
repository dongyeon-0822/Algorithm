import sys
input = sys.stdin.readline

N = int(input())
boxs = list(map(int, input().split()))
dp = [1] * N

for i, b in enumerate(boxs[1:], 1):
    for j in range(i):
        if boxs[j] < boxs[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))