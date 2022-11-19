# 플로이드 워셜 알고리즘 = 모든 지점애서 다른 모든지점까지의 최단 경로를 모두 구해야 하는 경우
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
requests = [list(map(int, input().split())) for _ in range(M)]

# 플로이드 워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for a,b,c in requests:
    if graph[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")