import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
indegree = [0] * (N+1)

for _ in range(M):
    order = list(map(int, input().split()))[1:]
    for i in range(len(order)-1):
        a, b = order[i], order[i+1]
        graph[a].append(b)
        indegree[b] += 1

def topology_sort():
    answer = []
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        visited[now] = True
        answer.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if not all(visited[1:]):
        print(0)
    else:
        for x in answer:
            print(x)

topology_sort()
