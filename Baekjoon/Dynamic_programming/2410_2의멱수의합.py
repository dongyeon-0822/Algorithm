N = int(input())
MOD = 1000000000

dp = [0] * (N + 1)
dp[0] = 1
power_of_two = [1 << i for i in range(21)]

for power in power_of_two:
    if power > N: break
    for i in range(power, N + 1):
        dp[i] = (dp[i] + dp[i - power]) % MOD

print(dp[N])