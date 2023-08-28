import sys
import heapq
input = sys.stdin.readline

answer = 0
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort(key=lambda x:(-x[0], -x[1]))

heap = []
deadline = schedule[0][0]
for d, w in schedule:
    while d < deadline:
        answer += -heapq.heappop(heap) if heap else 0
        deadline -= 1
    heapq.heappush(heap, (-w))

while deadline and heap:
    answer += -heapq.heappop(heap)
    deadline -= 1

print(answer)