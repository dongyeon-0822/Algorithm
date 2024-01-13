import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1, N + 1):
    graph[a][a] = 0
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = -1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] >= 0 and graph[k][j] >= 0 or graph[i][k] <= 0 and graph[k][j] <= 0:
                graph[i][j] = graph[i][j] if abs(graph[i][j]) < abs(graph[i][k] + graph[k][j]) else graph[i][k] + \
                                                                                                    graph[k][j]

for g in graph[1:]:
    print(g[1:].count(INF))
