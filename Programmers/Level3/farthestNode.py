import heapq

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for x in graph[node]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))

    dijkstra(1, graph, distance)
    long_distance = max(distance[1:])
    print(distance)
    return distance.count(long_distance)

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])