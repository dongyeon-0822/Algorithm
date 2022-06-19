import sys
input = sys.stdin.readline

N = int(input())
loss = list(map(int, input().split()))
loss.sort()

loss_sum = []
if N % 2 == 0:
    for i in range(N // 2):
        loss_sum.append(loss[i] + loss[N - 1- i])
else:
    loss_sum.append(loss[-1])
    for i in range((N - 1) // 2):
        loss_sum.append(loss[i] + loss[N - 2 - i])

print(max(loss_sum))