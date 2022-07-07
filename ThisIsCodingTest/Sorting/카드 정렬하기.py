# https://www.acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)
length = len(cards)
answer = 0
while length > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards,tmp)
    answer += tmp
    length -= 1
print(answer)