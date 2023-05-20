import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,d = map(int, input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

for _ in range(M):
    a,b = map(int, input().split())
    visited = [False] * (N + 1)

    q = deque()
    q.append([a,0])
    visited[a] = True
    while q:
        x, d = q.popleft()
        if x == b:
            print(d)
        for nx, nd in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append([nx, d+nd])
