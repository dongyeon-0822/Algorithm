import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key= lambda x: x[0])
cnt = 0
for i, a in enumerate(arr):
    if i == 0:
        pass
    if arr[i - 1][0] == a[0] and arr[i - 1][1] != a[1]:
        cnt += 1
print(cnt)