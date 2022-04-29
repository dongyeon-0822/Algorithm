N, M = map(int, input().split())
balls = list(map(int, input().split()))

total = N * (N - 1) // 2
sub = 0
for m in range(M):
    cnt = balls.count(m + 1)
    if cnt >= 2:
        sub += (cnt * (cnt - 1) // 2)
print(total - sub)