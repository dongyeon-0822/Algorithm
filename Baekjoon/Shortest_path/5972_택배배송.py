import sys, heapq
input = sys.stdin.readline


INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
distance = [INF] * (N+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n, d in graph[node]:
            cost = dist + d
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q,(cost, n))

dijkstra(1)
print(distance[N])
print(distance)
