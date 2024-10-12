import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minute = list(map(int, input().split()))

def get_blue(n):
    count = 1
    tmp = 0
    for m in minute:
        if tmp + m <= n:
            tmp += m
        else:
            tmp = m
            count += 1
    return count

answer = 0
low, mid, high = max(minute), 0, sum(minute)
while low <= high:
    mid = (low + high) // 2
    blue = get_blue(mid)
    if blue > M:
        low = mid + 1
    else:
        high = mid - 1
        answer = mid
print(answer)

