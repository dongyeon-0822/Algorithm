# 풀이 참고!
import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)] # R,G,B
dp = [[int(1e9)] * 3 for _ in range(N)]

answer = []
for c in range(3): # 첫 번째 집의 색을 고정
    for i in range(3):
        if i == c:
            dp[0][i] = costs[0][i]
        else:
            dp[0][i] = int(1e9)
    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    for i in range(3):
        if i != c:
            answer.append(dp[N-1][i])
print(min(answer))