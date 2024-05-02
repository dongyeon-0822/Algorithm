import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []

for _ in range(N):
    n = int(input())
    if n == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, n)