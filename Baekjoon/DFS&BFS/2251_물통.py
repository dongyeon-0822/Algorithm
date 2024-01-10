import sys
from collections import deque
input = sys.stdin.readline

answer = []
bottles_volume = A, B, C = list(map(int, input().split()))
q = deque()
visited = []

bottles = (0, 0, C)
if bottles[0] == 0 and bottles[2] > 0:
    answer.append(bottles[2])
q.append(bottles)
visited.append((0, 0, C))
while q:
    bottles = q.popleft()
    for s, e in [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]]:
        new_bottle = []
        if bottles[s] > 0 and bottles[s] + bottles[e] <= bottles_volume[e]: # 한 물통이 비거나
            new_bottle = list(bottles)
            new_bottle[s] = 0
            new_bottle[e] += bottles[s]
        elif bottles[s] > 0 and bottles[e] < bottles_volume[e]: # 다른 물통이 찰 때
            new_bottle = list(bottles)
            sub = bottles_volume[e] - bottles[e]
            new_bottle[s] -= sub
            new_bottle[e] += sub
        if new_bottle and tuple(new_bottle) not in visited:
            if new_bottle[0] == 0 and new_bottle[2] >= 0:
                answer.append(new_bottle[2])
            q.append(new_bottle)
            visited.append(tuple(new_bottle))
answer.sort()
print(*answer, sep=" ")
