import sys
input = sys.stdin.readline
import heapq

N = int(input().rstrip())
arr = []
for i in range(N):
    n = int(input().rstrip())
    if n == 0:
        if len(arr) == 0:
            print(0)
        else:
            max_value = heapq.heappop(arr)[1]
            print(max_value)
    else:
        heapq.heappush(arr, (-n, n))