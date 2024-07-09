n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    i, j, k = map(int, input().split())
    print(sorted(arr[i-1:j])[k-1])