import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[int(1e9)] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answers = []
for i in range(1, N+1):
    answers.append([sum(graph[i][1:]), i])
answers.sort()
print(answers[0][1])