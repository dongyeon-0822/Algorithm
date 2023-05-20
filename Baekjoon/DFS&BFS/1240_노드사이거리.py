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
    distance = 0

    q = deque()
    q.append(a)
    visited[a] = True
    while q:
        x = q.popleft()
        is_found = False
        for nx, d in graph[x]:
            if not visited[nx]:
                distance += d
                if nx == b:
                    print(distance)
                    is_found = True
                    break
                q.append(nx)
        if is_found:
            break
