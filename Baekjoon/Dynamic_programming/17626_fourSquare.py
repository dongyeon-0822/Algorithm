# 다른 풀이 참조함
# python3은 시간초과 -> pypy3으로 통과

import sys
input = sys.stdin.readline

N = int(input())
global dp
dp = [0] * 50001
for x in range(1,224): # 제곱수들에 미리 1 대입
    dp[x * x] = 1

def square(n):
    min_num = 4
    if dp[n] != 0:
        return dp[n]
    for i in range(int(n ** 0.5), 0, -1):
        min_num = min(min_num, 1 + square(n - i*i))
    dp[n] = min_num
    return dp[n]

print(square(N))