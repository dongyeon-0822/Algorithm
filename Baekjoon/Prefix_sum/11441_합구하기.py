import sys
input = sys.stdin.readline


N = int(input())
prefix_sum = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    prefix_sum[i] += prefix_sum[i - 1]

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])