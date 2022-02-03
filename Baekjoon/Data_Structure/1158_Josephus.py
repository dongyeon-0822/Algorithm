# 시간초과
N, K = list(map(int, input().split()))
arr = []
flag = [0] * N
for i in range(N):
    arr.append(i + 1)
print('<', end="")
idx = 0
for i in range(N):
    cnt = 0
    while 0 in flag:
        if not flag[idx]:
            cnt += 1
        if cnt == K:
            cnt = 0
            flag[idx] = 1
            print(arr[idx], end="")
            if 0 in flag:
                print(", ", end="")
        idx += 1
        if idx >= N:
            idx = 0
print('>', end="")