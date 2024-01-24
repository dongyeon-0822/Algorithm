import sys
import heapq
input = sys.stdin.readline

answer = 0
N, M = map(int, input().split())
ladders = dict([list(map(int, input().split())) for _ in range(N)])
snakes = dict([list(map(int, input().split())) for _ in range(M)])
dice = [1,2,3,4,5,6]

q = []
visited = [False] * 101
heapq.heappush(q, (0, 1))
visited[1] = True
while q:
    n, x = heapq.heappop(q)
    if x == 100:
        answer = n
        break
    if x in ladders: # 사다리
        x = ladders[x]
        visited[x] = True
    elif x in snakes: # 뱀
        x = snakes[x]
        visited[x] = True
    for d in dice:
        if x + d <= 100 and not visited[x + d]:
            heapq.heappush(q, (n+1, x+d))
            q.append((n + 1, x + d))
            visited[x + d] = True
print(answer)

# sol 2
# from collections import deque
#
# q = deque()
# visited = [False] * 101
# q.append((0,1))
# visited[1] = True
# while q:
#     n, x = q.popleft()
#     if x == 100:
#         answer = n
#         break
#     if x in ladders: # 사다리
#         x = ladders[x]
#         visited[x] = True
#     elif x in snakes: # 뱀
#         x = snakes[x]
#         visited[x] = True
#     for d in dice:
#         if x + d <= 100 and not visited[x + d]:
#             q.append((n + 1, x + d))
#             visited[x + d] = True
# print(answer)