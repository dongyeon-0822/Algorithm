import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lectures = list(map(int, input().split()))

def get_blueNum(n):
    count = 1
    tmp = 0
    for lecture in lectures:
        if tmp + lecture <= n:
            tmp += lecture
        else:
            count += 1
            tmp = lecture
    return count

answer = 0
low, mid, high = max(lectures), 0, sum(lectures) # 블루 레이의 크기
while low <= high:
    mid = (low + high) // 2
    num = get_blueNum(mid) # 필요한 블루 레이의 개수
    if num > M:
        low = mid + 1
    elif num <= M:
        high = mid - 1
        answer = mid

print(answer)