N, K = list(map(int, input().split()))
arr = []
flag = [0] * N
for i in range(N):
    arr.append(i + 1)
print('<', end="")
idx = 0
for i in range(N):
    idx += K - 1
    while idx >= len(arr):
        idx -= len(arr)
    pop = arr.pop(idx)
    if i < N - 1:
        print(pop, end=", ")
    else:
        print(pop, end="")
print('>', end="")