import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
relations = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    x,y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

distance = 0
q = deque()
q.append([a, distance])
visited[a] = True
while q:
    x, d = q.popleft()
    if x == b:
        distance = d
        break
    for nx in relations[x]:
        if not visited[nx]:
            visited[nx] = True
            q.append([nx, d+1])

if distance == 0:
    print(-1)
else:
    print(distance)
