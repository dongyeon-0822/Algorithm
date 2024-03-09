import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(m):
    x, y = heapq.heappop(cards), heapq.heappop(cards)
    heapq.heappush(cards, x+y)
    heapq.heappush(cards, x+y)

print(sum(cards))