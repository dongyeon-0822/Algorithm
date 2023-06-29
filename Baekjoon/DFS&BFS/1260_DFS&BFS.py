from collections import deque
import sys
input = sys.stdin.readline

def dfs(x, visited):
    visited[x] = True
    print(x, end=" ")
    for node in graph[x]:
        if not visited[node]:
            dfs(node, visited)

def bfs(x, visited):
    q = deque()
    q.append((0,x))
    visited[x] = True
    while q:
        d, n = q.popleft()
        print(n, end=" ")
        for nx in graph[n]:
            if not visited[nx]:
                visited[nx] = True
                q.append((d+1, nx))

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in range(1, N+1):
    graph[x].sort()

visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print()

visited_bfs = [False] * (N + 1)
bfs(V, visited_bfs)
