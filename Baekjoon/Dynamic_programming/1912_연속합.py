import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
for i, a in enumerate(arr[1:], 1):
    dp[i] = max(dp[i-1]+a, a)
print(max(dp))