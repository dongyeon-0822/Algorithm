import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]
indegree = [0] * (N + 1)
cost = [0] * (N + 1)
answer = [0]*(N+1)
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    indegree[i] = len(tmp) - 2
    cost[i] = tmp[0]
    for x in tmp[1:-1]:
        graph[x].append(i)

def topology_sort():
    q = deque()

    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] += cost[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            answer[i] = max(answer[i], answer[now] + cost[i])
            if indegree[i] == 0:
                q.append(i)


topology_sort()
for x in answer[1:]:
    print(x)
