import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * len(A)

for i, a in enumerate(A[1:], 1):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))