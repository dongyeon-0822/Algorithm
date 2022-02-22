N, M = map(int, input().split())

arr = []
for i in range(N):
	arr.append(min(list(map(int, input().split()))))
print(max(arr))