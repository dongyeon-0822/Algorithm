def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
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
    return distance

import sys, heapq
input = sys.stdin.readline

INF = int(1e7)
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

shortest_dist = dijkstra(1)
distance_v1 = shortest_dist[v1]
distance_v2 = shortest_dist[v2]

shortest_dist = dijkstra(v1)
distance_v1 += shortest_dist[v2]
distance_v2 += shortest_dist[N]

shortest_dist = dijkstra(v2)
distance_v2 += shortest_dist[v1]
distance_v1 += shortest_dist[N]

answer = min(distance_v1,distance_v2)
if answer >= INF:
    print(-1)
else:
    print(answer)