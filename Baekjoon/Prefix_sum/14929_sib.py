# 풀이 참고함

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

answer = 0
n_sum = arr[0]
for i in range(1, n):
    answer += arr[i] * n_sum
    n_sum += arr[i]

print(answer)
