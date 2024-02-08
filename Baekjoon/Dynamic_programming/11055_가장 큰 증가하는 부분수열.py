import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = A[:]

for i, a in enumerate(A[1:], 1):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))