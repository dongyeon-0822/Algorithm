from collections import deque

# 최단거리이므로 bfs 함수를 이용
def bfs(graph, start, visited, distance):
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[v] + 1
                queue.append(i)

N, M, K, X = map(int, input().split())

# 2차원 인접 리스트로 그래프 표현
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [False] * (N + 1)
distance = [-1] * (N + 1)
bfs(graph, X, visited, distance)

if K not in distance:
    print(-1)
else:
    for i in range(N + 1):
        for distance[i] == K:
            print(i)