import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

answer = []
start = 0
end = 0
result = 0
while start < len(arr):
    result = arr[end] - arr[start]
    if result>=M:
        start += 1
        answer.append(result)
    elif end+1 < len(arr):
        end += 1
    else:
        start += 1
print(min(answer))
