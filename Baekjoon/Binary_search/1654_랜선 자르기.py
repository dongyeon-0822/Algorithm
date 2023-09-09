import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = sorted([int(input()) for _ in range(K)])
answer = 0

low, mid, high = 1, 0, lines[-1]
while low <= high:
    mid = (low + high) // 2
    n = sum([line // mid for line in lines])
    if n >= N:
        low = mid + 1
        answer = mid
    else:
        high = mid - 1

print(answer)