N = int(input())

arr = []
for i in range(N):
    arr.append(input().split())
arr.sort(key=lambda x : int(x[1]))

for i in range(N):
    print(arr[i][0], end=" ")