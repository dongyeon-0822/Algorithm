import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]
parent = [-1] * (n+1)
distance =  [INF] * (n +1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

start_node, end_node = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next_node,d in enumerate(graph[node]):
            if next_node == 0: continue
            cost = d + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                parent[next_node] = node
                heapq.heappush(q,(cost, next_node))

dijkstra(start_node)
print(distance[end_node])
paths = [end_node]
while paths[-1] != start_node:
    paths.append(parent[paths[-1]])
print(len(paths))
for p in paths[::-1]:
    print(p, end=" ")
