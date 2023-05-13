import bisect

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
location = list(map(int, input().split()))
location.sort()


tape = 1
last_location = location[0] - 0.5 + L  # 첫번째 테이프 붙이기
while last_location < location[-1] + 0.5:
    idx = bisect.bisect_right(location, last_location)
    if location[idx-1] + 0.5 <= last_location:
        last_location = location[idx] - 0.5 + L
        tape += 1
    else:
        last_location += L
        tape += 1
print(tape)


