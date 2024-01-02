import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = [list(map(int,input().split())) for _ in range(N)]

answer = 0
rooms = []
classes.sort(key=lambda x:(x[0]))
for s, e in classes:
    if not rooms: # 비어 있다면
        heapq.heappush(rooms, e)
    else:
        if rooms[0] <= s: # 강의실 추가 X
            heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        else: # 강의실 추가 O
            heapq.heappush(rooms, e)
            answer = max(answer, len(rooms))
print(answer)
