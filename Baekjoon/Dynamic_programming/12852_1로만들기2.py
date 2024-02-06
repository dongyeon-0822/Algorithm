import sys
input = sys.stdin.readline

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

N = int(input())
dp = [[0] * 2 for _ in range(N+1)]
dp[0] = [0,0]
dp[1] = [0,0]
for i in range(2, N+1):
    tmp = [[dp[i-1][0], i-1]]
    if i % 3 == 0:
        tmp.append([dp[i // 3][0], i//3])
    if i % 2 == 0:
        tmp.append([dp[i // 2][0], i//2])
    tmp.sort(key=lambda x:x[0])
    dp[i][0] = tmp[0][0] + 1
    dp[i][1] = tmp[0][1]

print(dp[N][0])
n = N
while n >= 1:
    cnt, ex_n = dp[n]
    print(n, end=" ")
    n = ex_n