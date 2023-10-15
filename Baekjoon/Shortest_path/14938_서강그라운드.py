import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijkstra(start):
    distance = [int(1e9) for _ in range(n+1)]
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: continue
        for n, c in graph[node]:
            cost = dist + c
            if cost < m and cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))
                
