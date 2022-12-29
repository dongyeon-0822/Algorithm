# 메모
# 1 -> 1 -> 1
# 2 -> 00, 11 -> 2
# 3 -> 100, 001, 111 -> 3
# 4 -> 1100, 1001, 0011, 0000, 1111 -> 5
# 5 -> 11100, 11001, 10011, 00111, 10000, 00100, 00001, 11111 -> 8
# 6 -> 13
# dp[n] = dp[n-1] + dp[n-2]

import sys
input = sys.stdin.readline

N = int(input())

tile = [0] * (N+2) # N+1로 하면 100%에서 런타임에러
tile[0] = 0
tile[1] = 1
tile[2] = 2

for i in range(3,N+1):
    tile[i] = (tile[i-2] + tile[i-1])%15746

print(tile[N])

# 런타임 에러 미해결 -> 재귀?
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# tile = [0] * 1000001
#
# def memorizeTile(n):
#     if n == 0 or n == 1:
#         return 1
#     if tile[n] != 0:
#         return tile[n]
#     tile[n] = (memorizeTile(n - 1) + memorizeTile(n - 2))%15746
#     return tile[n]
#
# print(memorizeTile(N))