import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    amount = int(input())

    dp = [0] * (amount+1)
    for c in coin:
        if c <= amount: # 구하는 범위보다 작거나 같을 때만
            dp[c] += 1
            for i in range(c + 1, amount + 1):
                dp[i] += dp[i-c] # c원을 더하기 전의 경우의 수가 현재 값에 추가됨
    print(dp[amount])
