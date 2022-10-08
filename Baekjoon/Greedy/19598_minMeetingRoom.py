import sys
import heapq
input = sys.stdin.readline

N = int(input())
timeList = [list(map(int, input().split())) for _ in range(N)]

timeList.sort(key=lambda x : x[0]) # 시작하는 시간으로 정렬
count = [] # 방의 개수 저장
timeTable = []

for new_time in timeList:
    if len(timeTable) == 0:
        heapq.heappush(timeTable, new_time[1])
        count.append(len(timeTable))
    else:
        if timeTable[0] <= new_time[0]: # heap 의 최상위가 작거나 같다면
            heapq.heappop(timeTable)
            heapq.heappush(timeTable, new_time[1])
        else:
            heapq.heappush(timeTable, new_time[1])
            count.append(len(timeTable))
print(max(count))
