import sys
input = sys.stdin.readline

N = int(input())
if N % 2 == 0:
    print('CY')
else:
    print('SK')

# DP를 이용한 풀이
# dp = [0]*1000
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2
# for n in range(3, N+1):
#     dp[n] = min(dp[n-1] + 1, dp[n-3] + 1)
# if dp[n] % 2 == 0:
#     print('CY')
# else:
#     print('SK')