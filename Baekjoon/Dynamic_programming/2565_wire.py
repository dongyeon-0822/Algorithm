import sys
input = sys.stdin.readline

# LIS 알고리즘(최장증가수열) 공부하기! -> https://source-sc.tistory.com/14
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
dp = [0] * (n+1)

def lis_dp(n):
    max = 1;
    for i in range(n):
        dp[i] = 1;
        for j in range(i):
            if arr[j][1] < arr[i][1] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                if max < dp[i]:
                    max = dp[i]
    return max

print(n - lis_dp(n))