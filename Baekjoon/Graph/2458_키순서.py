import sys
input = sys.stdin.readline
INF = 999999

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]
for a in range(1,N+1):
    graph[a][a] = 0
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = -1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] >= 0 and graph[k][j] >= 0 or graph[i][k] <= 0 and graph[k][j] <= 0:
                graph[i][j] = graph[i][j] if abs(graph[i][j]) < abs(graph[i][k] + graph[k][j]) else graph[i][k] + graph[k][j]

answer = 0
for g in graph[1:]:
    if INF not in g[1:]:
        answer += 1
print(answer)