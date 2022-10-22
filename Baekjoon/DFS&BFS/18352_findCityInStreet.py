from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

# 2차원 인접 리스트로 그래프 표현
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [False] * (N + 1)
distance = [0] * (N + 1)

queue = deque([X])
visited[X] = True
# 큐가 빌때까지 반복
while queue:
    v = queue.popleft()
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            distance[i] = distance[v] + 1 # bfs 이므로 최단거리
            queue.append(i)

flag = False
for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        flag = True
if not flag:
    print(-1)
