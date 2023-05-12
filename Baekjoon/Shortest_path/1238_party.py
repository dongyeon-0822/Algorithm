def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: # 이미 처리한 적 있는 노드라면 무시
            continue
        for i in graph[node]: # 현재 노드와 연결된 노드들 확인
            cost = dist+i[1] # 거리 계산
            if cost < distance[i[0]]: # 현재 최단거리보다 작다면 갱신하고 힙에 push
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

# 다익스트라 알고리즘
import sys, heapq
sys = sys.stdin.readline

INF = int(1e9)
N,M,X = map(int, input().split())

go_graph = [[] for _ in range(N+1)]
back_graph = [[] for _ in range(N+1)]
go_distance = [INF] * (N+1)
back_distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    go_graph[a].append((b,c))
    back_graph[b].append((a,c))

dijkstra(X,go_distance, go_graph)
dijkstra(X,back_distance, back_graph)

print(max([x+y for x,y in zip(go_distance[1:], back_distance[1:])]))

