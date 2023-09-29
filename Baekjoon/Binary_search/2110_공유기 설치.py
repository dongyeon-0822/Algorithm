import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])
# distances = [houses[i+1] - houses[i] for i in range(N-1)]

# def get_wifi(n):
#     count = 1
#     d = 0
#     for distance in distances:
#         if d + distance < n:
#             d += distance
#         else:
#             count += 1
#             d = 0
#     return count

def get_wifi(n):
    count = 1
    prev_h = houses[0]
    for idx in range(1, N):
        if houses[idx] - prev_h >= n:
            count += 1
            prev_h = houses[idx]
    return count

answer = 0
low, mid, high = 1, 0, houses[-1] - houses[0]
while low <= high:
    mid = (low + high) // 2
    c = get_wifi(mid)
    if c < C:
        high = mid - 1
    else:
        low = mid + 1
        answer = mid
print(answer)